import cv2
import numpy as np
import argparse
import os

def apply_blur(image_path, blur_type='gaussian', kernel_size=5):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not load image")

    blur_type.lower() == 'gaussian'
    blurred = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

    # Get original file extension
    _, file_ext = os.path.splitext(image_path)
    file_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = f'{file_name}_blurred{file_ext}'
    
    # Create 'output' directory if it doesn't exist
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save the blurred image in the output directory
    output_path = os.path.join(output_dir, output_path)
    cv2.imwrite(output_path, blurred)
    return output_path

def main():
    parser = argparse.ArgumentParser(description='Blur an image using different methods')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('--type', type=str, default='gaussian', 
                        choices=['gaussian', 'median', 'average'],
                        help='Type of blur to apply')
    parser.add_argument('--kernel', type=int, default=5,
                        help='Kernel size for blur (must be odd number)')

    args = parser.parse_args()

    try:
        output_path = apply_blur(args.image_path, args.type, args.kernel)
        print(f"Successfully created blurred image: {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()