import logging
from hue_entertainment_pykit import setup_logs, Discovery, create_bridge, Entertainment, Streaming
import time

# Initialize default logging
setup_logs()
# setup_logs(level=logging.INFO) # alternatively customize the logging level (e.g., exclude DEBUG messages)
# setup_logs(level=logging.INFO, max_file_size=1024 * 1024, backup_count=1) # You can also further customize logging by specifying the maximum log file size and the number of backup files


# discovery = Discovery()

# returns dict[str, Bridge] where the key is name of the bridge and value is the Bridge model with all important info for connecting to Entertainment API
# bridges = discovery.discover_bridges()


# Set up the Bridge instance with the all needed configuration
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


# Set up the Entertainment API service
entertainment_service = Entertainment(bridge)

# Fetch all Entertainment Configurations on the Hue bridge
entertainment_configs = entertainment_service.get_entertainment_configs()

# # Add some Entertainment Area selection logic
# # For the purposes of example I'm going to do manual selection
entertainment_config = list(entertainment_configs.values())[0]

# Set up the Streaming service
streaming = Streaming(
    bridge, entertainment_config, entertainment_service.get_ent_conf_repo()
)

# Start streaming messages to the bridge
streaming.start_stream()

# Set the color space to xyb or rgb
streaming.set_color_space("xyb")

# values are x, y, brightness, light ID (inside the entertainment area)
streaming.set_input((0.0, 0.63435, 0.3, 0))  # Light command for the first light
streaming.set_input((0.63435, 0.0, 0.3, 1))  # Light command for the second light
# ... Add more inputs as needed for additional lights and logic

# For the purpose of example sleep is used for all inputs to process before stop_stream is called
# Inputs are set inside Event queue meaning they're on another thread so user can interact with application continuously
time.sleep(0.1)

# Stop the streaming session
streaming.stop_stream()