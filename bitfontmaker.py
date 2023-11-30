from PIL import Image # pip install Pillow

import os
import convert

image_dir_path = input("Enter image files directory: ")

if not os.path.exists(image_dir_path):
    print(f"\"{image_dir_path}\" is not a valid directory!")
    exit(1)

image_file_paths = filter(lambda path: os.path.isfile(path), list(map(lambda file_path: os.path.join(image_dir_path, file_path), os.listdir(image_dir_path))))

images_reversed = False

images_data = {}
images_width = -1
images_height = -1

for image_path in image_file_paths:
    with Image.open(image_path) as img:
        image_name = image_path.split('/')[-1].split('\\')[-1].split('.')[0]
    
        if not image_name.isdigit():
            print(f"Skipping \"{image_path}\" because it has an invalid name (it has to be the ascii index of a character)!")
            continue
        
        if images_width == -1 and images_height == -1:
            print(f"Set {img.width}x{img.height} as the base size.")
            images_width = img.width
            images_height = img.height

        if img.height != images_height or img.width != images_width:
            print(f"Skipping \"{image_path}\" because its size doesn't match the base size!")
            continue

        bytes_per_row = (images_width + 7) // 8

        pixels = list(img.getdata(0))
        
        if images_reversed:
            pixels.reverse()
        
        final_bytes = [0] * images_height * bytes_per_row

        for row in range(0, images_height):
            for byte in range(0, bytes_per_row):
                for bit in range(0, 8):
                    row_byte = byte * 8 + bit
                
                    if row_byte >= images_width:
                        break
                
                    if pixels[row * images_width + byte * 8 + bit] > 0:
                        final_bytes[row*bytes_per_row+byte] |= (1 << 7) >> bit
                                               
        images_data[int(image_name)] = final_bytes

        print(f"Processed {image_path}.")
    
images_info = convert.ImagesInfo(images_width, images_height)
    
print(f"Processed {len(images_data)} files.")
    
conversion_target = input("Specify the conversion target:\nc - Convert to a C source file.\ncpp - Convert to a c++ source file.\nrs - Convert to a Rust source file.\n")

match conversion_target:
    case "c":
        with open("out.c", "w") as file:
            file.write(convert.to_c_array(images_data, images_info))
    case "cpp":
        with open("out.cpp", "w") as file:
            file.write(convert.to_cpp_array(images_data, images_info))
    case "rs":
        with open("out.rs", "w") as file:
            file.write(convert.to_rs_array(images_data, images_info))
    case other:
        print("Invalid conversion target!")
        exit(1)
    
print(f"Finished the conversion.")