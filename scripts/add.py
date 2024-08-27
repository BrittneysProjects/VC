import json
import os

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Function to load the JSON data
def load_json():
    # Use an absolute path to open the file
    with open(os.path.join(BASE_DIR, '../response.json')) as json_obj:
        response = json.load(json_obj)
    return response

# Function to write data to the JSON file
def write_json(data, filename=os.path.join(BASE_DIR, '../response.json')):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=0)

# Function to prompt user for name and favorite sport
def call_sport():
    name = input("Please add your name: ")
    sport = input("Please add your favourite sports name: ")
    if sport == "":
        sport = 'Cricket'
    if name:
        response[name] = sport
        write_json(response)

if __name__ == "__main__":
    response = load_json()  # Load JSON only when the script is executed directly
    call_sport()
