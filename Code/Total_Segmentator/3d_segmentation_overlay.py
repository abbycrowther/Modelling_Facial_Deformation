import nibabel as nib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Load CT and segmentation
ct_img = nib.load("segrap_0120.nii")
ct_data = ct_img.get_fdata()

seg_img = nib.load("teeth_upper.nii")
seg_data = seg_img.get_fdata()

# Initial slice index
slice_idx = ct_data.shape[2] // 2  # start at middle slice

# Plot
fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.25)
l = ax.imshow(ct_data[:, :, slice_idx], cmap='gray')
l_seg = ax.imshow(seg_data[:, :, slice_idx], cmap='jet', alpha=0.3)

ax_slice = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax_slice, 'Slice', 0, ct_data.shape[2]-1, valinit=slice_idx, valfmt='%0.0f')

def update(val):
    idx = int(slider.val)
    l.set_data(ct_data[:, :, idx])
    l_seg.set_data(seg_data[:, :, idx])
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()
