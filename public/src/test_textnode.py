import unittest
from textnode import TextType

from textnode import TextNode

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
  
if __name__ == "__main__":
    unittest.main()
      
