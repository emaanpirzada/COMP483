from Bio import SeqIO
import sys

# Parses command-line arguments
assembly = sys.argv[1] # Path to the input assembly FASTA file
output_file = sys.argv[2] # Path to the output FASTA file

# Parses all sequence records
records = list(SeqIO.parse(assembly, "fasta")) # Turns the FASTA file into a list to make it easier to parse

# Finds the longest contig by comparing the sequence lengths of all records using the max() function and a lambda key.
longest = max(records, key=lambda x: len(x.seq))

# Writes the longest contig to the output FASTA file
SeqIO.write(longest, output_file, "fasta")