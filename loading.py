def load_tif(file_path):
    microscopy_volume = imread(file_path)
    return microscopy_volume
def load_nd2(file_path):
    raw_data = ND2Reader(file_path)
    microscopy_volume = np.transpose(raw_data, (1, 2, 0))
    return microscopy_volume
def load_nwb(file_path):
    io_obj = NWBHDF5IO(file_path, mode="r")
    nwb_file = io_obj.read()
    
    image_data = nwb_file.acquisition['NeuroPALImageRaw'].data[:]
    rotated_image = np.transpose(image_data, (1, 0, 2, 3))
    
    rgb_channel_indices = nwb_file.acquisition['NeuroPALImageRaw'].RGBW_channels[:3]
    microscopy_volume = rotated_image[:, :, :, rgb_channel_indices]
    
    image_dtype = microscopy_volume.dtype
    maximum_integer_value = np.iinfo(image_dtype).max
    microscopy_volume = (microscopy_volume/maximum_integer_value) * 255
    
    io_obj.close()
    return microscopy_volume
def load_parameters(file_format):
    match file_format:
        case 'nd2':
            is_normalized = False
            is_mip = False
            is_cropped = False
            zoom_level = (1, 1)
            gaussian_sigma = 0
            
        case 'tif' | 'tiff':
            is_normalized = False
            is_mip = True
            is_cropped = False
            zoom_level = (0.35, 0.35, 1)
            gaussian_sigma = 0.3
            
        case 'nwb':
            is_normalized = False
            is_mip = False
            is_cropped = True
            zoom_level = (1, 0.75, 1)
            gaussian_sigma = 0
            
        case _:
            raise ValueError("Unknown file format!")
            
    return is_normalized, is_mip, is_cropped, zoom_level, gaussian_sigma
