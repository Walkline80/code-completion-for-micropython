'''
SSL/TLS module

This module implements a subset of the corresponding CPython module, as described
below.

For more information, refer to the original CPython documentation: ssl.

This module provides access to Transport Layer Security (previously and widely
known as "Secure Sockets Layer") encryption and peer authentication facilities
for network sockets, both client-side and server-side.

[View Doc](https://docs.micropython.org/en/latest/library/ssl.html)
'''
# Constants
# Supported values for the `protocol`` parameter.
PROTOCOL_TLS_CLIENT: int = ...
PROTOCOL_TLS_SERVER: int = ...

# Supported values `for cert_reqs` parameter, and the `SSLContext.verify_mode`
# attribute.
CERT_NONE: int = ...
CERT_OPTIONAL: int = ...
CERT_REQUIRED: int = ...

# Functions
def wrap_socket(sock, server_side: bool = False, key=None, cert=None,
		cert_reqs: int = CERT_NONE, cadata=None, server_hostname=None, do_handshake: bool = True):
	'''
	Wrap the given sock and return a new wrapped-socket object.

	The implementation of this function is to first create an `SSLContext` and
	then call the `SSLContext.wrap_socket` method on that context object.

	The arguments `sock`, `server_side` and `server_hostname` are passed through
	unchanged to the method call.

	The argument `do_handshake` is passed through as `do_handshake_on_connect`.

	The remaining arguments have the following behaviour:

	- cert_reqs determines whether the peer (server or client) must present a
	valid certificate.

		Note that for mbedtls based ports, `ssl.CERT_NONE` and `ssl.CERT_OPTIONAL`
		will not validate any certificate, only `ssl.CERT_REQUIRED` will.

	- `cadata` is a bytes object containing the CA certificate chain (in DER format)
	that will validate the peer’s certificate.

	Currently only a single DER-encoded certificate is supported.

	Depending on the underlying module implementation in a particular MicroPython
	port, some or all keyword arguments above may be not supported.
	'''


class SSLContext(object):
	def __init__(self, protocol: int, /):
		'''
		Create a new SSLContext instance. The `protocol` argument must be one
		of the `PROTOCOL_*` constants.
		'''

	def load_cert_chain(self, certfile, keyfile):
		'''
		Load a private key and the corresponding certificate.

		The `certfile` is a string with the file path of the certificate.

		The `keyfile` is a string with the file path of the private key.

		Difference to CPython:

			MicroPython extension: `certfile` and `keyfile` can be bytes objects
			instead of strings, in which case they are interpreted as the actual
			certificate/key data.
		'''

	def load_verify_locations(self, cafile: str | None = None, cadata=None):
		'''
		Load the CA certificate chain that will validate the peer’s certificate.

		`cafile` is the file path of the CA certificates.

		`cadata` is a bytes object containing the CA certificates.

		Only one of these arguments should be provided.
		'''

	def get_ciphers(self):
		'''Get a list of enabled ciphers, returned as a list of strings.'''

	def set_ciphers(self, ciphers: list | str):
		'''
		Set the available ciphers for sockets created with this context.

		`ciphers` should be a list of strings in the `IANA cipher suite format`.
		'''

	def wrap_socket(self, sock, *, server_side: bool = False,
		do_handshake_on_connect: bool = True, server_hostname=None):
		'''
		Takes a `stream sock` (usually `socket.socket` instance of `SOCK_STREAM`
		type), and returns an instance of `ssl.SSLSocket`, wrapping the underlying
		stream.

		The returned object has the usual `stream` interface methods like `read()`,
		`write()`, etc.

		- `server_side` selects whether the wrapped socket is on the server or client side.

			A server-side SSL socket should be created from a normal socket
			returned from `accept()` on a non-SSL listening server socket.

		- `do_handshake_on_connect` determines whether the handshake is done as
		part of the `wrap_socket` or whether it is deferred to be done as part
		of the initial reads or writes For blocking sockets doing the handshake
		immediately is standard.

			For non-blocking sockets (i.e. when the sock passed into `wrap_socket`
			is in non-blocking mode) the handshake should generally be deferred
			because otherwise `wrap_socket` blocks until it completes.
	
			Note that in AXTLS the handshake can be deferred until the first read
			or write but it then blocks until completion.

		- `server_hostname` is for use as a client, and sets the hostname to check
		against the received server certificate.

			It also sets the name for Server Name Indication (SNI), allowing the
			server to present the proper certificate.
		'''

	@property
	def verify_mode(self) -> int:
		'''
		Set or get the behaviour for verification of peer certificates.

		Must be one of the `CERT_*` constants.

		Note:

			`ssl.CERT_REQUIRED` requires the device’s date/time to be properly
			set, e.g. using `mpremote rtc --set` or `ntptime`, and
			`server_hostname` must be specified when on the client side.
		'''

	@verify_mode.setter
	def verify_mode(self, value: int): ...
