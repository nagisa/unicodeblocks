import unittest
from unicodeblocks import blocks, blockof

class BlocksTests(unittest.TestCase):
    def test_gets_block_by_name(self):
        latin = blocks['Basic Latin']
        self.assertEqual(blocks['basiclatin'], latin)
        self.assertEqual(blocks['ba-sic lat-in'], latin)
        self.assertEqual(blocks['basic _ latin'], latin)
        self.assertEqual(blocks['BASIC latin'], latin)
        self.assertEqual(blocks['BaSiC LaTiN'], latin)

    def test_gets_block_by_name2(self):
        cjk = blocks['CJK Unified Ideographs Extension A']
        self.assertEqual(blocks['cjkunifiedideographsextensiona'], cjk)
        self.assertEqual(blocks['CJK UnifiedIdeographsExtension A'], cjk)
        self.assertEqual(blocks['CJK Unified Ideographs Extension-A'], cjk)
        self.assertEqual(blocks['CJK unified ideographs extension A'], cjk)
        self.assertEqual(blocks['CJK_Unified_Ideographs_Extension-A'], cjk)
        self.assertEqual(blocks['cjk-Unified-Ideographs-Extension-A'], cjk)

    def test_block_of(self):
        self.assertEqual(blockof('a'), blockof('b'))
        self.assertNotEqual(blockof('a'), blockof('ą'))
        self.assertEqual(blockof(chr(0)),
                         blockof(chr(127)))
        self.assertNotEqual(blockof(chr(127)),
                            blockof(chr(128)))
        with self.assertRaises(TypeError):
            blockof(1)
        with self.assertRaises(TypeError):
            blockof("hello")

class BlockTests(unittest.TestCase):
    def setUp(self):
        self.block = blocks['Hiragana']

    def test_in(self):
        self.assertIn('か', self.block)
        self.assertNotIn('カ', self.block)
        self.assertIn(chr(0x3040), self.block)
        self.assertIn(chr(0x309F), self.block)
        self.assertNotIn(chr(0x303F), self.block)
        self.assertNotIn(chr(0x30A0), self.block)
        with self.assertRaises(TypeError):
            0x309F in self.block

    def test_len(self):
        self.assertEqual(len(self.block), len(self.block))
        self.assertEqual(len(self.block), len(list(self.block)))
        self.assertEqual(len(self.block), 0x30a0 - 0x3040)

    def test_iter(self):
        hiragana = [chr(i) for i in range(0x3040, 0x309F + 1)]
        self.assertSequenceEqual(list(self.block), hiragana)

unittest.main()
