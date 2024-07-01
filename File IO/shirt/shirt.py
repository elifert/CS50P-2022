import sys
import os
from PIL import Image, ImageOps

def main():
    control_arguments()
    put_shirt_to(sys.argv[1])

def put_shirt_to(photo):
    shirt = Image.open("shirt.png")
    with Image.open(photo) as opened_photo:
         photo_resized = ImageOps.fit(opened_photo, shirt.size)
         photo_resized.paste(shirt, mask=shirt)
         photo_resized.save(sys.argv[2])

def control_arguments():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        extensions = [".jpg", ".jpeg", ".png"]
        file_name1, file_extension1 = os.path.splitext(sys.argv[1])
        file_name2, file_extension2 = os.path.splitext(sys.argv[2])
        if file_extension2.lower() not in extensions:
            sys.exit("Invalid output")
        elif file_extension1 != file_extension2:
            sys.exit("Input and output have different extensions")
        else:
            try:
                file1 = open(sys.argv[1])
            except FileNotFoundError:
                sys.exit("Invalid input")


if __name__ == "__main__":
    main()