import cv2
img = cv2.imread('images/img.png')
# cv2.imshow('Images', img)
resized = cv2.resize(img, (4, 4))
cv2.imshow('Image', resized)
cv2.imwrite('edited_images/newedit.png', resized)  # Specify the file extension here
cv2.waitKey(0)
cv2.destroyAllWindows()
