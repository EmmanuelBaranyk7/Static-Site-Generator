import unittest
from markdown_block import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node
from textnode import TextNode, TextType


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        block = "######## Heading 6"
        btype = block_to_block_type(block)
        self.assertEqual(btype, BlockType.HEADING)

    def test_block_to_block_type_CODE(self):
        block = "```This is a code block```"
        btype = block_to_block_type(block)
        self.assertEqual(btype, BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = ">This is a quote block"
        btype = block_to_block_type(block)
        self.assertEqual(btype, BlockType.QUOTE)

    def test_block_to_block_type_UL(self):
        block = "- this is an unordered list"
        btype = block_to_block_type(block)
        self.assertEqual(btype, BlockType.UNORDEREDLIST)

    def test_block_to_block_type_OL(self):
        block = "4. THis is an ordered list"
        btype = block_to_block_type(block)
        self.assertEqual(btype, BlockType.ORDEREDLIST)

    def test_block_to_block_type_paragraph(self):
        block = "This is a paragaph block"
        btype = block_to_block_type(block)
        self.assertEqual(btype, BlockType.PARAGRAPH)

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

def test_headings(self):
        md = """
    # Heading 1

    ## Heading 2

    ### Heading 3 with *italic*
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3 with <i>italic</i></h3></div>"
        )

def test_quotes(self):
        md = """
    > This is a quote
    > with multiple lines
    > and **bold** text
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with multiple lines and <b>bold</b> text</blockquote></div>"
        )

def test_unordered_list(self):
        md = """
    - Item 1
    - Item 2 with `code`
    - Item 3 with *emphasis*
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2 with <code>code</code></li><li>Item 3 with <i>emphasis</i></li></ul></div>"
        )

def test_ordered_list(self):
        md = """
    1. First item
    2. Second item with **bold**
    3. Third item with `code`
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item with <b>bold</b></li><li>Third item with <code>code</code></li></ol></div>"
        )

if __name__ == "__main__":
    unittest.main()
