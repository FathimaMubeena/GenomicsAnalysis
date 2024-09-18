# Write a Python program that reads the file "sequence.fasta" and prints the number of nucleotides of each type (A, C, G, T) in the sequence.
# The program should also print the number of codons that encode each amino acid in the sequence.
# The program should also print the amino acid sequence encoded by the sequence.
# The program should also print the number of times each amino acid appears in the sequence.
import argparse

def read_fasta_file(file_path):
    with open(file_path, 'r') as file:
        sequence = file.read()
    return sequence

def count_nucleotides(sequence):
    nucleotides = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in sequence:
        if nucleotide in nucleotides:
            nucleotides[nucleotide] += 1
    return nucleotides

def count_codons(sequence):
    codons = {}
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        if len(codon) == 3:
            if codon in codons:
                codons[codon] += 1
            else:
                codons[codon] = 1
    return codons

def translate_sequence(sequence):
    return sequence.replace('T', 'U')

def count_amino_acids(sequence):
    amino_acids = {}
    for amino_acid in sequence:
        if amino_acid in amino_acids:
            amino_acids[amino_acid] += 1
        else:
            amino_acids[amino_acid] = 1
    return amino_acids

def main():
    # read the arguments from the command line
    parser = argparse.ArgumentParser(description='Genomic analysis of COVID-19')
    parser.add_argument('file_path', help='The path to the FASTA file')
    args = parser.parse_args()
    # read the sequence from the file
    sequence = read_fasta_file(args.file_path)
    # count the nucleotides
    nucleotides = count_nucleotides(sequence)
    print(nucleotides)
    # count the codons
    codons = count_codons(sequence)
    print(codons)
    # translate the sequence
    amino_acid_sequence = translate_sequence(sequence)
    print("amino_acid_sequence:  \n"+amino_acid_sequence)

    # count the amino acids
    amino_acids = count_amino_acids(amino_acid_sequence)
    print(amino_acids)

if __name__ == '__main__':
    main()

# Run the program from the command line with file in resources folder with command argument
# python genomic_analysis_covid19.py resources/covid19.fasta


