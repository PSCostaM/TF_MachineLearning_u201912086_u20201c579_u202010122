import os
import cv2

def is_blank_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is not loaded properly
    if image is None:
        print(f"Error loading image: {image_path}")
        return False

    # Calculate the sum of all pixels
    image_sum = image.sum()

    # If the sum is 0 or equal to the product of dimensions and 255, it's a blank image
    if image_sum == 0 or image_sum == image.size * 255:
        return True

    return False

def delete_blank_images(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is an image (you can add more types if needed)
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            if is_blank_image(file_path):
                print(f"Deleting blank image: {file_path}")
                os.remove(file_path)

# Replace 'your_folder_path' with the path to your folder
folder_path = '/home/dele/Documents/Machine_learning/Testing_TF/chair_images'
delete_blank_images(folder_path)
