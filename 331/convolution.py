from typing import Optional

import numpy as np
import math


def convolution2D(
        image: np.array, kernel: np.array, padding: Optional[int] = None, stride: int = 1
) -> np.array:
    """Calculate the convolution between the input image and a filter, returning the feature map.

    Args:
        image (np.array): Input image as 2d array with height x width. Supposed to have equal dimensions.
        kernel (np.array): Filter or kernel as 2d array with height x width. Supposed to have equal and odd dimensions.
        padding (Optional[int]): Border around the image with pixels of value 0. If None, defaults to p = (f - 1) / 2.
        stride (int): Step length to move the filter over the image. Defaults to 1.

    Returns:
        np.array: the feature map constructed from the image and the kernel.
    """

    if not isinstance(image, np.ndarray) or not isinstance(kernel, np.ndarray):
        raise TypeError

    if image.ndim != 2 or kernel.ndim != 2:
        raise ValueError

    row, col = image.shape
    if row != col:
        raise ValueError

    row, col = kernel.shape
    if row != col:
        raise ValueError

    if not np.issubdtype(image.dtype, np.number) or not np.issubdtype(kernel.dtype, np.number):
        raise TypeError

    if (kernel.size % 2) == 0:
        raise ValueError

    if kernel.size > image.size:
        raise ValueError

    if padding is None:
        p = (kernel.shape[0] - 1) / 2
    else:
        if not isinstance(padding, int):
            raise TypeError
        if padding < 0:
            raise ValueError
        p = padding

    if stride <= 0:
        raise ValueError

    if not isinstance(stride, int):
        raise TypeError

    # calculate feature map dimension
    n_out = math.floor(((image.shape[0] + (2 * p) - kernel.shape[0]) / stride) + 1)

    # initialize feature_map
    feature_map = np.zeros((n_out, n_out))

    # apply padding
    image = np.pad(image, pad_width=int(p), mode='constant', constant_values=0)
    # print(image)

    j = 0
    # populate feature_map
    # move feature map from top to bottom over image
    for row in range(0, image.shape[1] + 1, stride):
        # column-wise population for each row
        # move feature map from left to right over image
        i = 0
        if j == n_out:
            break
        row_elements = []
        for col in range(kernel.shape[1], image.shape[1] + stride, stride):
            if i > image.shape[1]:
                break
            # print(image[row:n_out+row, i:col])
            image_subset = image[row:kernel.shape[1] + row, i:col]
            if image_subset.shape != kernel.shape:
                break
            # print(i)
            # print(image_subset)
            row_elements.append(np.sum(np.multiply(image_subset, kernel)))
            i += stride
        # print(j)
        feature_map[j, :] = row_elements
        j += 1

    return feature_map
