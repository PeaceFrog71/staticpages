from htmlnode import LeafNode
from extraction_tools import extract_markdown_links, extract_markdown_images


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and 
            self.text_type == other.text_type
            and 
            self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def __str__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(value=text_node.text)
        case "bold":
            return LeafNode(tag="b", value=text_node.text)
        case "italic":
            return LeafNode(tag="i", value=text_node.text)
        case "code":
            return LeafNode(tag="code", value=text_node.text)
        case "link":
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case "image":
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("Invalid text node type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return_nodes = []
    for working_node in old_nodes:
        if working_node.text_type != text_type_text:
            return_nodes.append(working_node)
            continue

        text_divided = working_node.text.split(delimiter)
        # if length is even then unmatched delimiter, if odd then matched
        if len(text_divided) % 2 == 0:
            raise ValueError("Delimiter not matched in text.")
        
        for i in range(len(text_divided)):
            if text_divided[i] == "":
                continue
            if i % 2 == 0:
                return_nodes.append(TextNode(text_divided[i], text_type_text))
            else:
                return_nodes.append(TextNode(text_divided[i], text_type))
            
        # the odd elements will be the delimited strings that should be converted to new type
        # then append the new textnode to the return nodes list.
        
    return return_nodes