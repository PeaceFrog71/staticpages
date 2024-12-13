import re
from textnode import *
from text_types import *



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