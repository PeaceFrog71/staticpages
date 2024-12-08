from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
    #Text types
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    HEADER = "header"

class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        if not isinstance(text_type, TextType):
            raise ValueError("text_type must be an instance of a TextType enum")
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
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("text_type must be a valid TextType enum.")
        
