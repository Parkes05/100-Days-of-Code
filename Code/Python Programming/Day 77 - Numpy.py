import numpy as np
import matplotlib.pyplot as plt
from scipy import datasets
from PIL import Image


# 1-dimensional array - vector
my_array = np.array([1.1, 9.2, 8.1, 4.7])
# print(my_array.shape)
# print(my_array[2])
# print(my_array.ndim)


# 2-dimensional array - matrix
array_2d = np.array([[1, 2, 3, 6, 9], 
                     [2, 3, 4, 5, 7]])
# print(array_2d.shape)
# print(array_2d.ndim)
# print(array_2d[0, 2])
# print(array_2d[0:2])


# n-dimensional array - tensor
mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                         [[7, 86, 6, 98],
                          [5, 1, 0, 4]],
                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])
# print(mystery_array)
# print(mystery_array.shape)
# print(mystery_array.ndim)
# print(mystery_array[2, 1, 3])
# print(mystery_array[2, 1, :])
# print(mystery_array[:, :, 0])


a = np.arange(10, 30)
# print(a)
# print(a.shape)
# print(a[-3:])
# print(a[4:7])
# print(a[13:])
# print(a[::2])

# print(a[::-1])
# print(np.flip(a))

b = np.array([6, 0, 9, 0, 0, 5, 0])
non_zero = b[np.nonzero(b)]
# print(non_zero)

c = np.random.random(size=(3, 3, 3))
# print(c)

x = np.linspace(0, 100, num=9)
# print(x)

y = np.linspace(-3, 3, num=9)
# print(y)

# plt.plot(x, y)
# plt.show()

noise = np.random.random(size=(128, 128, 3))
# print(noise)
# plt.imshow(noise)
# plt.show()

v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])
sum = v1 + v2
mul = v1 * v2
# print(sum)
# print(mul)


list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]
# print(list1 + list2)


array_2d = np.array([[1, 2, 3, 4], 
                     [5, 6, 7, 8]])
# print(array_2d + 10)
# print(array_2d * 5)

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])
 
b1 = np.array([[4, 1, 3],
               [5, 8, 5]])
matrix_mul = np.matmul(a1, b1)
# print(matrix_mul)
# print(a1 @ b1)


img = datasets.face()
# plt.imshow(img)
# plt.show()
# print(type(img))
# print(img.shape)
# print(img)

srbg_img = img / 255
# print(srbg_img)
grey_vals = np.array([0.2126, 0.7152, 0.0722])
black_white = np.matmul(srbg_img, grey_vals)
# print(black_white)
# plt.imshow(black_white, cmap='gray')
# plt.show()

flipped_img = np.flip(black_white)
# plt.imshow(flipped_img, cmap='gray')
# plt.show()

rot_90 = np.rot90(srbg_img)
# plt.imshow(rot_90)
# plt.show()

inverse = 255 - img
# plt.imshow(inverse)
# plt.show()


my_img = Image.open('yummy_macarons.jpg')
img_array = np.array(my_img)
# print(img_array)
# plt.imshow(img_array)
plt.imshow(255 - img_array)
plt.show()