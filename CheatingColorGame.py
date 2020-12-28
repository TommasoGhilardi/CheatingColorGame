# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:25:46 2020

@author: Tommaso
"""
import cv2
import time
import pyautogui
import numpy as np
from selenium import webdriver
from collections import Counter

# =============================================================================
# Load the website and get ready
# =============================================================================
browser = webdriver.Firefox(executable_path=r'C:\\Users\\krav\\Documents\\geckodriver.exe')  # executable to use firefox
browser.maximize_window()  # maximise
browser.get('https://enplay.gamen.com/play111')  # Load website
time.sleep(5)

'''Remove Banner'''
screenWidth, screenHeight = pyautogui.size()  # Get the size of the primary monitor.
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)  # Move the mouse on the banner
pyautogui.click()  # Click the Banner
time.sleep(7)

'''Press start'''
screen_size = pyautogui.size()  # screen size
pyautogui.moveTo(screen_size.width / 1.8, screen_size.height / 1.2)  # Move the mouse to approximately the START button
pyautogui.click()  # Click START.
time.sleep(3)

# =============================================================================
# Playing the game
# =============================================================================
while True:

    '''Screenshot'''
    im = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)  # working in BRG
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # Conversion to grayscale
    gray = gray[300:1080, 500:1400]  # Cutting out part of the image

    '''Circles'''
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.7, 60, minRadius=1, maxRadius=78)  # Finding the circles
    circles = np.uint16(np.around(circles))
    centers = [[z[0] + 500, z[1] + 300] for z in circles[0, :]]  # List of the centers

    if type(circles) == type(None):
        break  # Stop the script when you loose

    # =============================================================================
    # Making a choice
    # =============================================================================
    colors = [sum(image[r[1], r[0]]) for r in centers]  # Detecting the colors of the centers
    count = Counter(colors)  # Counting colors occurrence
    minimum = min(count, key=count.get)  # Finding the color less used

    pyautogui.moveTo(centers[colors.index(minimum)][0], centers[colors.index(minimum)][1])  # Moving to the answer
    pyautogui.click()  # Click the mouse.
    time.sleep(0.15)  # Wait next level
