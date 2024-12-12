import re
from textnode import *




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




#Links split delimiter
#Consider a helper function to execute common code.