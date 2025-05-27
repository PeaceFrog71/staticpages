from textnode import TextNode, TextType

def main():
	test_node =  TextNode("Some test text", TextType.BOLD, "https://boot.dev")
	print(test_node)
	
main()
