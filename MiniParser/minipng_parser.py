import struct
import sys


''' *******************************Question 1 à 3*********************************************
def read_minipng_with_comments(file_path):
    comments = []
    width = height = pixel_type = None
    
    with open(file_path, 'rb') as file:
        magic_number = file.read(8)
        if magic_number != b'Mini-PNG':
            raise ValueError("fichier MiniPNG invalide")
        while True:
            block_type = file.read(1)
            if not block_type:
                break
            block_length = int.from_bytes(file.read(4), byteorder='big')           
            if block_type == b'H':
                width = int.from_bytes(file.read(4), byteorder='big')
                height = int.from_bytes(file.read(4), byteorder='big')
                pixel_type = 'black-and-white' if file.read(1) == b'\x00' else 'autre nuance de couleur'
            elif block_type == b'C':
                comment = file.read(block_length).decode('ascii')
                comments.append(comment)
            else:
                file.seek(block_length, 1)   
    return width, height, pixel_type, comments

 
def read_minipng_with_comments(file_path):
    comments = []
    width = height = 0
    pixel_type = None
    data_size = 0  # Ajout pour suivre la taille totale des données des blocs D
    with open(file_path, 'rb') as file:
        magic_number = file.read(8)
        if magic_number != b'Mini-PNG':
            raise ValueError("fichier MiniPNG invalide")
        while True:
            block_type = file.read(1)
            if not block_type:
                break
            block_length = int.from_bytes(file.read(4), byteorder='big')
            if block_type == b'H':
                width = int.from_bytes(file.read(4), byteorder='big')
                height = int.from_bytes(file.read(4), byteorder='big')
                pixel_type_byte = file.read(1)
                pixel_type = 'black-and-white' if pixel_type_byte == b'\x00' else 'autre nuance de couleur'
            elif block_type == b'C':
                comment = file.read(block_length).decode('ascii')
                comments.append(comment)
            elif block_type == b'D':
                data_size += block_length  
                file.seek(block_length, 1)  
            else:
                file.seek(block_length, 1)
    if pixel_type == 'black-and-white':
        expected_size = (width * height + 7) // 8 
    else:
        raise NotImplementedError("la vérification pour les types de pixels autres que noir et blanc n'est pas implémentée.")
    # ici on verifie la cohérence des données
    if data_size != expected_size:
        raise ValueError(f"incohérence des données: la taille attendue est {expected_size}, celle obtenue est {data_size}")
    return width, height, pixel_type, comments
'''
  
'''*******************************Question 4**********************************************

#fonction pour afficher les images en noir et blanc
def display_bw_image(width, height, image_data):
    for row in range(height):
        for col in range(width):
            byte_index = (row * width + col) // 8
            bit_index = 7 - (col % 8)
            pixel = (image_data[byte_index] >> bit_index) & 1
            print('X' if pixel == 0 else ' ', end='')
        print()  

def read_minipng_with_comments_and_display(file_path):
    comments = []
    width = height = pixel_type = None
    image_data = bytearray()
    data_size = 0
    with open(file_path, 'rb') as file:
        magic_number = file.read(8)
        if magic_number != b'Mini-PNG':
            raise ValueError("fichier MiniPNG invalide")     
        while True:
            block_type = file.read(1)
            if not block_type:
                break
            block_length = int.from_bytes(file.read(4), byteorder='big')
            if block_type == b'H':
                width = int.from_bytes(file.read(4), byteorder='big')
                height = int.from_bytes(file.read(4), byteorder='big')
                pixel_type_byte = file.read(1)
                pixel_type = 'black-and-white' if pixel_type_byte == b'\x00' else 'autre nuance de couleur'
            elif block_type == b'C':
                comment = file.read(block_length).decode('ascii')
                comments.append(comment)
            elif block_type == b'D':
                data_size += block_length  
                image_data += file.read(block_length)
            else:
                file.seek(block_length, 1)
    if pixel_type == 'black-and-white':
        expected_size = (width * height + 7) // 8
    if data_size != expected_size:
        raise ValueError(f"incohérence des données: la taille attendue est {expected_size}, celle obtenue est {data_size}")
    print("Width : "+str(width))
    print("Height : "+str(height))
    print("Pixel Type : "+str(pixel_type))
    print("Comments : "+str(comments))
    if pixel_type == 'black-and-white':
        display_bw_image(width, height, image_data)
    else:
        print("Ce type de pixel n'est pas encore supporté !")
    return width, height, pixel_type, comments

'''

