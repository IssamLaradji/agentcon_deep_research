from flask import Flask, jsonify, render_template, request

import helpers

app = Flask(__name__)

CHUNK_PATH = "outputs/task_8_chunks.json"
EMBEDDING_PATH = "outputs/task_8_embeddings.pkl"
OUTPUT_PATH = "outputs/task_12.json"


def task_12():
    """
    Goal:
        Make the Flask app more of a notebook style where after outputting the insights and citations from the 3 files, the user can ask a follow up question and the system will output the insights and citations from the 3 files again.
    Instructions for task 12:
        - Create a Flask app with a query endpoint that returns insights and citations based on a user query and then after the user has seen the insights and citations, the user can ask a follow up question and the system will output the insights and citations from the 3 files again.
        - Use the RAG mechanisms from tasks 8, 9, 10
        - You can copy paste the relevant code from those tasks into small helper functions here
        - It should be a notebook style so the search bar should re-appear after the user has seen the insights and citations everytime
        - Save the outputs in task_12.json
    """
    # YOUR CODE HERE
