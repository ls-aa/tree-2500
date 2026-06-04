Dataset: Tree-2500-5
AM: gt
ORDER: 2
Runs: 10

Per-run total time:
Run 1: 28.411639 sec
Run 2: 26.411106 sec
Run 3: 26.683915 sec
Run 4: 26.248960 sec
Run 5: 26.252622 sec
Run 6: 26.422577 sec
Run 7: 26.696240 sec
Run 8: 26.000084 sec
Run 9: 27.620363 sec
Run 10: 27.194977 sec
Run time mean ± std: 26.794248 ± 0.744395 sec

Mean ± std by method:

[fastgreedy] origin / Original
Q: 0.919160 ± 0.000000
NMI: 0.539139 ± 0.000000
ARI: 0.161629 ± 0.000000
ACC: 0.180000 ± 0.000000
macro_F1: 0.303077 ± 0.000000
micro_F1: 0.180000 ± 0.000000
runtime_sec: 0.019121 ± 0.000976
total_cd_mode_runtime_sec: 5.543655 ± 0.174552

[fastgreedy] weighted / DecisionTree
Q: 0.919397 ± 0.000435
NMI: 0.547210 ± 0.009217
ARI: 0.161572 ± 0.006997
ACC: 0.171320 ± 0.009059
macro_F1: 0.291141 ± 0.013273
micro_F1: 0.171320 ± 0.009059
runtime_sec: 0.069232 ± 0.013082
total_cd_mode_runtime_sec: 5.543655 ± 0.174552

[fastgreedy] weighted / RandomForest
Q: 0.919617 ± 0.000547
NMI: 0.551000 ± 0.008320
ARI: 0.163436 ± 0.008865
ACC: 0.170160 ± 0.009746
macro_F1: 0.289444 ± 0.014871
micro_F1: 0.170160 ± 0.009746
runtime_sec: 0.071468 ± 0.024698
total_cd_mode_runtime_sec: 5.543655 ± 0.174552

[fastgreedy] weighted / VotingClassifier_hard
Q: 0.919160 ± 0.000000
NMI: 0.539139 ± 0.000000
ARI: 0.161629 ± 0.000000
ACC: 0.180000 ± 0.000000
macro_F1: 0.303077 ± 0.000000
micro_F1: 0.180000 ± 0.000000
runtime_sec: 0.062219 ± 0.000860
total_cd_mode_runtime_sec: 5.543655 ± 0.174552

[fastgreedy] weighted / VotingClassifier_soft
Q: 0.919185 ± 0.000269
NMI: 0.545832 ± 0.008807
ARI: 0.162079 ± 0.007038
ACC: 0.175120 ± 0.009460
macro_F1: 0.296136 ± 0.013921
micro_F1: 0.175120 ± 0.009460
runtime_sec: 0.072861 ± 0.031736
total_cd_mode_runtime_sec: 5.543655 ± 0.174552

[fastgreedy] weighted / XGBoost
Q: 0.919372 ± 0.000402
NMI: 0.545217 ± 0.006104
ARI: 0.164758 ± 0.003456
ACC: 0.183880 ± 0.005794
macro_F1: 0.309243 ± 0.008283
micro_F1: 0.183880 ± 0.005794
runtime_sec: 0.101368 ± 0.015935
total_cd_mode_runtime_sec: 5.543655 ± 0.174552

[infomap] origin / Original
Q: 0.786459 ± 0.006514
NMI: 0.809023 ± 0.044777
ARI: 0.818564 ± 0.064904
ACC: 0.916240 ± 0.041052
macro_F1: 0.918794 ± 0.035605
micro_F1: 0.916240 ± 0.041052
runtime_sec: 0.582554 ± 0.024596
total_cd_mode_runtime_sec: 8.953286 ± 0.370164

[infomap] weighted / DecisionTree
Q: 0.786359 ± 0.001357
NMI: 0.827582 ± 0.025284
ARI: 0.844403 ± 0.030195
ACC: 0.934200 ± 0.013819
macro_F1: 0.934276 ± 0.013903
micro_F1: 0.934200 ± 0.013819
runtime_sec: 0.640435 ± 0.022351
total_cd_mode_runtime_sec: 8.953286 ± 0.370164

[infomap] weighted / RandomForest
Q: 0.779600 ± 0.024512
NMI: 0.831022 ± 0.033692
ARI: 0.837695 ± 0.056930
ACC: 0.920320 ± 0.055147
macro_F1: 0.913526 ± 0.075336
micro_F1: 0.920320 ± 0.055147
runtime_sec: 0.629043 ± 0.039745
total_cd_mode_runtime_sec: 8.953286 ± 0.370164

[infomap] weighted / VotingClassifier_hard
Q: 0.786459 ± 0.006514
NMI: 0.809023 ± 0.044777
ARI: 0.818564 ± 0.064904
ACC: 0.916240 ± 0.041052
macro_F1: 0.918794 ± 0.035605
micro_F1: 0.916240 ± 0.041052
runtime_sec: 0.632444 ± 0.037740
total_cd_mode_runtime_sec: 8.953286 ± 0.370164

[infomap] weighted / VotingClassifier_soft
Q: 0.779162 ± 0.024359
NMI: 0.810948 ± 0.030332
ARI: 0.814508 ± 0.051868
ACC: 0.907760 ± 0.052491
macro_F1: 0.902018 ± 0.071581
micro_F1: 0.907760 ± 0.052491
runtime_sec: 0.642366 ± 0.026150
total_cd_mode_runtime_sec: 8.953286 ± 0.370164

