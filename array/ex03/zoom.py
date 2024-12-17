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


def main():
    """
    This function loads an image, prints its shape, zooms into a specific region,
    and displays the zoomed image.

    Args:
        None

    Returns:
        None
    """
    try:
        img = ft_load("animal.jpeg")
        print(img)

        zoomed = img[:400, :400, :1]
        print(f"New shape after slicing: {zoomed.shape} or {zoomed.shape[:2]}")
        print(zoomed)

        display_image(zoomed, title="Zoomed Image")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
