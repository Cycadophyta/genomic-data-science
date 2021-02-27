from read_fasta import read_fasta
from naive_counts import naive_counts
from boyer_moore import bm_counts
from bm_preproc import BoyerMoore
from kmer_index import Index, SubseqIndex
from approximate_match import indexed_approximate_match, subseq_approximate_match


directory = "/home/runner/genomic-data-science/4-sequencing-algorithms/4.2-homework/"
filename = "chr1.GRCh38.excerpt.fasta"
sequences = read_fasta(directory + filename)
human_chr1 = "".join(sequences)

t = human_chr1


p = "GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG"

naive_occurences, naive_alignments, naive_comparisons = naive_counts(p, t)
print(f"1. Naive exact matching tries {naive_alignments} alignments.")
print(f"2. Naive exact matching compares {naive_comparisons} characters.")

p_bm = BoyerMoore(p)
bm_occurences, bm_alignments, bm_comparisons = bm_counts(p, p_bm, t)
print(f"3. Boyer-Moore tried {bm_alignments} alignments.")

p = "GGCGCGGTGGCTCACGCCTGTAAT"
n = 2

index = Index(t, 8)
indexed_matches, indexed_hits = indexed_approximate_match(p, t, index, n)
print(f"4. Indexed approximate matching found {len(indexed_matches)} matches.")
print(f"5. Indexed approximate matching scored {indexed_hits} index hits.")


p = "GGCGCGGTGGCTCACGCCTGTAAT"
k = 8
ival = 3
n = 2

subseq_index = SubseqIndex(t, k, ival)

occurrences, num_index_hits = subseq_approximate_match(p, t, subseq_index, n)

print(f"6. Using a subsequence index, {num_index_hits} index hits were found when querying T for {p}.")