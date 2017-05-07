val = 85999

## loop through all files
for i2 in range(1, 4717):
    if i2 == 3807 or i2 == 4041:
       with open("E:\mix\StringAlgorithms\TermProject\Probability_python\genomes\lclAP009384.1_cds_BAF" + str(
               val) + ".2_" + str(i2) + ".fasta", 'r') as myfile:
           myfile.readline()
           seq = myfile.read().replace('\n', '')
           val += 1

    else :
        with open("E:\mix\StringAlgorithms\TermProject\Probability_python\genomes\lclAP009384.1_cds_BAF" + str(
                val) + ".1_" + str(i2) + ".fasta", 'r') as myfile:
            myfile.readline()
            seq = myfile.read().replace('\n', '')
            val += 1

    kmer = {}
    k = 6

    # for i in range(len(seq) - k):
    #     b = seq[i:i+k - 1]
    #
    #     if b not in kmer:
    #         kmer[b] = [0.0000001, 0.0000001, 0.0000001, 0.0000001]
    #
    #     if seq[i+k] == 'A':
    #         kmer[b][0] += 1
    #     elif seq[i+k] == 'C':
    #         kmer[b][1] += 1
    #     elif seq[i+k] == 'T':
    #         kmer[b][2] += 1
    #     else:
    #         kmer[b][3] += 1
    #
    # for b in kmer:
    #     s = sum(kmer[b])
    #     for c in range(4):
    #         kmer[b][c] = kmer[b][c] / s
# find k mer sequences
    total = 0
    for i in range(len(seq) - k + 1):
        b = seq[i:i + k]
        if b not in kmer:
            kmer[b] = 0.000001

        else:
            kmer[b] += 1.0
        total += 1
    for b in kmer:
        kmer[b] = kmer[b] / total

    path = "\\target_" + str(i2) + ".txt"

    letters = ['A', 'C', 'T', 'G']
## print all possibilities
    with open("E:\mix\StringAlgorithms\TermProject\Probability_python\\target_6mer" + path, 'w') as f:
        for l1 in letters:
            for l2 in letters:
              for l3 in letters:
                 for l4 in letters:
                     for l5 in letters:
                         for l6 in letters:
                            b = l1 + l2 + l3 + l4 + l5 + l6

                            if b in kmer:
        #print("{},{},{},{}".format(kmer[b][0], kmer[b][1], kmer[b][2], kmer[b][3]))
                                # f.write(str(kmer[b]))
                                # f.write("\n")
                                print(b)
                            else:
                                # f.write("0.000001")
                                # f.write("\n")
                                pass



