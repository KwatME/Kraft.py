def reverse_complement_dna_sequence(dna_sequence):

    dna_complement = {"A": "T", "T": "A", "C": "G", "G": "C", "N": "N"}

    return "".join(dna_complement[dna] for dna in reversed(dna_sequence))
