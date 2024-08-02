import re


def extract_markdown_images(text):
    image_list = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return image_list
    

def extract_markdown_links(text):
    link_list = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return link_list