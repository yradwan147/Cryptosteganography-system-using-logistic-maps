# lamb = 3.56695 (onset of chaos for logistic map function)
def logistic_gen(lamb, x_node):
    x_next = x_node
    while True:
        x_next = lamb*x_next*(1-x_next)
        binary_x = eval(str(x_next)[str(x_next).find('.')+1:].lstrip('0'))
        binary_x = bin(int(binary_x)).replace("0b", "")
        yield binary_x


def dtB_lengther(value):
    x = value
    if len(value) < 8:
        filler = '0'*(8-len(x))
        filler += x
        x = filler
    return x


def permute(pixel, s1, s2):
    new_pixel = []
    if s1 == 0 and s2 == 0:
        new_pixel = pixel
    elif s1 == 0 and s2 == 1:
        new_pixel.extend([pixel[2], pixel[0], pixel[1]])
    elif s1 == 1 and s2 == 0:
        new_pixel.extend([pixel[1], pixel[2], pixel[0]])
    elif s1 == 1 and s2 == 1:
        new_pixel.extend([pixel[2], pixel[1], pixel[0]])
    return tuple(new_pixel)


def unpermute(pixel, s1, s2):
    new_pixel = []
    if s1 == 0 and s2 == 0:
        new_pixel = pixel
    elif s1 == 0 and s2 == 1:
        new_pixel.extend([pixel[1], pixel[2], pixel[0]])
    elif s1 == 1 and s2 == 0:
        new_pixel.extend([pixel[2], pixel[0], pixel[1]])
    elif s1 == 1 and s2 == 1:
        new_pixel.extend([pixel[2], pixel[1], pixel[0]])
    return tuple(new_pixel)


def encrypt(pixel_matrix):
    gen = logistic_gen(4, 0.2)
    new_pixel_matrix = []
    for pixel in pixel_matrix:
        new_pixel = []
        crypt1 = next(gen)
        crypt2 = next(gen)
        crypt3 = next(gen)
        s1, s2 = int(crypt1[-1], 2) ^ int(crypt2[-1], 2) ^ int(crypt3[-1],
                                                               2), int(crypt1[-2], 2) ^ int(crypt2[-2], 2) ^ int(crypt3[-2], 2)
        pixel = permute(pixel, s1, s2)
        # print(pixel)
        new_pixel.append(dtB_lengther(bin(int(pixel[0], 2) ^ int(
            crypt1[-8:], 2)).replace('0b', '')))
        # print(int(crypt3[-8:], 2))
        new_pixel.append(dtB_lengther(bin(int(pixel[1], 2) ^ int(
            crypt2[-8:], 2)).replace('0b', '')))
        new_pixel.append(dtB_lengther(bin(int(pixel[2], 2) ^ int(
            crypt3[-8:], 2)).replace('0b', '')))
        new_pixel_matrix.append(new_pixel)
    return new_pixel_matrix


def decrypt(pixel_matrix):
    gen = logistic_gen(4, 0.2)
    new_pixel_matrix = []
    for pixel in pixel_matrix:
        new_pixel = []
        crypt1 = next(gen)
        crypt2 = next(gen)
        crypt3 = next(gen)
        s1, s2 = int(crypt1[-1], 2) ^ int(crypt2[-1], 2) ^ int(crypt3[-1],
                                                               2), int(crypt1[-2], 2) ^ int(crypt2[-2], 2) ^ int(crypt3[-2], 2)
        new_pixel.append(dtB_lengther(bin(int(pixel[0], 2) ^ int(
            crypt1[-8:], 2)).replace('0b', '')))
        # print(int(crypt3[-8:], 2))
        new_pixel.append(dtB_lengther(bin(int(pixel[1], 2) ^ int(
            crypt2[-8:], 2)).replace('0b', '')))
        new_pixel.append(dtB_lengther(bin(int(pixel[2], 2) ^ int(
            crypt3[-8:], 2)).replace('0b', '')))
        # print(s1, s2)
        new_pixel = unpermute(new_pixel, s1, s2)
        new_pixel_matrix.append(list(new_pixel))
    return new_pixel_matrix


# crypter = encrypt([('101001', '11111', '1111'), ('1011101',
#                   '0000010', '0101011'), ('11111111', '00000000', '10101010')])
# print(crypter)
# print(decrypt(crypter))