'''*******************************Question 6 et 7*********************************************

import sys

#permet d'afficher les images qui sont en noir et blanc
def display_bw_image(width, height, image_data):
    for row in range(height):
        for col in range(width):
            byte_index = (row * width + col) // 8
            bit_index = 7 - (col % 8)
            pixel = (image_data[byte_index] >> bit_index) & 1
            print('X' if pixel == 0 else ' ', end='')
        print()  

#permet de convertir au format ppm
def convert_to_ppm(width, height, pixel_type, image_data, output_file):
    if pixel_type == 'color' or pixel_type == 'gray-level' or pixel_type == 'palette':
        header = "P6\n{} {}\n255\n".format(width, height) if pixel_type == 'color' else "P5\n{} {}\n255\n".format(width, height)
    with open(output_file, 'wb') as ppm_file:
        ppm_file.write(header.encode())
        ppm_file.write(image_data)
    print(f"image convertir au format PPM : {output_file}")

def read_minipng_with_comments_and_display(file_path):
    comments = []
    width = height = pixel_type = None
    image_data = bytearray()
    data_size = 0
    with open(file_path, 'rb') as file:
        magic_number = file.read(8)
        if magic_number != b'Mini-PNG':
            raise ValueError("fichier MiniPNG invalide")
        
        while True:
            block_type = file.read(1)
            if not block_type:
                break
            block_length = int.from_bytes(file.read(4), byteorder='big')
            
            if block_type == b'H':
                width = int.from_bytes(file.read(4), byteorder='big')
                height = int.from_bytes(file.read(4), byteorder='big')
                pixel_type_byte = file.read(1)
                if pixel_type_byte == b'\x00':
                    pixel_type = 'black-and-white'
                elif pixel_type_byte == b'\x01':
                    pixel_type = 'gray-level'
                elif pixel_type_byte == b'\x02':
                    pixel_type = 'palette'
                elif pixel_type_byte == b'\x03':
                    pixel_type = 'color'
                else:
                    raise ValueError("type de pixel non supporté")
            elif block_type == b'C':
                comment = file.read(block_length).decode('ascii')
                comments.append(comment)
            elif block_type == b'D':
                data_size += block_length  
                image_data += file.read(block_length)
            else:
                file.seek(block_length, 1)
    
    if pixel_type in ['black-and-white', 'gray-level', 'palette']:
        expected_size = width * height
        if pixel_type == 'black-and-white':
            expected_size = (expected_size + 7) // 8
    elif pixel_type == 'color':
        expected_size = width * height * 3
    else:
        raise ValueError("type de pixel non supporté pour le check de la cohérence des données")
    
    if data_size != expected_size:
        raise ValueError(f"Incohérence des données: la taille attendue est {expected_size}, celle obtenue est {data_size}")
    
    print("Width:", width)
    print("Height:", height)
    print("Pixel Type:", pixel_type)
    print("Comments:", ', '.join(comments))

    if pixel_type == 'black-and-white':
        display_bw_image(width, height, image_data)
    else:  # Pour les niveaux de gris, palette, et couleur on convertit au format ppm
        output_filename = file_path + ".ppm"
        convert_to_ppm(width, height, pixel_type, image_data, output_filename)
        
'''

'''*******************************Question 8 et 9*********************************************'''

import sys

#permet d'afficher les images en noir et blanc
def display_bw_image(width, height, image_data):
    for row in range(height):
        for col in range(width):
            byte_index = (row * width + col) // 8
            bit_index = 7 - (col % 8)
            pixel = (image_data[byte_index] >> bit_index) & 1
            print('X' if pixel == 0 else ' ', end='')
        print()  

