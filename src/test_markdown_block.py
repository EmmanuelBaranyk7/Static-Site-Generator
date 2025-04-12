import unittest
from markdown_block import markdown_to_blocks, block_to_block_type, BlockType
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


if __name__ == "__main__":
    unittest.main()
