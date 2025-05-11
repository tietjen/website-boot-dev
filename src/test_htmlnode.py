import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("a", "Test", None, {"href": "https://www.google.com"})
        self.assertEqual("HTMLNode(tag: 'a', value: 'Test', children: 'None', props: '{'href': 'https://www.google.com'}')", repr(node))
        
    def test_props_to_html(self):
        node = HTMLNode("a", "Test", None, {"href": "https://www.google.com", "a": "https:example.com"})
        self.assertEqual(' href="https://www.google.com" a="https:example.com"', node.props_to_html())
        
    def test_empty(self):
        node = HTMLNode()
        self.assertEqual("HTMLNode(tag: 'None', value: 'None', children: 'None', props: 'None')", repr(node))