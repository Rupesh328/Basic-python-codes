import cv2

# Load the image
img = cv2.imread('aero1.jpg')

# Check if image is loaded successfully
if img is None:
    print("Failed to load image. Please check the path and file format.")
else:
    # Display the image
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
