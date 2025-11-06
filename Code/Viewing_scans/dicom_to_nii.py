import SimpleITK as sitk

# Path to folder containing DICOM files
dicom_folder = r"Z:\FacialDeformation_MPhys\rhabdo_data_proton\DICOMS\UIDQQ0x1x1Hx7\"

reader = sitk.ImageSeriesReader()
dicom_names = reader.GetGDCMSeriesFileNames(dicom_folder)
reader.SetFileNames(dicom_names)
image = reader.Execute()

sitk.WriteImage(image, r"Z:\FacialDeformation_MPhys\rhabdo_data_proton\DICOMS\abby\UIDQQ0x1x1Hx7\CT.nii.gz")
