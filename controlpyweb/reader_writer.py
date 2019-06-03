from controlpyweb.abstract_reader_writer import AbstractReaderWriter
import requests
import json
from typing import Union, Optional


class ReaderWriter(AbstractReaderWriter):

    def __init__(self, url: str):
        """
        :param url: The address of the IO Base module from/to which IO is written
        """
        self._url = f'https://{url}/customState.json'    # type: str
        self._io = dict()
        self._changes = dict()

    def _get(self):
        r = requests.get(self._url)
        r = None if r is None else r.json()
        return r

    def dumps(self):
        """Returns the current IO key/values as json string"""
        return json.dumps(self._io)

    def loads(self, json_str: str):
        """Replaces the current IO key/values with that from the json string"""
        self._io = json.loads(json_str)

    def read(self, addr: str) -> Optional[Union[bool, int, float, str]]:
        """Returns the value of a single IO from the memory store"""
        val = self._io.get(addr)
        return val

    def read_immediate(self, addr: str) -> object:
        """Makes a hardware call to the base module to retrieve the value of the IO"""
        vals = self._get()
        if vals is None:
            return None
        return vals.get(addr)

    def update_from_hardware(self):
        """Makes a hardware call to the base module to retrieve the value of all IOs, stores their
        results in memory."""
        vals = self._get()
        if vals is not None:
            self._io = vals

    def send_changes_to_hardware(self):
        """ Takes the collection of changes made using the write command and
        sends them all to the hardware collectively. """
        if self._changes is None:
            return self.read()
        r = requests.get(self._url, params=self._changes)
        r = None if r is None else r.json()
        return r

    def write(self, addr: str, value: object):
        if isinstance(value, bool):
            value = '1' if value else '0'
        self._io[addr] = value
        self._changes[addr] = value

    def write_immediate(self, addr: str, value: object):
        r = requests.get(self._url, params={addr, value})
        r = None if r is None else r.json()
        return r
