# Import dependencies
import os
import time
from colorthief import ColorThief
from PIL import Image
from itertools import product

# Resize image to 500x500 px
def resize():
    name = input("Name of original image(no need to put extension): ")

    #Create an Image Object from an Image
    im = Image.open(f"input/{name}.jpg")

    #Make the new image half the width and half the height of the original image
    resized_im = im.resize((500, 500))

    #Save the cropped image
    resized_im.save('input/img.jpg')

# Divide the image into 10000 images
def divide(filename, dir_in, dir_out, d):
    '''
    Taken from:
    https://stackoverflow.com/a/65698752/14460555
    '''
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size

    grid = product(range(0, h-h % d, d), range(0, w-w % d, d))
    for i, j in grid:
        box = (j, i, j+d, i+d)
        out = os.path.join(dir_out, f'{name}_{i}_{j}{ext}')
        img.crop(box).save(out)

# Put the image in text file
def create(dir):
    # Take the image as img_j_i
    for i in range(0, 100):
        i = i*5
        for j in range(0, 100):
            j = j*5
            # print("J",j)
            out = os.path.join(dir, f'img_{j}_{i}.jpg')

            img = Image.open(out)
            img = img.convert('RGB')
            width, height = img.size
            r_total = 0
            g_total = 0
            b_total = 0
            count = 0
            for x in range(0, width):
                for y in range(0, height):
                    r, g, b = img.getpixel((x, y))
                    r_total += r
                    g_total += g
                    b_total += b
                    count += 1
            most_present = (r_total/count, g_total/count, b_total/count)
            # print(most_present)
            f = open("how_to_do.txt", "a+")
            if most_present < (150, 150, 150):
                if i < 1:
                    f.write("$\n")
                #print("Black:", out)
                if i > 1:
                    j = int(j/5)
                    f.seek(0)
                    get_all = f.readlines()
                    # print(j)
                    # print(get_all)
                    # print(get_all[j])
                    str1 = get_all[j]
                    newstr = str1.strip()
                    get_all[j] = f'{newstr}$\n'
                    # print(get_all)
                    # time.sleep(2)
                    with open('how_to_do.txt', 'w') as file:
                        file.writelines(get_all)
                        file.close()

            if most_present > (150, 150, 150):
                if i < 1:
                    f.write(".\n")
                #print("White:", out)
                if i > 1:
                    f.seek(0)
                    #file = open("how_to_do.txt", "r")
                    get_all = f.readlines()
                    # file.close()
                    # print(j)
                    j = int(j/5)
                    # print(j)
                    # print(get_all)
                    # print(get_all[j])
                    str1 = get_all[j]
                    newstr = str1.strip()
                    get_all[j] = f'{newstr}.\n'
                    # print(get_all)
                    # time.sleep(2)
                    with open('how_to_do.txt', 'w') as file:
                        file.writelines(get_all)
                        file.close()
            f.close()

        # print("I",i)


def fix():
    f = open("how_to_do.txt", "r")
    f.seek(0)
    get_all = f.readlines()
    # print(get_all)
    f.close()
    new_strings = []
    for string in get_all:
        new_string = string.replace(".", " ")
        new_strings.append(new_string)
        # print(new_string)

    with open('how_to_do.txt', 'w') as file:
        file.writelines(new_strings)
        file.close()
