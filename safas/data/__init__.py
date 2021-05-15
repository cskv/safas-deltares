"""
Load test images.

Note: this is the same loader mechanism used by scikit-image
See: https://github.com/scikit-image/scikit-image/blob/main/skimage/data/__init__.py
"""

# import os as _os
# import skimage
# import numpy as np
# from warnings import warn
import pandas as pd

import os
data_dir = os.path.abspath(os.path.dirname(__file__))

__all__ = ['mudflocs']


def _load(f, as_gray=False):
    """Load an image file located in the data directory.

    Args:
        f (str):         File name.
        as_gray (bool):  optional, True if conversion of the image to grayscale is needed.

    Returns:
        (ndarray):       Image loaded from ``safas.data_dir``.
    """
    # importing io is quite slow since it scans all the backends
    # we lazy import it here
    from skimage.io import imread
    return imread(os.path.join(data_dir, f), plugin='pil', as_gray=as_gray)


def noisy():
    """fetches noisy image.

    Returns:
        (ndarray): Noisy gray level floc image.
    """
    return _load("noisy.png")


def mudflocs():
    """ fetches mudfloc image.

    Returns:
        Gray-level "mudflocs" image. Example image of mud flocs in settling column.
        Higher number density. camera : (1000, 1000, 3) uint8 ndarray
        Mudflocs image.
    """
    return _load("mudflocs.png")


def clayflocs():
    """fetches clayflocs image.

    Returns:
        Gray-level "clayflocs" image. Example image of clay flocs in settling column.
        Lower number density. camera : (1000, 1000) uint8 ndarray
        clayflocs image.
    """
    return _load("clayflocs.png")


def brightmudflocs():
    """fetches brightmudflocs image.

    Returns:
        Gray-level "clayflocs" image. Example image of clay flocs in settling colum.
        Brighter light source w. mean approx. 225 on uint8 scale.
        camera : (1000, 1000, 3) uint8 ndarray
        brightmudflocs image.
    """
    return _load("brightmudflocs.png")


def clearfloc():
    """fetches clearfloc image

    Returns:
        Gray-level "clearfloc" image. Example image of a single mud floc with a clear background.
        camera : (512, 512, 3) uint8 ndarray
        clearfloc image.
    """
    return _load("clearfloc.png")


def noisyfloc():
    """Gray-level "noisyfloc" image.
    Example image of a single mud floc with a noisy background.

    Returns
    -------
    camera : (512, 512, 3) uint8 ndarray
        noisyfloc image.
    """
    return _load("noisyfloc.png")


def por_flocs():
    """fetches por_flocs Excel file to Dataframe.

    Returns:
        (pandas data frame): results from video measurement of the POR sample
    """
    return pd.read_excel('por_flocs.xlsx')
