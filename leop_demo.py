"""A simple LEOP demonstration for a simulated satellite in KSP.

Before running this script:
1. Load the 'sandbox' saved game in KSP
2. Load the 'CubeSat 3' vessel which is in a 87 km circular orbit around Kerbin.
3. Retract the antennas and solar panels.
4. Make the satellite tumble using the Q/W/A keys.
"""

import time
import krpc

### create a connection to the KSP game
conn = krpc.connect(name="SampleConnection")

vessel = conn.space_center.active_vessel
vessel.control.sas = False
vessel.control.rcs = False

### set up streams for telemetry
roll = conn.add_stream(getattr, vessel.flight(), "roll")
pitch = conn.add_stream(getattr, vessel.flight(), "pitch")
heading = conn.add_stream(getattr, vessel.flight(), "heading")

### first, detumble the satellite
conn.ui.message("Initiating detumbling sequence")
vessel.control.sas = True
# ToDo: use the telemetry to determine when the satellite is detumbled
time.sleep(15)
conn.ui.message("Detumbling successful")
time.sleep(2)

### next, deploy the antennas and solar panels
conn.ui.message("Deploying antennas")
time.sleep(2)
vessel.parts.antennas[1].deployed = True
time.sleep(2)
vessel.parts.antennas[2].deployed = True
time.sleep(2)
conn.ui.message("Antenna deployment successful")
time.sleep(5)
conn.ui.message("Deploying solar panels")
time.sleep(2)
vessel.parts.solar_panels[0].deployed = True
time.sleep(2)
vessel.parts.solar_panels[1].deployed = True
time.sleep(5)
conn.ui.message("Solar panel deployment successful")
time.sleep(2)

### now point in the right direction
conn.ui.message("Initiating pointing sequence towards Kerbin")
time.sleep(2)
ap = vessel.auto_pilot
ap.reference_frame = vessel.orbital_reference_frame
ap.engage()
ap.target_direction = (-1, 0, 0)
ap.wait()
time.sleep(2)
conn.ui.message("Successfully pointing towards Kerbin")
# ap.disengage()
