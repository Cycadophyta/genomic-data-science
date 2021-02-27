#!/usr/bin/env python

"""naive_counts.py: Naive exact matching with counts of character comparisons and alignments tried."""

__author__ = "Hamish McLean"

def naive_counts(p, t):
    '''Finds the positions of all exact matches of p in t.'''
    occurrences = []
    character_comparisons = 0
    alignments_tried = 0
    for i in range(len(t) - len(p) + 1):
        alignments_tried += 1
        match = True
        for j in range(len(p)):
            character_comparisons += 1
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences, alignments_tried, character_comparisons