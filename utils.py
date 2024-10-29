import matplotlib.pyplot as plt
import numpy as np

def histogram(image):
    hist = {i : 0 for i in range(256)}
    for h in range(image.shape[0]):
        for w in range(image.shape[1]):
            hist[image[h, w]] += 1
    return hist

def visualize(image, histogram_=True, cdf=False):
    # Original Image
    plt.subplot2grid((2, 4), (0, 0), colspan=2)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.title('Image')

    # FFT : Amplitude 
    plt.subplot2grid((2, 4), (0, 2), colspan=2)
    image_fft = np.fft.fft2(image)
    image_fft = np.fft.fftshift(image_fft)
    image_amp = 20 * np.log(np.abs(image_fft))
    plt.imshow(image_amp, cmap='gray')
    plt.axis('off')
    plt.title('Amplitude Spectrum')

    if histogram_:
        # Histogram
        ax = plt.subplot2grid((2, 4), (1, 0), colspan=4)
        image_hist = histogram(image)
        plt.bar(image_hist.keys(), image_hist.values())
        plt.xlim(0, 255)
        plt.title('Histogram')
        # CDF
        if cdf:
            hist_values = np.array(list(image_hist.values()))
            cdf_values = np.cumsum(hist_values) / np.sum(hist_values)
            cdf_scaled = cdf_values * max(hist_values)
            plt.plot(list(image_hist.keys()), cdf_scaled, color='red', label='CDF', linewidth=1)
            plt.legend()

def visualizePixel(img):
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.colorbar()