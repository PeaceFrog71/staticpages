import re




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


