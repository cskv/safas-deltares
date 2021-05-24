# import sys
from matplotlib import pyplot as plt

import cv2

# from safas import filters
from safas import data
# from safas.filters.sobel_focus import imfilter as sobel_filter
from safas.filters.imfilters_module import add_contours

# load images from the safas/data module
clear = data.clearfloc()
noisy = data.noisyfloc()

# convert to grayscale, apply Otsu's binarization, add contours at the threshold
clear_g = cv2.cvtColor(clear.copy(), cv2.COLOR_BGR2GRAY)
ret_clear, clear_th = cv2.threshold(clear_g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
clear_cont = add_contours(clear.copy(), clear_th, [0, 255, 0])

noisy_g = cv2.cvtColor(noisy.copy(), cv2.COLOR_BGR2GRAY)
ret_noisy, noisy_th = cv2.threshold(noisy_g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
noisy_cont = add_contours(noisy.copy(), noisy_th, [0, 255, 0])

# plot the images and their gray level intensity histograms
f, ax = plt.subplots(2, 2, dpi=150, figsize=(7.5, 7))
ax = ax.ravel()

for a in [ax[0], ax[1]]:
    a.set_xticks([])
    a.set_yticks([])

for a in [ax[2], ax[3]]:
    a.set_xlabel('gray level [--]')
    a.set_ylabel('Frequency [--]')
    a.set_ylim(0, 500)

ax[0].imshow(clear_cont)
ax[0].set_title('Clear background')

ax[1].imshow(noisy_cont)
ax[1].set_title('Noisy background')

ax[2].hist(clear.ravel(), bins=255)
ax[2].axvline(ret_clear, linestyle='--', color='r')
ax[2].set_title('Clear histogram')

ax[3].hist(noisy.ravel(), bins=255)
ax[3].axvline(ret_noisy, linestyle='--', color='r')
ax[3].set_title('Noisy histogram')

plt.tight_layout()
plt.show()

save = False

if save:
    plt.savefig('png/clear_noisy.png', dpi=900)
