import cv2
import numpy as np

image_names = ['basketball1.jpg', 'basketball2.jpg', 'basketball3.jpg', 'basketball4.jpg', 'basketball5.jpg']


def show_image(image):
    '''
    Shows an image and waits for a keystroke
    :param image: numpy.ndarray
    '''
    cv2.imshow('image', image)
    print 'Hit Esc to continue'
    cv2.waitKey()
    cv2.destroyWindow('image')

def draw_circle_on_image(image, x, y, r):
    '''
    Draws a circle on a given image
    :param image: numpy.ndarray
    :param x: x coordinate of the circle (int)
    :param y: y coordinate of the circle (int)
    :param r: circle radius (int)
    '''
    cv2.circle(image, (x, y), r, (0, 255, 0), 4)

def create_circle_interior_mask(x, y, r, size):
    '''
    Creates a binary mask of a circle interior
    :param x: x coordinate of the circle (int)
    :param y: y coordinate of the circle (int)
    :param r: circle radius (int)
    :param size: mask size (tuple)
    :return: numpy.ndarray
    '''
    circle_mask = np.zeros(size)
    cv2.circle(circle_mask, (x, y), r, 255, -1)
    return circle_mask

def create_hsv_mask(image, lower_hue, lower_sat, lowe_val, upper_hue, upper_sat, upper_val):
    '''
    Creates an HSV mask of values in the color range
    Converts hue, saturation and value from http://colorizer.org/'s format to OpenCV
    :param image: np.ndarray
    :param lower_hue: int
    :param lower_sat: int
    :param lowe_val: int
    :param upper_hue: int
    :param upper_sat: int
    :param upper_val: int
    :return: numpy.ndarray
    '''
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_color = np.array([lower_hue / 2, lower_sat * 255 / 100, lowe_val * 255 / 100])
    upper_color = np.array([upper_hue / 2, upper_sat * 255 / 100, upper_val * 255 / 100])
    hsv_mask = cv2.inRange(hsv, lower_color, upper_color)
    return hsv_mask

if __name__ == '__main__':

    for image_name in image_names:
        image = cv2.imread('images/' + image_name)

        # TODO: add your code here

        show_image(image)