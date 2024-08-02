import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html
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
        self.assertEqual(str(context.exception), "Parent nodes must have children")
        self.assertEqual(str(context.exception), "Parent nodes must have children")
        
        node_with_children = ParentNode(
            tag="p",
            children=
            [
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
            props={"class": "bold", "id": "test", "style": "color: red;"}
        )
        print(node_with_children.to_html())
        self.assertEqual(node_with_children.to_html(), "<p class=\"bold\" id=\"test\" style=\"color: red;\"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    

    def test_text_html(self):
        node_boldtxt = TextNode(text_type="bold", text="This is some BOLD text")
        node_italictxt = TextNode(text_type="italic", text="This is some ITALIC text")
        node_codetxt = TextNode(text_type="code", text="This is some CODE text")
        node_linktxt = TextNode(text_type="link", text="This is a LINK", url="www.google.com")
        node_imgtxt = TextNode(text_type="image", text="This is an IMAGE", url="https://cdn1.vox-cdn.com/uploads/chorus_asset/file/4019352/september-1st-doodle-do-not-translate-5078286822539264-hp.0.gif")

        self.assertEqual(text_node_to_html(node_boldtxt).to_html(), "<b>This is some BOLD text</b>")
        self.assertEqual(text_node_to_html(node_italictxt).to_html(), "<i>This is some ITALIC text</i>")
        self.assertEqual(text_node_to_html(node_codetxt).to_html(), "<code>This is some CODE text</code>")
        self.assertEqual(text_node_to_html(node_linktxt).to_html(), "<a href=\"www.google.com\">This is a LINK</a>")
        self.assertEqual(text_node_to_html(node_imgtxt).to_html(), "<img src=\"https://cdn1.vox-cdn.com/uploads/chorus_asset/file/4019352/september-1st-doodle-do-not-translate-5078286822539264-hp.0.gif\" alt=\"This is an IMAGE\"></img>")   