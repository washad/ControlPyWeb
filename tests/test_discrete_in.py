import unittest
from unittest.mock import MagicMock

from assertpy import assert_that

from controlpyweb.single_io import SingleIO, DiscreteIn


class Container:
    single_io1 = SingleIO(name="SIO1", addr="0.1", default="Hello", reader=MagicMock())
    single_io2 = SingleIO(name="SIO2", addr="0.2", default="Hello", reader=MagicMock())
    discrete_in_1 = DiscreteIn(name="DiscreteIn1", addr="0.2", default=False, reader=MagicMock())
    discrete_in_2 = DiscreteIn(name="DiscreteIn2", addr='0.3', default=True, reader=MagicMock())


class TestDiscreteIn(unittest.TestCase):

    def setUp(self):
        self.container = Container()
        self.reader1_read_method = MagicMock()
        self.reader2_read_method = MagicMock()
        self.container.single_io1._reader_writer.read = self.reader1_read_method
        self.container.single_io2._reader_writer.read = self.reader2_read_method

    def test_equality(self):
        container = self.container
        container.discrete_in_1 = False
        container.discrete_in_1 = True
        assert_that(container.discrete_in_1.leading_edge).is_true()
        assert_that(container.discrete_in_1.leading_edge).is_false()