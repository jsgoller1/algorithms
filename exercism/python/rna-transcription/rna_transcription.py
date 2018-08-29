"""
See README for exercise description.
---
Understand:

In this problem, we need to replace specific characters
in the string with other characters as defined by the mapping
in the README. Our input will be a DNA string, and our output
will be an RNA string with each character replaced by its complement.

----
Plan:

The solution here is super simple - start with an empty RNA string,
loop through the DNA string, and append the complementary nucleotide
to the RNA string for each DNA nucleotide.

----
Execute - see below.
----
Review: This problem was very simple, as it just involved
appending to a string the result of a dictionary lookup. It is O(N)
for time since every character of the DNA string must be examined, and
O(N) for space as we must produce an RNA string equally as long as the input
string.
"""

DNA_TO_RNA = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}


def to_rna(dna_strand):
    rna_strand = ""
    for nuc in dna_strand:
        rna_strand += DNA_TO_RNA[nuc]
    return rna_strand
