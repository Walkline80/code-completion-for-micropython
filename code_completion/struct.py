'''
pack and unpack primitive data types

This module implements a subset of the corresponding CPython module, as described below.

For more information, refer to the original CPython documentation: struct.
'''
# Docs: https://docs.micropython.org/en/latest/library/struct.html

# Functions
def calcsize(fmt: str) -> int:
	'''Return the number of bytes needed to store the given `fmt`.'''

def pack(fmt: str, v1, v2) -> bytes:
	'''
	Pack the values `v1`, `v2`, `…` according to the format string `fmt`.

	The return value is a bytes object encoding the values.
	'''

def pack_into(fmt: str, buffer, offset: int, v1, v2):
	'''
	Pack the values `v1`, `v2`, `…` according to the format string `fmt` into a `buffer` starting at `offset`.

	`offset` may be negative to count from the end of `buffer`.
	'''

def unpack(fmt: str, data) -> tuple:
	'''
	Unpack from the `data` according to the format string `fmt`.

	The return value is a tuple of the unpacked values.
	'''

def unpack_from(fmt: str, data, offset: int = 0, /) -> tuple:
	'''
	Unpack from the `data` starting at `offset` according to the format string `fmt`.

	`offset` may be negative to count from the end of data.

	The return value is a tuple of the unpacked values.
	'''
