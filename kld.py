import numpy as np
import scipy.stats as sc
#read the first seq as ref/target
# val = 86002
# with open("E:\mix\StringAlgorithms\TermProject\Probability_python\genomes\lclAP009384.1_cds_BAF86001.1_3.fasta", 'r') as myfile:
#     myfile.readline()
#     seq = myfile.read().replace('\n', '')
# ref_length = len(seq)
#
# selected_targets = []
#
# #loop through other sequences
# c = 0
# for m in range(4, 4716):
#     if m == 3807 or m == 4041:
#         with open("E:\mix\StringAlgorithms\TermProject\Probability_python\genomes\lclAP009384.1_cds_BAF" + str(
#                 val) + ".2_" + str(m) + ".fasta", 'r') as myfile2:
#             myfile2.readline()
#             seq = myfile2.read().replace('\n', '')
#             val += 1
#     else:
#         with open("E:\mix\StringAlgorithms\TermProject\Probability_python\genomes\lclAP009384.1_cds_BAF" + str(
#                 val) + ".1_" + str(m) + ".fasta", 'r') as myfile:
#             myfile.readline()
#             seq = myfile.read().replace('\n', '')
#             val += 1
#     target_length = len(seq)
#     if ref_length in range(target_length - 200, target_length + 200):
#         selected_targets.insert(c, m)
#         c += 1


## the reference file
M = np.genfromtxt('E:\mix\StringAlgorithms\TermProject\Probability_python\\target_6mer\\target_3.txt')
#N = np.genfromtxt("E:\mix\StringAlgorithms\TermProject\Probability_python\\target_5mer\\target_" + str(selected_targets[0]) + ".txt")
# N = np.genfromtxt('E:\mix\StringAlgorithms\TermProject\Probability_python\\target_5mer\\target_4.txt')
# temp = sc.entropy(M, N)

# kld_i = selected_targets[0]

#find the target file
#for i in range(1, len(selected_targets)):
for i in range(5, 4616):
    # N = np.genfromtxt("E:\mix\StringAlgorithms\TermProject\Probability_python\\target_5mer\\target_" +
    #                   str(selected_targets[i]) + ".txt", delimiter=',')
    N = np.genfromtxt("E:\mix\StringAlgorithms\TermProject\Probability_python\\target_6mer\\target_" +
                                        i + ".txt", delimiter=',')
    kld = sc.entropy(M, N)

# #find entropy
#     kld = sc.entropy(M, N)
# #    sum_kld = sum(kld)
#     if kld < temp:
#         temp = kld
#         kld_i = selected_targets[i]

    print("divergence: " + str(kld) + " number: " + str(i))