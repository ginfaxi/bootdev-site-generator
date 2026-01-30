from textnode import TextNode
from textnode import TextType

def main():
    node = TextNode("Anchor text", TextType.TEXT, "https://www.boot.dev")
    print(node)

main()