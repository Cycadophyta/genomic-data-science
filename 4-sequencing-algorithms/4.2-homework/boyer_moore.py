#!/usr/bin/env python

"""boyer_moore.py: Boyer-Moore matching with counts of character comparisons and alignments tried."""

__author__ = "Hamish McLean"


def boyer_moore(p, p_bm, t):
    """Do Boyer-Moore matching to find occurences of p in t using a preprocessed tables, p_bm."""
    i = 0
    occurrences = []
    while i < len(t) - len(p) + 1:
        shift = 1
        mismatched = False
        for j in range(len(p)-1, -1, -1):
            if p[j] != t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift
    return occurrences


def bm_counts(p, p_bm, t):
    """Do Boyer-Moore matching to find occurences of p in t using a preprocessed tables, p_bm. Also count alignments and character comparisons.
    """
    i = 0
    occurrences = []
    alignments_tried = 0
    character_comparisons = 0
    while i < len(t) - len(p) + 1:
        shift = 1
        mismatched = False
        for j in range(len(p)-1, -1, -1):
            character_comparisons += 1
            if p[j] != t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift
        alignments_tried += 1
    return occurrences, alignments_tried, character_comparisons