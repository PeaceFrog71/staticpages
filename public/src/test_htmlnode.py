import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode

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
            tag="p",
            children=
            [
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )
        print(node_with_children.to_html())
        self.assertEqual(node_with_children.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        
    def test_text_to_html(self):
        node_boldtxt = TextNode(text_type="b", text="This is some BOLD text")
        node_italictxt = TextNode("i", "This is some ITALIC text")
        node_codetxt = TextNode("code", "This is some CODE text")
        node_linktxt = TextNode("link", "This is a LINK", "www.google.com")
        node_imgtxt = TextNode("image", "This is an IMAGE", "https://cdn1.vox-cdn.com/uploads/chorus_asset/file/4019352/september-1st-doodle-do-not-translate-5078286822539264-hp.0.gif")
        
        node_boldhtml = LeafNode().text_node_to_html(node_boldtxt)
             
        
        
        self.assertEqual(node_boldhtml, "<b>This is some BOLD text</b>")
        
        