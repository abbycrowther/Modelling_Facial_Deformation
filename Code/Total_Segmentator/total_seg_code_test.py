import nibabel as nib
from totalsegmentator.python_api import totalsegmentator

if __name__ == "__main__":
    # option 1: provide input and output as file paths
    totalsegmentator(D:\Users\Abigail Crowther\Desktop\Uni\Year 4\MPhys Projects\Semester 1 - Modelling Facial Deformation\segrap_0120.nii, D:\Users\Abigail Crowther\Desktop\Uni\Year 4\MPhys Projects\Semester 1 - Modelling Facial Deformation\total_seg_test)
    
    # option 2: provide input and output as nifti image objects
    input_img = nib.load(D:\Users\Abigail Crowther\Desktop\Uni\Year 4\MPhys Projects\Semester 1 - Modelling Facial Deformation\segrap_0120.nii)
    output_img = totalsegmentator(segrap_0120.nii)
    nib.save(segrap_0120_test, D:\Users\Abigail Crowther\Desktop\Uni\Year 4\MPhys Projects\Semester 1 - Modelling Facial Deformation\total_seg_test)