# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 13:17:45 2025

@author: ninaj
"""

import nibabel as nib
import cv2
import numpy as np

# Load NIfTI file
img = nib.load(r"Z:\FacialDeformation_MPhys\rhabdo_data_proton\DICOMS\abby\UIDQQ0x1x1Hx7\CT.nii.gz")
data = img.get_fdata()

# Normalize data to 0-255 for 8-bit video
data_min = data.min()
data_max = data.max()
data_norm = ((data - data_min) / (data_max - data_min) * 255).astype(np.uint8)

# Get video dimensions
height, width = data_norm.shape[0], data_norm.shape[1]

# Create video writer (change FPS if you want)
video = cv2.VideoWriter(
    r"Z:\FacialDeformation_MPhys\rhabdo_data_proton\DICOMS\abby\UIDQQ0x1x1Hx7\ct_video.avi",
    cv2.VideoWriter_fourcc(*'XVID'),
    15,
    (width, height),
    isColor=False
)


# Write each slice as a frame
for i in range(data_norm.shape[2]):
    frame = data_norm[:, :, i]
    video.write(frame)

video.release()
print("Video saved as ct_video.avi")
