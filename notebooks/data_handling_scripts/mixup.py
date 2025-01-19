import cv2

# Load the two input images
img1 = cv2.imread(r'F:\Model\detectionb96aec27-1449-11ee-ab46-5c260a488791.jpg')
img2 = cv2.imread(r'F:\Model\detectionba1e7f2e-1449-11ee-a365-5c260a488791.jpg')

# Resize the images to the same height
height = 640
width1 = int(img1.shape[1] * height / img1.shape[0])
width2 = int(img2.shape[1] * height / img2.shape[0])
img1_resized = cv2.resize(img1, (width1, height))
img2_resized = cv2.resize(img2, (width2, height))

# Concatenate the two images horizontally
result = cv2.hconcat([img1_resized, img2_resized])

# saving the image 
cv2.imwrite("final_present.jpg" , result)