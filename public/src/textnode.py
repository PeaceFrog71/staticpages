from enum import Enum

class BlockType(Enum):
    #Block types
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    LINK = "link"
    IMAGE = "image"
    code = "code"
    heading = "heading"
    quote = "quote"
    paragraph = "paragraph"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"

class TextNode:
    def __init__(self, text, text_type: BlockType, url=None):
        if not isinstance(text_type, BlockType):
            raise ValueError("text_type must be an instance of a BlockType enum")
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
        return f"TextNode(\"{self.text}\", {self.text_type}, {self.url})"

    def __str__(self):
        return f"TextNode(\"{self.text}\", {self.text_type}, {self.url})"


    
