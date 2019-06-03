

class ControlPyWebReadOnlyError(Exception):
    def __init__(self):
        super().__init__("The ControlPyWeb type cannot be set, it is read only!")
