import os
import numpy as np
from collections import deque


def add_edge(adj, edges, u, v):
    if u == v:
        return False
    a, b = min(u, v), max(u, v)
    if b in adj[a]:
        return False
    adj[a].add(b)
    adj[b].add(a)
    edges.append((a, b))
    return True


def has_common_neighbor(adj, u, v):
    return len(adj[u].intersection(adj[v])) > 0


def within_distance(adj, src, dst, max_depth=3):
    """Check whether dst is within max_depth hops from src."""
    if src == dst:
        return True

    visited = {src}
    q = deque([(src, 0)])

    while q:
        node, depth = q.popleft()
        if depth >= max_depth:
            continue

        for nb in adj[node]:
            if nb == dst:
                return True
            if nb not in visited:
                visited.add(nb)
                q.append((nb, depth + 1))

    return False


def generate_tree2500_5(
    out_dir="Tree-2500-5",
    n_nodes=2500,
    n_communities=5,
    feature_dim=256,
    community_feature_dim=40,
    intra_extra_edges_per_comm=20,
    inter_extra_edges=25,
    p_pref=0.7,
    active_comm_features=14,
    active_noise_features=5,
    feature_dropout=0.15,
    seed=42,
):
    rng = np.random.default_rng(seed)
    os.makedirs(out_dir, exist_ok=True)

    assert n_nodes % n_communities == 0
    assert n_communities * community_feature_dim <= feature_dim

    size_per_comm = n_nodes // n_communities

    labels = np.zeros(n_nodes, dtype=np.int64)
    communities = []
    roots = []

    start = 0
    for c in range(n_communities):
        nodes = np.arange(start, start + size_per_comm)
        communities.append(nodes)
        labels[nodes] = c
        roots.append(start)
        start += size_per_comm

    adj = [set() for _ in range(n_nodes)]
    edges = []

    # 1. 每个社区内部生成随机递归树
    for c, nodes in enumerate(communities):
        existing = [int(nodes[0])]

        for new_node in nodes[1:]:
            new_node = int(new_node)

            degrees = np.array([len(adj[v]) for v in existing], dtype=np.float64)
            pref_prob = (degrees + 1.0) / np.sum(degrees + 1.0)
            uniform_prob = np.ones(len(existing), dtype=np.float64) / len(existing)

            prob = p_pref * pref_prob + (1.0 - p_pref) * uniform_prob
            parent = int(rng.choice(existing, p=prob))

            add_edge(adj, edges, new_node, parent)
            existing.append(new_node)

    # 2. 用一条社区根节点链连接所有社区，保证全图连通
    for i in range(n_communities - 1):
        add_edge(adj, edges, roots[i], roots[i + 1])

    # 3. 每个社区内部加少量长距离边，避免过多局部闭合，保持 tree-like
    for c, nodes in enumerate(communities):
        added = 0
        tries = 0
        nodes = list(map(int, nodes))

        while added < intra_extra_edges_per_comm and tries < 200000:
            tries += 1
            u, v = rng.choice(nodes, size=2, replace=False)
            u, v = int(u), int(v)

            if v in adj[u]:
                continue

            if has_common_neighbor(adj, u, v):
                continue

            if within_distance(adj, u, v, max_depth=3):
                continue

            if add_edge(adj, edges, u, v):
                added += 1

        print(f"Community {c}: added {added} intra long-range edges.")

    # 4. 加少量社区间边，增强难度，但不破坏植入社区结构
    added = 0
    tries = 0

    while added < inter_extra_edges and tries < 300000:
        tries += 1

        c1, c2 = rng.choice(n_communities, size=2, replace=False)
        u = int(rng.choice(communities[c1]))
        v = int(rng.choice(communities[c2]))

        if v in adj[u]:
            continue

        if has_common_neighbor(adj, u, v):
            continue

        if add_edge(adj, edges, u, v):
            added += 1

    print(f"Added {added} inter-community edges.")

    edges = np.array(edges, dtype=np.int64)

    # 5. 构造稀疏二值属性
    X = np.zeros((n_nodes, feature_dim), dtype=np.float32)
    all_features = np.arange(feature_dim)

    for i in range(n_nodes):
        c = labels[i]

        comm_start = c * community_feature_dim
        comm_end = (c + 1) * community_feature_dim
        comm_pool = np.arange(comm_start, comm_end)
        noise_pool = np.setdiff1d(all_features, comm_pool)

        comm_feats = rng.choice(
            comm_pool,
            size=active_comm_features,
            replace=False,
        )

        noise_feats = rng.choice(
            noise_pool,
            size=active_noise_features,
            replace=False,
        )

        feats = np.concatenate([comm_feats, noise_feats])
        keep_mask = rng.random(len(feats)) > feature_dropout
        feats = feats[keep_mask]

        X[i, feats] = 1.0

    # 6. 保存无向边和双向 edge_index；不进行 train/val/test 数据集划分
    edge_index_undirected = edges.T

    edge_index_bidirectional = np.concatenate(
        [edges.T, edges[:, [1, 0]].T],
        axis=1,
    )

    np.savetxt(
        os.path.join(out_dir, "edges.csv"),
        edges,
        fmt="%d",
        delimiter=",",
        header="source,target",
        comments="",
    )

    np.save(os.path.join(out_dir, "features.npy"), X)
    np.save(os.path.join(out_dir, "labels.npy"), labels)

    np.savez(
        os.path.join(out_dir, "tree2500_5.npz"),
        x=X,
        y=labels,
        edge_index=edge_index_bidirectional,
        edge_index_undirected=edge_index_undirected,
    )

    # 7. 可选：保存 mat 文件，方便部分传统代码读取
    try:
        import scipy.sparse as sp
        from scipy.io import savemat

        row = np.concatenate([edges[:, 0], edges[:, 1]])
        col = np.concatenate([edges[:, 1], edges[:, 0]])
        data = np.ones(len(row), dtype=np.float32)

        A = sp.csr_matrix((data, (row, col)), shape=(n_nodes, n_nodes))

        Y_onehot = np.zeros((n_nodes, n_communities), dtype=np.float32)
        Y_onehot[np.arange(n_nodes), labels] = 1.0

        savemat(
            os.path.join(out_dir, "tree2500_5.mat"),
            {
                "A": A,
                "X": X,
                "labels": labels.reshape(-1, 1),
                "Y": Y_onehot,
            },
        )

    except Exception as e:
        print("Skip .mat saving because scipy is unavailable or failed:", e)

    # 8. 打印基本统计
    degrees = np.array([len(adj[i]) for i in range(n_nodes)])
    print("\nDataset generated:", out_dir)
    print("Nodes:", n_nodes)
    print("Communities:", n_communities)
    print("Edges:", len(edges))
    print("Average degree:", degrees.mean())
    print("Min degree:", degrees.min())
    print("Max degree:", degrees.max())
    print("Feature shape:", X.shape)
    print("Files saved to:", os.path.abspath(out_dir))

    return {
        "A_adj_list": adj,
        "edges": edges,
        "features": X,
        "labels": labels,
    }


if __name__ == "__main__":
    generate_tree2500_5(
        out_dir="Tree-2500-5",
        n_nodes=2500,
        n_communities=5,
        feature_dim=256,
        community_feature_dim=40,
        intra_extra_edges_per_comm=20,
        inter_extra_edges=25,
        p_pref=0.7,
        active_comm_features=14,
        active_noise_features=5,
        feature_dropout=0.15,
        seed=42,
    )
