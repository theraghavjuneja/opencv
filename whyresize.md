#### Scaling and Resizing
- image resizing means the scaling of images
- to reduce number of pixels(Helpful in training neural network, as it decreases model complexity)
- zoom in zoom out etc.

#### Interpolation choice
- cv2.INTER_AREA(shrink)
- cv2.INTER_CUBIC(slow nut effecient)
- cv2.INTER_LINEAR(used when zooming required, fefault)