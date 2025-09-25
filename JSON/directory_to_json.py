import os
import json

def create_directory_json(path):
    result = {'name': os.path.basename(path), 'type': 'folder', 'children': []}

    if not os.path.isdir(path):
        return result
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if os.path.isdir(entry_path):
            result['children'].append(create_directory_json(entry_path))
        else:
            result['children'].append({'name': entry, 'type': 'file'})

    return result

def main():
    path = input("Enter Directory Path: ")
    print("Path: ", path)
    directory = create_directory_json(path)

    with open('directory.json', 'w') as outfile:
        json.dump(directory, outfile, indent=4)

if __name__ == "__main__":
    main()