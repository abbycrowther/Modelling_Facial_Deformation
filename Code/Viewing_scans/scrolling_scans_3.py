'''
IMPORTANT: if code appears to not be working on laptop/macbook
enter "%matplotlib qt" into IPython Console before running the code again.

https://matplotlib.org/3.6.1/gallery/event_handling/image_slices_viewer.html
code from this link was edited to include data from an MRI image.
'''
import matplotlib.pyplot as plt
import nibabel as nib

class IndexTracker:
   
    def __init__(self, ax, X):
        self.ax = ax #defines plotting axis
        ax.set_title('use scroll wheel to navigate images', size=15)

        self.X = X
        rows, cols, self.slices = X.shape
        self.ind = self.slices//2

        self.im = ax.imshow(self.X[:, :, self.ind]) #displays image
        self.update()
       
    def on_scroll(self, event):
        print("%s %s" % (event.button, event.step))
        if event.button == 'up':
            self.ind = (self.ind + 1) % self.slices
        else:
            self.ind = (self.ind - 1) % self.slices
        self.update()
   
    def update(self):
        self.im.set_data(self.X[:, :, self.ind])
        self.ax.set_ylabel('slice %s' % self.ind, size = 15)
        self.im.axes.figure.canvas.draw()

img = nib.load("image3.nii")

fig, ax = plt.subplots(1, 1)

X = img.get_fdata()


tracker = IndexTracker(ax, X)


fig.canvas.mpl_connect('scroll_event', tracker.on_scroll)
plt.show()