import os
import cv2
import numpy as np

def load_data(data_dir, img_size=(224, 224)):
    images = []
    labels = []
    
    categories = os.listdir(data_dir)  # Get class names
    for label, category in enumerate(categories):
        category_path = os.path.join(data_dir, category)
        
        if not os.path.isdir(category_path):
            continue  # Skip if it's not a directory
        
        for file in os.listdir(category_path):
            img_path = os.path.join(category_path, file)
            img = cv2.imread(img_path)
            
            # ✅ Check if image is loaded correctly
            if img is None or img.size == 0:
                print(f"⚠️ Warning: Could not read image {img_path}. Skipping...")
                continue  # Skip to the next image
            
            img = cv2.resize(img, img_size)  # Resize image
            images.append(img)
            labels.append(label)
    
    images = np.array(images) / 255.0  # Normalize pixel values
    labels = np.array(labels)
    
    print(f"✅ Loaded {len(images)} images from {data_dir}")
    return images, labels
