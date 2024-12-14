import unittest
from textnode import TextNode, TextType
from tools import *

class TestingTools(unittest.TestCase):
    '''tools used to extract text for the purpose of creating various HTML Nodes'''
    def test_image(self):
        '''extracts image data from raw text strings'''
        print("testing image extraction...")
        text_image =  """This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)
        and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"""
        expected_output = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                           ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text_image), expected_output )

    def test_link(self):
        '''extracts link data from raw text strings'''
        print("testing link extraction...")
        text_link = """This is text with a link [to boot dev](https://www.boot.dev)
        and [to youtube](https://www.youtube.com/@bootdotdev)"""
        output = extract_markdown_links(text_link)
        expected_output = [("to boot dev", "https://www.boot.dev"),
                           ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text_link), expected_output)
        
    def test_link2(self):
        '''extracts no link data from raw text strings'''
        print("testing link extraction...")
        text_link = """This is text with a link to nothing"""
        expected_output = []
        self.assertEqual(extract_markdown_links(text_link), expected_output)
        
        text_link2 = None
        with self.assertRaises(ValueError):
            extract_markdown_links(text_link2)

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
        input_text = TextNode("This is a test string. It contains **a delimiter** that will be split into two nodes.", text_type=text_type_text)
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
        input_text = TextNode("This is a test string. It contains **a delimiter** that will be split into two nodes.", text_type=text_type_text)
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

    #Test Split Nodes Image
    def setUp(self):
        self.text_node = TextNode("example", TextType.TEXT)
        self.bold_node = TextNode("bold text", TextType.BOLD)
        self.italic_node = TextNode("italic text", TextType.ITALIC)
        self.code_node = TextNode("code text", TextType.CODE)
        self.link_node = TextNode("link text", TextType.LINK, url="http://example.com")
        self.image_node = TextNode("alt text", TextType.IMAGE, url="http://image.com/image.jpg")
        self.input_text0 = ""
        self.output_expected0 = []
        self.input_text1 = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.output_expected1 = [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.input_text2 = "[link](https://boot.dev) and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a `code block` word and an *italic* with a **text** This is"
        self.output_expected2 = [
        TextNode("link", TextType.LINK, "https://boot.dev"),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word and an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" with a ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" This is", TextType.TEXT),
        ]
        self.input_text3 = "This is text with an italic word and a code block and an obi wan image(https://i.imgur.com/fJRm4Vk.jpeg) and a link(https://boot.dev)"
        self.output_expected3 = [TextNode("This is text with an italic word and a code block and an obi wan image(https://i.imgur.com/fJRm4Vk.jpeg) and a link(https://boot.dev)", TextType.TEXT)]

        # Block testing variables
        input_block = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        output_block = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item""",
        ]

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

    
    #Test Split Nodes Links

    def test_split_nodes_link_no_links(self):
            old_nodes = [self.text_node, self.bold_node, self.italic_node]
            result = split_nodes_link(old_nodes)
            self.assertEqual(result, old_nodes)

    def test_split_nodes_link_with_links(self):
        old_nodes = [self.text_node, self.link_node, self.bold_node]
        result = split_nodes_link(old_nodes)
        expected = [
            self.text_node,
            TextNode("link text", TextType.LINK, url="http://example.com"),
            self.bold_node
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_multiple_links(self):
        second_link_node = TextNode("link text2", TextType.LINK, url="http://example2.com")
        old_nodes = [self.link_node, self.text_node, second_link_node]
        result = split_nodes_link(old_nodes)
        expected = [
            TextNode("link text", TextType.LINK, url="http://example.com"),
            self.text_node,
            TextNode("link text2", TextType.LINK, url="http://example2.com")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_empty_list(self):
        old_nodes = []
        result = split_nodes_link(old_nodes)
        self.assertEqual(result, []) 

	# Testing Text to TextNodes Function
    def test_text_to_textnodes(self):
        self.assertEqual(text_to_textnodes(self.input_text0), self.output_expected0)
        self.assertEqual(text_to_textnodes(self.input_text1), self.output_expected1)
        self.assertEqual(text_to_textnodes(self.input_text2), self.output_expected2)
        self.assertEqual(text_to_textnodes(self.input_text3), self.output_expected3)
    # Testing block splitter

    def test_markdown_to_blocks(self):
        self.assertEqual(markdown_to_blocks(self.block_input, self.block_output))