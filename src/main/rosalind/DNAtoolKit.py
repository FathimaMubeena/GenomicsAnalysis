# DNA Toolkit file
import collections
Nucleotides = [ "A","C","G","T"]# we are going to use  these list in our functions

# Check the sequence to make sure it is a DNA String
def validateSeq(dna_seq: str):
    # Convert the input string to uppercase
    tmpseq = dna_seq.upper()

    # Iterate through each character and perform an action (e.g., print it)
    for nuc in tmpseq:
        if nuc not in Nucleotides: return False
    return tmpseq
# scecond function count nucleotide frequency function
def countNucFrequency(seq) :
     tmpFreqDict = {"A": 0,"C":0,"G": 0, "T": 0}
     for nuc in seq:
       tmpFreqDict[nuc] += 1
     return tmpFreqDict
    #return dict(collections.Counter(seq))
#Module name called collection(it has a method - Count)



# """ why do we need a validation seq function ?
#Imagine you are working with a DNA data that are coming from some txt files,Csv files or an online data base we just want to make a sure its a valid DNA string
# meaning it doesnt contain any unexpected characters and only has those four nucleotides ACGT or a combination of those four nucleotides,if it is not a valid DNA string,
# Im not interested in working with it,so our validate seek with sequence for short functions accepts a string then it creates a temporary string
# which is upper case and then we just loop through each character in that string to make sure it is one of these four characters if it is not if it at least one character does not match breaks
# out of the loop and we can return false because were not interested in working with a string anymore because it has atleast one invalid character
# if all the characters match just fine then were going to return an upper case version"""

# count the nucleotides
def countNucFrequency(seg) :
    tmpFreqDict = { "A": 0,"C":0,"G":0,"T":0}
    for nuc in seg:
        tmpFreqDict [nuc] += 1
    return tmpFreqDict