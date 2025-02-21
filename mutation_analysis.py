from Bio.Seq import Seq

# Define Original DNA Sequence (length must be a multiple of 3)
original_dna = Seq("ATGCGTACGTAGCTAGCTAGCGATCGTACGATCGTAGCTAGCTAGTAC")

# Introduce a Mutation (Change 'T' to 'C' at position 9)
mutated_dna = original_dna[:9] + "C" + original_dna[10:]

# Ensure length is still a multiple of 3
if len(mutated_dna) % 3 != 0:
    mutated_dna += "A"  # Append 'A' to maintain a multiple of 3 if needed

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
