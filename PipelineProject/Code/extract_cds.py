import sys
import argparse
from Bio import SeqIO

# Creates a function to parse command line arguments
def check_arg(args=None):
    parser = argparse.ArgumentParser(description="Extract CDS sequences from genome")
    parser.add_argument("-i", "--input", required=True, help="Genome FASTA file") # Adds genome FASTA argument
    parser.add_argument("-a", "--gff", required=True, help="GFF annotation file") # Adds GFF annotation argument
    parser.add_argument("-o", "--output", required=True, help="Output CDS FASTA file") # Adds output FASTA argument
    parser.add_argument("-c", "--count",required=True, help="CDS count file") # Adds count output argument
    return parser.parse_args(args)

# Parses command-line arguments and assigns them to variables
arguments = check_arg(sys.argv[1:])
genome_file = arguments.input
gff_file = arguments.gff
output_file = arguments.output
count_file = arguments.count

# Parses the genome FASTA file into a dictionary keyed by sequence ID
genome_records = SeqIO.to_dict(SeqIO.parse(genome_file, "fasta"))

# Initializes a counter to track the total number of CDS features extracted
cds_count = 0

# Opens the output FASTA file for writing extracted CDS sequences
with open(output_file, "w") as out_fasta:
  # Opens and iterates through each line of the GFF annotation file
  with open(gff_file) as gff:
    for line in gff:
      if line.startswith("#"): # Skips any comments
        continue
      # Splits the GFF columns
      fields = line.strip().split("\t")
      seq_id = fields[0]
      feature_type = fields[2]
      # Processes CDS features
      if feature_type != "CDS":
        continue
      # Converts the start/end to Python indexing, finds the index of strand and attributes
      start = int(fields[3]) -1
      end = int(fields[4])
      strand = fields[6]
      attributes = fields[8]
      protein_id = attributes.split(";")[0].split("=")[1] # Extracts the protein id from the genome
      seq = genome_records[seq_id].seq[start:end] # Extracts the sequence from the genome
      # Finds the reverse complement if on the negative strand
      if strand == "-":
        seq = seq.reverse_complement()
      # Writes the protein id and sequence to the fasta file and adds 1 to the CDS count.
      out_fasta.write(f">{protein_id}\n{seq}\n")
      cds_count += 1

# Writes the CDS count to an output file.
with open(count_file, "w") as out_count:
  out_count.write(f"The HCMV genome (GCF_000845245.1) has {cds_count} CDS.\n")