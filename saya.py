import itertools
import re

# Membuka file dan membaca semua baris
with open('Matrix.txt', 'r') as file:
    # Membaca dua baris pertama dan membaginya menjadi dua angka terpisah
    dimensions = file.readline().strip().split()
    n = int(dimensions[0])
    m = int(dimensions[1])
    
    matrix = []
    
    # Membaca elemen-elemen matriks
    for _ in range(n):
        matrix_item = file.readline().strip()
        matrix.append(matrix_item)
    
    # Menggabungkan elemen matriks menjadi satu string
    # Menggunakan zip_longest untuk menggabungkan elemen dengan aman
    encoded_string = "".join(char for group in itertools.zip_longest(*matrix, fillvalue='') for char in group)
    
    # Menggunakan regex untuk mengganti pattern tertentu dengan spasi
    pat = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
    decoded_string = re.sub(pat, ' ', encoded_string)
    
    print(decoded_string)
