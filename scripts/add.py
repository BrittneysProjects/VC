import json
import os

# User can add name and favourite sport in response.json
# Default sport "Cricket" will be added in case user does not provide a favorite sport

def load_json(filename='../response.json'):
    # Ensure the file exists before trying to open it
    if os.path.exists(filename):
        with open(filename) as json_obj:
            response = json.load(json_obj)
    else:
        # Return an empty dictionary if the file does not exist
        response = {}
    return response

def write_json(data, filename='../response.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=0)

def call_sport():
    response = load_json()  # Load existing data
    name = input("Please add your name: ").strip()  # Remove any leading/trailing whitespace
    sport = input("Please add your favourite sports name: ").strip()  # Remove any leading/trailing whitespace
    
    if not sport:  # If no sport is provided, default to 'Cricket'
        sport = 'Cricket'
        
    if name:  # Ensure a name is provided
        response[name] = sport  # Update the response dictionary
        write_json(response)  # Write the updated data back to the JSON file
    else:
        print("Name cannot be empty.")

# Example usage
if __name__ == "__main__":
    call_sport()
