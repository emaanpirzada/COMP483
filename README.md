Some words I wrote on the compbio server

Pipeline Project Step One:
I retrieved the four FASTQ files using "fasterq-dump --split-files [accession number]". I used --split-files to split them into paired-end reads. I then created sample test data using "head -n 10000 [datafile].fastq > [samplefile].fastq". I repeated the first step four times (once for each accession number) and the second step eight times (once for each paired-end read file).