# 4. Algorithms for DNA Sequencing

Lecture slides are available in PDF format from (a) the "resource" links next to each video lecture, and (b) this GitHub repo:

[BenLangmead/ads1-slides](https://github.com/BenLangmead/ads1-slides): Slides for Algorithms for DNA Sequencing Coursera class

The Jupyter notebooks used in the practical sessions are available in ipynb format from this GitHub repo:

[BenLangmead/ads1-notebooks](https://github.com/BenLangmead/ads1-notebooks): Copies of notebooks used in the practical sessions for Algorithms for DNA Sequencing

## 4.1 DNA Sequencing, Strings and Matching 
- First-gen / Sanger / Chain termination sequencing
- Used in the human genome project
- Next-gen / Second-gen / Massively parallel sequencing
- The Human Genome Project ended around 2003, and second-generation sequencing arrived around 2005-2007 or so
- Much cheaper per kb
- Works by sequencing by synthesis

### Sequencing principles
- Sequencers are bad at reading long stretches of DNA, but good at reading lots of short stretches of DNA.
- Sequencers read lots of random snippets of the input DNA (sequencing reads)
- Massively parallel sequencers produce reads of ~ 150-200 nt long
- So many reads are taken to create redundant information about every position in the genome

### Strings in Python 
- String S is a list of characters from the alphabet Σ
- For DNA, Σ = {A, T, C, G}
- |S| = string length = len(S)
- ε = empty string; |ε| = 0; len(‘’)
- Concatenation: s + t
- Subset: s[a:b]
- Prefix: s[:a]
- Suffix: s[-b:]

### Massively parallel sequencing

#### In vitro: 
- Extract DNA
- Chop into 100-200 nt single-stranded snippets
- Deposit on slide
- Snippets amplified into clusters of clones
- Add polymerase and terminated nucleotides
- Only one complimentary nucleotide can be incorporated
- Terminated nucleotides are fluorescent
- Snapshot recorded
- Terminators removed
- Repeat 

#### In silico: 
- Snapshots collected in order
- Snapshots compared for each template strand
- Reverse complemented for the original sequence
- Sequencing errors and base qualities
- A non-terminated base can be added to one of the clones in a cluster. This will result in the next base being added
- This clone is now out of sync for the rest of the read
- If this happens a few times, enough of the clones are out of sync to affect the read
- Base caller software deals with ambiguity to determine the most likely bases
- Base quality: Q
- Q = -10 log(p)
- Probability, p, is calculated as the proportion of measurements that agree

### FASTQ format
- Name
- Sequence
- ?
- Base quality

Base quality is an ASCII encoded version of Q

### Analysing Sequencing Data
- Genomes of unrelated humans are ~ 98.9 - 99.9 % similar
- Reads need to be stitched together first (assembly)
- Reference genomes make assembly much easier
- Without a reference, reads must be assembled from scratch (de novo assembly)
- 2nd-gen sequencers output billions of reads, each need to be aligned to the reference
- The human reference genome is ~ 3 billion bp long 
- Alignment is a huge computational task
- Fortunately, there are already very efficient algorithms and data structures for working with strings
