## Advanced Lane Finding
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)


In this project, your goal is to write a software pipeline to identify the lane boundaries in a video, but the main output or product we want you to create is a detailed writeup of the project.  Check out the [writeup template](https://github.com/udacity/CarND-Advanced-Lane-Lines/blob/master/writeup_template.md) for this project and use it as a starting point for creating your own writeup.  

The Project
---

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.


### [Rubric](https://review.udacity.com/#!/rubrics/571/view) Points

### Output Video
---
[![Advance Lane Finding](http://img.youtube.com/vi/LfWLHwiUgXg/0.jpg)](https://www.youtube.com/watch?v=LfWLHwiUgXg&feature=youtu.be "Advance Lane Finding")

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### 1. Camera Calibration and undistortion
--- 

I start by preparing "object points", which will be the (x, y, z) coordinates of the chessboard corners in the world. Here I am assuming the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image. Thus, objp is just a replicated array of coordinates, and objpoints will be appended with a copy of it every time I successfully detect all chessboard corners in a test image. imgpoints will be appended with the (9, 6) pixel position of each of the corners in the image plane with each successful chessboard detection. For my purposes I have used x = 9 and y = 6 for the internal corners of the chessboard.

I then used the output objpoints and imgpoints to compute the camera calibration and distortion coefficients using the cv2.calibrateCamera() function. I applied this distortion correction to the test image using the cv2.undistort() function and obtained this result:

![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/undist_cam.png)

The result after applying undistortion to the test image:

![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/undist_img.png)

### 2. Perspective Transform
---
I did a perspective transform first to have a better visualization of the binary imag when it is applied after it. I have used cv2.getPerspectiveTransform() in my top_down_view() method to do the transformation. the src and dst points are hard coded using the visual inspection according to the image.

![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/perspective.png)


### 3. Create a binary image
---
To create the binary image I have used color thresholds for L channel and B channel of the HSL and LAB images to catch the yellow and white colors in the image. One can try numerous combinations to explore the various color spaces and gradient thresholds in x and y directions to make this more robust.
After deciding the thresholds for colors, I replaces the pixels values for pixel which fall in specified range to 1 and rest of the pixel values to 0.

![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/top_down_bin.png)


### 4. Detect the lane line pixels and curve fitting
---
To detect the lanes I have used the sliding window search as mentioned in the lecture slides. I use a second order polynomial to fit the lane pixels found in the sliding image search. This is specified in the findlines() method in my P4.ipynb notebook.

![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/hist.png)
![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/find_lane.png)
### 5. Determine the road curvature and vehicle offset
---
The road curvature and vehicle offset are calculated using np.polyfit(). Once we know the road curvature, the vehicle offset from the center can be calculated using the shape of binary warped image ( half of shape[1]).

The radius is found using the equation: 

R curve = ([1+dx/dy)^2]^1.5)/abs(d^2y/dx^2)


### 6. Warp the detected lanes back to original image
---
The lanes found and the polyfit curve is warped on th eoriginal image using the same cv2.warpPerspective() fucntion but now with Minv matrix.

![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/final_warp.png)

### 7. Visual Display of the final image
---
In order to make the green lane-coverage output on the road smooth, I take the average of the polynomial fitting of the latest 20 frames to be the current fitting. The smoothing operation can be found in the function process_image(input_image). After smoothing, the output video is much more stable.

![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/final_out.png)


### 8. Discussion
---
Limitations: This current implementation is rather sensitive to lighting conditions. As the contrast with the road and lane color change the gradient of the image did not detect the lane, hence I stopped using the gradient in generating a binary image. A potential approach would be using gradient angle to pickup lanes. However, this also caused the side of the road to be detected on the bridge. 

The other limitation is the noisiness of the fit. This is caused by using a quadtratic fit for each frame. A solution would be using a bezier or clothoid curve that is not sensitive to local changes. Additionally it is worth applying a sliding window mean on the fit coefficients to smooth out the results and avoid instatenous changes due to changes in the gradient or lighting conditions.


## How to write a README
A well written README file can enhance your project and portfolio.  Develop your abilities to create professional README files by completing [this free course](https://www.udacity.com/course/writing-readmes--ud777).

