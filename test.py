from phue import Bridge
import random
import time

# https://github.com/studioimaginaire/phue

b = Bridge('192.168.1.189')

# uncomment this line to register the app (only needed once). press the physical bridge button and then run this.
#b.connect()

# turn he light off and on
# b.set_light(7, 'on', False)
# time.sleep(1)
# b.set_light(7, 'on', True)



# change the light color
# b.set_light(1, 'xy', [random.random(), random.random()])
# b.set_light(7, 'xy', [1, 1])

# change brightness
# b.set_light(1, 'bri', 254)



lights = b.lights


# print list of lights with all info
# for l in lights:
#     attrs = [
#         "name", "light_id", "type", "brightness", "colormode", "colortemp", "colortemp_k",
#         "effect", "hue", "on", "reachable", "saturation", "transitiontime", "xy", "alert", "bridge"
#     ]
#     for attr in attrs:
#         try:
#             value = getattr(l, attr)
#             print(f"{attr}: {value}")
#         except Exception as e:
#             print(f"{attr}: Not available for this light type")
#     # print(f"Light object dir: {dir(l)}") # prints full list of attributes
#     print("---\n")


# print list of lights with abbreviated info
for l in lights:
    print(f"light_id: {l.light_id}, name: {l.name}")


groups = b.groups

# print list of groups with light ids
for g in groups:
    light_ids = [l.light_id for l in g.lights]
    print(f"group_id: {g.group_id}, name: {g.name}, lights: {light_ids}")



# Set brightness of each light to 127
# for l in lights:
#     l.brightness = 127







# lights = b.lights
# groups = b.groups

# print list of lights with abbreviated info
# for l in lights:
#     print(f"light_id: {l.light_id}, name: {l.name}")

# print list of groups with light ids
# for g in groups:
#     light_ids = [l.light_id for l in g.lights]
#     print(f"group_id: {g.group_id}, name: {g.name}, lights: {light_ids}")



# print list of schedules
# print(b.get_schedule())




# for light_name in light_names:
#     print(light_name)
#     # light_names[light_name].on = True
#     # b.set_light(light_name, 'on', True) # this also works
#     b.set_light(light_name, {'on' : True, 'transitiontime' : 10, 'bri' : 254})



