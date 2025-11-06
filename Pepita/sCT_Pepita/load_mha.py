import SimpleITK as sitk
import matplotlib.pyplot as plt
import numpy as np

# Load the MHA
img = sitk.ReadImage("/home/abigail/Synthrad2025_Task_1/Predictions/Out/Dataset/910/sCT.mha")
arr = sitk.GetArrayFromImage(img)  # shape: [slices, height, width]

# Inspect shape
print("Image shape (slices, height, width):", arr.shape)

# Get middle slice
mid_slice = arr[arr.shape[0] // 2]

# Optional: normalize for better display
mid_slice_norm = (mid_slice - np.min(mid_slice)) / (np.max(mid_slice) - np.min(mid_slice))

# Display
plt.imshow(mid_slice_norm, cmap='gray')
plt.title("Middle Slice")
plt.axis('off')
plt.show()
