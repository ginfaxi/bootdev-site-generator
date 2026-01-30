import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    # happy case All
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    # Text Not Equal
    def test_not_eq_text(self):
        node = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("World", TextType.TEXT)
        self.assertNotEqual(node, node2)

    # Text Type Not Equal
    def test_not_eq_text_type(self):
        node = TextNode("Text", TextType.ITALIC)
        node2 = TextNode("Text", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    # Happy Path: url=None
    def test_eq_url_none(self):
        node = TextNode("Text", TextType.TEXT, None)
        node2 =  TextNode("Text", TextType.TEXT)
        self.assertEqual(node, node2)

    # URL Not Equal
    def test_not_eq_url(self):
        node = TextNode("Text", TextType.LINK, "https://boot.dev")
        node2 = TextNode("Text", TextType.LINK, "https://google.com")
        self.assertNotEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()