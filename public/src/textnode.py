class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if  self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def __str__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def split_node_delimiter(old_nodes, delimiter, text_type):
    return_nodes = []
    for node in old_nodes:
        if delimiter in node:
            split_list = node.split(delimiter)
            for i in range(len(split_list)):
                if i%2 == 0:
                    return_nodes.append(TextNode(text = split_list[i], text_type= "text"))
                else:
                    return_nodes.append(TextNode(text= split_list[i], text_type= text_type))
    return return_nodes
        