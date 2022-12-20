
def decode(huffman_codes,Encode_filename,Decode_filename):
    huffman_codes = {v: k for k, v in huffman_codes.items()}
    encode_file = open(Encode_filename,"rb")
    decode_file = open(Decode_filename, "w")
    binary_read = str(encode_file.read())
    match_code = ''
    for bit in binary_read[2:]:
        match_code+=bit
        if match_code in huffman_codes:
            decode_file.write(huffman_codes[match_code])
            match_code = ''
    decode_file.close()
    encode_file.close()