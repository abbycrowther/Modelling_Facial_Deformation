import SimpleITK as sitk
import os

def nii_to_mha(input_path, output_path):
    # Read the NIfTI image
    image = sitk.ReadImage(input_path)
    
    # Rescale intensity to 0–255 to safely convert to UInt8
    image_rescaled = sitk.RescaleIntensity(image, outputMinimum=0, outputMaximum=255)
    
    # Cast to UInt8
    image_uint8 = sitk.Cast(image_rescaled, sitk.sitkUInt8)
    
    # Write as MHA
    sitk.WriteImage(image_uint8, output_path)
    print(f"Converted {input_path} → {output_path} (UInt8)")

if __name__ == "__main__":
    input_file = "/home/abigail/synthetic_CT/910/MR_Mask.nii"
    output_file = "/home/abigail/Synthrad2025_Task_1/Dataset/HN/910/MASK.mha"
    nii_to_mha(input_file, output_file)
