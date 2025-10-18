import cv2
from shifting import apply_shift
from bluring import apply_blur
from compress import apply_compress
from PSNR import calculate_psnr, calculate_ssim

def main():
    # Replace with your image path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_name = 'test_image1.jpg'
    image_path = os.path.join(script_dir, image_name)
    
    try:
        # Create distorted images using existing functions
        original = cv2.imread(image_path)
        if original is None:
            raise ValueError("Could not load original image")
            
        # Create distorted versions using existing functions
        blurred_path = apply_blur(image_path, blur_type='gaussian', kernel_size=5)
        shifted_path = apply_shift(image_path, shift_amount=1)
        compressed_path = apply_compress(image_path, compression_ratio=10)
        
        # Read back the distorted images
        blurred = cv2.imread(blurred_path)
        shifted = cv2.imread(shifted_path)
        compressed = cv2.imread(compressed_path)
        
        # Calculate metrics for blurred image
        print("Metrics for blurred image:")
        psnr_blur = calculate_psnr(original, blurred)
        ssim_blur = calculate_ssim(original, blurred)
        print(f"PSNR: {psnr_blur:.2f}")
        print(f"SSIM: {ssim_blur:.4f}")
        
        # Calculate metrics for shifted image
        print("\nMetrics for shifted image:")
        psnr_shift = calculate_psnr(original, shifted)
        ssim_shift = calculate_ssim(original, shifted)
        print(f"PSNR: {psnr_shift:.2f}")
        print(f"SSIM: {ssim_shift:.4f}")
        
        # Calculate metrics for compressed image
        print("\nMetrics for compressed image:")
        psnr_compressed = calculate_psnr(original, compressed)
        ssim_compressed = calculate_ssim(original, compressed)
        print(f"PSNR: {psnr_compressed:.2f}")
        print(f"SSIM: {ssim_compressed:.4f}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":

    main()
