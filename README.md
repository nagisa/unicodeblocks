# unicodeblocks – Character blocks defined in unicode

This module supplements `unicodedata` standard library module with ability
to lookup and work with unicode blocks.

## API

### unicodeblocks.version

Version of module.

### unicodeblocks.unidata_version

The version of Unicode database used in this module.

### unicodeblocks.Block(name, start, end)

#### unicodeblocks.Block.name

Normalized name of block.

#### unicodeblocks.Block.start

The first codepoint mapped by block. Inclusive.

#### unicodeblocks.Block.end

The last codepoint mapped by block. Inclusive.

#### unicodeblocks.Block.__contains__(self, chr)

Checks either character is in this block.

#### unicodeblocks.Block.__len__(self):

Count of codepoints mapped by Block.

#### unicodeblocks.Block.__lt__(self, other):

Checks if both other.start and other.end are lower than self.start and
self.end.

#### unicodeblocks.Block.__gt__(self, other):

Checks if both other.start and other.end are greater than self.start and
self.end.

#### unicodeblocks.Block.__eq__(self, other):

Checks if both other.start equals to self.start and other.end equals to
self.end.

### unicodeblocks.blockof(chr)

Will return a `Block` which maps the codepoint of chr or `None` in case not
block maps the codepoint.

### unicodeblocks.blocks

A dictionary-like collection of all blocks defined by Unicode.

#### unicodeblocks.blocks.names()

Returns a list of names of blocks in dictionary. Use this instead of .keys()
if you want names presentable to user.

## Notes

Module doesn't check for if characters are assigned within block.
For example see `\u38D`. If you care about validity of characters, you should
try to obtain their name with `unicodedata` module.
