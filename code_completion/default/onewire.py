'''
OneWire driver for MicroPython

The OneWire driver is implemented in software and works on all pins.

[View OneWire Driver Doc](https://docs.micropython.org/en/latest/esp32/quickref.html#onewire-driver)
[View onewire.py](https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/bus/onewire/onewire.py)
'''
class OneWireError(Exception): ...


class OneWire(object):
	SEARCH_ROM: int = ...
	MATCH_ROM: int = ...
	SKIP_ROM: int = ...

	def __init__(self, pin): ...

	def reset(self, required: bool = False):
		'''Reset the bus.'''

	def readbit(self):
		'''Read a bit.'''

	def readbyte(self) -> bytes:
		'''Read a byte.'''

	def readinto(self, buf): ...

	def writebit(self, value):
		'''Write a bit on the bus.'''

	def writebyte(self, value):
		'''Write a byte on the bus.'''

	def write(self, buf):
		'''Write bytes on the bus.'''

	def select_rom(self, rom):
		'''Select a specific device by its ROM code.'''

	def scan(self) -> list:
		'''Return a list of devices on the bus.'''

	def crc8(self, data): ...
