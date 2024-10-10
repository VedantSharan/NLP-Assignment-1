import os


def read_text_files(directory):
    """
    Reads all text files in the given directory and returns a list of file paths and corresponding content.

    Args:
    directory (str): Path to the directory containing text files.

    Returns:
    file_paths (list of str): List of file paths.
    file_contents (list of str): List of file contents.
    """
    file_paths = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.txt')]
    file_contents = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents.append(file.read())
    return file_paths, file_contents


def create_shingles(text, k):
    """
    Creates a set of shingles (k-grams) from the input text.

    Args:
    text (str): The text to shingle.
    k (int): The number of words in each shingle.

    Returns:
    set of tuples: A set of shingles (tuples of words).
    """
    words = text.split()  # Split the text into words
    shingles = set()
    for i in range(len(words) - k + 1):
        shingle = tuple(words[i:i + k])  # Create a shingle of length k
        shingles.add(shingle)
    return shingles


def jaccard_similarity(shingles1, shingles2):
    """
    Computes the Jaccard similarity between two sets of shingles.

    Args:
    shingles1 (set of tuples): The set of shingles from the first document.
    shingles2 (set of tuples): The set of shingles from the second document.

    Returns:
    float: Jaccard similarity score between 0 and 1.
    """
    intersection = len(shingles1.intersection(shingles2))
    union = len(shingles1.union(shingles2))
    if union == 0:
        return 0
    return intersection / union


def deduplicate_documents(file_contents, file_paths, k=5, threshold=0.8):
    """
    Identifies duplicate documents based on shingling and Jaccard similarity.

    Args:
    file_contents (list of str): List of document contents.
    file_paths (list of str): List of file paths corresponding to the documents.
    k (int): Length of shingles (default is 5 words).
    threshold (float): Similarity threshold above which documents are considered duplicates (default is 0.8).

    Returns:
    unique_files (list of str): List of file paths corresponding to unique documents.
    duplicates (list of tuple): List of tuples containing pairs of duplicate file paths.
    """
    unique_files = []
    duplicates = []
    shingle_sets = [create_shingles(content, k) for content in file_contents]

    n = len(file_contents)
    duplicate_flags = [False] * n  # Keeps track of which files have been marked as duplicates

    for i in range(n):
        if not duplicate_flags[i]:  # Only check if the document hasn't been marked as a duplicate
            unique_files.append(file_paths[i])
            for j in range(i + 1, n):
                if not duplicate_flags[j]:
                    similarity = jaccard_similarity(shingle_sets[i], shingle_sets[j])
                    if similarity >= threshold:  # Compare document i with document j
                        duplicate_flags[j] = True
                        duplicates.append((file_paths[i], file_paths[j]))  # Mark as duplicate pair

    return unique_files, duplicates


def save_results(unique_files, duplicates, output_dir):
    """
    Saves the unique files and duplicates list to an output directory.

    Args:
    unique_files (list of str): List of unique file paths.
    duplicates (list of tuple): List of tuples of duplicate file paths.
    output_dir (str): Path to the directory where results will be saved.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Write unique file paths to a file
    with open(os.path.join(output_dir, 'unique_files.txt'), 'w', encoding='utf-8') as f:
        for file_path in unique_files:
            f.write(file_path + '\n')

    # Write duplicate file pairs to a file
    with open(os.path.join(output_dir, 'duplicates.txt'), 'w', encoding='utf-8') as f:
        for dup_pair in duplicates:
            f.write(f'{dup_pair[0]} -- {dup_pair[1]}\n')


# Example Usage:
if __name__ == '__main__':
    directory = 'path_to_your_text_files'
    output_directory = 'deduplication_results'

    # Step 1: Read all text files from the directory
    file_paths, file_contents = read_text_files(directory)

    # Step 2: Deduplicate documents based on shingling and Jaccard similarity
    unique_files, duplicates = deduplicate_documents(file_contents, file_paths, k=5, threshold=0.8)

    # Step 3: Save the results (unique documents and duplicates) to the output directory
    save_results(unique_files, duplicates, output_directory)
