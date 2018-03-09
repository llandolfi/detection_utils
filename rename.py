import os
import argparse



parser = argparse.ArgumentParser(description='Merge several folders into one')
parser.add_argument('name', metavar='N', help='common name part')

args = parser.parse_args()

search_name = args.name

imdir = 'images'
if not os.path.isdir(imdir):
    os.mkdir(imdir)

fidget_folders = [folder for folder in os.listdir('.') if search_name in folder]

n = 0
for folder in fidget_folders:
    for imfile in os.scandir(folder):
        os.rename(imfile.path, os.path.join(imdir, '{:06}.jpg'.format(n)))
        n = n + 1