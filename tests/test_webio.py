from controlpyweb.single_io import DiscreteIn, DiscreteOut
from controlpyweb.webio_module import WebIOModule
from assertpy import assert_that
import unittest
import json



incoming = """
    {
    "vin":"23.6",
    "register1":"0",
    "device1DigitalInput1":"1",
    "device1DigitalInput2":"0",
    "device1DigitalInput3":"0",
    "device1DigitalInput4":"0",
    "device1DigitalInput5":"0",
    "device1DigitalInput6":"0",
    "device1DigitalInput7":"0",
    "device1DigitalInput8":"0",
    "redLamp":"1",
    "amberLamp":"1",
    "greenLamp":"0",
    "flashLamp":"0",
    "allowStart":"0",
    "device2Relay6":"0",
    "device2Relay7":"0",
    "device2Relay8":"0",
    "utcTime":"1559533814",
    "timezoneOffset":"-25200",
    "serialNumber":"00:0C:C8:04:24:B2"
    }  
"""


class Module(WebIOModule):
    Button1 = DiscreteIn("Button1", "device1DigitalInput1")
    Button2 = DiscreteIn("Button2", "device1DigitalInput2")
    Button3 = DiscreteIn("Button3", "device1DigitalInput3")
    Lamp1 = DiscreteOut("Lamp1", "redLamp")
    Lamp2 = DiscreteOut("Lamp2", "amberLamp")

    def __init__(self, url: str):
        super().__init__(url)


module = Module("dummy url")


class TestWebIO(unittest.TestCase):

    def setUp(self):
        module.loads(incoming)
        self.incoming = json.loads(incoming)    # type: dict

    def test_can_read_common_properties(self):
        assert_that(module.serial_number).is_equal_to("00:0C:C8:04:24:B2")
        assert_that(module.vin).is_equal_to(23.6)
        assert_that(module.time_of_read.day).is_equal_to(2)

    def test_can_read_values(self):
        assert_that(module.Button1).is_true()
        assert_that(module.Button2).is_false()

    def test_can_write_values(self):
        module.Lamp1 = True
        assert_that(module.read("redLamp")).is_equal_to("1")
        module.Lamp1 = False
        assert_that(module.read("redLamp")).is_equal_to('0')

    def test_that_dumps_captures_changes(self):
        module.Lamp1 = True
        module.Lamp2 = True
        print(module.dumps())