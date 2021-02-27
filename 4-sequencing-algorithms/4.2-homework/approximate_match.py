#!/usr/bin/env python

"""appproximate_match.py includes functions for approximate matching using a text index or Boyer-Moore.

- indexed_approximate_match() uses a kmer index.
- bm_approximate_match() uses Boyer-Moore.
- subseq_approximate_match() uses a subsequence index.
"""

__author__ = "Hamish McLean"


from bm_preproc import BoyerMoore
from boyer_moore import boyer_moore


def indexed_approximate_match(p, t, index, n):
    """Find the occurences of pattern, p, in text, t, within a hamming distance, n, using a kmer index.
    """
    segment_length = int(round(len(p) / (n+1)))
    all_matches = set()
    total_hits = 0
    for i in range(n+1):
        start = i*segment_length
        end = min((i+1)*segment_length, len(p))
        hits = index.query(p[start:end])
        total_hits += len(hits)
        for hit in hits:
            if hit < start or hit-start+len(p) > len(t):
                continue
            mismatches = 0
            for j in range(0, start):
                if not p[j] == t[hit-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            for j in range(end, len(p)):
                if not p[j] == t[hit-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            if mismatches <= n:
                all_matches.add(hit - start)
    return list(all_matches), total_hits


def bm_approximate_match(p, t, n):
    """Find the occurences of pattern, p, in text, t, within a hamming distance, n, using Boyer-Moore.
    """
    segment_length = int(round(len(p) / (n+1)))
    all_matches = set()
    for i in range(n+1):
        start = i*segment_length
        end = min((i+1)*segment_length, len(p))
        p_bm = BoyerMoore(p[start:end], alphabet='ACGT')
        matches = boyer_moore(p[start:end], p_bm, t)
        # Extend matching segments to see if whole p matches
        for m in matches:
            if m < start or m-start+len(p) > len(t):
                continue
            mismatches = 0
            for j in range(0, start):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            for j in range(end, len(p)):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            if mismatches <= n:
                all_matches.add(m - start)
    return list(all_matches)



def subseq_approximate_match(p, t, index, n):
    """Find the occurences of pattern, p, in text, t, within a hamming distance, n, using a subsequence index.
    """
    total_hits = 0
    all_matches = set()
    for i in range(n+1):
        start = i
        end = min(i+index.span, len(p))
        hits = index.query(p[i:end])
        total_hits += len(hits)
        for hit in hits:
            if hit < start or hit-start+len(p) > len(t):
                continue
            mismatches = 0
            for j in range(0, start):
                if not p[j] == t[hit-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            for j in range(end, len(p)):
                if not p[j] == t[hit-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            if mismatches <= n:
                all_matches.add(hit - start)
    return list(all_matches), total_hits