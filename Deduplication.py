import os
from simhash import Simhash, SimhashIndex


def read_file(filepath):
    """Reads the content of a file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def compute_simhash(text):
    """Computes the Simhash for the given text."""
    return Simhash(text)


def deduplicate_files(directory, threshold=3):
    """Deduplicates text files in the specified directory using Simhash."""
    simhashes = {}
    duplicates_to_remove = []

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            # Read file content
            content = read_file(filepath)

            # Compute Simhash
            file_simhash = compute_simhash(content)

            # Check for duplicates
            is_duplicate = False
            for existing_file, existing_simhash in simhashes.items():
                hamming_distance = file_simhash.distance(existing_simhash)
                if hamming_distance <= threshold:
                    print(f"Duplicate found: {filename} is similar to {existing_file} "
                          f"(Hamming distance: {hamming_distance})")
                    # Add the current duplicate to the list to be removed
                    duplicates_to_remove.append(filepath)
                    is_duplicate = True
                    break

            if not is_duplicate:
                simhashes[filename] = file_simhash

    return duplicates_to_remove


# Set your directory path containing text files
directory = fr"C:\Users\surri\PycharmProjects\NLP\PublicTV"

# Deduplicate files
duplicates = deduplicate_files(directory)

# Remove one of the duplicates (keeping the first file encountered)
for duplicate_file in duplicates:
    os.remove(duplicate_file)
    print(f"Removed: {duplicate_file}")
