class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
  
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        gen_html = ""
        for key, value in self.props.items():
            gen_html += f" {key}=\"{value}\""
        return gen_html
    
    def __repr__(self) -> str:
        return f"""
        Node tag:       {self.tag}
        Node value:     {self.value}
        Node children:  {self.children}
        Node props:     {self.props}
        """

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None,props=None):
        super().__init__(tag, value, children, props)
        if value is None:
            raise ValueError("All leaf nodes must have a value")
        
    def to_html(self):
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None,props=None):
        super().__init__(tag, value, children, props)
        if children is None:
            raise ValueError("All parent nodes must have children")
        
    def to_html(self):
        if self.tag is None:
            return "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"