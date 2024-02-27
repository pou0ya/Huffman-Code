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

        traverse(node.left, code + "0")
        traverse(node.right, code + "1")

    traverse(curr_node, curr_code)
    return codes

def main():
    text = input("Enter the text to encode: ").lower()

    letter_counts = {}
    total_letters = 0

    for letter in text:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
            total_letters += 1

    unique_letters = list(letter_counts.keys())
    probabilities = [letter_counts[letter] / total_letters for letter in unique_letters]
    codes = huffman_coding(unique_letters, probabilities)
    encoded_text = ''.join([codes[letter] for letter in text if letter.isalpha()])

    print("\nEncoded text:", encoded_text, "\n")
    print("Letter\tCodeword  Probability")
    print("------  --------  -----------")

    for letter in unique_letters:
        print(f"  {letter}\t  {codes[letter]}\t     {letter_counts[letter] / total_letters:.2f}")

if __name__ == "__main__":
    main()