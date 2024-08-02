import unittest
#from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html
from textnode import TextNode, split_node_delimiter

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split_node_delimiter(self):
        delimiter = "*"
        text_type_input = "bold"
        text_type_text = "text"
        input_text = "This is a test string. It contains *a delimiter* that will be split into two nodes."
        expected_output = [
            TextNode("This is a test string. It contains ", text_type_text),
            TextNode("a delimiter", text_type_input),
            TextNode(" that will be split into two nodes.", text_type_text)
        ]
        
        self.assertEqual(split_node_delimiter(old_nodes=[input_text], delimiter=delimiter, text_type=text_type_input), expected_output)

    def test_split_node_delimiter2(self):
        delimiter = "**"
        text_type_input = "header"
        text_type_text = "text"
        input_text = "This is a test string. It contains **a delimiter** that will be split into two nodes."
        expected_output = [
            TextNode("This is a test string. It contains ", text_type_text),
            TextNode("a delimiter", text_type_input),
            TextNode(" that will be split into two nodes.", text_type_text)
        ]
        
        self.assertEqual(split_node_delimiter(old_nodes=[input_text], delimiter=delimiter, text_type=text_type_input), expected_output)
        
    def test_split_node_delimiter3(self):
        delimiter = "a"
        text_type_input = "link"
        text_type_text = "text"
        input_text = "This is a test string. It contains **a delimiter** that will be split into two nodes."
        expected_output = [
            TextNode("This is ", text_type_text),
            TextNode(" test string. It cont", text_type_input),
            TextNode("ins **", text_type_text),
            TextNode(" delimiter** th", text_type_input),
            TextNode("t will be split into two nodes.", text_type_text)
        ]
        
        self.assertEqual(split_node_delimiter(old_nodes=[input_text], delimiter=delimiter, text_type=text_type_input), expected_output)