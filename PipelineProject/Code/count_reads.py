import sys
import subprocess

# Parses command line arguments
fastq_file = sys.argv[1] # Path to the input FASTQ file
bam_file = sys.argv[2] # Path to the BAM file
sample = sys.argv[3] # Sample name/identifier
output_file = sys.argv[4] # Path to the output summary report file

# Counts the number of read pairs in the original FASTQ file
with open(fastq_file) as f:
  lines = sum(1 for _ in f) # Counts the total number of lines
reads = lines // 4 # Dividing total lines by 4 gives the number of reads

# Counts the number of aligned reads in the BAM file

bam_reads = int(subprocess.check_output(f"samtools view -c {bam_file}", shell=True).strip())

# Writes the number of read pairs and bam reads to an output file
with open(output_file, "w") as out:
  out.write(f"Sample {sample} had {reads} read pairs before and {bam_reads} read pairs after Bowtie2 filtering.\n")