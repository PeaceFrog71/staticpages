import unittest
from extraction_tools import extract_markdown_images, extract_markdown_links


class TestExtractionTools(unittest.TestCase):
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

    """ def test_split_nodes_image(self):
        text_type_text = "text"
        text_type_input = "image"
        input_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type_text)
        
        self.assertEqual(split_nodes_image([input_node]),
        [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_input, "https://www.boot.dev"),
            TextNode(" and ", text_type_input),
            TextNode(
                "to youtube", text_type_input, "https://www.youtube.com/@bootdotdev"
            ),
        ])
    def test_split_nodes_link(self):
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