import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):

    # ---------------------------------------------- HTML Node tests ---------------------------------------------
    # verify props
    def test_props_to_html_multiple_props(self):
        node = HTMLNode(
            tag="tag",
            value="Google",
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        result = node.props_to_html()
        self.assertIn(' href="https://www.google.com"', result)
        self.assertIn(' target="_blank"', result)

    # test values
    def test_values(self):
        node = HTMLNode("tagTest", "valueTest")
        self.assertEqual(node.tag, "tagTest")
        self.assertEqual(node.value, "valueTest")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    # props none
    def test_props_to_html_none(self):
        node = HTMLNode(tag="tag test", value="val test", props=None)
        self.assertEqual(node.props_to_html(), "")

    # props empty dictionary
    def test_props_to_html_empty_dict(self):
        node = HTMLNode(tag="tag test", value="val test", props={})
        self.assertEqual(node.props_to_html(), "")

    # test error raise
    def test_to_html_raises(self):
        node = HTMLNode(tag = "tag test", value="val test")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    # ---------------------------------------------------- Test Leaf Node --------------------------------------------
    # paragraph 
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello world")
        self.assertEqual(node.to_html(), "<p>Hello world</p>")

    # a link
    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "google", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">google</a>')

    # text
    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Text")
        self.assertEqual(node.to_html(), "Text")
    
    # raise error empty value
    def test_leaf_to_html_raises_empty_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    # -------------------------------------------------- Parent Node tests -------------------------------------------
    # html with children
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    # html with grandchildren
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    # multiple children
    def test_to_html_multiple_children_mixed(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    # html with props
    def test_to_html_with_props(self):
        node = ParentNode("div", [LeafNode("span", "x")], {"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><span>x</span></div>')

    # raise without tag
    def test_raises_without_tag(self):
        node = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            node.to_html()

    # raise without children
    def test_raises_without_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    # empty children list
    def test_empty_children_list_renders_empty_tag(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")