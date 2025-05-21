from enum import Enum
import re

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