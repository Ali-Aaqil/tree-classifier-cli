from pathlib import Path

def list_images(folder_path):
    # Convert to Path object
    folder = Path(folder_path)

    # Loop through all .jpg and .png files (case-insensitive)
    for image_file in folder.glob("*"):
        if image_file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            print(image_file.name)

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ").strip()
    list_images(folder_path)