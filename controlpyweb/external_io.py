import gettext
from controlpyweb.webio_module import WebIOModule
from controlpyweb.single_io import DiscreteIn, DiscreteOut
from assertpy import assert_that

_ = gettext.gettext

"""
"bowl2Gate":"0",
"spare5":"0",
"robotHasPin":"0",
"vacRangeError":"0",
"p1GateOpen":"0",
"p1GateClosed":"0",
"p2GateOpen":"0",
"p2GateClosed":"0",
"pin2OpenClose":"1",
"cnctrOpenClose":"0",
"bowl1Gate":"0",
"p1PinPresent":"1",
"p2PinPresent":"0",
"vaccuumOn":"0",
"utcTime":"11145724",
"timezoneOffset":"-25200",
"serialNumber":"00:0C:C8:04:52:3F"
} 
"""


class ExternalIO(WebIOModule):
    Pin1CCW = DiscreteOut(_("P1: CCW"), "pin1MovetoGrab")
    Pin1CW = DiscreteOut(_("P1: CW"), "pin1MovetoPick")
    Pin2CCW = DiscreteOut(_("P2: CCW"), "pin2MovetoGrab")
    Pin2CW = DiscreteOut(_("P2: CW"), "pin2MovetoPick")
    ConnectorCW = DiscreteOut(_("Connector: CW"), "cnctrMovetoGrab")
    ConnectorCCW = DiscreteOut(_("Connector: CCW"), "cnctrMovetoPlace")
    Bowl1AirAssist = DiscreteOut(_("Bowl1: Air Assist"), "bowl1AirAssist")
    Bowl2AirAssist = DiscreteOut(_("Bowl2: Air Assist"), "bowl2AirAssist")
    Pin1Push = DiscreteOut(_("P1: Push"), "pin1PushPin")
    Pin2Push = DiscreteOut(_("P2: Push"), "pin2PushPin")
    Pin1Eject = DiscreteOut(_("P1_Eject"), "pin1EjectPin")
    Pin2Eject = DiscreteOut(_("P2_Eject"), "pin2EjectPin")
    Pin1OpenCollet = DiscreteOut(_("P1: Open Colet"), "pin1OpenCollet")
    Pin2OpenCollet = DiscreteOut(_("P2: Open Colet"), "pin2OpenCollet")
    Bowl1OpenGate = DiscreteOut(_("P1: Open Gate"), "bowl1OpenGate")
    Bowl2OpenGate = DiscreteOut(_("P2: Open Gate"), "bowl2OpenGate")
    EnableVacuum = DiscreteOut(_("Enable Vacuum"), "enableVacuum")
    ConnectorOpenGrips = DiscreteOut(_("Connector: Open Grips"), 'cnctrOpenGrips')
    
    Pin1Present = DiscreteIn(_("P1: Is Present"), 'pin1IsPresent')
    Pin2Present = DiscreteIn(_("P2: Is Present"), 'pin2IsPresent')
    VacuumLow = DiscreteIn(_("Vacuum Low"), "vacuumLow")
    VacuumLowLow = DiscreteIn(_("Vacuum Low Low"), "vacuumLowLow")

    @property
    def vacuum_is_on(self):
        return not self.VacuumLowLow

    @property
    def hector_has_pin(self):
        return self.vacuum_is_on and not self.VacuumLow

    def p1_move_to_grab(self):
        self.Pin1CCW = True
        self.Pin1CW = False

    def p1_move_to_center(self):
        self.Pin1CCW = True
        self.Pin1CW = True

    def p1_move_to_pick(self):
        self.Pin1CCW = False
        self.Pin1CW = True

    def p2_move_to_grab(self):
        self.Pin2CCW = True
        self.Pin2CW = False

    def p2_move_to_center(self):
        self.Pin2CCW = True
        self.Pin2CW = True

    def p2_move_to_pick(self):
        self.Pin2CCW = False
        self.Pin2CW = True

    def connector_move_to_place(self):
        self.ConnectorCW = True
        self.ConnectorCCW = False

    def connector_move_to_center(self):
        self.ConnectorCW = True
        self.ConnectorCCW = True

    def connector_move_to_grab(self):
        self.ConnectorCW = False
        self.ConnectorCCW = True


if __name__ == '__main__':
    external = ExternalIO("192.168.100.121")
    external.update_from_module()
    all_members = [d for d in dir(external) if not d.startswith('__')]
    for member in all_members:
        attr = getattr(external, member)
        if not isinstance(attr, DiscreteIn):
            continue
        print(attr)

    assert_that(external.Pin1OpenCollet).is_not_equal_to(external.Pin1Push)
    assert_that(external.Pin1OpenCollet).is_equal_to(external.Pin1Present)
