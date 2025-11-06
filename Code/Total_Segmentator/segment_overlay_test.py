import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

# Load the CT scan
ct_img = nib.load('D:\Users\Abigail Crowther\Desktop\Uni\Year 4\MPhys Projects\Semester 1 - Modelling Facial Deformation\Data\segrap_0120.nii')
ct_data = ct_img.get_fdata()

# Load the segmentation
seg_img = nib.load('D:\Users\Abigail Crowther\Desktop\Uni\Year 4\MPhys Projects\Semester 1 - Modelling Facial Deformation\Data\skull.nii')
seg_data = seg_img.get_fdata()

# Choose a slice index to visualize
slice_idx = ct_data.shape[2] // 2  # middle slice

# Display
plt.figure(figsize=(8,8))
plt.imshow(ct_data[:, :, slice_idx], cmap='gray')  # CT in grayscale
plt.imshow(seg_data[:, :, slice_idx], cmap='jet', alpha=0.3)  # Segmentation overlay
plt.axis('off')
plt.show()
