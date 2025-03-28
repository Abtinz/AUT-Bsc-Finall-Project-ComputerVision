import os
import shutil

def process_and_merge_dataset(dataset_paths, final_dataset_path):
    """
    Updates labels and merges datasets into a structured final dataset folder.

    Arguments:
    - dataset_paths: A dictionary containing keys ('train', 'test', 'valid') with
                     sub-dictionaries for 'labels' and 'images' paths.
    - final_dataset_path: Path to the final dataset (e.g., "final_data_set").
    """

    for dataset_type, paths in dataset_paths.items():
        src_label_folder = paths['labels']
        src_image_folder = paths['images']
        
        final_labels_folder = os.path.join(final_dataset_path, dataset_type, "labels")
        final_images_folder = os.path.join(final_dataset_path, dataset_type, "images")

        for filename in os.listdir(src_label_folder):
            label_file_path = os.path.join(src_label_folder, filename)
            image_file_path = os.path.join(src_image_folder, filename.replace(".txt", ".jpg"))  # Corresponding image file

            if os.path.isfile(label_file_path) and label_file_path.endswith(".txt"):
                with open(label_file_path, "r") as file:
                    lines = file.readlines()

                modified_lines = []
                
                for line in lines:

                    parts = line.strip().split()
                    
                    if parts[0] == 'index-n':
                        parts[0] = 'changing-index'

                    
                    modified_lines.append(" ".join(parts) + "\n")

                # here we will update labels to integrate with final dataset and wil write it directly in  final_label_path
                final_label_path = os.path.join(final_labels_folder, filename)
                with open(final_label_path, "w") as file:
                    file.writelines(modified_lines)

                print(f"Updated labels and copied: {final_label_path}")

                # here we will copy image if it exists
                if os.path.isfile(image_file_path):
                    final_image_path = os.path.join(final_images_folder, os.path.basename(image_file_path))
                    shutil.copy2(image_file_path, final_image_path)
                    print(f"Copied image: {final_image_path}")
dataset_paths = {
    "train": {
        "labels": "C:\\Users\\abt\\Documents\\Real-time-obstacle-detector\\data sets\\Bench Detector.v1i.yolov8\\train\\labels",
        "images": "C:\\Users\\abt\\Documents\\Real-time-obstacle-detector\\data sets\\Bench Detector.v1i.yolov8\\train\\images",
    },
    "test": {
        "labels": "C:\\Users\\abt\\Documents\\Real-time-obstacle-detector\\data sets\\Bench Detector.v1i.yolov8\\test\\labels",
        "images": "C:\\Users\\abt\\Documents\\Real-time-obstacle-detector\\data sets\\Bench Detector.v1i.yolov8\\test\\images",
    },
    "valid": {
        "labels": "C:\\Users\\abt\\Documents\\Real-time-obstacle-detector\\data sets\\Bench Detector.v1i.yolov8\\valid\\labels",
        "images": "C:\\Users\\abt\\Documents\\Real-time-obstacle-detector\\data sets\\Bench Detector.v1i.yolov8\\valid\\images",
    }
}

final_dataset_path = "C:\\Users\\abt\\Documents\\Real-time-obstacle-detector\\data sets\\dataset\\dataset"

process_and_merge_dataset(dataset_paths, final_dataset_path)
