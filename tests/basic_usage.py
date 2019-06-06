from controlpyweb.single_io import AnalogIn, DiscreteOut
from controlpyweb.webio_module import WebIOModule


class AnalogIn(WebIOModule):
    ExcitationVoltage = AnalogIn("DC Exitation Voltage", "excitationvdc")
    NestPressure = AnalogIn("Nest Pressure", "nestpressurevdc")


class OutputModule(WebIOModule):
    NestValve = DiscreteOut("Nest Valve Pressure Ena", 'pressurevalve')


anaIn = AnalogIn("192.168.100.20")
out = OutputModule("192.168.100.30")

out.update_from_module()
anaIn.update_from_module()

print(anaIn.ExcitationVoltage)
print(anaIn.NestPressure)
print(out.NestValve)

out.NestValve = not out.NestValve

out.send_changes_to_module()
out.update_from_module()

print(out.NestValve)
