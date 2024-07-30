import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"class": "bold", "id": "test"})
        node2 = HTMLNode(props={"href": "www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), f" class=\"bold\" id=\"test\"")
        self.assertEqual(node2.props_to_html(), f" href=\"www.google.com\" target=\"_blank\"")
        
        node3 = HTMLNode(tag="p", value="This is some text", props={"class": "bold", "id": "test", "style": "color: red;"})
        self.assertEqual(node3.props_to_html(), " class=\"bold\" id=\"test\" style=\"color: red;\"")
        
        node4 = HTMLNode(tag="p", value="This is some text")
        self.assertEqual(node4.__repr__(), """
        Node tag:       p
        Node value:     This is some text
        Node children:  None
        Node props:     {}
        """)
        
    def test_to_html(self):
        node = LeafNode(tag="p", value="This is some text", props={"class": "bold", "id": "test", "style": "color: red;"})
        self.assertEqual(node.to_html(), "<p class=\"bold\" id=\"test\" style=\"color: red;\">This is some text</p>")
        
    def test_ParentNode(self):
        with self.assertRaises(ValueError) as context: 
            ParentNode(tag="div", props={"class": "bold", "id": "test", "style": "color: red;"})
        self.assertEqual(str(context.exception), "All parent nodes must have children")
        
        node_with_children = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        
        self.assertEqual(node_with_children.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>") 
        