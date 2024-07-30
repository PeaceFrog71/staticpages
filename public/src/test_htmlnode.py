import unittest

from htmlnode import HTMLNode, LeafNode

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
        Node props:     None
        """)
        
    def test_to_html(self):
        node = LeafNode(tag="p", value="This is some text", props={"class": "bold", "id": "test", "style": "color: red;"})
        self.assertEqual(node.to_html(), "<p class=\"bold\" id=\"test\" style=\"color: red;\">This is some text</p>")
        
        