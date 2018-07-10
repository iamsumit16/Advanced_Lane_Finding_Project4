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
[![Advance Lane Finding](http://img.youtube.com/vi/GLfWLHwiUgXg/0.jpg)](https://www.youtube.com/watch?v=LfWLHwiUgXg&feature=youtu.be "Advance Lane Finding")

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### 1. Camera Calibration and undistortion
--- 
The code for this step is contained in the first code cell of the IPython notebook located in "./examples/example.ipynb" (or in lines # through # of the file called some_file.py).

I start by preparing "object points", which will be the (9, 6, 0) coordinates of the chessboard corners in the world. Here I am assuming the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image. Thus, objp is just a replicated array of coordinates, and objpoints will be appended with a copy of it every time I successfully detect all chessboard corners in a test image. imgpoints will be appended with the (9, 6) pixel position of each of the corners in the image plane with each successful chessboard detection.

I then used the output objpoints and imgpoints to compute the camera calibration and distortion coefficients using the cv2.calibrateCamera() function. I applied this distortion correction to the test image using the cv2.undistort() function and obtained this result:

![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/undist_cam.png)

![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/undist_img.png)

### 2. Perspective Transform
---
![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/perspective.png)


### 3. Create a binary image
---
![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/top_down_bin.png)


### 4. Detect the lane line pixels and curve fitting
---
![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/hist.png)
![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/find_lane.png)
### 5. Determine the road curvature and vehicle offset
---
![alt text]()
### 6. Warp the detected lanes back to original image
---
![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/final_warp.png)

### 7. Visual Display of the final image
---
![alt text](https://github.com/iamsumit16/Advanced_Lane_Finding_Project4/blob/master/output%20images/final_out.png)



## How to write a README
A well written README file can enhance your project and portfolio.  Develop your abilities to create professional README files by completing [this free course](https://www.udacity.com/course/writing-readmes--ud777).

