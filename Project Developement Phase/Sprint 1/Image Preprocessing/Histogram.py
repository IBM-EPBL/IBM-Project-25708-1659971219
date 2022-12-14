# -*- coding: utf-8 -*-
"""histogram.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nqzMVaK2M0dabPzzqauH3Ak1mJKKwoaL
"""

import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread

I = imread('/content/23ea1618-d554-47fb-bc03-a1b978f14fbf___RS_HL 6008.JPG')
J = imread('/content/25de086c-ea7e-42b0-83fd-bc7d1e584d0a___RS_HL 5852.JPG')

plt.figure()
plt.subplot(121), plt.imshow(I)
plt.subplot(122), plt.imshow(J)
plt.show()

plt.figure(figsize=(10, 10))
plt.imshow(np.abs(I[:, :, 0].astype(float) - J[:, :, 0].astype(float)), cmap='gray')
plt.show()

d = imread('/content/23ea1618-d554-47fb-bc03-a1b978f14fbf___RS_HL 6008.JPG')
mask = imread('/content/25de086c-ea7e-42b0-83fd-bc7d1e584d0a___RS_HL 5852.JPG')

print(np.amin(d), np.amax(d))
print(np.amin(mask), np.amax(mask))

plt.figure(), plt.imshow(mask), plt.show()

mask = mask[:, :, 0]

maskInv = np.zeros_like(mask)
maskInv[mask == 0] = 255
maskInv[mask == 255] = 0
plt.figure(), plt.imshow(maskInv, cmap='gray'), plt.show()
