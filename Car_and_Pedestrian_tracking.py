
import cv2

#Step by step

"""
# 1. Our Image or Video file / Importing The Image or Video
img_file = "Car_Image.jpg"

# 2. Our pre-trained car classifier
classifier_file = "car_detector.xml" 

#  3. Create opencv image / reads pixels in image file
img = cv2.imread(img_file)

# 4. covert to greyscale (needed for haar cascade)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 5. create car classifier / Called Cascade because there is a lot of Haar features running
car_tracker = cv2.CascadeClassifier(classifier_file)

#detect cars of any size or scale/ look at open cv documentation
cars = car_tracker.detectMultiScale(black_n_white)

#Draw rectangles around the cars / Interpolation
for (x, y, w, h) in cars:
    # the parameters are (x, y) - top left point (x + width, y + height) - bottom right point (RGB), (width of rectangle)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)


# the parameters are (x, y) - top left point (x + width, y + height) - bottom right point (RGB), (width of rectangle)
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)


# 6. Display the image with the faces spotted / displays image for a milisecond - need waitKey to pause the image
cv2.imshow("Clever Programmer Car Detector", img) #black_n_white to img

# 7. Don't autoclose (wait here in the cod and listen for a key press)
cv2.waitKey()

print("Code Completed")
"""



"""
# 1. Our Image or Video file / Importing The Image or Video
video = cv2.VideoCapture("Tesla_Dashcam.mp4")

# 2. Our pre-trained car classifier
classifier_file = "car_detector.xml" 

# 5. create car classifier / Called Cascade because there is a lot of Haar features running
car_tracker = cv2.CascadeClassifier(classifier_file)

# Run forever until the car or video stops or crashes.
while True:

    # Read the current frame, then move to the next. Rad video frame by frame. This is a tuple
    read_successful, frame = video.read()

    # Safe coding
    if read_successful:
        # Must convert to greyscale. This function only works if video.read() is successful
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

#detect cars of any size or scale/ look at open cv documentation
cars = car_tracker.detectMultiScale(grayscale)


#Draw rectangles around the cars / Interpolation
for (x, y, w, h) in cars:
    # the parameters are (x, y) - top left point (x + width, y + height) - bottom right point (RGB), (width of rectangle)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

# 6. Display the image with the faces spotted / displays image for a milisecond - need waitKey to pause the image
cv2.imshow("Clever Programmer Car Detector", frame) #read_succesful to grayscale

# 7. Don't autoclose (wait here in the cod and listen for a key press)
cv2.waitKey(1)

print("Code Completed")
"""



"""
# 1. Our Image or Video file / Importing The Image or Video
video = cv2.VideoCapture("Motorcycle.mp4")

# 2. Our pre-trained car classifier
car_tracker_file = "car_detector.xml"
pedestrian_tracker_file = "haarcascade_fullbody.xml"

#Create Car and pedestrain Classifier
car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrain_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

# Run forever until the car or video stops or crashes.
while True:

    # Read the current frame, then move to the next. Rad video frame by frame. This is a tuple
    read_successful, frame = video.read()

    # Safe coding
    if read_successful == True:
        # Must convert to greyscale. This function only works if video.read() is successful
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

#detect cars AND pedestrains of any size or scale/ look at open cv documentation
cars = car_tracker.detectMultiScale(grayscale)
ped = pedestrain_tracker.detectMultiScale(grayscale)

#Draw rectangles around the cars / Interpolation
for (x, y, w, h) in cars:
    # the parameters are (x, y) - top left point (x + width, y + height) - bottom right point (RGB), (width of rectangle)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    #Draw rectangles around the pedestrains / Interpolation
for (x, y, w, h) in ped:
    # the parameters are (x, y) - top left point (x + width, y + height) - bottom right point (RGB), (width of rectangle)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

# 6. Display the image with the faces spotted / displays image for a milisecond - need waitKey to pause the image
cv2.imshow("Clever Programmer Car Detector", frame) #read_succesful to grayscale

# 7. Don't autoclose (wait here in the cod and listen for a key press)
cv2.waitKey()
"""

cap = cv2.VideoCapture("NYC.mp4")
ret, frame = cap.read()

car_tracker_file = "car_detector.xml"
pedestrian_tracker_file = "haarcascade_fullbody.xml"

grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrain_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

cars = car_tracker.detectMultiScale(grayscale)
ped = pedestrain_tracker.detectMultiScale(grayscale)

while (1):
    ret, frame = cap.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    car_tracker = cv2.CascadeClassifier(car_tracker_file)
    pedestrain_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

    cars = car_tracker.detectMultiScale(grayscale)
    ped = pedestrain_tracker.detectMultiScale(grayscale)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    for (x, y, w, h) in ped:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if cv2.waitKey(1) & 0xFF == ord('q') or ret==False:
        cap.release()
        cv2.destroyAllWindows()
        break
    cv2.imshow("Clever Programmer Car Detector", frame) #read_succesful to grayscale


 
   



"""
car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrain_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

if ret == True:
        # Must convert to greyscale. This function only works if video.read() is successful
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

cars = car_tracker.detectMultiScale(grayscale)
ped = pedestrain_tracker.detectMultiScale(grayscale)

for (x, y, w, h) in cars:
    # the parameters are (x, y) - top left point (x + width, y + height) - bottom right point (RGB), (width of rectangle)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    #Draw rectangles around the pedestrains / Interpolation
for (x, y, w, h) in ped:
    # the parameters are (x, y) - top left point (x + width, y + height) - bottom right point (RGB), (width of rectangle)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
"""
"""
cap = cv2.VideoCapture("Motorcycle.mp4")
ret, frame = cap.read()
while(1):
   ret, frame = cap.read()
   cv2.imshow('frame',frame)
   if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
       cap.release()
       cv2.destroyAllWindows()
       break
   cv2.imshow('frame',frame)
"""