import random
import glob
import os
import shutil


save_root_path =  "../dataset/curated_dataset/" 
image_dir = "../dataset/curated_dataset/yolo/images/"
label_dir = "../dataset/curated_dataset/yolo/labels/"
folders = {"train": 0.85, "val": 0.1, "test": 0.05}


def copyfiles(fil, folder):
    basename = os.path.basename(fil)
    filename = os.path.splitext(basename)[0]

    # copy image
    src = fil
    dest = os.path.join(save_root_path, folder,"images", f"{filename}.jpg")
    shutil.copyfile(src, dest)

    # copy annotations
    src = os.path.join(label_dir, f"{filename}.txt")
    dest = os.path.join(save_root_path, folder, "labels", f"{filename}.txt")
    if os.path.exists(src):
        shutil.copyfile(src, dest)


lower_limit = 0
files = glob.glob(os.path.join(image_dir, '*.jpg'))
random.shuffle(files)
check_sum = sum([folders[x] for x in folders])
assert check_sum == 1.0, "Split proportion is not equal to 1.0"


for folder in folders:
    if not os.path.exists(save_root_path + folder):
        os.mkdir(save_root_path + folder)
    save_label_dir = os.path.join(save_root_path, folder, "labels")
    if not os.path.exists(save_label_dir):
        os.mkdir(save_label_dir)
    save_image_dir = os.path.join(save_root_path, folder, "images")
    if not os.path.exists(save_image_dir):
        os.mkdir(save_image_dir)

    limit = round(len(files) * folders[folder])
    for fil in files[lower_limit:lower_limit + limit]:
        copyfiles(fil, folder)
    lower_limit = lower_limit + limit
