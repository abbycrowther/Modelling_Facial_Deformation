import SimpleITK as sitk

# Load the .mha file
image = sitk.ReadImage("segrap_0120.mha")

sitk.WriteImage(image, "segrap_0120.nii.gz")
