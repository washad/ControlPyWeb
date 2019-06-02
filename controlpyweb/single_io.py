from controlpyweb.abstract_reader import ReaderWriter
import threading
from controlpyweb.errors import IOReadOnlyException

lock = threading.Lock()


class SingleIO:
    def __init__(self, name: str, addr: str, default: object, reader: ReaderWriter):
        self.name = name
        self.addr = addr
        self._reader_writer = reader
        self._value = default

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __get__(self, instance, owner):
        self.read()
        return self

    def __set__(self, obj, value):
        raise IOReadOnlyException

    def __str__(self):
        return f'{type(self).__name__}: {self.name} = {self.value}'

    @property
    def value(self):
        return self._convert_type(self._value)

    @staticmethod
    def _convert_type(value):
        return value

    def read(self):
        with lock:
            val = self._reader_writer.read(self.addr, self.name)
            self._value = val
            return val

    def read_immediate(self):
        with lock:
            val = self._reader_writer.read_immediate(self.addr, self.name)
            self._value = val
            return val


class DiscreteIn(SingleIO):
    def __init__(self, name: str, addr: str, default: bool, reader: ReaderWriter):
        super().__init__(name, addr, default, reader)

    @staticmethod
    def _convert_type(value):
        return bool(value)

    def __bool__(self):
        return self.value


class IOOut(DiscreteIn):
    def __init__(self, name: str, addr: str, default: bool, writer: ReaderWriter):
        super().__init__(name, addr, default, writer)

    def __set__(self, instance, value):
        self.write(value)

    def write(self, value):
        self._reader_writer.write(self.name, self.addr, self._convert_type(value))
        self._value = value

    def write_immediate(self, value):
        self._reader_writer.write_immediate(self.name, self.addr, self._convert_type(value))
        self._value = value


class DiscreteOut(IOOut, DiscreteIn):
    def __init__(self, name: str, addr: str, default: bool, writer: ReaderWriter):
        super().__init__(name, addr, default, writer)


