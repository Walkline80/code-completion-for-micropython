'''
binary/ASCII conversions

This module implements a subset of the corresponding `CPython` module, as described
below.

For more information, refer to the original `CPython` documentation: [binascii](https://docs.python.org/3.5/library/binascii.html#module-binascii).

This module implements conversions between binary data and various encodings of
it in ASCII form (in both directions).

[View Doc](https://docs.micropython.org/en/latest/library/binascii.html)
'''
# Functions
def hexlify(data, sep=None) -> bytes:
	'''
	Convert the bytes in the `data` object to a hexadecimal representation.

	Returns a bytes object.

	If the additional argument `sep` is supplied it is used as a separator
	between hexadecimal values.
	'''

def unhexlify(data) -> bytes:
	'''
	Convert hexadecimal `data` to binary representation.

	Returns bytes string.

	(i.e. inverse of hexlify)
	'''

def a2b_base64(data) -> bytes:
	'''
	Decode base64-encoded `data`, ignoring invalid characters in the input.

	Conforms to [RFC 2045 s.6.8](https://tools.ietf.org/html/rfc2045#section-6.8).

	Returns a bytes object.
	'''

def b2a_base64(data, *, newline=True) -> bytes:
	'''
	Encode binary `data` in base64 format, as in [RFC 3548](https://tools.ietf.org/html/rfc3548.html).

	Returns the encoded data followed by a newline character if `newline` is
	`True`, as a bytes object.
	'''
