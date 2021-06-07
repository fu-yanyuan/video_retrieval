import cv2 as cv

# videoName = "Honda_NSX" 
videoFile = "videos/Honda_NSX.mp4"
imagesFolder_gallery = "v_cars/gallery/honda"
imagesFolder_query = "v_cars/query/honda"

cap = cv.VideoCapture(videoFile)
frameRate = cap.get(5)  # refer to cap.get()
print("#frames =", cap.get(7)) # total number of frames in this video 
print("fps =", cap.get(5)) # framerate
print("h, w = ", cap.get(4), cap.get(3))

while cap.isOpened():
    frameID = cap.get(1) # current frame number
    isTrue, frame = cap.read()
    if not isTrue:
        print("can't receive any frame (stream end?)")
        break
    cv.imshow('frame', frame)

    # resize 
    # to be done in the PyRetri

    # save frames
    if frameID % round(frameRate) == 0:
        fileName = imagesFolder_gallery + "/image_" + str(int(frameID/round(frameRate))) + ".jpg"
        cv.imwrite(fileName, frame)

    # quit or save for query
    k = cv.waitKey(20)
    if k == ord('q'):
        break
    elif k == ord('s'):
        fileName_2 = imagesFolder_query + "/image_" + str(int(frameID)) + "_q.jpg"
        cv.imwrite(fileName_2, frame)



cap.release()
print("done!")
