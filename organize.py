import os
import shutil
import sys

def organize_voc_dataset(source_dir):
    """
    Organizes a VOC dataset into the correct structure for FiftyOne:
    - Images go into {source_dir}/data/
    - XML annotations go into {source_dir}/labels/
    
    Args:
        source_dir: Directory containing the image and XML files
    """
    # Create data and labels directories if they don't exist
    data_dir = os.path.join(source_dir, "data")
    labels_dir = os.path.join(source_dir, "labels")
    
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(labels_dir, exist_ok=True)
    
    # Counter for files moved
    images_moved = 0
    annotations_moved = 0
    skipped_files = 0
    
    # Process all files in the source directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        
        # Skip directories and the data/labels directories themselves
        if os.path.isdir(source_path):
            continue
            
        # Process image files
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            dest_path = os.path.join(data_dir, filename)
            shutil.move(source_path, dest_path)  # Changed to move
            images_moved += 1
            print(f"Moved image: {filename} to data/")
            
        # Process XML annotation files
        elif filename.lower().endswith('.xml'):
            dest_path = os.path.join(labels_dir, filename)
            shutil.move(source_path, dest_path)  # Changed to move
            annotations_moved += 1
            print(f"Moved annotation: {filename} to labels/")
            
        else:
            skipped_files += 1
            print(f"Skipped file (not an image or XML): {filename}")
    
    print("\nSummary:")
    print(f"Images moved to data/: {images_moved}")
    print(f"Annotations moved to labels/: {annotations_moved}")
    print(f"Files skipped: {skipped_files}")
    
    if images_moved != annotations_moved:
        print("\nWARNING: The number of images and annotations doesn't match.")
        print("Each image should have a corresponding XML file with the same base name.")
    
    print("\nDataset organization complete. You can now use FiftyOne with:")
    print(f"""
import fiftyone as fo

dataset = fo.Dataset.from_dir(
    dataset_dir="{source_dir}",
    dataset_type=fo.types.VOCDetectionDataset,
    name="cctv_gun_detection"
)

session = fo.launch_app(dataset)
    """)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        source_directory = sys.argv[1]
    else:
        source_directory = input("Enter the path to your dataset directory: ")
    
    organize_voc_dataset(source_directory)
