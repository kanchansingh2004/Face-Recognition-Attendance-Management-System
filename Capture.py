import cv2
import numpy as np
import os

# Create a VideoCapture object to access the webcam
video_capture = cv2.VideoCapture(0)

# Counter to track the number of pictures taken
count = 0

while count < 30:
    # Capture a frame from the webcam
    ret, frame = video_capture.read()

    # Check if frame capture was successful
    if not ret:
        print("Error: Failed to capture frame")
        break

    # Save the captured frame as a picture
    cv2.imwrite(f"picture_{count}.jpg", frame)

    # Display the captured image (optional)
    cv2.imshow("Captured Image", frame)

    # Wait for a key press (optional)
    # cv2.waitKey(1)

    # Increment the picture counter
    count += 1

# Release the VideoCapture object
video_capture.release()

# Close all open windows
cv2.destroyAllWindows()



# Specify the path to the folder containing the images
image_folder = "C:\python"

# Choose a feature extraction method (e.g., SIFT or ORB)
feature_extractor = cv2.SIFT_create()  # Replace with your preferred method

# Iterate through the images in the folder
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg"):
        # Load the image
        img = cv2.imread(os.path.join(image_folder, filename))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect keypoints and extract features
        keypoints, descriptors = feature_extractor.detectAndCompute(gray, None)

        # Create a file to store the features
        feature_filename = f"{filename[:-4]}_features.npy"  # Replace .npy with your preferred format
        feature_path = os.path.join(image_folder, feature_filename)

        # Save the features to the file
        np.save(feature_path, descriptors)

        print(f"Features extracted and saved for {filename}")