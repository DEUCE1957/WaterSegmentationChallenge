import cv2, copy, math, time, random, numpy as np 
import matplotlib.cm as cm, matplotlib as mlt, matplotlib.pyplot as plt
from pathlib import Path as p
from PIL import Image

base_path = p(__file__).parent
now = time.strftime("%Y-%m-%d_%Hh-%Mm-%Ss")
score_path = base_path / "scores"
score_path.mkdir(exist_ok=True)
with open(score_path / f"{now}.csv", "w") as f:
    f.write(f"ImageID,TimeToGenerate (s),Similarity Score (-1 to 1)") ## Header
data_dir = base_path / "data"
ims = [im_path for im_path in data_dir.glob("*.jpg")]
save_dir = data_dir / "segmented" / f"{now}"
save_dir.mkdir(exist_ok=True)

lut = np.array([[  1,  1,  1], # Used to visualise, correct, false positive and false negative masks values
                [  1,  0,  0],
                [  0,  1,  0],
                [0.5,0.5,0.5]]) 

for im_path in ims:
    im = cv2.imread(str(im_path))
    print(f"'{im_path.stem}' Image Shape: {im.shape}")
    start = time.time()
    # >> INSERT ANALYTICAL WATER SEGMENTATION CODE HERE <<
    """Note: If you want to use a non-standard python library (e.g. Skimage), please FREEZE your python environment using
                pip freeze > requirements.txt
        Then add the import statement HERE (not at the top of the file), since you will only hand in the code block you added (not the whole script)
    """
    binary_mask = np.ones((im.shape[0], im.shape[1])).astype(np.uint8) ## Replace this with your finale binary mask (255 = water, 0 = not water). 
                                            ## Make sure this is a 2D array (i.e. no colour channels)
    # >> END ANALYTICAL WATER SEGMENTATION CODE <<
    duration = time.time() - start

    reference_mask = cv2.imread(str(data_dir / "Ground Truths" / im_path.name), 0)
    _, thresh_ref = cv2.threshold(reference_mask, 75, 2, 0) # Set any values over 75 to 2, 0 otherwise
    _, thresh_extract = cv2.threshold(binary_mask, 75, 1, 0) # Set any values over 75 to 1, 0 otherwise
    C = lut[thresh_ref + thresh_extract] # Lookup RGB colour corresponding to whether masks match
    print(f"Generated mask for {im_path.stem} in {duration:.5f}s")
    comparison = np.sum(np.where(binary_mask == reference_mask, 1, -1))/float(np.sum(np.ones(reference_mask.shape)))
    print(f"Pixel-wise similarity: {comparison:.4f} (from -1 [complete mismatch] to 1 [perfect match])")
    with open(score_path / f"{now}.csv", "a") as f:
        f.write(f"{im_path.stem},{duration},{comparison}\n")

    # >> Add transluscent red mask preview over RGB Image <<
    RED = np.tile([0, 0, 255], reps=(im.shape[0], im.shape[1])).reshape(im.shape) # Pure red image
    im = np.where(np.stack([binary_mask for i in range(3)], axis=2), 0.5 * im + 0.5 * RED, im)
    im = im.astype(np.uint8)

    fig, axes = plt.subplots(figsize=(im.shape[1]/250,im.shape[0]/500), nrows=1, ncols=3)
    axes[0].imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB)) # Raw image with Red Mask overlay
    axes[1].imshow(binary_mask, cmap=cm.gray) # Binary Mask
    axes[2].imshow(C) # Binary Mask comparison to ground truth
    plt.savefig(save_dir / f"{im_path.name}".replace(".", "_WATER."), dpi=100)