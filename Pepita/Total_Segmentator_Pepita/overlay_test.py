import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

# Load the CT scan
ct_img = nib.load("CT_WHOLE_CNS.nii")
ct_data = ct_img.get_fdata()

# Load the segmentation
seg_img = nib.load("teeth_lower.nii.gz")
seg_data = seg_img.get_fdata()

# Choose a slice index to visualize
slice_idx = ct_data.shape[2] // 2  # middle slice

# Display
plt.figure(figsize=(8,8))
plt.imshow(ct_data[:, :, slice_idx], cmap='gray')  # CT in grayscale
plt.imshow(seg_data[:, :, slice_idx], cmap='jet', alpha=0.3)  # Segmentation overlay
plt.axis('off')
plt.show()
