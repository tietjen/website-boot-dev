import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_diff(self):
        node = TextNode("Node A", TextType.CODE)
        node2 = TextNode("Node B", TextType.IMAGE, "https://example.com")
        self.assertNotEqual(node, node2)
        
    def test_url_none(self):
        node = TextNode("Link A", TextType.LINK)
        self.assertEqual(node.url, None)
        
    def test_repr(self):
        node = TextNode("Example", TextType.LINK, "https://example.com")
        self.assertEqual("TextNode(Example, link, and https://example.com)", repr(node))


if __name__ == "__main__":
    unittest.main()
