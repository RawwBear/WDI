def find_10_largest(seq):
    # we need to remove zero if it's last because we don't want '' in our list
    if str(seq)[-1] == '0':
        seq = seq[:-1]
    if str(seq)[0] == '0':
        seq = seq[1:]
    seq = [int(i) for i in str(seq).split('0')]
    # if seq[-1] == '': seq.pop()
    #input sequence: 10120130230...where 0 is the end-of-data marker
    #sort the sequence in descending order
    for i in range(len(seq)-1):
        for j in range(i+1, len(seq)):
            if seq[i] < seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
    return seq

print(find_10_largest(12112000111))

