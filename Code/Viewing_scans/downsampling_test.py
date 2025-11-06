import SimpleITK as sitk
from totalsegmentator import TotalSegmentator

# Paths
input_file = "Mandible_L.nii"
downsampled_file = "Mandible_L_small.nii"
output_dir = "segmentation_output"

# Load image
img = sitk.ReadImage(input_file)

# Get original spacing
orig_spacing = img.GetSpacing()  # (x, y, z)
print("Original spacing:", orig_spacing)

# Define downsampling factor (e.g., 2x in x and y, keep z)
downsample_factors = [2.0, 2.0, 1.0]  
new_spacing = [orig_spacing[i] * downsample_factors[i] for i in range(3)]
print("New spacing:", new_spacing)

# Resample image
resample = sitk.ResampleImageFilter()
resample.SetOutputSpacing(new_spacing)
resample.SetSize([
    int(img.GetSize()[i] / downsample_factors[i]) for i in range(3)
])
resample.SetInterpolator(sitk.sitkLinear)  # linear for intensity images
resample.SetOutputDirection(img.GetDirection())
resample.SetOutputOrigin(img.GetOrigin())
resample.SetDefaultPixelValue(img.GetPixelIDValue())

img_small = resample.Execute(img)

# Save downsampled image
sitk.WriteImage(img_small, downsampled_file)
print("Downsampled image saved to:", downsampled_file)
