import os
import gensim
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def read_files(file_list):
    """Read and tag the content of each file."""
    documents = []
    for file_path in file_list:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        documents.append(TaggedDocument(words=content.split(), tags=[file_path]))
    return documents

def train_doc2vec_model(documents):
    """Train a Doc2Vec model."""
    model = Doc2Vec(vector_size=100, window=2, min_count=1, workers=4, epochs=40)
    model.build_vocab(documents)
    model.train(documents, total_examples=model.corpus_count, epochs=model.epochs)
    return model

def deduplicate_doc2vec(file_list):
    """Deduplicate files using Doc2Vec."""
    documents = read_files(file_list)
    model = train_doc2vec_model(documents)

    # Get vectors for each document
    vectors = np.array([model.dv[tag] for tag in model.dv.index_to_key])

    # Calculate cosine similarity matrix
    cosine_sim = cosine_similarity(vectors)

    duplicates = []
    threshold = 0.9  # Similarity threshold for identifying duplicates

    for i in range(len(file_list)):
        for j in range(i + 1, len(file_list)):
            if cosine_sim[i, j] >= threshold:
                duplicates.append((file_list[i], file_list[j]))

    return duplicates

# Example usage
file_list = ['file1.txt', 'file2.txt', 'file3.txt']  # Add your text files here
duplicates = deduplicate_doc2vec(file_list)
print("Duplicate files:", duplicates)
