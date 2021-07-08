
# importing the required packages
import cv2
import os
import cvzone
import argparse
from cvzone.SelfiSegmentationModule import SelfiSegmentation

# Resizing the sample background images to the format of the real-time video feed
def resizer(filename, width, height):
    os.mkdir(filename+'/resized')
    for root, subdirs, files in os.walk(filename):
        for f in files:
            if f.endswith('jpg'):
                img = cv2.imread(filename + '/' + f)
                img = cv2.resize(img, (width, height))
                cv2.imwrite(filename + '/resized/' + f, img)

# Initializing the webcam with the required width, height and frames per second
def init(width, height, fps):
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)
    cap.set(cv2.CAP_PROP_FPS, fps)
    return cap

if __name__ == "__main__":
    filename = 'E:/College Stuff/Fun Projects/Image Processing/Background Removal/BackgroundImages'

    # Collecting the width, height, frames per second and the swapping threshold as command line arguments
    parser = argparse.ArgumentParser(description='Change the background of your video')
    parser.add_argument('--width', type=int, default=640, help='the width of the image')
    parser.add_argument('--height', type=int, default=480, help='the height of the image')
    parser.add_argument('--fps', type=int, default=60, help='Max frame rate of the video')
    parser.add_argument('--threshold', type=float, default=0.7, help='Threshold for changing the background ')
    args = parser.parse_args()
    width, height, fps, threshold = args.width, args.height, args.fps, args.threshold

    # Running the resizing function
    resizer(filename, width, height)

    # SelfiSegmentation() is the function of cvzone that performs the swap
    segmentor = SelfiSegmentation()
    fpsReader = cvzone.FPS()
    cap = init(width, height, fps)

    # Reading all the sample backgrounds and appending them into a list
    listImg = os.listdir("BackgroundImages/resized")
    imgList = []
    for imgPath in listImg:
        img = cv2.imread(f'BackgroundImages/resized/{imgPath}')
        imgList.append(img)

    indexImg = 0
    print(indexImg)

    # Running the video while applying the operations that perform the background swap
    while True:
        success, img = cap.read()
        imgOut = segmentor.removeBG(img, imgList[indexImg], threshold = threshold)

        # Stacking the main image and the background swapped image side by side
        imgStack = cvzone.stackImages([img, imgOut], 2, 1)
        _, imgStack = fpsReader.update(imgStack)
        cv2.imshow("image", imgStack)

        # Waiting for key press to change the background image or to exit
        key = cv2.waitKey(1)
        if key == ord('a'):
            if indexImg > 0:
                indexImg -= 1
            print(indexImg)
        elif key == ord('d'):
            if indexImg < len(imgList) - 1:
                indexImg += 1
            print(indexImg)
        elif key == ord('q'):
            for file in listImg:
                os.remove(f'{filename}/resized/{file}')
            os.rmdir(filename+'/resized')
            break
