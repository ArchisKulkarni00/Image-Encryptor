import cv2
import numpy as np

image = cv2.imread('img2.jpg')
seed = 5
# source = np.random.seed(5)
# arr1 = np.random.uniform(4,255,image.shape)
# print(arr1)
# source = np.random.seed(5)
arr2 = np.random.uniform(4,255,image.shape).astype(np.uint8)
# print(arr2)
# print(image.shape)
encrypt = cv2.bitwise_xor(arr2,image)
decrypt = cv2.bitwise_xor(arr2,encrypt)
cv2.imshow('hello',encrypt)
cv2.imshow('hello1',arr2)
cv2.imshow('hello2',decrypt)
cv2.waitKey(0)