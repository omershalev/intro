'''
Basketball segmentation
Based on the following two articles:
https://docs.opencv.org/3.1.0/da/d53/tutorial_py_houghcircles.html
https://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles
'''
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

        hsv_mask = create_hsv_mask(image, 20, 60, 60, 40, 100, 100)
        # show_image(hsv_mask)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 200)
        basketball_x = None
        basketball_y = None
        basketball_r = None
        max_correspondence = -np.inf
        if circles is not None:
            circles = np.round(circles[0, :]).astype('int')
            for (x, y, r) in circles:
                circle_mask = create_circle_interior_mask(x, y, r, (np.size(image, 0), np.size(image, 1)))
                hsv_and_circle_mask = hsv_mask * circle_mask
                correspondence = float(np.count_nonzero(hsv_and_circle_mask)) / np.count_nonzero(circle_mask)
                if max_correspondence < correspondence:
                    max_correspondence = correspondence
                    basketball_x = x
                    basketball_y = y
                    basketball_r = r
                    # show_image(circle_mask)
        else:
            print 'No circles found'

        draw_circle_on_image(image, basketball_x, basketball_y, basketball_r)
        show_image(image)