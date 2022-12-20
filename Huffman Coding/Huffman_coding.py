from encode import encode
from decode import decode
class Node:
        # Node of our Huffman Tree 
            #1) Left pointing towards left child
            #2) right pointing toward right child
            #3) val is int value of our Node
            #4) cur_str is current concnated string
    def __init__(self,left=None,right=None,cur_str = '',val=0):
        self.left = left   
        self.right = right
        self.val = val
        self.cur_str = cur_str

def traverse(root,huffman_codes,code):

    # Simple Tree Treaversal algorithm (Post-Order)
    # If root.left exists go to left child append '0' to code 
    # If root.right exists go to right child append '1' to code
    # if both does not exists append code to huffman_codes

    if not root.left and not root.right:
        huffman_codes[root.cur_str] = code
        return 
    if root.left:
        traverse(root.left,huffman_codes,code+'0')
    if root.right:
        traverse(root.right,huffman_codes,code+'1')  

def make_huffman_tree(ele_freq):
    # In this we are goint to make a binary tree also known as Huffman Tree
    
    # 1) we will pop least value elements
    # 2) We will check if the items we have poped is already in a making_node(i.e nodes of them are alreay not created)
    # 3) If not created  We will make two leaf Node object then we will make their parent object which will be combination of those two
        #3.1) This parent node will be child to another node.To retreive it and to join it we will store it in making_nodes dict
    # 4) If created assign left or right variable to their respective node
    # 5) Follow above step till length becomes 1 . That element will be root of our Tree

    making_nodes = {}
    while len(ele_freq)>1:
        ele_freq = dict(sorted(ele_freq.items(),key=lambda x : x[1], reverse=True))
        l = ele_freq.popitem()
        r = ele_freq.popitem()
        if l[0] not in making_nodes:
            making_nodes[l[0]] = Node(None,None,l[0],l[1])
        left = making_nodes[l[0]]
        if r[0] not in making_nodes:
            making_nodes[r[0]] = Node(None,None,r[0],r[1])
        right = making_nodes[r[0]]
        new_node = Node(left,right,left.cur_str+right.cur_str,left.val+right.val)
        making_nodes[new_node.cur_str] = new_node
        new_ele_freq_ele = [new_node.cur_str,new_node.val]
        ele_freq[new_node.cur_str] = new_node.val
    root =  ele_freq.popitem()   
    # Root of our tree
    # Now we need to create Huffman Codes . 
    # To crete it we will traverse the Tree 
    #   1) Whenever we move to left child we will append our code value by 0
    #   2) Whenever we move to right child we will append our code value by 1
    huffman_codes = {}
    traverse(making_nodes[root[0]],huffman_codes,'')
    return huffman_codes

def find_frequency(arr):
    # Simple Calulation of count or frequency of words in the list
    ele_freq = {}
    for i in range(len(arr)):
        if arr[i] not in ele_freq:
            ele_freq[arr[i]] = 1
        else:
            ele_freq[arr[i]]+=1
    return ele_freq
    
if __name__ == "__main__":
    file_to_compress = "demo.txt"
    input_file = open(file_to_compress, "r")            #Open File
    input_text = input_file.read()                      #Read file

    # Calling find_freqeuncy method which will return dict containing frequency of elements
    ele_freq = find_frequency(list(input_text)) 
    print(ele_freq)
    print()
    # Calling make_huffman_tree function which will return Huffmam codes for the frequency of elements        
    huffman_codes = make_huffman_tree(ele_freq)
    print(huffman_codes)

    # Using Huffman Codes (Bits of corresponding char) Encoding the file
    encode_file_name = "Encoded.txt"
    encode(huffman_codes,input_text,encode_file_name)

    # Decoding the encoded file with encoded file and huffman codes
    decode_file_name = "Decoded.txt"
    decode(huffman_codes,encode_file_name,decode_file_name)
    input_file.close()