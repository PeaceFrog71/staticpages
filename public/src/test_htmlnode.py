import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"class": "bold", "id": "test"})
        node2 = HTMLNode(props={"href": "www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " class=\"bold\" id=\"test\"")
        self.assertEqual(node2.props_to_html(), " href=\"www.google.com\" target=\"_blank\"")
        
        node3 = HTMLNode(tag="p", value="This is some text", props={"class": "bold", "id": "test", "style": "color: red"})
        self.assertEqual(node3.props_to_html(), " class=\"bold\" id=\"test\" style=\"color: red\"")
        
        node4 = HTMLNode(tag="p", value="This is some text")
        self.assertEqual(node4.__repr__(), """
        Node tag:       p
        Node value:     This is some text
        Node children:  None
        Node props:     None
        """)
        
    def test_to_html(self):
        node = LeafNode(tag="p", value="This is some text", props={"class": "bold", "id": "test", "style": "color: red"})
        self.assertEqual(node.to_html(), "<p class=\"bold\" id=\"test\" style=\"color: red\">This is some text</p>")
        
    def test_ParentNode(self):
        with self.assertRaises(ValueError) as context: 
            ParentNode(tag="div", props={"class": "bold", "id": "test", "style": "color: red"})
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
            props={"class": "bold", "id": "test", "style": "color: red"}
        )
        #print(node_with_children.to_html())
        self.assertEqual(node_with_children.to_html(), "<p class=\"bold\" id=\"test\" style=\"color: red\"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

        node_with_parents_as_children = ParentNode(
            tag="p",
            children=
            [
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                node_with_children,
                LeafNode(tag=None, value="Normal text"),
            ],
            props={"class": "bold", "id": "test", "style": "color: red"}
        )

        self.assertEqual(node_with_parents_as_children.to_html(), "<p class=\"bold\" id=\"test\" style=\"color: red\"><b>Bold text</b>Normal text<p class=\"bold\" id=\"test\" style=\"color: red\"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>Normal text</p>")

    