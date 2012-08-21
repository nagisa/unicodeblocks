# unicodeblocks

An utility to work with unicodeblocks in Python

## Usage

Module contains two classes: `Block` and `Blocks`. `Blocks` is just a
collection of `Block`.
Also there's prebuilt instance of `Blocks` that contains all 220 Unicode 6.1.0
blocks.

```python
>>> import unicodeblocks
>>> unicodeblocks.blocks
Blocks(...220 * Block...)
```

### Blocks

You can do quite a lot strange things with `Blocks`.

For example, if you want to know which block character belongs to, you can do it:

```python
>>> unicodeblocks.blocks.block_of('-')
Block('Basic Latin', 0x0, 0x7f)
>>> unicodeblocks.blocks.block_of('か')
Block('Hiragana', 0x3040, 0x309f)
>>> unicodeblocks.blocks.block_of('日')
Block('CJK Unified Ideographs', 0x4e00, 0x9fff)
```

You can iterate trough them:
```
>>> unicodeblocks.blocks.blocks()
<generator object __iter__ at 0x2d5df50>
>>> len(list(itertools.chain(*unicodeblocks.blocks.blocks())))
253440 # of characters in all unicode blocks.
```

And trough names of blocks as well:
```python
>>> list(unicodeblocks.blocks.names())
['Basic Latin', 'Latin-1 Supplement', 'Latin Extended-A', 'Latin Extended-B', 'I
PA Extensions',…]
```

Getting one specific block is easy as well:
```python
unicodeblocks.blocks['cyrillic']
Block('Cyrillic', 0x400, 0x4ff)
```
Keys are not case sensitive.
As per specification spaces, dashes and underscores are ignored as well.
```python
>>> unicodeblocks.blocks['cy ri-ll_ic']
Block('Cyrillic', 0x400, 0x4ff)
```

### Block

They are ordeable, so you can sort them.

There's three atributes available:
```python
>>> latin.name # Full name of block
'Latin Extended-A'
>>> latin.start # Block start codepoint
256
>>> latin.end # Block end codepoint
383
```

You can check if letter belongs to some block:
```python
>>> 'ą' in latin
True
```
Get length of block or all letters in it:
```python
>>> len(latin)
128
>>> list(latin)
['Ā', 'ā', 'Ă', 'ă', 'Ą', 'ą', 'Ć', 'ć', 'Ĉ', 'ĉ', 'Ċ', 'ċ', 'Č', 'č', 'Ď', 'ď',
 'Đ', 'đ', 'Ē', 'ē', 'Ĕ', 'ĕ', 'Ė', 'ė', 'Ę', 'ę', 'Ě', 'ě', 'Ĝ', 'ĝ', 'Ğ', 'ğ',
 'Ġ', 'ġ', 'Ģ', 'ģ', 'Ĥ', 'ĥ', 'Ħ', 'ħ', 'Ĩ', 'ĩ', 'Ī', 'ī', 'Ĭ', 'ĭ', 'Į', 'į',
 'İ', 'ı', 'Ĳ', 'ĳ', 'Ĵ', 'ĵ', 'Ķ', 'ķ', 'ĸ', 'Ĺ', 'ĺ', 'Ļ', 'ļ', 'Ľ', 'ľ', 'Ŀ',
 'ŀ', 'Ł', 'ł', 'Ń', 'ń', 'Ņ', 'ņ', 'Ň', 'ň', 'ŉ', 'Ŋ', 'ŋ', 'Ō', 'ō', 'Ŏ', 'ŏ',
 'Ő', 'ő', 'Œ', 'œ', 'Ŕ', 'ŕ', 'Ŗ', 'ŗ', 'Ř', 'ř', 'Ś', 'ś', 'Ŝ', 'ŝ', 'Ş', 'ş',
 'Š', 'š', 'Ţ', 'ţ', 'Ť', 'ť', 'Ŧ', 'ŧ', 'Ũ', 'ũ', 'Ū', 'ū', 'Ŭ', 'ŭ', 'Ů', 'ů',
 'Ű', 'ű', 'Ų', 'ų', 'Ŵ', 'ŵ', 'Ŷ', 'ŷ', 'Ÿ', 'Ź', 'ź', 'Ż', 'ż', 'Ž', 'ž', 'ſ']
```
You can merge two blocks to get instance of `Blocks` for easy manipulation.
```python
>>> unicodeblocks.blocks['basic latin'] + unicodeblocks.blocks['latin extended a']
Blocks(Block('Basic Latin', 0x0, 0x7f),Block('Latin Extended-A', 0x100, 0x17f))
```
You can also add a `Block` to a instance of `Blocks` in same way, so addition
is chainable.

## Notes

This module doesn't check for validity of characters that doesn't exist in a
middle of block. For example see `\u38D`. If you care about valid unicode
characters, you should try to obtain their name with `unicodedata` module.