[infomap] weighted / XGBoost
Q: 0.781572 ± 0.021967
NMI: 0.807281 ± 0.041541
ARI: 0.814868 ± 0.059727
ACC: 0.907080 ± 0.053825
macro_F1: 0.902949 ± 0.073539
micro_F1: 0.907080 ± 0.053825
runtime_sec: 0.670937 ± 0.035599
total_cd_mode_runtime_sec: 8.953286 ± 0.370164

[leiden] origin / Original
Q: 0.920981 ± 0.000602
NMI: 0.541379 ± 0.008711
ARI: 0.158920 ± 0.005005
ACC: 0.162760 ± 0.003469
macro_F1: 0.278731 ± 0.005245
micro_F1: 0.162760 ± 0.003469
runtime_sec: 0.022829 ± 0.002495
total_cd_mode_runtime_sec: 5.572394 ± 0.152051

[leiden] weighted / DecisionTree
Q: 0.920861 ± 0.000479
NMI: 0.547570 ± 0.009769
ARI: 0.160991 ± 0.007681
ACC: 0.165400 ± 0.008986
macro_F1: 0.282734 ± 0.012909
micro_F1: 0.165400 ± 0.008986
runtime_sec: 0.075147 ± 0.027357
total_cd_mode_runtime_sec: 5.572394 ± 0.152051

[leiden] weighted / RandomForest
Q: 0.921067 ± 0.000468
NMI: 0.552127 ± 0.008214
ARI: 0.165970 ± 0.006133
ACC: 0.170480 ± 0.007261
macro_F1: 0.290566 ± 0.010813
micro_F1: 0.170480 ± 0.007261
runtime_sec: 0.075929 ± 0.025884
total_cd_mode_runtime_sec: 5.572394 ± 0.152051

[leiden] weighted / VotingClassifier_hard
Q: 0.920981 ± 0.000602
NMI: 0.541379 ± 0.008711
ARI: 0.158920 ± 0.005005
ACC: 0.162760 ± 0.003469
macro_F1: 0.278731 ± 0.005245
micro_F1: 0.162760 ± 0.003469
runtime_sec: 0.085349 ± 0.035092
total_cd_mode_runtime_sec: 5.572394 ± 0.152051

[leiden] weighted / VotingClassifier_soft
Q: 0.920852 ± 0.000433
NMI: 0.545559 ± 0.007297
ARI: 0.162384 ± 0.007117
ACC: 0.167120 ± 0.012118
macro_F1: 0.285021 ± 0.017443
micro_F1: 0.167120 ± 0.012118
runtime_sec: 0.071022 ± 0.012309
total_cd_mode_runtime_sec: 5.572394 ± 0.152051

[leiden] weighted / XGBoost
Q: 0.920945 ± 0.000361
NMI: 0.539106 ± 0.007060
ARI: 0.159596 ± 0.005957
ACC: 0.163200 ± 0.009411
macro_F1: 0.279296 ± 0.013914
micro_F1: 0.163200 ± 0.009411
runtime_sec: 0.113225 ± 0.023763
total_cd_mode_runtime_sec: 5.572394 ± 0.152051

[louvain] origin / Original
Q: 0.919595 ± 0.000795
NMI: 0.530934 ± 0.005702
ARI: 0.153451 ± 0.003480
ACC: 0.166400 ± 0.009249
macro_F1: 0.282967 ± 0.013600
micro_F1: 0.166400 ± 0.009249
runtime_sec: 0.199594 ± 0.039280
total_cd_mode_runtime_sec: 6.685832 ± 0.730513

[louvain] weighted / DecisionTree
Q: 0.919576 ± 0.000524
NMI: 0.548848 ± 0.008347
ARI: 0.162128 ± 0.006988
ACC: 0.169960 ± 0.006710
macro_F1: 0.288886 ± 0.010267
micro_F1: 0.169960 ± 0.006710
runtime_sec: 0.215781 ± 0.037994
total_cd_mode_runtime_sec: 6.685832 ± 0.730513

[louvain] weighted / RandomForest
Q: 0.919649 ± 0.000339
NMI: 0.557196 ± 0.006083
ARI: 0.170746 ± 0.007030
ACC: 0.177080 ± 0.007180
macro_F1: 0.299847 ± 0.010451
micro_F1: 0.177080 ± 0.007180
runtime_sec: 0.223193 ± 0.033502
total_cd_mode_runtime_sec: 6.685832 ± 0.730513

[louvain] weighted / VotingClassifier_hard
Q: 0.919595 ± 0.000795
NMI: 0.530934 ± 0.005702
ARI: 0.153451 ± 0.003480
ACC: 0.166400 ± 0.009249
macro_F1: 0.282967 ± 0.013600
micro_F1: 0.166400 ± 0.009249
runtime_sec: 0.242760 ± 0.020840
total_cd_mode_runtime_sec: 6.685832 ± 0.730513

[louvain] weighted / VotingClassifier_soft
Q: 0.919502 ± 0.000363
NMI: 0.548397 ± 0.010584
ARI: 0.164321 ± 0.009811
ACC: 0.173720 ± 0.013205
macro_F1: 0.294446 ± 0.019029
micro_F1: 0.173720 ± 0.013205
runtime_sec: 0.216917 ± 0.039113
total_cd_mode_runtime_sec: 6.685832 ± 0.730513

[louvain] weighted / XGBoost
Q: 0.919347 ± 0.000496
NMI: 0.541046 ± 0.009897
ARI: 0.164654 ± 0.007206
ACC: 0.176760 ± 0.008518
macro_F1: 0.298487 ± 0.012316
micro_F1: 0.176760 ± 0.008518
runtime_sec: 0.246715 ± 0.019456
total_cd_mode_runtime_sec: 6.685832 ± 0.730513
