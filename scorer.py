from skimage.io import imread
import numpy as np
from PIL import Image
import random
import math


def entropy(img):
    # print((matrix == 1).sum())
    p = np.array([(img == v).sum() for v in range(0, 256)])
    # print(p[:10])
    # print(p[0])
    p = p/p.sum()

    e = -(p[p > 0]*np.log2(p[p > 0])).sum()
    # print(e)
    return e


def pixel_corr(img, n):

    img = Image.open(img)
    pixels = img.load()
    [xs, ys] = img.size

    adj_pixels_r = []
    adj_pixels_g = []
    adj_pixels_b = []
    for x in range(n):
        x1 = random.choice(range(xs-1))
        y1 = random.choice(range(ys-1))
        new_pixel = pixels[x1, y1]
        new_pixel_adj = pixels[x1+1, y1]
        adj_pixels_r.append([new_pixel[0], new_pixel_adj[0]])
        adj_pixels_g.append([new_pixel[1], new_pixel_adj[1]])
        adj_pixels_b.append([new_pixel[2], new_pixel_adj[2]])

    cov = (1/n)*sum((adj_pixels_r[i][0]-(1/n)*sum(adj_pixels_r[j][0] for j in range(n)))*(
        adj_pixels_r[i][1]-(1/n)*sum(adj_pixels_r[j][1] for j in range(n))) for i in range(n))

    d_x = (1/n)*sum((adj_pixels_r[i][0]-(1/n)*sum(adj_pixels_r[j][0]
                                                  for j in range(n)))**2 for i in range(n))
    d_y = (1/n)*sum((adj_pixels_r[i][1]-(1/n)*sum(adj_pixels_r[j][1]
                                                  for j in range(n)))**2 for i in range(n))

    p = cov/((math.sqrt(d_x)*math.sqrt(d_y)))

    return p


def MAE(orig_img, encry_img):
    img_original = Image.open(orig_img)
    pixels_original = img_original.load()
    img_encrypted = Image.open(encry_img)
    pixels_encrypted = img_encrypted.load()
    [xs, ys] = img_original.size

    sum_diff_r = 0
    sum_diff_g = 0
    sum_diff_b = 0
    for i in range(xs):
        for j in range(ys):
            sum_diff_r += (pixels_original[i, j]
                           [0] - pixels_encrypted[i, j][0])
            sum_diff_g += (pixels_original[i, j]
                           [1] - pixels_encrypted[i, j][1])
            sum_diff_b += (pixels_original[i, j]
                           [2] - pixels_encrypted[i, j][2])

    MAE_r = (1/(xs*ys))*sum_diff_r
    MAE_g = (1/(xs*ys))*sum_diff_g
    MAE_b = (1/(xs*ys))*sum_diff_b
    return MAE_r, MAE_g, MAE_b


def MSE(orig_img, encry_img):
    img_original = Image.open(orig_img)
    pixels_original = img_original.load()
    img_encrypted = Image.open(encry_img)
    pixels_encrypted = img_encrypted.load()
    [xs, ys] = img_original.size

    sum_diff_r = 0
    sum_diff_g = 0
    sum_diff_b = 0
    for i in range(xs):
        for j in range(ys):
            sum_diff_r += (pixels_original[i, j]
                           [0] - pixels_encrypted[i, j][0])**2
            sum_diff_g += (pixels_original[i, j]
                           [1] - pixels_encrypted[i, j][1])**2
            sum_diff_b += (pixels_original[i, j]
                           [2] - pixels_encrypted[i, j][2])**2

    MSE_r = (1/(xs*ys))*sum_diff_r
    MSE_g = (1/(xs*ys))*sum_diff_g
    MSE_b = (1/(xs*ys))*sum_diff_b
    return MSE_r, MSE_g, MSE_b

# print(entropy(imread('output.png')))
# print(entropy(imread('crypt.png')))
# sum = 0
# # for i in range(100):
# # print(i)
# x = pixel_corr('crypt.png', 1000)
#sum += x
# sum_corr = 0
# for l in range(50):
#     sum_corr += pixel_corr('crypt.png', 1000)


# print(sum_corr/50)
print(MAE('input.jpeg', 'crypt.png'))
print(MSE('input.jpeg', 'crypt.png'))

# (58.575, 56.004, 52.713)
# (10119.615, 10220.863, 10032.52)