def read_palette(file, block_length):
    palette = []
    for _ in range(block_length // 3):
        color = tuple(file.read(3))  # permet de lire 3 octets pour R,G,B
        palette.append(color)
    return palette

def print_palette(palette):
    print("Entrées palette:")
    for index, color in enumerate(palette):
        print(f"{index}: RGB{color}")

def convert_image_data_to_rgb(width, height, pixel_type, image_data, palette):
    if pixel_type == 'palette':
        rgb_data = bytearray()
        for index in image_data:
            rgb_data += bytearray(palette[index])
        return rgb_data
    else:
        return image_data

def convert_to_ppm(width, height, pixel_type, image_data, palette, output_file):
    if pixel_type == 'color':
        header = f"P6\n{width} {height}\n255\n"
        rgb_data = image_data
    elif pixel_type == 'gray-level':
        header = f"P5\n{width} {height}\n255\n"
        rgb_data = image_data
    elif pixel_type == 'palette':
        rgb_data = bytearray()
        for index in image_data:
            rgb_data += bytearray(palette[index])
        header = f"P6\n{width} {height}\n255\n"
    else:
        raise ValueError(f"type de pixel non supporté : {pixel_type}")   
    with open(output_file, 'wb') as ppm_file:
        ppm_file.write(header.encode())
        ppm_file.write(rgb_data)
    
    print(f"image convertie au format PPM : {output_file}")


def read_minipng_with_comments_and_display(file_path):
    comments = []
    palette = []
    width = height = pixel_type = None
    image_data = bytearray()
    data_size = 0
    
    with open(file_path, 'rb') as file:
        magic_number = file.read(8)
        if magic_number != b'Mini-PNG':
            raise ValueError("fichier MiniPNG invalide")
        
        while True:
            block_type = file.read(1)
            if not block_type:
                break
            block_length = int.from_bytes(file.read(4), byteorder='big')
            
            if block_type == b'H':
                width = int.from_bytes(file.read(4), byteorder='big')
                height = int.from_bytes(file.read(4), byteorder='big')
                pixel_type_byte = file.read(1)
                if pixel_type_byte == b'\x00':
                    pixel_type = 'black-and-white'
                elif pixel_type_byte == b'\x01':
                    pixel_type = 'gray-level'
                elif pixel_type_byte == b'\x02':
                    pixel_type = 'palette'
                elif pixel_type_byte == b'\x03':
                    pixel_type = 'color'
                else:
                    raise ValueError("type de pixel non supporté")
            elif block_type == b'C':
                comment = file.read(block_length).decode('ascii')
                comments.append(comment)
            elif block_type == b'D':
                data_size += block_length
                image_data += file.read(block_length)
            elif block_type == b'P':
                palette = read_palette(file, block_length)
                print_palette(palette)
            else:
                file.seek(block_length, 1)
    
    if pixel_type in ['black-and-white', 'gray-level', 'palette']:
        expected_size = width * height
        if pixel_type == 'black-and-white':
            expected_size = (expected_size + 7) // 8
    elif pixel_type == 'color':
        expected_size = width * height * 3
    else:
        raise ValueError("type de pixel non supporté pour le check des données")
    
    if data_size != expected_size:
        raise ValueError(f"incohérence des données: la taille attendue est {expected_size}, celle obtenue est {data_size}")
    
    print("Width:", width)
    print("Height:", height)
    print("Pixel Type:", pixel_type)
    print("Comments:", ', '.join(comments))
#pour afficher si l'image est en noir et blanc
    if pixel_type == 'black-and-white':
        display_bw_image(width, height, image_data)
    else:  #pour convertir l'image pour les niveaux de gris, palette, et couleur vraie
        output_filename = file_path + ".ppm"
        convert_to_ppm(width, height, pixel_type, image_data, palette, output_filename)

#les images qui ne sont pas en noir et blanc et transformer au format PPM j'ai pu les visualiser sur ce site : imagetostl.com/view-ppm-online
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python minipng_parser.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    read_minipng_with_comments_and_display(filename)


