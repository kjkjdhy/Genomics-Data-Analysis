from Bio.Seq import Seq

# Define Original DNA Sequence
original_dna = Seq("ATGCGTACGTAGCTAGCTAGCGATCGTACGATCGTAGCTAGCTAGTACG")

# Introduce a Mutation (Change 'T' to 'A' at position 10)
mutated_dna = original_dna[:10] + "A" + original_dna[11:]

# Translate DNA to Protein
original_protein = original_dna.translate()
mutated_protein = mutated_dna.translate()

# Display Results
print(f"Original DNA: {original_dna}")
print(f"Mutated DNA:  {mutated_dna}\n")
print(f"Original Protein: {original_protein}")
print(f"Mutated Protein:  {mutated_protein}")

# Save output to a file
with open("mutation_results.txt", "w") as file:
    file.write(f"Original DNA: {original_dna}\n")
    file.write(f"Mutated DNA: {mutated_dna}\n\n")
    file.write(f"Original Protein: {original_protein}\n")
    file.write(f"Mutated Protein: {mutated_protein}\n")
