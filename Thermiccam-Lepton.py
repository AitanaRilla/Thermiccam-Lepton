import pylepton as pylept
import numpy as npy
import cv2

#Show thermal video from lepton
while True:
    with pylept.Lepton() as lept:
        a, _ = lept.capture()
    cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)  # extend contrast
    npy.right_shift(a, 8, a)  # fit data into 8 bits
    cv2.imshow("Lepton", npy.uint8(a))  # display it!
    if cv2.waitKey(1) == 27:
        exit(0)
