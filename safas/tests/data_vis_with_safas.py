# import sys
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter

import pandas as pd

# import cv2

# from safas import filters
# from safas import data
# from safas.filters.sobel_focus import imfilter as sobel_filter
# from safas.filters.imfilters_module import add_contours

# load the excel file as a Pandas DataFrame
df = pd.read_excel('../../notebooks/data/floc_props.xlsx', engine='openpyxl')
# see the keys
print(df.keys())

# plot velocity vs major_axis_length
f, ax = plt.subplots(1, 1, figsize=(3.5, 2.2), dpi=250)

# note: remove *10 factor if floc_props.xlsx file is updated: previous version was output in [cm/s]
ax.plot(df.major_axis_length, df.vel_mean * 10, marker='o', linestyle='None')
ax.set_xlabel('Floc size [$\mu$m]')
ax.set_ylabel('Settling velocity [mm/s]')

# convert to log-log
ax.loglog()
ax.axis([100, 5000, 0.1, 100])

for axis in [ax.xaxis, ax.yaxis]:
    axis.set_major_formatter(ScalarFormatter())

plt.tight_layout()
plt.show()

save = False
if save:
    plt.savefig('png/vel_size.png', dpi=900)
