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
    num_symbols = int(input("Enter the number of symbols: "))
    symbols = [f"x_{i+1}" for i in range(num_symbols)]
    probabilities = []
    for i in range(num_symbols):
        prob = float(input(f"Enter the probability for symbol {symbols[i]}: "))
        probabilities.append(prob)

    codes = huffman_coding(symbols, probabilities)

    sorted_codes = sorted(codes.items(), key=lambda x: (len(x[1]), x[1], probabilities[symbols.index(x[0])]))

    print("\nSymbol\tCode")
    print("-------\t----")
    for symbol, code in sorted_codes:
        print(f"{symbol}\t{code}")

if __name__ == "__main__":
    main()