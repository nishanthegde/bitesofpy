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

    if padding is None:
        p = (kernel.shape[0] - 1) / 2
    else:
        p = padding

    # if padding > 0:
    #     image = np.pad(image, pad_width=int(padding), mode='constant', constant_values=0)

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


def main():
    print("thank you for looking after mama and naia")

    KERNEL_1x1 = np.array([[1]])
    IMAGE_1x1 = np.array([[1]])
    IMAGE_3x3 = np.random.rand(3, 3)
    KERNEL_3x3_SHARPEN = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    image_nh_3x3 = np.array([[105, 102, 100], [103, 99, 103], [101, 98, 104]])
    kernel_nh_3x3 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    IMAGE_9x9 = np.random.rand(9, 9)
    KERNEL_3x3_SHARPEN = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    IMAGE_256x256 = np.random.rand(256, 256)
    KERNEL_5x5 = np.random.rand(5, 5)

    # feature_map = convolution2D(IMAGE_3x3, KERNEL_3x3_SHARPEN, 0, 1)
    # feature_map = convolution2D(IMAGE_9x9, KERNEL_3x3_SHARPEN, 0, 1)
    # feature_map = convolution2D(IMAGE_9x9, KERNEL_3x3_SHARPEN, None, 1)
    # feature_map = convolution2D(IMAGE_9x9, KERNEL_3x3_SHARPEN, 0, 2)
    # feature_map = convolution2D(IMAGE_9x9, KERNEL_3x3_SHARPEN, None, 2)
    # feature_map = convolution2D(IMAGE_9x9, KERNEL_3x3_SHARPEN, 0, 3)
    # feature_map = convolution2D(IMAGE_9x9, KERNEL_3x3_SHARPEN, 2, 3)
    feature_map = convolution2D(IMAGE_256x256, KERNEL_5x5, None, 3)
    print(feature_map)


if __name__ == "__main__":
    main()
