import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    if text is None:
        raise ValueError("Invalid Input. Expected text input.")
    image_list = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return image_list

def extract_markdown_links(text):
    if text is None:
        raise ValueError("Invalid Input. Expected text input.")
    link_list = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return link_list

# Processes Lists of TextNodes and returns a new List of Nodes that are TextNodes and the text_type requested.
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return_nodes = []
    for working_node in old_nodes:
        if working_node.text_type != TextType.TEXT:
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
                # the odd elements will be the strings that will remain TEXT
                return_nodes.append(TextNode(text_divided[i], TextType.TEXT))
            else:
                # the odd elements will be the delimited strings that should be converted to new type
                # then append the new textnode to the return nodes list.
                return_nodes.append(TextNode(text_divided[i], text_type))        
    return return_nodes

#make a seperate function for each delimter type.
#Images split delimiter
def split_nodes_image(old_nodes):
    new_nodes = []
    images = []
    for this_node in old_nodes:
        if (this_node.text_type != TextType.TEXT):
            new_nodes.append(this_node)
        else:
            images = extract_markdown_images(this_node.text);
            num_images = images.__len__()
            if num_images == 0:
                new_nodes.append(this_node)
            else:
                index = 0
                working_text = this_node.text
                while (index < num_images) :
                    image = images[index] 
                    image_mask = f"![{image[0]}]({image[1]})"
                    split_text = working_text.split(image_mask, 1)  
                    
                    if split_text[0] != "":
                        new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                    new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                    if split_text[1] != "":
                        working_text = split_text[1]
                        if (index == num_images - 1): 
                            new_nodes.append(TextNode(working_text, TextType.TEXT))
                    
                    index += 1


    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    links = []
    for this_node in old_nodes:
        if (this_node.text_type != TextType.TEXT):
            new_nodes.append(this_node)
        else:
            links = extract_markdown_links(this_node.text);
            num_links = links.__len__()
            if num_links == 0:
                new_nodes.append(this_node)
            else:
                index = 0
                working_text = this_node.text
                while (index < num_links) :
                    link = links[index] 
                    link_mask = f"[{link[0]}]({link[1]})"
                    split_text = working_text.split(link_mask, 1)  
                    
                    if split_text[0] != "":
                        new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                    new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                    if split_text[1] != "":
                        working_text = split_text[1]
                        if (index == num_links - 1): 
                            new_nodes.append(TextNode(working_text, TextType.TEXT))
                    
                    index += 1
    return new_nodes



def text_to_textnodes(text):
    first_text = TextNode(text, TextType.TEXT)
    initial_list = [first_text]
    """Split in this order:
        1. Code blocks (to protect their contents)
        2. Images (most specific with !)
        3. Links
        4. Bold (**)
        5. Italic (*) 
    """
    codeblocks_list = split_nodes_delimiter(initial_list, "`", TextType.CODE)
    images_list = split_nodes_image(codeblocks_list)
    links_list = split_nodes_link(images_list)
    bold_list = split_nodes_delimiter(links_list, "**", TextType.BOLD)
    italic_list = split_nodes_delimiter(bold_list, "*", TextType.ITALIC)

    return italic_list       

def text_node_to_html(text_node):
    from htmlnode import LeafNode #Importing here to avoid circular dependancy
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
        
# Block handling tools
def markdown_to_blocks(markdown):
    if markdown is None:
        return []
    markdown_input = markdown
    markdown_input = markdown_input.split('\n\n')
    markdown_output = []
    for item in markdown_input:
        item = item.strip()
        if item != "":
            markdown_output.append(item)
    return markdown_output

def block_to_blocktype(markdown):
    header_pattern = r"^#{1,6} "
    code_pattern = r"^```[\s\S]*?```$"
    quote_pattern = r"^(> .*(\n|$))+"
    unlist_pattern = r"^(\* |\- ).*(\n|$)+"
    orlist_pattern = r"^(\d+)\. .*$" #doesnt check for numerical order. Use a loop to validate numerical order

    patterns = [(quote_pattern, TextType.QUOTE), (code_pattern, TextType.CODE), (header_pattern, TextType.HEADER), (unlist_pattern, TextType.UL), (orlist_pattern, TextType.OL)]

    for pattern, text_type in patterns:
        if re.match(pattern, markdown, re.DOTALL):
            if pattern != orlist_pattern:
                return text_type
            else:
                return validate_ordered_list(markdown)

    return TextType.PARAGRAPH

def validate_ordered_list(block):
    # Pattern to match a line with a number, dot, and space
    pattern = r"^(\d+)\. .*$"
    lines = block.splitlines()
    
    expected_number = 1
    for line in lines:
        match = re.match(pattern, line)
        if not match:
            return TextType.PARAGRAPH  # Line does not match the pattern
        
        number = int(match.group(1))
        if number != expected_number:
            return TextType.PARAGRAPH  # Number is not in the expected sequence
        
        expected_number += 1  # Increment expected number for the next line
    
    return TextType.OL