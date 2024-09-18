import argparse
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import pandas as pd
import matplotlib.pyplot as plt
from Bio import motifs

"""# Genomics Data Analysis
**Goal:** is to analyze genomic data of Covid-19 with Biopython
**Data:** Covid19 wuhan virus - DNA sequencing data
we applied the Biopython fundamentals to a real-world use case to understand how to perform sequence analysis.
## Sequence analysis of Covid-19

A sequence is a series of letters
**The type of Sequence** - String together in a protein
1. DNA -  A, G, C, and T
2. RNA -  A, G, C, and U
3. Amino acids -  D, T, S, E, P, G, A, C, V, M, I, L, Y, F, H, K, R, W, Q, and N

**Seq object**
The first and the most important object to deal with sequence data in Biopython is the `Seq object`. 
It essentially combines a Python string with biological methods such as DNA, RNA, or Protein.

Each Seq object has two important attributes:
1. Data - The actual sequence string ('ATCTGTCCTACT').
2. Alphabet - determines type of sequence

Supports 2 types of Methods:
1. General Methods - (find, count, and so on)
2. Nucleotide Methods - (complement, reverse_complement, transcribe, back_transcribe, translate, and so on)

**SeqRecord**

This object differs from the Seq object in that it holds a sequence (as a Seq object) with additional information such as identifier, name, and description.

**SeqIO Object** :

 supporting file formats as input and output
 1. FASTA
 2. FASTA-2line
 3. FASTQ
 4. GenBank or GB

FASTA format file
"""

# Open the file and iteratively parse the sequence
# The parse() method takes two arguments
# fh_in – the file handle and
# fasta - the file format.

## Data Extraction
"""
The full sequence of the Wuhan virus can be downloaded (https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2?report=fasta); save it as covid19.fasta locally on your computer.
"""
# read the sequence from the file and return the sequence
def read_fasta_file(file_path):
    with open(file_path) as fh_in:
        for record in SeqIO.parse(fh_in, "fasta"):
            print(f'sequence information: {record}')
            print(f'sequence length: {len(record)}')
            print(f'sequence: {record.seq}')
            print(f'sequence description: {record.description}')
            print(f'sequence name: {record.name}')
            print(f'sequence id: {record.id}')
            print(f'sequence features: {record.features}')
            print(f'sequence annotations: {record.annotations}')
            print(f'sequence letter_annotations: {record.letter_annotations}')
            print(f'sequence dbxrefs: {record.dbxrefs}')
            print(f'sequence format: {record.format}')
            print(f'sequence upper: {record.seq.upper()}')
            print(f'sequence lower: {record.seq.lower()}')
            print(f'sequence complement: {record.seq.complement()}')
            print(f'sequence reverse_complement: {record.seq.reverse_complement()}')
            print(f'sequence transcribe: {record.seq.transcribe()}')
            print(f"GC content of {record} : {gc_fraction(record):.2f}")
    return record.seq

### Calculating nucleotide content
def calculate_nucleotide_content(sequence: str):
     seq_record = sequence
     seq_length = len(seq_record)
     print(f'% of Ts: {round(seq_record.count("T")/seq_length*100, 2)}')
     print(f'% of As: {round(seq_record.count("A")/seq_length*100, 2)}')
     print(f'% of Cs: {round(seq_record.count("C")/seq_length*100, 2)}')
     print(f'% of Gs: {round(seq_record.count("G")/seq_length*100, 2)}')

### Dinucleotide content
def calculate_dinucleotide_content(sequence: str):
    seq_record = sequence
    nucl = ['A', 'T', 'C', 'G']
    di_nucl_dict = {}
    for n1 in nucl:
        for n2 in nucl:
            di = str(n1) + str(n2)
            di_nucl_dict[di] = seq_record.count(di)
    return di_nucl_dict

### EDA and visualization for dinucleotide plot
def plot_dinucleotide_content(di_nucl_dict):
    di = [k for k, v in di_nucl_dict.items()]
    counts = [v for k, v in di_nucl_dict.items()]
    print(di_nucl_dict)
    plt.bar(di,counts)
    plt.ylabel("Counts")
    plt.show()

"""
## Modeling

Two types
1. Statistical-based methods
2. ML-based methods
"""

# statistical-based methods
# 1. Position frequency matrix (PFM) also called as count
# 2. Position weight matrix (PWM) also called as score
# 3. Information content (IC)
# 4. Consensus sequence
# 5. Motif finding
# 6. Sequence alignment
# 7. Phylogenetic analysis
# 8. Gene prediction
# 9. Protein structure prediction
# 10. Protein-protein interaction prediction
# 11. Protein function prediction
# 12. Protein localization prediction
# 13. Protein post-translational modification prediction

# ML-based methods
# 1. Sequence classification
# 2. Sequence clustering
# 3. Sequence regression
# 4. Sequence generation
# 5. Sequence translation
# 6. Sequence tagging
# 7. Sequence alignment
# 8. Sequence prediction
# 9. Sequence recommendation
# 10. Sequence completion
# 11. Sequence summarization
# 12. Sequence representation learning
# 13. Sequence similarity learning
# 14. Sequence embedding
# 15. Sequence matching
# 16. Sequence ranking
# 17. Sequence retrieval
# 18. Sequence search
# 19. Sequence optimization
# 20. Sequence generation


"""### Motif finder

A motif is a pattern in a nucleotide or amino acid sequence that has a specific structure.

The important attributes that are available for motif objects are
1. Position frequency matrix (PFM) also called as count
2.
"""
def create_motif():
    # create a simple DNA motif object
    my_motif = [Seq("ACGT"), Seq("TCGA"), Seq("CGGC")]
    # creating a list of Seq objects
    seq = motifs.create(my_motif)
    print(seq)
    # print count or PFM
    print(seq.counts)
    seq.weblogo('my_motif.png')

def main():
    # read the arguments from the command line
    parser = argparse.ArgumentParser(description='Genomic analysis of COVID-19')
    parser.add_argument('file_path', help='The path to the FASTA file')
    args = parser.parse_args()
    # read the sequence from the file
    sequence = read_fasta_file(args.file_path)

    # count the nucleotides
    print(calculate_nucleotide_content(sequence))

    # Display dictionary consisting of all possible dinucleotides as keys and counts for those dinucleotides as values.
    di_nucl_dict = calculate_dinucleotide_content(sequence)
    print(calculate_dinucleotide_content(sequence))

    # plot the dinucleotide content
    plot_dinucleotide_content(di_nucl_dict)

if __name__ == '__main__':
    main()