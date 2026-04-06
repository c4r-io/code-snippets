import numpy as np
import matplotlib.pyplot as plt
from nd2reader import ND2Reader
from scipy.ndimage import zoom, gaussian_filter


raw_microscopy_data = ND2Reader('20191010_tail_01.nd2')

image_shape = raw_microscopy_data .shape
z_index = np.argmin(image_shape)
maximum_intensity_projection = np.max(raw_microscopy_data, axis=z_index)

min_pixel_value = np.min(maximum_intensity_projection)
max_pixel_value = np.max(maximum_intensity_projection)
normalized_image = (maximum_intensity_projection - min_pixel_value) / (max_pixel_value - min_pixel_value)

downsample_factor = (1, 1)
downsampled_image = zoom(normalized_image, downsample_factor)

smooth_factor = 0.02
smoothed_image = gaussian_filter(downsampled_image, sigma=smooth_factor)

plt.imshow(smoothed_image)
plt.title('Processed Microscopy Image')
plt.show()