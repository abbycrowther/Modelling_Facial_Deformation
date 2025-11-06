from totalsegmentator.python_api import totalsegmentator

# Replace with your actual file paths
input_file = r"D:\Users\Abigail Crowther\Desktop\SegRap2023_Training_Set_120cases_Update_Labels\segrap_0000\Brain.nii.gz"
output_dir = r"D:\Users\Abigail Crowther\Desktop\Uni\Year 4\MPhys Projects\Semester 1 - Modelling Facial Deformation"

# Run segmentation
totalsegmentator(
    input_file,     # positional argument
    output_dir,     # positional argument
    device="cpu"    # optional keyword argument; use "cuda" if you have a GPU
)
