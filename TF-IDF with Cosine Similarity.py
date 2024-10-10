from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
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


def compute_tfidf_matrix(corpus):
    """
    Computes the TF-IDF matrix for a given list of documents.

    Args:
    corpus (list of str): List of document contents.

    Returns:
    tfidf_matrix (scipy.sparse.csr_matrix): The TF-IDF matrix where rows represent documents and columns represent terms.
    vectorizer (TfidfVectorizer): The fitted TF-IDF vectorizer.
    """
    vectorizer = TfidfVectorizer(stop_words='english',
                                 max_features=5000)  # You can adjust max_features for large corpora
    tfidf_matrix = vectorizer.fit_transform(corpus)
    return tfidf_matrix, vectorizer


def compute_cosine_similarity(tfidf_matrix):
    """
    Computes the cosine similarity matrix for the given TF-IDF matrix.

    Args:
    tfidf_matrix (scipy.sparse.csr_matrix): The TF-IDF matrix.

    Returns:
    similarity_matrix (numpy.ndarray): Cosine similarity matrix where each element (i, j) represents
                                       the cosine similarity between document i and document j.
    """
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix


def deduplicate_documents(similarity_matrix, file_paths, threshold=0.95):
    """
    Identifies duplicate documents based on cosine similarity and removes duplicates.

    Args:
    similarity_matrix (numpy.ndarray): Cosine similarity matrix.
    file_paths (list of str): List of file paths corresponding to the documents.
    threshold (float): Similarity threshold above which documents are considered duplicates. Default is 0.95.

    Returns:
    unique_files (list of str): List of file paths corresponding to unique documents.
    duplicates (list of tuple): List of tuples containing pairs of duplicate file paths.
    """
    n = similarity_matrix.shape[0]
    unique_files = []
    duplicates = []
    duplicate_flags = [False] * n  # Keeps track of which files have been marked as duplicates

    for i in range(n):
        if not duplicate_flags[i]:  # Only check if the document hasn't been marked as a duplicate
            unique_files.append(file_paths[i])
            for j in range(i + 1, n):
                if similarity_matrix[i, j] >= threshold:  # Compare document i with document j
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

    # Step 2: Compute the TF-IDF matrix for all documents
    tfidf_matrix, vectorizer = compute_tfidf_matrix(file_contents)

    # Step 3: Compute cosine similarity between all document pairs
    similarity_matrix = compute_cosine_similarity(tfidf_matrix)

    # Step 4: Deduplicate documents based on similarity threshold
    unique_files, duplicates = deduplicate_documents(similarity_matrix, file_paths, threshold=0.95)

    # Step 5: Save the results (unique documents and duplicates) to the output directory
    save_results(unique_files, duplicates, output_directory)
