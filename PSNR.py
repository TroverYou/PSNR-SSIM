import cv2
import numpy as np
from pathlib import Path
import argparse
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim

def calculate_psnr(img1, img2):
    """
    Calculate PSNR (Peak Signal-to-Noise Ratio) between two images using skimage.
    Higher values indicate better quality (less difference between images).
    """
    # Convert images to grayscale for PSNR calculation
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # Calculate PSNR between two images using scikit-image
    return psnr(gray1, gray2)

def calculate_ssim(img1, img2):
    """
    Calculate SSIM (Structural Similarity Index) between two images.
    Returns a value between -1 and 1, where 1 means identical images.
    """
    # Convert images to grayscale for SSIM calculation
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # Calculate SSIM between two images using scikit-image
    score = ssim(gray1, gray2)
    return score

def main():
    # Set up argument Parser
    parser = argparse.ArgumentParser(description='Calculate PSNR and SSIM between two images')
    parser.add_argument('image1', help='Path to first image')
    parser.add_argument('image2', help='Path to second image')
    args = parser.parse_args()

    # Check if files exist
    if not Path(args.image1).exists():
        print(f"Error: File {args.image1} does not exist")
        return
    if not Path(args.image2).exists():
        print(f"Error: File {args.image2} does not exist")
        return

    # Read images
    try:
        img1 = cv2.imread(args.image1)
        img2 = cv2.imread(args.image2)

        # Check if images were loaded successfully
        if img1 is None or img2 is None:
            print("Error: Could not load one or both images")
            return

        # Check if images have the same dimensions
        if img1.shape != img2.shape:
            print("Error: Images must have the same dimensions")
            return

        # Calculate PSNR
        psnr_value = calculate_psnr(img1, img2)
        
        # Calculate SSIM
        ssim_value = calculate_ssim(img1, img2)

        # Print results
        print(f"\nResults for comparing {Path(args.image1).name} and {Path(args.image2).name}:")
        print(f"PSNR: {psnr_value:.2f} dB")
        print(f"SSIM: {ssim_value:.4f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
