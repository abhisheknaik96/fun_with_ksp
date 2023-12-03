"""A simple tutorial to test the kRPC API"""

import time
import krpc

# create a connection to the KSP game
conn = krpc.connect(name="SampleConnection")

vessel = conn.space_center.active_vessel
vessel.control.sas = False
vessel.control.rcs = False

# set up streams for telemetry
roll = conn.add_stream(getattr, vessel.flight(), "roll")
pitch = conn.add_stream(getattr, vessel.flight(), "pitch")
heading = conn.add_stream(getattr, vessel.flight(), "heading")

# these actions will start rolling the craft 
for i in range(10):
    print(f"Current roll: {roll():.3f}, pitch: {pitch():.3f}, heading: {heading():.3f}")

    action = [1, 0, 0]
    print(f"Taking action: {action}")

    vessel.control.roll = action[0]
    vessel.control.pitch = action[1]
    vessel.control.yaw = action[2]

    time.sleep(0.5)
