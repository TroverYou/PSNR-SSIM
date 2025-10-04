# PSNR-SSIM
Using the scikit-image library to calculate the PSNR and SSIM values of a grey-scaled image with its distorted versions: blurred, compressed, or shifted.

This code shows that PSNR and SSIM both are relatively co-dependent with each other with similar relative values (i.e. if PSNR is high, SSIM is closer to 1 and vice versa). Furthermore, it shows that the higher the resolution/data size of the original image is, the higher the values of the metric values will be.

In the main function, you can change the kernal size of the blur, the shift amount, and the compression ratio. The metrics show the obvious result that using higher alterations to the image lowers the resulting metric values.
