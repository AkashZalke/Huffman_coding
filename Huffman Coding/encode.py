def encode(huffman_codes,temp,encode_file_name):
    # we will write our encoded code in another file

    #Open as binary file as we are writing in binary 
    
    encode_file = open(encode_file_name, "wb")
    for x in temp:    
        binary_str = bytes(huffman_codes[x], 'utf-8')
        encode_file.write(binary_str)
    encode_file.close()