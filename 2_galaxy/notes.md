# 2. Genomic Data Science with Galaxy

## 2.1: Introduction

## 2.2: Galaxy 101
Genomic Intervals
Galaxy tutorial: https://galaxyproject.org/tutorials/g101/

Question: On human chromosome 22, which coding exons have the most repeats?
In Galaxy, go to ‘Get Data’ → ‘UCSC Main’
First choose gene data (coding exons) for chromosome 32 and send to Galaxy, then select repeats and send to Galaxy.
To compare the datasets, go to ‘operate on genomic intervals’ → ‘Join’
Select the datasets → execute
To count how many entries there are in both datasets (ie how many repeats per exon), go to ‘join, subtract and group’ → ‘group’
Group by exon name column → + operation: count on exon name col → execute
We now have the number of repeats in each exon
We can now join the grouped data with the original exon data to get full exon data 
This dataframe can be cut (‘text manipulation’ → ‘cut’) to select specified cols
Workflows
An abstract representation of a multi-step analysis.
Represented as a set of tools and the flow of datasets between them – without being tied to specific datasets.
Workflows can be made from scratch or by example, where analysis is performed and the workflow extracted from the history.
History is saved automatically and can be recovered.
To extract workflow go to history options → ‘extract workflow’ 
The workflow can now be viewed and edited by going to the ‘workflow’ tab
Workflows can be used in new analyses by selecting them in the tools menu
In this case, we will use the saved workflow on the known gene and CpG islands (dense CG regions) datasets
Annotation, Sharing, and Publishing
Galaxy objects can be tagged or annotated.
Tags can be searched
Histories can be shared with specific users or published for everyone in the history options
https://usegalaxy.org/u/cycadophyta/h/exons-and-repeats 
Galaxy pages (like jupyter?) can be used to present the analysis, these are often used as supplementary information pages
Pages are accessed by ‘user’ → ‘pages’
Galaxy objects can be embedded

## 2.3: Working with Sequence Data
Sequence Data Quality Control
Import data: shared data → data libraries → Illumina iDEA Datasets → BT20 paired-end RNA-seq subsampled (end 1)
This data is in FASTQ format https://en.wikipedia.org/wiki/FASTQ_format
Analysis tools: FastQC
This outputs an HTML page of QC analysis
http://bit.ly/FastQCBoxPlot
There are a bunch of other tools for working with FASTQ data
What manipulations should you do on your data? (depends on downstream needs)
Trim columns
Filter rows (discard low quality reads)
Trim variable regions (results in different read lengths)
Tools for figuring out what to do with data:
http://seqanswers.com/
https://www.biostars.org/
ChIP seq with MACS
Model-based Analysis of ChIP Seq (MACS)

## 2.4: RNA-seq
RNA-seq Analysis: Mapping
Data: Data libraries → demonstration data → all Human RNA data
Options:
Align-then-assemble: more sensitive, but requires a reference genome
de novo: likely to only capture highly expressed transcripts
TopHat has been deprecated so I will use HISAT2
RNA alignment requires an aligner that is ‘splice aware’
RNA-seq Analysis: Assembly, Quantitation and Differential Expression
Spliced alignment data provides approximate locations of exons and splice junctions
Cufflinks has been deprecated so I will use StringTie for transcript assembly
Reference annotations will be used to show gene names and info
StringTie Merge to merge multiple assemblies
Featurecounts then DESeq2 can be used to determine differential expression

## 2.5: Running Your Own Galaxy

## Project
Upload data
FASTQC: 0 flagged sequences
Bowtie2 to align to hg19 human genome
Should realign before calling variants… 
FreeBayes to call variants
SnpEff to annotate VCF files with gene names
Bcftools counts to find number of SNPs and Indels
Combine VCF files somehow
