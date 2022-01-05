from encryptor import encrypt, decrypt
from PIL import Image
import numpy as np
import math

# Decimal to binary


def dTB(n):
    x = bin(n).replace("0b", "")
    if len(x) < 8:
        filler = '0'*(8-len(x))
        filler += x
        x = filler
    return x

# Read image


def read_img(jpg):
    img_matrix = []
    im = Image.open(jpg)
    # pixel access object
    img = im.load()
    print(im.size)
    [xs, ys] = im.size  # width*height

# Examine every pixel in im
    for x in range(0, xs):
        for y in range(0, ys):
            # get the RGB color of the pixel
            [r, g, b] = img[y, x]
            img_matrix.append([dTB(r), dTB(g), dTB(b)])
            # r = r + rtint
            # g = g + gtint
            # b = b + btint
            # value = (r, g, b)
            # img.putpixel((x, y), value)
    return img_matrix


def alter_img(img_matrix):
    matrix = img_matrix[:]
    #     im = Image.open(jpg)
    #     img = im.load()
    #     print(im.size)
    #     [xs, ys] = im.size  # width*height
    #     # l7 = input(img[0, 0])

    # # Examine every pixel in im
    #     i = 0
    #     for x in range(0, xs):
    #         for y in range(0, ys):
    #             # l4 = input((matrix[i][0], matrix[i][1], matrix[i][2]))
    #             value = (int(matrix[i][0], 2), int(
    #                 matrix[i][1], 2), int(matrix[i][2], 2))
    #             # print(value)
    #             img[x, y] = value
    #             i += 1
    #     l6 = input(img[0, 0])
    for pixel in matrix:
        pixel[0] = int(pixel[0], 2)
        pixel[1] = int(pixel[1], 2)
        pixel[2] = int(pixel[2], 2)
        if (pixel[0] not in range(0, 256) or pixel[1] not in range(0, 256) or pixel[2] not in range(0, 256)):
            h = input('Error')
    data = np.array(matrix)
    dim = int(math.sqrt(len(img_matrix)))
    shape = (dim, dim, 3)
    data = data.reshape(shape)
    data_sub = data.astype(np.uint8)
    im = Image.fromarray(data_sub)
    # x = input(im)
    im.save("output.png")


def hide_img(holder_img, input_img):
    input_img = encrypt(input_img)
    i = 0
    for pixel in input_img:
        # test1 = input(pixel)
        for x in range(8):
            # test2 = input(
            #     (holder_img[i+x][0], holder_img[i+x][1], holder_img[i+x][2]))
            holder_img[i+x][0] = holder_img[i+x][0][:-1] + pixel[0][x]
            holder_img[i+x][1] = holder_img[i+x][1][:-1] + pixel[1][x]
            holder_img[i+x][2] = holder_img[i+x][2][:-1] + pixel[2][x]
        # test3 = input(
            #     (holder_img[i+x][0], holder_img[i+x][1], holder_img[i+x][2]))
        i += 8

    print(i)
    return holder_img, i


def find_img(holder_img, number_of_pixels):
    holder = read_img(holder_img)
    # print(holder[:5])
    new_img = []
    # l3 = input(holder[:5])
    i = 0
    for x in range(number_of_pixels//8):
        new_pix_r = ''
        new_pix_g = ''
        new_pix_b = ''
        for j in range(8):
            new_pix_r += holder[x*8 + j][0][-1]
            new_pix_g += holder[x*8 + j][1][-1]
            new_pix_b += holder[x*8 + j][2][-1]
        new_img.append([new_pix_r, new_pix_g, new_pix_b])
        # l8 = input((int(new_pix_r, 2), int(new_pix_g, 2), int(new_pix_b, 2)))
    # final = [[] for x in range(int(math.sqrt(len(new_img))))]
    # for m in range(int(math.sqrt(len(new_img)))):
    #     final[m].extend(new_img[m*64:(m+1)*64])
    # # p = input(final)
    # img = Image.fromarray(np.array(final), 'RGB')
    # img = img.save('found.jpg')
    new_img = decrypt(new_img)
    for pixel in new_img:
        pixel[0] = int(pixel[0], 2)
        pixel[1] = int(pixel[1], 2)
        pixel[2] = int(pixel[2], 2)
        if (pixel[0] not in range(0, 256) or pixel[1] not in range(0, 256) or pixel[2] not in range(0, 256)):
            h = input('Error')
    data = np.array(new_img)
    dim = int(math.sqrt(number_of_pixels//8))
    shape = (dim, dim, 3)
    data = data.reshape(shape)
    data_sub = data.astype(np.uint8)
    im = Image.fromarray(data_sub)
    # x = input(im)
    im.save("found.png")


# JPEG format
holder_img = read_img('holder.jpeg')
# print(holder_img)
input_img = read_img('input.jpeg')

# o = input(holder_img[:2])


altered_holder, no_pixels = hide_img(holder_img, input_img)
alter_img(altered_holder)

# holder_img = read_img('holder.jpeg')
# output_img = read_img('output.png')
# print(holder_img[0], ':', output_img[0])

find_img('output.png', no_pixels)
