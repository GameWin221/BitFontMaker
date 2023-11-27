class ImagesInfo:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.begin_letter = ' '
        self.end_letter = '~'
        self.letter_count = ord(self.end_letter) - ord(self.begin_letter) + 1 
        self.bytes_per_row = (self.width + 7) // 8
        self.bytes_per_letter = self.bytes_per_row * self.height
        self.bytes_count = self.letter_count * self.bytes_per_letter

def to_c_array(images_data: dict, info: ImagesInfo):    
    data = "// Font info:\n"
    data += f"//\tWidth: {info.width}, Height: {info.height}\n"
    data += f"//\tLetter count: {info.letter_count}, Starts from letter \"{info.begin_letter}\" (index 0), Ends at letter \"{info.end_letter}\" (index {info.letter_count-1})\n"
    data += f"//\tBytes per letter: {info.bytes_per_letter}, Bytes per letter row: {info.bytes_per_row}, Bytes in array: {info.bytes_count}\n\n"
    data += "const static unsigned char FONT_TABLE[" + str(info.bytes_count) + "] = {\n"
    
    for letter in range(ord(info.begin_letter), ord(info.end_letter)+1):
        data += f"/* {chr(letter)} */ "
    
        if letter in images_data:
            for byte in images_data[letter]:      
                data += f"0x{byte:02x},"
        else:
            for i in range(0, info.bytes_per_letter):
                data += "0x00,"
    
        data += "\n"
    
    data += "};\n\n"
    
    return data

def to_cpp_array(images_data: dict, info: ImagesInfo):    
    data = "// Font info:\n"
    data += f"//\tWidth: {info.width}, Height: {info.height}\n"
    data += f"//\tLetter count: {info.letter_count}, Starts from letter \"{info.begin_letter}\" (index 0), Ends at letter \"{info.end_letter}\" (index {info.letter_count-1})\n"
    data += f"//\tBytes per letter: {info.bytes_per_letter}, Bytes per letter row: {info.bytes_per_row}, Bytes in array: {info.bytes_count}\n\n"
    data += "constexpr static unsigned char FONT_TABLE[" + str(info.bytes_count) + "] = {\n"
    
    for letter in range(ord(info.begin_letter), ord(info.end_letter)+1):
        data += f"/* {chr(letter)} */ "
    
        if letter in images_data:
            for byte in images_data[letter]:      
                data += f"0x{byte:02x},"
        else:
            for i in range(0, info.bytes_per_letter):
                data += "0x00,"
    
        data += "\n"
    
    data += "};\n\n"
    
    return data

def to_rs_array(images_data: dict, info: ImagesInfo):    
    data = "// Font info:\n"
    data += f"//\tWidth: {info.width}, Height: {info.height}\n"
    data += f"//\tLetter count: {info.letter_count}, Starts from letter \"{info.begin_letter}\" (index 0), Ends at letter \"{info.end_letter}\" (index {info.letter_count-1})\n"
    data += f"//\tBytes per letter: {info.bytes_per_letter}, Bytes per letter row: {info.bytes_per_row}, Bytes in array: {info.bytes_count}\n\n"
    data += "const FONT_TABLE: [u8; " + str(info.bytes_count) + "] = [\n"
    
    for letter in range(ord(info.begin_letter), ord(info.end_letter)+1):
        data += f"/* {chr(letter)} */ "
    
        if letter in images_data:
            for byte in images_data[letter]:      
                data += f"0x{byte:02x},"
        else:
            for i in range(0, info.bytes_per_letter):
                data += "0x00,"
    
        data += "\n"
    
    data += "];\n\n"
    
    return data