from typing import Optional

import numpy as np


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
        padding = (kernel.shape[0] - 1) / 2

    if padding > 0:
        image = np.pad(image, pad_width=int(padding), mode='constant', constant_values=0)

    # return image
    return np.multiply(image, kernel)


def main():
    print("thank you for looking after mama and naia")
    KERNEL_1x1 = np.array([[1]])
    IMAGE_1x1 = np.array([[1]])
    IMAGE_3x3 = np.random.rand(3, 3)
    KERNEL_3x3_SHARPEN = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    # feature_map = convolution2D(IMAGE_1x1, KERNEL_1x1, 0, 1)
    feature_map = convolution2D(IMAGE_3x3, KERNEL_3x3_SHARPEN, None, 1)
    print(feature_map)
    print(feature_map.shape)
    # np.testing.assert_array_equal(feature_map.shape, (1, 1))


if __name__ == "__main__":
    main()
