import cv2
import numpy as np
import argparse
import os

def apply_compress(image_path, compression_ratio=10):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not load image")

    # Create output filename with jpg extension
    file_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = f'{file_name}_compressed.jpg'
    
    # Create 'output' directory if it doesn't exist
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save the compressed image in JPEG format
    # compression_ratio is inverted (0-100) where 100 is best quality
    quality = int(100 / compression_ratio)
    quality = max(1, min(quality, 100))  # Ensure quality is between 1 and 100
    
    output_path = os.path.join(output_dir, output_path)
    cv2.imwrite(output_path, img, [cv2.IMWRITE_JPEG_QUALITY, quality])
    return output_path

def main():
    parser = argparse.ArgumentParser(description='Compress image to JPEG format')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('--ratio', type=float, default=10,
                        help='Compression ratio (default: 10)')

    args = parser.parse_args()

    try:
        if args.ratio <= 0:
            raise ValueError("Compression ratio must be positive")
            
        output_path = apply_compress(args.image_path, args.ratio)
        print(f"Successfully created compressed image: {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()