# BitFontMaker
Little python script that converts images to a source file with an array of the font's bytes.
Makes the process of creating monospace bit fonts a *bit* easier when working with images. There is an example font included in the `example8x5` directory.

# Supported conversions
The script supports:
- C++
- C
- Rust
- You can easily add your own conversions...

# Usage
- Make a directory and put your letter image files in it.
- The letter images must follow the naming convention: `{ascii_code}.{extension}`, e.g.: `65.png` for the image of letter A.
- All the images must have identical sizes.
- Run the script: `bitfontmaker.py` (You might need to do `pip install Pillow` first)
- Specify the source directory containing your letter image files, e.g.: `./example8x5` or an absolute path.
- Specify the conversion target, e.g.: `c` for a C array. 
