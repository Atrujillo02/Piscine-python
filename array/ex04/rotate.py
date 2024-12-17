import numpy as np
import cv2
from load_image import ft_load


def display_image(img, title="Image"):
    """
    This function displays an image using OpenCV.

    Args:
        img (np.array): The image to display (NumPy array).
        title (str): The title of the OpenCV window.

    Returns:
        None
    """
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow(title, img_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def manual_transpose(img):
    """
    This function transposes a 2D or 3D image manually (without using library functions).

    Args:
        img (np.array): The image to transpose (NumPy array).

    Returns:
        np.array: A transposed version of the input image.
    """
    rows, cols, channels = img.shape
    transposed = np.zeros((cols, rows, channels), dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            for c in range(channels):
                transposed[j, i, c] = img[i, j, c]
    return transposed


def main():
    """
    This function loads an image, cuts a square region, transposes it manually,
    and displays the transposed image.

    Args:
        None

    Returns:
        None
    """
    img = ft_load("animal.jpeg")

    cutted = img[:400, :400, :1]
    print(f"The shape of image is: {cutted.shape} or {cutted.shape[:2]}")
    print(cutted)

    transposed = manual_transpose(cutted)
    transposed = transposed[:, :, 0]
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)

    display_image(transposed, title="Transposed Image")

if __name__ == "__main__":
    main()
