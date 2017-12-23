'''
In order to be able to run this example, first execute
sudo apt-get install python-tk
'''

import matplotlib.pyplot as plt
import cv2
import numpy as np

fig = plt.figure()

image = cv2.imread('butterfly.jpg')
sub_plot = fig.add_subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
sub_plot.set_title('Image')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sub_plot = fig.add_subplot(1, 3, 2)
plt.imshow(gray, cmap='gray')
sub_plot.set_title('Grayscale image')

print 'Average pixel value is ' + str(np.mean(gray))
print 'Median pixel value is ' + str(np.median(gray))

sub_plot = fig.add_subplot(1, 3, 3)
plt.hist(image.flatten(), 50, normed=1, facecolor='green', alpha=0.75)
sub_plot.set_title('Histogram')

plt.show()