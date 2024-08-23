import unittest
from textnode import TextNode, split_nodes_delimiter

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        delimiter = "*"
        text_type_input = "bold"
        text_type_text = "text"
        input_text = TextNode("This is a test string. It contains *a delimiter* that will be split into two nodes.", text_type=text_type_text)
        expected_output = [
            TextNode(text="This is a test string. It contains ", text_type=text_type_text),
            TextNode(text="a delimiter", text_type=text_type_input),
            TextNode(text=" that will be split into two nodes.", text_type=text_type_text)
        ]
        
        self.assertEqual(split_nodes_delimiter(old_nodes=[input_text], delimiter=delimiter, text_type=text_type_input), expected_output)

    def test_split_nodes_delimiter2(self):
        delimiter = "**"
        text_type_input = "header"
        text_type_text = "text"
        input_text = input_text = TextNode("This is a test string. It contains **a delimiter** that will be split into two nodes.", text_type=text_type_text)
        expected_output = [
            TextNode("This is a test string. It contains ", text_type_text),
            TextNode("a delimiter", text_type_input),
            TextNode(" that will be split into two nodes.", text_type_text)
        ]
        
        self.assertEqual(split_nodes_delimiter(old_nodes=[input_text], delimiter=delimiter, text_type=text_type_input), expected_output)
        
    def test_split_nodes_delimiter3(self):
        delimiter = "a"
        text_type_input = "link"
        text_type_text = "text"
        input_text = input_text = TextNode("This is a test string. It contains **a delimiter** that will be split into two nodes.", text_type=text_type_text)
        expected_output = [
            TextNode("This is ", text_type_text),
            TextNode(" test string. It cont", text_type_input),
            TextNode("ins **", text_type_text),
            TextNode(" delimiter** th", text_type_input),
            TextNode("t will be split into two nodes.", text_type_text)
        ]
        
        self.assertEqual(split_nodes_delimiter(old_nodes=[input_text], delimiter=delimiter, text_type=text_type_input), expected_output)
        
    def test_split_nodes_delimiter4(self):
        delimiter = "**"
        text_type_input = "header"
        text_type_text = "text"
        input_text = TextNode("**a delimiter**This is a test string. It contains that will be split into two nodes.", text_type=text_type_text)
        expected_output = [
            TextNode("a delimiter", text_type_input),
            TextNode("This is a test string. It contains that will be split into two nodes.", text_type_text)
        ]
        
        self.assertEqual(split_nodes_delimiter(old_nodes=[input_text], delimiter=delimiter, text_type=text_type_input), expected_output)