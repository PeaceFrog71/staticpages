import unittest
from extraction_tools import extract_markdown_images, extract_markdown_links

class TestExtractionTools(unittest.TestCase):
    '''tools used to extract text for the purpose of creating various HTML Nodes'''
    def test_image(self):
        '''extracts image data from raw text strings'''
        text_image =  """This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)
        and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"""
        expected_output = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                           ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text_image), expected_output )

    def test_link(self):
        '''extracts link data from raw text strings'''
        text_link = """This is text with a link [to boot dev](https://www.boot.dev)
        and [to youtube](https://www.youtube.com/@bootdotdev)"""
        expected_output = [("to boot dev", "https://www.boot.dev"),
                           ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text_link), expected_output)
