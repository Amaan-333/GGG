import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, freq, symbol='', left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

    # For heap comparisons
    def __lt__(self, other):
        return self.freq < other.freq

# Function to generate Huffman codes
def generate_huffman_codes(node, code='', code_map={}):
    if node:
        if not node.left and not node.right:  # Leaf node
            code_map[node.symbol] = code
        generate_huffman_codes(node.left, code + '0', code_map)
        generate_huffman_codes(node.right, code + '1', code_map)
    return code_map

# Main function to perform Huffman Encoding
def huffman_encoding(s):
    # Frequency map of characters
    freq_map = {char: s.count(char) for char in set(s)}
    print("Frequency:", freq_map)

    # Priority queue (min-heap) for nodes
    heap = [Node(freq, symbol) for symbol, freq in freq_map.items()]
    heapq.heapify(heap)

    # Build Huffman Tree using a greedy strategy
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        merged_node = Node(n1.freq + n2.freq, left=n1, right=n2)
        heapq.heappush(heap, merged_node)

    # Generate Huffman codes
    code_map = generate_huffman_codes(heap[0])
    print("Huffman Codes:", code_map)

    # Encode the input string
    encoded_string = ''.join(code_map[char] for char in s)
    print("Encoded String:", encoded_string)

# Input string for encoding
s = input("Enter the string: ")
huffman_encoding(s)



"""
 the time complexity of Huffman Encoding is Huffman Encoding is a lossless compression algorithm that assigns shorter codes to more frequent characters to minimize data size. The program:

Counts character frequencies.
Builds a Huffman Tree using a greedy strategy.
Generates unique binary codes for each character.
Encodes the input string using these codesO(nlogn), where n is the length of the input string.

"""
