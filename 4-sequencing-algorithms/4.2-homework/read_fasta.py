#!/usr/bin/env python

"""read_fasta.py: unpacks fasta sequences into a list."""

__author__ = "Hamish McLean"


def read_fasta(filename):
    ''''Reads a FASTA file and returns a list of sequences.'''
    sequences = []
    with open(filename) as fasta:
        while True:
            seq = fasta.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
    return sequences[1:]