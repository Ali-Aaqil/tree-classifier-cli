from pathlib import Path

def list_images(folder_path):
    # Convert to Path object
    folder = Path(folder_path)

    # Loop through all .jpg and .png files (case-insensitive)
    for image_file in folder.glob("*"):
        if image_file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            print(image_file.name)
            #todo apply image scanning technique, recieve output, right now we just return a debug object
            scan_result = {
                'file_name': image_file.name,
                'tree_status': 'Yes'
            }
            #pass output to write function
            print(scan_result)
            
            
            write_results(scan_result['file_name'], scan_result['tree_status'])



# todo
# Given a scanned image output, i want to update an output file (txt file) with the image file name and whether there is a tree in said image

def write_results(file_name, tree_status):
    #todo remove static write location
    output_file = "C:\\scratch\\outputs\\output.txt"
    output_path = Path(output_file)

    filename = file_name
    treestatus = tree_status

    with open(output_path, 'a') as outputfile:
        outputfile.write(f"File: {filename}, Status: {treestatus}\n")


if __name__ == "__main__":
    #write_results("test1", "Yes")
    folder_path = input("Enter the path to the folder: ").strip()
    list_images(folder_path)