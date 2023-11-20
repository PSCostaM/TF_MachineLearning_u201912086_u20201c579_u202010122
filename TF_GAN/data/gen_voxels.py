from zipfile import ZipFile
import os
import sys
import urllib.request
import shutil

# check for and download files

# Download binvox executable for Linux
binvox_url = "https://example.com/binvox-linux"  # Replace with the actual download link
binvox_path = "../../binvox"  # Change this to the desired executable name

# Uncomment the following lines once you have the correct binvox URL
# if not os.path.exists(binvox_path):
#     print("Downloading binvox for Linux...")
#     urllib.request.urlretrieve(binvox_url, binvox_path)
#     os.chmod(binvox_path, 0o775)  # Make the binvox executable

# Download the chairs dataset if not present
if not os.path.exists("03001627.zip"):
    chairs = "http://shapenet.cs.stanford.edu/shapenet/obj-zip/03001627.zip"
    answer = input("Chairs dataset (03001627.zip) is missing! Large download (1.4G): Continue? (Y/N)")
    if answer.strip()[0].lower() == 'y':
        print("Downloading... this might take a while.")
        urllib.request.urlretrieve(chairs, "03001627.zip")
        print("Finished downloading.")
    else:
        print(f"Please download the ShapeNet chairs dataset at {chairs}.")
        quit()

# make chair model directory
if not os.path.isdir('chair_models/'):
    os.mkdir('chair_models/')

n_models = 500  # number of models to extract

chairs = "03001627.zip"
with ZipFile(chairs, 'r') as zf:
    files = zf.namelist()
    objs = [file for file in files if ".obj" in file]
    for i in range(min(n_models, len(objs))):
        model_name = objs[i][9:-10]
        zf.extract(objs[i])
        os.system(f"{binvox_path} -d 64 -cb {objs[i]}")  # Use the correct binvox executable
        shutil.copyfile(f"{objs[i][:-4]}.binvox", f"chair_models/{model_name}.binvox")
        shutil.rmtree(objs[i][:-9])
