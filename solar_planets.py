import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (20,213), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Mercury", (120,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Venus", (180,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Earth", (250,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Mars", (380,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Jupiter", (450,100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Saturn", (720,280), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Uranus", (950,140), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Neptune", (1120,280), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

cv2.imshow("Display Image ", img)
cv2.waitKey(0)

print(img)