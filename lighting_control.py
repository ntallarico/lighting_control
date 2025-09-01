import logging
from hue_entertainment_pykit import setup_logs, Discovery, create_bridge, Entertainment, Streaming
import time


# initialize logging, exclude DEBUG messages
setup_logs(level=logging.INFO)


# discovery = Discovery()
# # returns dict[str, Bridge] where the key is name of the bridge and value is the Bridge model with all important info for connecting to Entertainment API
# bridges = discovery.discover_bridges()


# set up the Bridge instance
bridge = create_bridge(
    identification="770fb9d5-e914-439e-9e11-4871fd2cc9be",
    rid="b6fbbc5c-4522-4aa6-a25b-5b1ce5b5d3f4",
    ip_address="192.168.1.189",
    swversion=1972076030,
    username="s-t-m7NrhEqmscS4xaEwz4FJoDovlhnGZ6wU7817",
    hue_app_id="91371714-b11e-4837-9574-a3c37589a7b7",
    clientkey="A860EE4432070DA799B5FFF87F367A25",
    name="Hue Bridge"
)

# set up streaming
entertainment_service = Entertainment(bridge) # set up the Entertainment API service
entertainment_configs = entertainment_service.get_entertainment_configs() # fetch all Entertainment Configurations on the Hue bridge
entertainment_config = list(entertainment_configs.values())[0] # select first entertainment config (living room party zone)
streaming = Streaming(bridge, entertainment_config, entertainment_service.get_ent_conf_repo()) # set up the Streaming service

# start streaming session and inital config
streaming.start_stream() # start streaming session
streaming.set_color_space("xyb") # set the color space to xyb


# dictionary of light names mapped to id inside entertainment area
lights = {
    "Living Room - Fan - 2"               : 0
    , "Living Room - Fan - 3"             : 1
    , "Living Room - Wall - Right"        : 2
    , "Living Room - Wall - Left"         : 3
    , "Living Room - Fan - 1"             : 4
    , "Living Room - Chandelier - Left"   : 5
    , "Living Room - Chandelier - Right"  : 6
    , "Laundry Hallway"                   : 7
}


# # user chooses light number to activate
# try:
#     while True:
#         lightnum = int(input("enter light number\n"))
#         # values are x, y, brightness, light ID (inside the entertainment area)
#         streaming.set_input((0.0, 0.63435, 1, lightnum))
#         streaming.set_input((0.0, 0.63435, 1, lightnum))
#         streaming.set_input((0.0, 0.63435, 1, lightnum))
#         time.sleep(2)
#         streaming.set_input((0.459, 0.4103, 1, lightnum))
#         streaming.set_input((0.459, 0.4103, 1, lightnum))
#         streaming.set_input((0.459, 0.4103, 1, lightnum))
# except KeyboardInterrupt:
#     # stop stream
#     print("stopping stream")
#     time.sleep(0.1) # sleep briefly to ensure all inputs processed before we stop the stream
#     streaming.stop_stream() # stop streaming session

# do stuff
delay = 0.1
try:
    while True:
        for light in lights:
            streaming.set_input((0.0, 0.63435, 1, lights[light]))
        time.sleep(delay)
        for light in lights:
            streaming.set_input((0.0, 0.63435, 0, lights[light]))
            # streaming.set_input((0.459, 0.4103, 1, lights[light]))
        time.sleep(delay)
except:
    # stop stream
    print("stopping stream")
    time.sleep(0.1) # sleep briefly to ensure all inputs processed before we stop the stream
    streaming.stop_stream() # stop streaming session