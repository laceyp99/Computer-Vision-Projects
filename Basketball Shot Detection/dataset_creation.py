import os
import pathlib
import random

# Find the root directory of the script
root_dir = pathlib.Path(__file__).resolve().parent

# Define directories for frames and labels where the dataset is currently stored
frames_dir = os.path.join(root_dir, 'frames')
labels_dir = os.path.join(root_dir, 'labels')

# Create directories for train and eval splits
train_images_dir = os.path.join(root_dir, 'datasets/images/train')
eval_images_dir = os.path.join(root_dir, 'datasets/images/val')
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(eval_images_dir, exist_ok=True)

train_labels_dir = os.path.join(root_dir, 'datasets/labels/train')
eval_labels_dir = os.path.join(root_dir, 'datasets/labels/val')
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(eval_labels_dir, exist_ok=True)

random.seed(42)  # For reproducibility

# Function to create train and eval splits
def create_split(data_dir, split_ratio=0.8):
    all_files = sorted(os.listdir(data_dir))
    random.shuffle(all_files)  # Shuffle the files for randomness
    split_index = int(len(all_files) * split_ratio)
    train_files = all_files[:split_index]
    eval_files = all_files[split_index:]
    return train_files, eval_files

# Function to move files from one directory to another
def move_files(file_list, src_dir, dest_dir):
    for file_name in file_list:
        src_path = os.path.join(src_dir, file_name)
        dest_path = os.path.join(dest_dir, file_name)
        os.rename(src_path, dest_path)

# Create train and eval splits for images and labels
train_images_files, eval_images_files = create_split(frames_dir)
train_label_files, eval_label_files = create_split(labels_dir)
# Move files to their respective directories
move_files(train_images_files, frames_dir, train_images_dir)
move_files(eval_images_files, frames_dir, eval_images_dir)
move_files(train_label_files, labels_dir, train_labels_dir)
move_files(eval_label_files, labels_dir, eval_labels_dir)