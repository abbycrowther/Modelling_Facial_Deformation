import SimpleITK as sitk
import os

def mha_to_nii(input_path, output_path):
   
    image = sitk.ReadImage(input_path)
    sitk.WriteImage(image, output_path)
    print(f"Converted {input_path} → {output_path}")

if __name__ == "__main__":
    
    input_file = r"D:\Users\Abigail Crowther\Desktop\Uni\Year 4\MPhys Projects\Semester 1 - Modelling Facial Deformation\Data\SegRap2023_Validation_Set_20cases\head-neck-ct\segrap_0120.mha"
    output_file = r"D:\Users\Abigail Crowther\Desktop\Uni\Year 4\MPhys Projects\Semester 1 - Modelling Facial Deformation\Data\SegRap2023_Validation_Set_20cases\head-neck-ct\segrap_0120.nii"
    mha_to_nii(input_file, output_file)
