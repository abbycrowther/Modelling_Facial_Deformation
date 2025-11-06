import SimpleITK as sitk

dicom_folder = r"Z:\FacialDeformation_MPhys\rhabdo_data_proton\DICOMS\abby\UIDQQ0x1x1Hx7\full_CT"

reader = sitk.ImageSeriesReader()
dicom_names = reader.GetGDCMSeriesFileNames(dicom_folder)
reader.SetFileNames(dicom_names)
image = reader.Execute()

sitk.WriteImage(image, r"Z:\FacialDeformation_MPhys\rhabdo_data_proton\DICOMS\abby\UIDQQ0x1x1Hx7\CT.nii.gz")

print("Done!")



