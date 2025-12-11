import helpers
import json


def task_6(mode="evaluate"):
    """
    Goal:
        Evaluate the Recall of the Insight extraction using LLM-as-a-Judge (Predict and Evaluate)
    Instructions:
        - Load the user query from the file outputs/task_4_groundtruth.json
        - Load the groundtruth answers from the file outputs/task_4_groundtruth.json
        - Load the predicted insights from the file outputs/task_5_insights.json
        - Evaluate the recall of the predicted insights using the groundtruth answers
        - Save the evaluation report to the file outputs/task_6_evaluation_report.json
    """
    # YOUR CODE HERE
