import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, IMG_PATH):
        self.IMG_PATH = IMG_PATH
        self.img = cv2.imread(IMG_PATH)
        if self.img is None:
            raise FileNotFoundError("No image was found")

    @staticmethod
    def method_to_resize():
        methods = {
            'linear': cv2.INTER_LINEAR,
            'nearest': cv2.INTER_NEAREST,
            'polynomial': cv2.INTER_CUBIC,
        }
        print("Available interpolation methods:")
        for key, value in methods.items():
            print(f"  - {key.capitalize()}: OpenCV code {value}")

    def resize_image(self, fx, fy, method='linear'):
        methods = {
            'linear': cv2.INTER_LINEAR,
            'nearest': cv2.INTER_NEAREST,
            'polynomial': cv2.INTER_CUBIC,
        }
        if method not in methods:
            raise ValueError(f"Invalid method. Choose from {list(methods.keys())}.")
        
        self.img = cv2.resize(self.img,fx=fx,fy=fy)
        print(f"Resized image dimensions: {self.get_dimensions()}") 
    def blur_image(self, blur_type='box', ksize=(5, 5)):
        """
        Blur the image using different techniques.
        
        :param blur_type: Type of blurring ('box', 'gaussian', 'adaptive')
        :param ksize: Kernel size, tuple (width, height)
        """
        if blur_type == 'box':
            self.img = cv2.blur(self.img, ksize)
            print("Applied Box Blurring")
        elif blur_type == 'gaussian':
            self.img = cv2.GaussianBlur(self.img, ksize, 0)
            print("Applied Gaussian Blurring")
        elif blur_type == 'adaptive':
            self.img = cv2.adaptiveThreshold(self.img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
            print("Applied Adaptive Blurring")
        else:
            raise ValueError("Invalid blur type. Choose from 'box', 'gaussian', or 'adaptive'.")


    def display_image(self, window_name='Image'):
        cv2.imshow(window_name, self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_image(self, output_path):
        try:
            # cv2.imshow('Image',self.img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imwrite(output_path, self.img)
            print(f"Image saved to {output_path}")
        except Exception as e:
            print(f"Error saving image: {e}")

    def get_dimensions(self):
        return self.img.shape


if __name__ == '__main__':
    IMG_PATH = 'images/img.png'
    processor = ImageProcessor(IMG_PATH)
    print(f"Original image dimensions: {processor.get_dimensions()}")
    processor.resize_image(10, 10)
    
    processor.save_image('edited_images/asdf.png')
