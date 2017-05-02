seq = 'AGATAGATAGATCC'
kmer = {}
k = 5


for i in range(len(seq) - k):
    b = seq[i:i+k - 1]

    if b not in kmer:
        kmer[b] = [0, 0, 0, 0]

    if seq[i+k] == 'A':
        kmer[b][0] += 1
    elif seq[i+k] == 'C':
        kmer[b][1] += 1
    elif seq[i+k] == 'T':
        kmer[b][2] += 1
    else:
        kmer[b][3] += 1


for b in kmer:
    s = sum(kmer[b])
    for c in range(4):
        kmer[b][c] = kmer[b][c] / s


letters = ['A', 'C', 'T', 'G']

for l1 in letters:
    for l2 in letters:
        for l3 in letters:
            for l4 in letters:
                b = l1 + l2 + l3 + l4
                if b in kmer:
                    print("{},{},{},{}".format(kmer[b][0], kmer[b][1], kmer[b][2], kmer[b][3]))
                else:
                    pass
                    #print("0.25,0.25,0.25,0.25")
