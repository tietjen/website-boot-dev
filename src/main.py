from textnode import TextNode, TextType

def main():
    node = TextNode("bla", TextType.LINK, "http:/example.com")
    print(node)
    
if __name__ == "__main__":
    main()
    
