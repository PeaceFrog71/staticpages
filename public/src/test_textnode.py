import unittest
from textnode import TextType, TextNode, text_node_to_html

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)
  
	def test_eq2(self):
		node = TextNode("This is another test node", TextType.BOLD)
		node2 = TextNode("This is a different test node", TextType.BOLD)
		self.assertNotEqual(node, node2)
  
	def test_eq3(self):
		node = TextNode("This is a text node", TextType.TEXT)
		node2 = TextNode("This is a text node.", TextType.BOLD)
		self.assertNotEqual(node, node2)
  
	def test_values(self):
		node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
		node2 = TextNode("This is a text node", TextType.BOLD, "www.google.com")
		node3 = TextNode("This is a different test node", TextType.TEXT, "www.yahoo.com")
		self.assertEqual(node.text, node2.text)
		self.assertEqual(node.text_type, node2.text_type)
		self.assertEqual(node.url, node2.url)
		self.assertNotEqual(node.text, node3.text)
		self.assertNotEqual(node.text_type, node3.text_type)
		self.assertNotEqual(node.url, node3.url)

	def test_text_html(self):
		print("\nTesting text node to html function")
		node_normtxt = TextNode(text_type=TextType.TEXT, text="This is some text")
		node_boldtxt = TextNode(text_type=TextType.BOLD, text="This is some BOLD text")
		node_italictxt = TextNode(text_type=TextType.ITALIC, text="This is some ITALIC text")
		node_codetxt = TextNode(text_type=TextType.CODE, text="This is some CODE text")
		node_linktxt = TextNode(text_type=TextType.LINK, text="This is a LINK", url="www.google.com")
		node_imgtxt = TextNode(text_type=TextType.IMAGE, text="This is an IMAGE", url="https://cdn1.vox-cdn.com/uploads/chorus_asset/file/4019352/september-1st-doodle-do-not-translate-5078286822539264-hp.0.gif")
		node_headertxt = TextNode(text_type=TextType.HEADER, text="This is some text")
		with self.assertRaises(ValueError, msg=None):
			TextNode(text_type="header", text="This is some text")
			text_node_to_html(node_headertxt).to_html()

		self.assertEqual(text_node_to_html(node_normtxt).to_html(), "This is some text")
		self.assertEqual(text_node_to_html(node_boldtxt).to_html(), "<b>This is some BOLD text</b>")
		self.assertEqual(text_node_to_html(node_italictxt).to_html(), "<i>This is some ITALIC text</i>")
		self.assertEqual(text_node_to_html(node_codetxt).to_html(), "<code>This is some CODE text</code>")
		self.assertEqual(text_node_to_html(node_linktxt).to_html(), "<a href=\"www.google.com\">This is a LINK</a>")
		self.assertEqual(text_node_to_html(node_imgtxt).to_html(), "<img src=\"https://cdn1.vox-cdn.com/uploads/chorus_asset/file/4019352/september-1st-doodle-do-not-translate-5078286822539264-hp.0.gif\" alt=\"This is an IMAGE\"></img>")

	# Testing Text to TextNodes Function
	def setup():
		
	def test_text_to_textnodes(self):
		
  
if __name__ == "__main__":
    unittest.main()
      
