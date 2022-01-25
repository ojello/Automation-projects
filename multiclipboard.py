import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

# Creates json file
def save_data(filepath, data):
    # opening filepath, then creates a new file or override a file if it exists
    with open(filepath, "w") as f:
        # dump data into file 'f' and creates the file
        json.dump(data, f)

# Reads json file
def load_data(filepath):
    # load file
    try:
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    # if file doesn't exist, return empty dictionary
    except:
        return {}


# if the length is two arguments:
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA) 

    if command =="save":
        # asks user for the key
        key = input("Enter a key: ")
        # stores the key associated with whatever value is associated with the clipboard 
        data[key] = clipboard.paste()
        # calls saved_data, and rewrites the file and saves all of the data
        save_data(SAVED_DATA, data)

        print("Data saved!")
    elif command == "load":
        # ask user for the key
        key = input("Enter a key: ")
        # check if key exists in the dictionary
        if key in data:
            # copy data to clipboard
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")

    elif command == "list":
        print(data)
    else:
        print("Unknown command")
    
else:
    print("Please pass exactly one command.")




