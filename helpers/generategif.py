import glob
from PIL import Image
from random import sample

# filepaths
fp_in = "N:\\minecraft-ml\\selfjumping\\training\\space\\*.png"
fp_out = "N:\\minecraft-ml\\selfjumping\\training\\Jump.gif"

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=sample(imgs,100),
         save_all=True, duration=0, loop=0)
