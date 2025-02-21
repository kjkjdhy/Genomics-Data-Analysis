from Bio.Seq import Seq

# Define Original DNA Sequence
original_dna = Seq("ATGCGTACGTAGCTAGCTAGCGATCGTACGATCGTAGCTAGCTAGTACG")

# Ensure the sequence length is a multiple of 3
trimmed_dna = original_dna[: len(original_dna) - (len(original_dna) % 3)]

# Introduce a Mutation (Change 'T' to 'A' at position 10)
mutated_dna = trimmed_dna[:10] + "A" + trimmed_dna[11:]

# Translate DNA to Protein
original_protein = trimmed_dna.translate()
mutated_protein = mutated_dna.translate()

# Display Results
print(f"Original DNA: {trimmed_dna}")
print(f"Mutated DNA:  {mutated_dna}\n")
print(f"Original Protein: {original_protein}")
print(f"Mutated Protein:  {mutated_protein}")

# Save output to a file
with open("mutation_results.txt", "w") as file:
    file.write(f"Original DNA: {trimmed_dna}\n")
    file.write(f"Mutated DNA: {mutated_dna}\n\n")
    file.write(f"Original Protein: {original_protein}\n")
    file.write(f"Mutated Protein: {mutated_protein}\n")
