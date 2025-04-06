def countNucFrequency(seq) :
    tmpFreqDict = {"A":0,"C":0, "G": 0,"T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

# create a DNA string and assign a random sequence
DNAString = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
result = countNucFrequency (DNAString)
#print(result)
#print(type(result))
print(' '.join([str(val) for key, val in result.items()]))
