# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 12:15:08 2025

@author: ninaj
"""

import nibabel as nib

# Load your NIfTI file
img = nib.load(r"Z:\FacialDeformation_MPhys\rhabdo_data_proton\DICOMS\UIDQQ0x7axQ0Q1\CT1.2.826.0.1.3680043.2.135.735751.52663672.7.1645803422.468.17.dcm")

# Convert image data to a NumPy array
data = img.get_fdata()

import matplotlib.pyplot as plt

# Show the middle slice in the z direction
slice_index = data.shape[2] // 2
plt.imshow(data[:, :, slice_index], cmap="gray")
plt.axis("off")
plt.show()

# Loop through slices along z-axis
for i in range(0, data.shape[2], 10):  # every 10th slice
    plt.imshow(data[:, :, i], cmap="gray")
    plt.title(f"Slice {i}")
    plt.axis("off")
    plt.show()
    



