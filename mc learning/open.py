import cv2

camera_port = 0
#camera = cv2.VideoCapture(camera_port)
camera = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)
# Check if the webcam is opened correctly
if not camera.isOpened():
    raise IOError("Cannot open webcam")

return_value, image = camera.read()
print("We take a picture of you, check the folder")
cv2.imwrite("image.png", image)

camera.release() # Error is here
cv2.destroyAllWindows()