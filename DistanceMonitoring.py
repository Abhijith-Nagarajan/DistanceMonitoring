 # Distance monitoring using opencv

#Importing the required libraries
import cv2 
import pygetwindow as pgw

video = cv2.VideoCapture(0)

faces_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces_cascade.load("haarcascade_frontalface_default.xml")

def compute_distance(image,x,y,w,h):
    ''' This function calculates the distance between the object and camera'''
    
    #Step 1- Display coordinates of the face    
    center_x = x+w//2
    center_y = y+h//2

    #Step 2- Find the area of the face
    area = w*h
    dist = int(4390.0*(area**(-0.406)))
    
    print("Distance in cm: {}".format(dist))
    
    image_dist = cv2.putText(image,"Distance: "+str(dist)+"cm",(x-w,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 0),2)
    
    cv2.imshow("Image",image_dist)
    cv2.waitKey(1)    
        
    window = pgw.getWindowsWithTitle('Spyder (Python 3.8)')[0]
        
    if dist<65:
        window.minimize()
    else: 
        if window.isMinimized:
           window.maximize() 
           
    if 0xFF == ord('q'):
        exit()
    
def detect_face(image,image_gray):
    '''This function detects the face and returns the face with a bounding box'''
    faces = faces_cascade.detectMultiScale(image_gray, 1.15, 3) # We apply the detectMultiScale method from the face cascade to locate one or several faces in the image.
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2) # We paint a rectangle around the face.
        compute_distance(image,x,y,w,h)
    return

while True:    
    success, image = video.read()
    # Laterally inverting the image
    image = cv2.flip(image,1)
    image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    detect_face(image,image_gray) 
    if not success:  
        break
    
# The webcam is turned off    
video.release() 
# All the windows inside which the images are displayed are destroyed. 
cv2.destroyAllWindows() 
    
    