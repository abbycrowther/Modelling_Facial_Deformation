import SimpleITK as sitk

# Load the .mha file
image = sitk.ReadImage("segrap_0120.mha")

# Save as .nii (or .nii.gz for compressed)
sitk.WriteImage(image, "segrap_0120.nii")
t