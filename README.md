# Background_Swapper

### Introduction to OpenCv and CVzone

OpenCV is an open-source computer vision library that provides privileges to play with different images and video streams and also helps in end-to-end projects like object detection, face detection, object tracking, etc.

CVzone is a computer vision package that makes us easy to run like face detection, hand tracking, pose estimation, etc., and also image processing and other AI functions. At the core, it uses OpenCV and MediaPipe libraries. 


### Steps done in the code

1. We first resize the sample background images to the resolution of our video feed, this is necessary to prevent parts of the background from being cut in the final feed. We save all the resized images into a new folder named 'resized' in the same directory as that of our sample images.

2. We then initialize the webcam to ensure that it shows the video feed in the resolution we specify in the command line.

3. We then append all the resized background images into a stack so that we can switch the background image using a simple key press.

4. We then open the webcam and display the feed, with the left side having the direct feed and the right side showing the feed with the swapped background while waiting for a key press which is used to either swap the background image (keys 'a' and 'd') or exit the session (key 'q').
