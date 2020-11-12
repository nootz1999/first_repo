import cv2
img_file = r"C:\Users\pc\Downloads\chemical_hearts.jpg"

img_original = cv2.imread(img_file)

cv2.imshow('original', img_original)
cv2.waitKey(0)
cv2.destroyAllWindows()