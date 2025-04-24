from pathlib import Path
from imageai.Classification import ImageClassification
import os

def image_analysis(image_file):
    
    execution_path = os.getcwd()
    prediction = ImageClassification()
    prediction.setModelTypeAsResNet50()
    prediction.setModelPath(os.path.join(execution_path, "resnet50-19c8e357.pth"))
    prediction.loadModel()

    predictions, probabilities = prediction.classifyImage(str(image_file), result_count=5 )
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)

def list_images(folder_path, output_path):
    # Convert to Path object
    folder = Path(folder_path)

    # Loop through all .jpg and .png files (case-insensitive)
    for image_file in folder.glob("*"):
        if image_file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            print(image_file.name)
            #todo apply image scanning technique, recieve output, right now we just return a debug object
            analysis = image_analysis(image_file)
            scan_result = {
                'file_name': image_file.name,
                'tree_status': 'Yes'
            }
            #pass output to write function
            print(scan_result)
            
            
            write_results(scan_result['file_name'], scan_result['tree_status'], output_path)

# todo
# Given a scanned image output, i want to update an output file (txt file) with the image file name and whether there is a tree in said image

def write_results(file_name, tree_status, output_path):
    #todo remove static write location
    output_file = f"{output_path}\\output.txt"
    output_path = Path(output_file)

    filename = file_name
    treestatus = tree_status

    with open(output_path, 'a') as outputfile:
        outputfile.write(f"File: {filename}, Status: {treestatus}\n")


if __name__ == "__main__":
    #write_results("test1", "Yes")
    folder_path = input("Enter the path to the folder: ").strip()
    output_path = input("Enter an output folder path: ").strip()
    list_images(folder_path, output_path)