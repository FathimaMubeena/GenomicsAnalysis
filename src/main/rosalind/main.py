# where we are just going to testing our code; DNA toolkit that by that is going to be our main file( lot of functionality
from DNAtoolKit import *
import random
rndDNAStr = "ATTTCGT"
print(validateSeq(rndDNAStr))

# lets check with lower case
rndDNAStr = "ATtttccccggggTTCGT"
print(validateSeq(rndDNAStr))

# lets check with random character
rndDNAStr = "ATTTCGTSSSXXXX"
print(validateSeq(rndDNAStr))

# Creating a random DNA sequence for testing:
randDNAStr = ''.join( [random. choice(Nucleotides)
                         for nuc in range(50)])
print(validateSeq(randDNAStr))
print(countNucFrequency(randDNAStr))

DNAStr = validateSeq(randDNAStr)
print(countNucFrequency(DNAStr))


# # scecond function count nucleotide frequency function
# def countNucFrequency(seq) :
#     tmpFreqDict = {"A": 0,"C":0,"G": 0, "T": 0}
#     for nuc in seq:
#         tmpFreqDict[nuc] += 1
#     return tmpFreqDict




# we can add one more feature to that instead of defining DNAstring every time we can make it generate a random DNA sting
# we can use pythons random module lets import it find and lets generate a random string every time we run main.py that
# def main():
#     rndDNAStr = "ATTTCG"
#     print(validateSeq(rndDNAStr))
#
#     randDNAStr = ''.join( [random. choice(Nucleotides)
#                         for nuc in range(20)])
#     print(validateSeq(randDNAStr))
#     print (countNucFrequency(randDNAStr))
#
#
# if __name__ == "__main__":
#     main()