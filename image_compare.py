from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

imageA = Image.open('./image/IMG_0479.jpg')
imageB = Image.open('./image/IMG_0480.jpg')

imageA_gray = imageA.convert('LA')
imageB_gray = imageB.convert('LA')

imageA = np.asanyarray(imageA)
imageB = np.asanyarray(imageB)
imageA_gray = np.asanyarray(imageA_gray)
imageB_gray = np.asanyarray(imageB_gray)

height = imageA.shape[0]
width = imageA.shape[1]

part = 4

height/=part
width/=part

height = (int)(height)
width = (int)(width)

h_begin = 0
h_end = height

w_begin = 0
w_end = width

print('h', height)
print('w', width)

A = []
B = []
A_gray = []
B_gray = []

for i in range(part):
    a = imageA[h_begin:h_end]
    b = imageB[h_begin:h_end]
    ag = imageA_gray[h_begin:h_end]
    bg = imageB_gray[h_begin:h_end]

    for j in range(part):
        a_1 = a[:, w_begin:w_end]
        b_1 = b[:, w_begin:w_end]
        a_1g = ag[:, w_begin:w_end]
        b_1g = bg[:, w_begin:w_end]

        w_begin+=width
        w_end+=width

        A.append(a_1)
        B.append(b_1)

        A_gray.append(a_1g)
        B_gray.append(b_1g)

    h_begin+=height
    h_end+=height
    w_begin = 0
    w_end = width

m = []

for i in range(len(A)):
    m.append(ssim(A_gray[i], B_gray[i], multichannel=True, gaussian_weights=True))
    fig = plt.figure()
    plt.suptitle('SSIM: %.2f' %m[i])
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(A[i])
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(B[i])
    plt.show()

print(m)
