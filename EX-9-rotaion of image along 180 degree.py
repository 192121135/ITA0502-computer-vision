import cv2
path = r"C:\Users\yasee\OneDrive\Pictures\little girl.jpeg" 
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_180)
cv2.imshow(window_name, image)
cv2.waitKey(0)
