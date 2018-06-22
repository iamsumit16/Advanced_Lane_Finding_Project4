import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
%matplotlib inline
import collections
import glob



#Read calibration images
camera_cal_location = glob.glob('camera_cal/*.jpg')
cal_images = []
for f in camera_cal_location:
    img = mpimg.imread(f)
    cal_images.append(img)
print(len(cal_images), cal_images[0].shape)
nx = 9
ny = 6
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((nx*ny,3), np.float32)
objp[:,:2] = np.mgrid[0:nx, 0:ny].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d points in real world space
imgpoints = [] # 2d points in image plane.

for image in cal_images:
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (nx,ny), None)
    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)
        cv2.drawChessboardCorners(image, (nx, ny), corners, ret)
      
      
      
def undistort_img(img, objpoints, imgpoints):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None,None)
    undist = cv2.undistort(img, mtx, dist, None, mtx)
    return undist

def sobel_x(img, sobel_kernel=5,min_thres = 20, max_thres =100):
    imghsl = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    #Take the gradient in x separately in Channels L and S from HLS
    sobelx1 = cv2.Sobel(imghsl[:,:,1], cv2.CV_64F, 1,0, ksize=sobel_kernel)
    sobelx2 = cv2.Sobel(imghsl[:,:,2], cv2.CV_64F, 1,0, ksize=sobel_kernel)
    scaled_sobelx1 = np.uint8(255*sobelx1/ np.max(sobelx1))
    scaled_sobelx2 = np.uint8(255*sobelx2/ np.max(sobelx2))
    sobel_binaryx1 = np.zeros_like(scaled_sobelx1)
    sobel_binaryx1[(scaled_sobelx1 >= min_thres) & (scaled_sobelx1 <= max_thres)] = 1
    sobel_binaryx2 = np.zeros_like(scaled_sobelx2)
    sobel_binaryx2[(scaled_sobelx2 >= min_thres) & (scaled_sobelx2 <= max_thres)] = 1
    sobel_binary = np.zeros_like(scaled_sobelx1)
    sobel_binary[(sobel_binaryx1 ==1) | (sobel_binaryx2 ==1)]=1
    return sobel_binary

def abs_sobel_thresh(img, orient='x', sobel_kernel=5, thresh=(0,255)):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
    if orient=='x': abs_sobel = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel))
    if orient=='y': abs_sobel = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel))
    scaled_sobel = np.uint8(255*abs_sobel/np.max(abs_sobel)) # rescale 8-bit
    sobel_binary = np.zeros_like(scaled_sobel) # create a copy and apply threshold
    sobel_binary[(scaled_sobel >= thresh[0]) & (scaled_sobel <= thresh[1])] = 1
    return sobel_binary

def magnitude_thresh( img, sobel_kernel = 5, mag_thresh = (0,255)):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = sobel_kernel)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = sobel_kernel)
    gradmag = np.sqrt(sobelx**2 + sobely**2)
    scaled_sobel = up.uint8(255*gradmag/ np.max(gradmag))
    sobel_binary = np.zeros_like(scaled_sobel)
    sobel_binary[(scaled_sobel>= mag_thresh[0]) & (scaled_sobel <= mag_thresh[1])] = 1
    return sobel_binary

def dir_threshold(img, sobel_kernel = 5, thresh = (0, np.pi/2)):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    abs_sobelx = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = sobel_kernel))
    abs_sobely = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = sobel_kernel))
    abdgraddir = np.arctan2(abs_sobelx,abs_sobely)
    sobel_binary = np.zeros_like(absgraddir)
    sobel_binary[(absgraddir >= thresh[0])&(absgraddir <= thresh[1]) ]=1
    return sobel_binary

def mag_dir_thresh(img, sobel_kernel=3, mag_thresh=(0, 255), dir_thresh=(0,np.pi/2)):

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1,0, ksize=sobel_kernel) 
    sobely = cv2.Sobel(img, cv2.CV_64F, 0,1, ksize=sobel_kernel)
    gradmag = np.sqrt(sobelx**2 + sobely**2)
    abs_sobelx = np.absolute(sobelx)
    abs_sobely = np.absolute(sobely)
    absgraddir = np.arctan2(abs_sobely, abs_sobelx) 
    scaled_sobel = np.uint8(255*gradmag / np.max(gradmag))
    sobel_binary = np.zeros_like(scaled_sobel)
    sobel_binary[(scaled_sobel >= mag_thresh[0]) & (scaled_sobel <= mag_thresh[1]) & (absgraddir >= dir_thresh[0]) & (absgraddir <= dir_thresh[1]) ] = 1
    return sobel_binary
