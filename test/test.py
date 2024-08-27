import json
import sys
import os

# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.add import load_json

def add_function(json_obj):
    response = json.load(json_obj)
    # ... rest of your code

def save_data(data, file):
    json.dump(data, file, indent=0)

def test_load_json():
    response = load_json()
    assert isinstance(response, dict)
    assert response.get("Data Glacier") == "Cricket"
