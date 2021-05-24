
# Package for viewing the images
import matplotlib.pyplot as plt

# import cv2

# from safas import filters
from safas import data
from safas.filters.sobel_focus import imfilter
# from safas.filters.imfilters_module import add_contours

img = data.brightmudflocs()

img = img[400:1000, 400:1000, :]
print('shape:', img.shape)
# apply threshold to segment the image
params = {'img_thresh': 160,
          'apply_focus_filter': False,
          'apply_clearedge_filter': False,
          'contour_color': (0, 255, 0)}

thresh_labels, thresh_contours = imfilter.imfilter(src=img.copy(), **params)

# apply sobel-based gradient to segment the image
params = {'img_thresh': 160,
          'edge_thresh': 210,
          'edge_distance': 1,
          'apply_focus_filter': True,
          'apply_clearedge_filter': True,
          'contour_color': (0, 255, 0), }

sobel_labels, sobel_contours = imfilter.imfilter(src=img.copy(), **params)

f, ax = plt.subplots(1, 3, dpi=250, figsize=(7.5, 3.5))
ax = ax.ravel()
for a in ax:
    a.set_xticks([])
    a.set_yticks([])

ax[0].imshow(img)
ax[0].set_title('Raw image')
ax[1].imshow(thresh_contours)
ax[1].set_title('Threshold filter')
ax[2].imshow(sobel_contours)
ax[2].set_title('Sobel-focus filter')
plt.tight_layout()
plt.show()

save = True

if save:
    plt.savefig('png/filter_ex.png', dpi=900)
