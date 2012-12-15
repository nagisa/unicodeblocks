# -*- coding: utf-8 -*-
# Copyright (c) 2012, Simonas Kazlauskas

# Permission to use, copy,  modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
# OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.
from __future__ import unicode_literals
import collections
import itertools
from unicodeblocks import _blocklist

whitespace = [
    0x9, 0xA, 0xB, 0xC, 0xD, 0x20, 0x85, 0xA0, 0x1680, 0x180E, 0x2000,
    0x2001, 0x2002, 0x2003, 0x2004, 0x2005, 0x2006, 0x2007, 0x2008, 0x2009,
    0x200A, 0x2028, 0x2029, 0x202F, 0x205F, 0x3000
]

class Block(object):
    def __init__(self, name, start, end, *args, **kwargs):
        super(Block, self).__init__(*args, **kwargs)
        self.start = int(start)
        self.end = int(end)
        self.name = str(name)

    def __repr__(self):
        return "Block('{0.name}', {0.start:#x}, {0.end:#x})".format(self)

    def __contains__(self, item):
        return self.start <= ord(item) <= self.end

    def __len__(self):
        # Need to add one, because codepoints are inclusive.
        return self.end - self.start + 1

    def __iter__(self):
        return map(chr, range(self.start, self.end + 1)).__iter__()

    def __lt__(self, other):
        if not hasattr(other, 'start') or not hasattr(other, 'end'):
            return NotImplemented
        return self.start < other.start and self.end < other.end

    def __eq__(self, other):
        if not hasattr(other, 'start') or not hasattr(other, 'end'):
            return NotImplemented
        return self.start == other.start and self.end == other.end

    def __gt__(self, other):
        if not hasattr(other, 'start') or not hasattr(other, 'end'):
            return NotImplemented
        return self.start > other.start and self.end > other.end


class Blocks(collections.OrderedDict):
    """A dictionary-like object collection of blocks"""
    def __init__(self, *args):
        super(Blocks, self).__init__()
        setitem = collections.OrderedDict.__setitem__
        for block in sorted(args):
            self[block.name] = block

    def __getitem__(self, key):
        return super(Blocks, self).__getitem__(self._normalize_name(key))

    def __setitem__(self, key, val):
        return super(Blocks, self).__setitem__(self._normalize_name(key), val)

    def __repr__(self):
        args = ', '.join(map(repr, self.values()))
        return "Blocks({0})".format(args)

    def _normalize_name(self, name):
        """
        Will convert name to a string with ignored characters removed.

        As per specification:
        When comparing block names, casing, whitespace, hyphens, and underbars
        are ignored.
        """
        return name.lower().translate(self._normalize_name.ignore)
    _normalize_name.ignore = {k: None for k in whitespace + [45, 95]}

    def names(self):
        """
        Returns a list of names in dictionary. Use this instead of .keys()
        if you need names presentable to user.
        """
        return (block.name for block in self.values())


def blockof(char):
    for block in blocks.values():
        if char in block:
            return block


def _expanded_args(func):
    def wrap(args=None, kwargs=None):
        return func(*(args or []), **(kwargs or {}))
    return wrap

# Oh, this code is the cutest one, I've ever written.
blocks = _expanded_args(Blocks)(map(_expanded_args(Block), _blocklist.blocks))
