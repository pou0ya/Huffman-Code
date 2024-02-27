class Node:
    def __init__(self, symbol, probability, left=None, right=None):
        self.symbol = symbol
        self.probability = probability
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.probability > other.probability

def huffman_coding(symbols, probabilities):
    nodes = [Node(symbol, prob) for symbol, prob in zip(symbols, probabilities)]

    while len(nodes) > 1:
        nodes.sort()
        left, right = nodes.pop(), nodes.pop()
        parent = Node(None, left.probability + right.probability, left, right)
        nodes.append(parent)

    codes = {}
    curr_node = nodes[0]
    curr_code = ""

    def traverse(node, code):
        if node is None:
            return
        
        if node.symbol is not None:
            codes[node.symbol] = code
            return

        traverse(node.left, code + "1")
        traverse(node.right, code + "0")

    traverse(curr_node, curr_code)
    return codes

def main():
    letter_probabilities = {'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
                            'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
                            'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
                            'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
                            'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
                            'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
                            'y': 0.01974, 'z': 0.00074}

    text = input("Enter the text to encode: ").lower()

    # Calculate letter frequencies
    letter_freq = {}
    for letter in text:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1

    # Update probabilities based on letter frequencies
    total_letters = sum(letter_freq.values())
    updated_probabilities = {letter: letter_probabilities[letter] * freq / total_letters for letter, freq in letter_freq.items()}

    # Generate Huffman codes
    unique_letters = list(letter_freq.keys())
    codes = huffman_coding(unique_letters, [updated_probabilities[letter] for letter in unique_letters])
    encoded_text = ''.join([codes[letter] for letter in text])

    print("\nEncoded text:", encoded_text, "\n")
    print("Letter\tCodeword  Probability")
    print("------  --------  -----------")

    for letter in unique_letters:
        probability_formatted = "{:.5f}".format(updated_probabilities[letter])
        print(f"  {letter}\t  {codes[letter]}\t    {probability_formatted}")

if __name__ == "__main__":
    main()