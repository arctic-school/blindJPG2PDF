from PIL import Image
import os
import sys

ROOT = os.getcwd()
folders = [ i for i in os.listdir() if os.path.isdir(i) ]

for folder in folders:
    print(folder)
    os.chdir(ROOT + '\\' + folder)

    images = list()
    pdf_name = ROOT + '\\' + folder + '.pdf'

    for file_name in os.listdir():
        if file_name.split('.')[1] != 'jpg':
            continue

        images.append(
            Image.open(file_name)
                .convert('RGB')
        )
        print('  ' + file_name)

    try:
        pdf = images[0]
    except IndexError:
        print('\x1b[31m  NO FILES\x1b[0m')
        continue

    pdf.save(pdf_name, save_all=True, append_images=images[1:])