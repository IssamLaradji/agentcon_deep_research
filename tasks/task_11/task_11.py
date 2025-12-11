from flask import Flask, jsonify, render_template, request

import helpers

app = Flask(__name__)

CHUNK_PATH = "outputs/task_8_chunks.json"
EMBEDDING_PATH = "outputs/task_8_embeddings.pkl"
OUTPUT_PATH = "outputs/task_11.json"


def task_11():
    """
    Goal:
        Launch the Flask app which looks like Google with a nicer background where the user types a user query and outputs the insights and citations from the 3 files
    Instructions for task 11:
        - Create a Flask app with a query endpoint that returns insights and citations based on a user query.
        - Use the RAG mechanisms from tasks 8, 9, 10
        - You can copy paste the relevant code from those tasks into small helper functions here
        - Save the outputs in task_11.json
    """
    # YOUR CODE HERE


if __name__ == "__main__":
    task_11()
