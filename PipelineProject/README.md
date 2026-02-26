# RNA Sequence Analysis Pipeine
## Overview
This repository contains a Python Snakemake workflow that automates the analysis of Human herpesvirus 5 (HCMV) transcriptomes from RNA sequence data.
## Overview of Data
This code was originally developed to analyze HCMV transcriptomes from two donors:
| Donor | Days Post-Infection | SRA Accession Number |
| --- | --- | --- |
| Donor 1 | 2 | SRR5660030 |
| Donor 1 | 6 | SRR5660033 |
| Donor 3 | 2 | SRR5660044 |
| Donor 3 | 6 | SRR5660045 |
## How the Pipeline works
### Overview of Pipeline steps
For each sample, the Pipeline:
1. Extracts coding sequences (CDS) from each HCMV reference genome
2. Builds a kallisto transcriptome index
3. Quantifies the transcripts per million (TPM) using kallisto
4. Runs a sleuth differential expression analysis (R script)
5. Builds a Bowtie2 genome index
6. Saves only reads that map to the target genome to the genome index
7. Counts reads before and after mapping
8. Assembles RNA reads using SPADES
9. Extracts the longest contig from each assembly
10. Runs a BLASTN of the longest contig against the species' subfamily
11. Prints the results of the BLASTN to `PipelineReport.txt`
## Steps for use
### Install all dependencies
The following dependencies were used:
+ snakemake 7.32.4 (https://snakemake.readthedocs.io/en/v7.32.0/getting_started/installation.html)
+ Python 3.12.3 (https://www.python.org/downloads/release/python-3123/)
+ kallisto 0.51.1 (https://pachterlab.github.io/kallisto/download)
+ R 4.5.2 (https://cran.r-project.org/bin/windows/base/)
+ sleuth (https://pachterlab.github.io/sleuth/download)
+ bowtie2 2.5.2 (https://anaconda.org/bioconda/bowtie2)
+ spades v3.15.5 (https://github.com/ablab/spades/releases)
### Download the repository
In your Terminal, run:  
`git clone https://github.com/bofosu01/COMP483/PipelineProject.git`  
Move into the directory containing all the files in the repository.  
`cd COMP483`  
`cd PipelineProject`  
### Download the SRA data
First, retrieve each file and split it into forward and reverse reads.  
Example:  
`fasterq-dump SRR5660030 --split-files`  
Repeat this for each sample. Move each file into the `Samples` folder, then subsample each sample to reduce runtime.  
Example:  
`zcat Samples/SRR5660030_1.fastq.gz | head -n 40000 > Samples/test_SRR5660030_1.fastq`  
### Run the Pipeline
First, do a dry run to make sure everything is installed properly.  
`snakemake --dry-run`  
If this works without any errors, run the Pipeline.  
`snakemake --cores 4`
