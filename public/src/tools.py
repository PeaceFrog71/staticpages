import re
from htmlnode import ParentNode
from textnode import TextNode, TextType

     


        







def markdown_to_html_node(markdown):
    body_parent = ParentNode(tag="body", children=[])
    html_parent = ParentNode(tag="html", children=[body_parent])
    return html_parent