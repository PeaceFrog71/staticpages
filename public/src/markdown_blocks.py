from enum import Enum
import re
from markdown_blocks import text_to_textnodes 
from htmlnode import HTMLNode, LeafNode, ParentNode  # Assuming htmlnode is a module that provides HTML node classes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ORDERED_LIST = "ordered_list"
    UNORDERED_LIST = "unordered_list"

# Block handling tools
def markdown_to_blocks(markdown):
    clean_blocks = [block.strip() for block in markdown.split("\n\n") if block.strip()]
    return clean_blocks

def block_to_block_type(markdown):
    header_pattern = r"^#{1,6} "
    code_pattern = r"^```[\s\S]*?```$"
    quote_pattern = r"^(> .*(\n|$))+"
    unlist_pattern = r"^(\* |\- ).*(\n|$)+"
    orlist_pattern = r"^(\d+)\. .*$" #doesnt check for numerical order. Use a loop to validate numerical order

    patterns = [(quote_pattern, BlockType.QUOTE), (code_pattern, BlockType.CODE), (header_pattern, BlockType.HEADING), (unlist_pattern, BlockType.UNORDERED_LIST), (orlist_pattern, BlockType.ORDERED_LIST)]

    for pattern, block_type in patterns:
        if re.match(pattern, markdown, re.DOTALL):
            if pattern != orlist_pattern:
                return block_type
            else:
                return validate_ordered_list(markdown)

    return BlockType.PARAGRAPH

def validate_ordered_list(block):
    # Pattern to match a line with a number, dot, and space
    pattern = r"^(\d+)\. .*$"
    lines = block.splitlines()
    
    expected_number = 1
    for line in lines:
        match = re.match(pattern, line)
        if not match:
            return BlockType.PARAGRAPH  # Line does not match the pattern
        
        number = int(match.group(1))
        if number != expected_number:
            return BlockType.PARAGRAPH  # Number is not in the expected sequence
        
        expected_number += 1  # Increment expected number for the next line
    
    return BlockType.ORDERED_LIST


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    if not blocks:
        return LeafNode(tag=None, value="")  # Return an empty node if no blocks are found
    master_node = ParentNode(tag="div", children=[])
    
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            # Handle paragraph
            # Assuming text_to_textnodes is a function that converts text to HTML nodes
            text_nodes = text_to_textnodes(block, block.type)         
            pass
        elif block_type == BlockType.HEADING:
            # Handle heading
            pass
        elif block_type == BlockType.CODE:
            # Handle code
            pass
        elif block_type == BlockType.QUOTE:
            # Handle quote
            pass
        elif block_type == BlockType.UNORDERED_LIST:
            # Handle unordered list
            pass
        elif block_type == BlockType.ORDERED_LIST:
            # Handle ordered list
            pass

