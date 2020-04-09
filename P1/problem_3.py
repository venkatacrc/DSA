import sys
from collections import Counter
import heapq

class TreeNode:
    
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.bin = None
        self.left = None
        self.right = None
    
    def __str__(self):
        return "::key={} value={} bin={}, left={}, right={}::".format(self.key, self.value, self.bin, self.left, self.right)

    def __lt__(self, other):
        return self.key <= other.key

class Tree:

    def __init__(self):
        self.root = None

    def construct_tree(self, data):
        self.root
        data_dict = Counter(data)
        char_heap = []
        for v,k in data_dict.items():
            node = TreeNode(key=k, value=v)
            heapq.heappush(char_heap, node)
        while len(char_heap) > 1:
            node1 = heapq.heappop(char_heap)
            node2 = heapq.heappop(char_heap)
            k1 = node1.key
            k2 = node2.key
            new_node = TreeNode(key=k1+k2)
            new_node.left = node1
            new_node.right = node2
            heapq.heappush(char_heap, new_node)
        self.root = heapq.heappop(char_heap)
        return self.assign_values()
    
    def assign_values(self):
        encoded_dict = {}
        def rec_values(node,cur_value):
            if node.left == None and node.right == None:
                node.bin = cur_value
                encoded_dict[node.value] = cur_value
                # print("{}={}".format(node.value, cur_value))
                return
            else:
                rec_values(node.left, cur_value+'0')
                rec_values(node.right, cur_value+'1')
            return encoded_dict
        return rec_values(self.root, '')

    
    def display_tree(self):
        print(self.root)


        
def huffman_encoding(data):
    t = Tree()
    char_dict = t.construct_tree(data)
    encoded_data = ''
    for c in data:
        encoded_data += char_dict[c]
    return encoded_data, char_dict


def huffman_decoding(data,tree):
    decoded_data = ''
    cur_str = ''
    inv_tree = {v: k for k, v in tree.items()}
    # print(inv_tree)
    for c in data:
        cur_str += c
        # print(cur_str)
        if cur_str in inv_tree.keys():
            # print(cur_str)
            decoded_data += inv_tree[cur_str]
            cur_str = ''
    return decoded_data

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
