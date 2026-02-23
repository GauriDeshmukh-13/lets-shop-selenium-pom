import json
import os


def load_test_data(filename):
    file_path = os.path.join(os.path.dirname(__file__), "..", "testdata", filename)

    with open(file_path) as f:
        data = json.load(f)

    return data
