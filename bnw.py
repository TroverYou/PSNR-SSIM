import cv2
import numpy as np
import argparse
import os

def apply_bnw(image_path, threshold=None):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not load image")

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply threshold if specified
    if threshold is not None:
        _, bnw = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    else:
        bnw = gray

    # Create output filename with original extension
    _, file_ext = os.path.splitext(image_path)
    file_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = f'{file_name}_bnw{file_ext}'
    
    # Create 'output' directory if it doesn't exist
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save the black and white image in the output directory
    output_path = os.path.join(output_dir, output_path)
    cv2.imwrite(output_path, bnw)
    return output_path

def main():
    parser = argparse.ArgumentParser(description='Convert image to black and white')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('--threshold', type=int, default=None,
                        help='Threshold value (0-255) for binary B&W. If not set, creates grayscale.')

    args = parser.parse_args()

    try:
        if args.threshold is not None and (args.threshold < 0 or args.threshold > 255):
            raise ValueError("Threshold must be between 0 and 255")
            
        output_path = apply_bnw(args.image_path, args.threshold)
        print(f"Successfully created B&W image: {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()