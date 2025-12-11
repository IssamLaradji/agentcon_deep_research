import helpers


def task_8():
    """
    Goal:
        Chunk the three needle-in-haystack files, embed every chunk, and save the data for retrieval.
    Instructions:
        - Load the three needle-in-haystack files from the outputs/task_7_file_1.txt, outputs/task_7_file_2.txt, and outputs/task_7_file_3.txt
        - Chunk the three files into chunks of 64 tokens with 12 token overlap
        - Embed each chunk using Sentence Transformers
        - Save the chunks and embeddings to the outputs/task_8_chunks.json and outputs/task_8_embeddings.pkl
    """

    # YOUR CODE HERE
