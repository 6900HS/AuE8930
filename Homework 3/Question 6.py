#!/usr/bin/env python
# coding: utf-8

# Question 6 (5’)
# 
# Use OpenCV to do a bilateral filter to an image, modify from question6.py, you may use your favorite image, visualize the images before and after the filtering using matplotlib.

# In[31]:


# Bartley Cai
import cv2 
import matplotlib.pyplot as plt
import os

# image path
os.chdir("C:\\Users\\bartl\\Documents\\AuE8930")
# Read the image.
img = cv2.imread("flower_0.10_noisy.jpg") 
# Apply bilateral filter
bilateral = cv2.bilateralFilter(img, 15, 75, 75)
# Save the output. 
cv2.imwrite('bilateral.jpg', bilateral)
# need to change from bgr to rgb
orig = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
bilat = cv2.cvtColor(bilateral, cv2.COLOR_BGR2RGB)

#plot
plt.subplot(121)
plt.title("Original, RGB")
plt.imshow(orig)
plt.subplot(122)
plt.title("Bilateral Filter, RGB")
plt.imshow(bilat)
plt.show()

plt.subplot(121)
plt.title("Original, BGR")
plt.imshow(img)
plt.subplot(122)
plt.title("Bilateral Filter, BGR")
plt.imshow(bilateral)
plt.show()

