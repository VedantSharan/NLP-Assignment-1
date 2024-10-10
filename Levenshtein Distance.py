from Levenshtein import distance


def deduplicate_levenshtein(corpus, threshold=50):
    """
    Deduplicates documents in a corpus using Levenshtein distance as a measure of similarity.

    Args:
    corpus (list of str): A list containing the text of all documents.
    threshold (int): Maximum allowed Levenshtein distance for two documents to be considered duplicates.
                     A lower threshold means stricter deduplication (default is 50).

    Returns:
    unique_docs (list of int): A list of indices of unique documents in the corpus.
    duplicates (list of tuple): A list of tuples where each tuple contains the indices of duplicate documents.
    """
    unique_docs = []  # List to store the indices of unique documents
    duplicates = []  # List to store the duplicate document pairs

    # Iterate over all documents in the corpus
    for i, doc_i in enumerate(corpus):
        is_unique = True  # Assume the current document is unique

        # Compare the current document with all already identified unique documents
        for j in unique_docs:
            doc_j = corpus[j]

            # Calculate Levenshtein distance between the current document and a unique document
            dist = distance(doc_i, doc_j)

            # If the distance is below the threshold, they are considered duplicates
            if dist <= threshold:
                duplicates.append((i, j))  # Store the pair of duplicates
                is_unique = False  # Mark the current document as not unique
                break  # No need to check further unique docs if it's a duplicate

        # If the document is unique, add it to the unique_docs list
        if is_unique:
            unique_docs.append(i)

    return unique_docs, duplicates


def save_results(unique_docs, duplicates, corpus, output_dir):
    """
    Saves the deduplication results, i.e., unique documents and duplicate pairs, to the output directory.

    Args:
    unique_docs (list of int): Indices of unique documents in the corpus.
    duplicates (list of tuple): List of pairs of duplicate documents' indices.
    corpus (list of str): Original list of document texts.
    output_dir (str): Directory to save the results.
    """
    import os
    os.makedirs(output_dir, exist_ok=True)

    # Write unique documents to a file
    with open(os.path.join(output_dir, 'unique_docs.txt'), 'w', encoding='utf-8') as f:
        for idx in unique_docs:
            f.write(f"Document {idx}:\n{corpus[idx]}\n\n")

    # Write duplicate pairs to a file
    with open(os.path.join(output_dir, 'duplicates.txt'), 'w', encoding='utf-8') as f:
        for dup_pair in duplicates:
            f.write(f"Document {dup_pair[0]} is a duplicate of Document {dup_pair[1]}\n")


# Example Usage:
if __name__ == '__main__':
    corpus = ["first.txt","second.txt"]

    # Step 1: Deduplicate the corpus using Levenshtein distance
    unique_docs, duplicates = deduplicate_levenshtein(corpus, threshold=20)

    # Step 2: Save the deduplication results
    save_results(unique_docs, duplicates, corpus, output_dir='deduplication_results')
