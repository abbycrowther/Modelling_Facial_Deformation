import SimpleITK as sitk
import os

def nii_to_mha(input_path, output_path):
   
    image = sitk.ReadImage(input_path)
    sitk.WriteImage(image, output_path)
    print(f"Converted {input_path} → {output_path}")

if __name__ == "__main__":
    
    input_file = "/home/abigail/synthetic_CT/910/MR_T1_TFE_1.5mm.nii"
    output_file ="/home/abigail/Synthrad2025_Task_1/Dataset/HN/910/MR.mha"
    nii_to_mha(input_file, output_file)
