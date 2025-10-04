import cv2
import numpy as np
import argparse
import os

def apply_shift(image_path, shift_amount=1):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not load image")
    
    # Create shifted image
    shifted = np.zeros_like(img)
    
    # Copy the image with shift
    shifted[:, shift_amount:] = img[:, :-shift_amount]
    # Copy leftmost columns to fill the gap
    for i in range(shift_amount):
        shifted[:, i] = img[:, 0]

    # Create output filename with original extension
    _, file_ext = os.path.splitext(image_path)
    file_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = f'{file_name}_shifted{file_ext}'
    
    # Create 'output' directory if it doesn't exist
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save the shifted image in the output directory
    output_path = os.path.join(output_dir, output_path)
    cv2.imwrite(output_path, shifted)
    return output_path

def main():
    parser = argparse.ArgumentParser(description='Shift image pixels to the right')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('--shift', type=int, default=1,
                        help='Number of pixels to shift right (default: 1)')

    args = parser.parse_args()

    try:
        if args.shift < 0:
            raise ValueError("Shift amount must be positive")
            
        output_path = apply_shift(args.image_path, args.shift)
        print(f"Successfully created shifted image: {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()