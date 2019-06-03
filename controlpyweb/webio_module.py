from controlpyweb.reader_writer import ReaderWriter
import datetime


class WebIOModule(ReaderWriter):

    def __init__(self, url: str):
        super().__init__(url)
        members = [d for d in dir(self) if not d.startswith('__')]
        for member in members:
            try:
                attr = getattr(self, member)
                attr._reader_writer = self
            except AttributeError:
                pass

    @property
    def serial_number(self) -> str:
        return self.read("serialNumber")

    @property
    def vin(self) -> float:
        response = self.read("vin")
        if response is None:
            return -1
        return float(response)

    @property
    def time_of_read(self):
        response = self.read("utcTime")
        if response is None:
            return datetime.datetime.min
        return datetime.datetime.fromtimestamp(int(response))




