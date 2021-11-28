from cv2 import cv2
import  cvzone

OPTIONS = ["1. Beard", "2. Cool", "3. Native", "4. Pirate", "5. Star", "6. Sunglasses"]

for choices in OPTIONS:
    print(choices)



filter = None

while not filter:
    selection = input("Enter a number to select a filter: ")
    if selection == "1":
        filter = 'beard.png'
    elif selection == "2":
        filter = 'cool.png'
    elif selection == "3":
        filter = 'native.png'
    elif selection == "4":
        filter = 'pirate.png'
    elif selection == "5":
        filter = 'star.png'
    elif selection == "6":
        filter = 'sunglasses.png'
    else:
        print("Selection not available")


cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay = cv2.imread(filter, cv2.IMREAD_UNCHANGED)
while True:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        # cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
        overlay_resize = cv2.resize(overlay, (int(w*1.5), int(h*1.5)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75])
    cv2.imshow('Snap Dude', frame)
    if cv2.waitKey(10) == ord('q'):
        break
