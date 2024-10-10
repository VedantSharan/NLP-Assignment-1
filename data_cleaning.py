import os
import concurrent.futures
from multiprocessing import cpu_count


# Function to load bad words from a file (one word per line)
def load_bad_words(bad_words_file):
    with open(bad_words_file, 'r', encoding='utf-8') as file:
        bad_words = [line.strip() for line in file if line.strip()]
    return bad_words


# Function to check if any bad word is present in the text
def contains_bad_word(text, bad_words):
    for word in bad_words:
        if word in text:
            return True
    return False


# Function to check and delete files containing bad words
def process_file(file_path, bad_words):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        # Check if content contains any bad words
        if contains_bad_word(content, bad_words):
            print(f"Deleting file: {file_path} (contains bad words)")
            os.remove(file_path)
            return file_path  # Return the deleted file name for confirmation


# Function to get all .txt files from the directory
def get_txt_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".txt")]


# Multi-threading worker for handling each file
def thread_worker(file_paths, bad_words):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda file_path: process_file(file_path, bad_words), file_paths)


# Multi-processing function to distribute work across cores
def parallel_process(directory, bad_words):

    all_files = get_txt_files(directory)

    cpu_cores = cpu_count()
    chunk_size = len(all_files) // cpu_cores

    # Distribute files to different processes
    with concurrent.futures.ProcessPoolExecutor() as executor:
        chunks = [all_files[i:i + chunk_size] for i in range(0, len(all_files), chunk_size)]
        executor.map(lambda chunk: thread_worker(chunk, bad_words), chunks)


# Run the parallel process
if __name__ == '__main__':
    directory = 'path_to_your_directory'
    bad_words_file = 'kannada_bad_words.txt'

    bad_words = load_bad_words(bad_words_file)

    parallel_process(directory, bad_words)
