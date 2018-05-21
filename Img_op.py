
import numpy as np
import cv2

def main():
 # Load an color image in grayscale
  img = cv2.imread('Bright-blue-circuit-board.jpg',0)
  cv2.imshow('image', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__=="__main__":
    main()
