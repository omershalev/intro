import cv2
import numpy as np

images = ['basketball1.jpg', 'basketball2.jpg', 'basketball3.jpg', 'basketball4.jpg', 'basketball5.jpg']

if __name__ == '__main__':
    image = cv2.imread(r'/home/administrator/Downloads/basketball/' + images[0])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 200)
    hsv_mask = cv2.inRange(hsv, np.array([20 / 2, 60 * 255 / 100, 60 * 255 / 100]), np.array([40 / 2, 100 * 255 / 100, 100 * 255 / 100]))
    basketball_x, basketball_y, basketball_r = None, None, None    
    max_correspondence = -np.inf
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
     
        for (x, y, r) in circles:
            circle_mask = np.zeros((480, 640))
            cv2.circle(circle_mask, (x, y), r, 255, -1)
            hsv_and_circle_mask = hsv_mask * circle_mask
            correspondence = float(np.count_nonzero(hsv_and_circle_mask)) / np.count_nonzero(circle_mask)
            if max_correspondence < correspondence:
                max_correspondence = correspondence
                basketball_x, basketball_y, basketball_r = x, y, r
    else:
        print 'No circles found'

    cv2.circle(image, (basketball_x, basketball_y), basketball_r, (0, 255, 0), 4)
    cv2.imshow('image', image)
    cv2.waitKey()
    cv2.destroyWindow('image')