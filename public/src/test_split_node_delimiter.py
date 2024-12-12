import unittest
from textnode import TextNode, TextType, LeafNode
from extraction_tools import split_nodes_delimiter, split_nodes_image


class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        delimiter = "*"
        text_type_input = TextType.BOLD
        text_type_text = TextType.TEXT
        input_text = TextNode("This is a test string. It contains *a delimiter* that will be split into two nodes.", text_type=text_type_text)
        expected_output = [
            TextNode(text="This is a test string. It contains ", text_type=text_type_text),
            TextNode(text="a delimiter", text_type=text_type_input),
            TextNode(text=" that will be split into two nodes.", text_type=text_type_text)
        ]
        
        self.assertEqual(split_nodes_delimiter(old_nodes=[input_text], delimiter=delimiter, text_type=text_type_input), expected_output)

    def test_split_nodes_delimiter2(self):
        delimiter = "**"
        text_type_input = TextType.TEXT
        text_type_text = TextType.TEXT
        input_text = input_text = TextNode("This is a test string. It contains **a delimiter** that will be split into two nodes.", text_type=text_type_text)
        expected_output = [
            TextNode("This is a test string. It contains ", text_type_text),
            TextNode("a delimiter", text_type_input),
            TextNode(" that will be split into two nodes.", text_type_text)
        ]
        
        self.assertEqual(split_nodes_delimiter(old_nodes=[input_text], delimiter=delimiter, text_type=text_type_input), expected_output)
        
    def test_split_nodes_delimiter3(self):
        delimiter = "a"
        text_type_input = TextType.LINK
        text_type_text = TextType.TEXT
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
        text_type_input = TextType.TEXT
        text_type_text = TextType.TEXT
        input_text = TextNode("**a delimiter**This is a test string. It contains that will be split into two nodes.", text_type=text_type_text)
        expected_output = [
            TextNode("a delimiter", text_type_input),
            TextNode("This is a test string. It contains that will be split into two nodes.", text_type_text)
        ]
        
        self.assertEqual(split_nodes_delimiter(old_nodes=[input_text], delimiter=delimiter, text_type=text_type_input), expected_output)
    def setUp(self):
        self.text_node = TextNode("example", TextType.TEXT)
        self.bold_node = TextNode("bold text", TextType.BOLD)
        self.italic_node = TextNode("italic text", TextType.ITALIC)
        self.code_node = TextNode("code text", TextType.CODE)
        self.link_node = TextNode("link text", TextType.LINK, url="http://example.com")
        self.image_node = TextNode("alt text", TextType.IMAGE, url="http://image.com/image.jpg")

    def test_split_nodes_image_no_images(self):
        old_nodes = [self.text_node, self.bold_node, self.italic_node]
        result = split_nodes_image(old_nodes)
        self.assertEqual(result, old_nodes)

    def test_split_nodes_image_with_images(self):
        old_nodes = [self.text_node, self.image_node, self.bold_node]
        result = split_nodes_image(old_nodes)
        expected = [
            self.text_node,
            TextNode("alt text", TextType.IMAGE, url="http://image.com/image.jpg"),
            self.bold_node
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_multiple_images(self):
        second_image_node = TextNode("second alt text", TextType.IMAGE, url="http://image.com/second.jpg")
        old_nodes = [self.image_node, self.text_node, second_image_node]
        result = split_nodes_image(old_nodes)
        expected = [
            TextNode("alt text", TextType.IMAGE, url="http://image.com/image.jpg"),
            self.text_node,
            TextNode("second alt text", TextType.IMAGE, url="http://image.com/second.jpg")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_empty_list(self):
        old_nodes = []
        result = split_nodes_image(old_nodes)
        self.assertEqual(result, []) 
           
    def test_split_nodes_image(self):
        text_type_text = TextType.TEXT
        text_type_input = TextType.IMAGE
        input_node = TextNode("This is text with an image ![sunset](https://www.boot.dev/sunset.jpg) and ![sunrise](https://www.boot.dev/sunrise.jpg)", text_type_text)
        split_nodes = split_nodes_image([input_node])
        """self.assertEqual(split_nodes_image([input_node]),
        [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_input, "https://www.boot.dev"),
            TextNode(" and ", text_type_input),
            TextNode(
                "to youtube", text_type_input, "https://www.youtube.com/@bootdotdev"
            ),
        ])"""
    """ def test_split_nodes_link(self):
        text_type_text = "text"
        text_type_input = "link"
        input_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type_text)
        
        self.assertEqual(split_nodes_link([input_node]),
        [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_input, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
                "to youtube", text_type_input, "https://www.youtube.com/@bootdotdev"
            ),
        ]) """