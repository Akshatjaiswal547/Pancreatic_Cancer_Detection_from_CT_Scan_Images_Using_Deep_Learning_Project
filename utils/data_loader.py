import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

def load_data(data_dir, img_size=(224, 224)):
    images, labels = [], []

    # Ensure consistent class order (e.g., ['benign', 'malignant'] or ['normal', 'cancer'])
    class_names = sorted(os.listdir(data_dir))  

    # Map folder names to numeric labels
    label_map = {name: idx for idx, name in enumerate(class_names)}
    print("Label Mapping:", label_map)  # Debug: show class-to-index mapping

    for category in class_names:
        category_path = os.path.join(data_dir, category)
        for file in os.listdir(category_path):
            img_path = os.path.join(category_path, file)
            img = cv2.imread(img_path)

            if img is None:
                continue  # skip broken or unreadable images

            img = cv2.resize(img, img_size)
            images.append(img)
            labels.append(label_map[category])  # Use mapped integer label

    # Convert to numpy arrays
    images = np.array(images, dtype=np.float32) / 255.0  # Normalize pixel values
    labels = np.array(labels, dtype=np.int32)            # Ensure labels are integers (not one-hot)

    return images, labels

def split_data(images, labels, test_size=0.2, val_size=0.1):
    # Split into training + temp test
    X_train, X_temp, y_train, y_temp = train_test_split(images, labels, test_size=test_size, random_state=42, stratify=labels)

    # Split temp into validation and test
    val_ratio = val_size / (1 - test_size)  # adjust val size relative to remaining
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=1 - val_ratio, random_state=42, stratify=y_temp)

    return X_train, X_val, X_test, y_train, y_val, y_test
