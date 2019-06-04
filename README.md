# ControlPyWeb
A project to facilitate easy read/write to the ControlByWeb line of Automation/SCADA IO products. 


#### Installation Instructions
pip install controlpyweb


## Usage
The basis of functionality is the WebIOModule class. It both acts as a container for individual
IO and handles interraction with the actual hardware. 

Whe WebIOModule class is meant to be inherited and populated with various IO types. 