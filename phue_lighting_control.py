from phue import Bridge
import random
import time


# turn all lights in a zone to normal bright setting
def turn_on_group_bright(b, group_light_names, group_name):
    for l_name in group_light_names[group_name]:
        b.set_light(l_name, {'on' : True, 'transitiontime' : 5, 'bri' : 254, 'xy' : [0.459, 0.4103]})
        # print(f"{l_name} xy: {light_names[l_name].xy}")

# turn off lights in a group
def turn_off_group(b, group_light_names, group_name):
    for l_name in group_light_names[group_name]:
        b.set_light(l_name, {'on' : False})

def crazy_mode(b, group_light_names, group_name):
    try:
        while True:
            transition_time = 1
            color = [random.random(), random.random()]
            b.set_light(group_light_names["Party Zone"], {'on' : True, 'transitiontime' : transition_time, 'bri' : 254, 'xy' : color})
            time.sleep(transition_time/10)
    except KeyboardInterrupt:
        turn_on_group_bright(b, group_light_names, group_name)        
        # turn_on_group_bright(b, group_light_names, "Living Room")
    
def main():    
    b = Bridge('192.168.1.189')

    # uncomment this line to register the app (only needed once). press the physical bridge button and then run this.
    #b.connect()


    lights = b.lights
    groups = b.groups

    # get a dictionary mapping light names to light objects
    light_names = b.get_light_objects('name')

    # create a dictionary mapping group names to group objects
    group_names = {g.name: g for g in groups}

    # create a dictionary mapping group names to lists of light names
    group_light_names = {g.name: [l.name for l in g.lights] for g in groups}


    print("\nlight names:")
    for light_name in light_names:
        print(f" - {light_name}")

    print("\ngroup names:")
    for group_name in group_names:
        print(f" - {group_name}")
    print()

    turn_off_group(b, group_light_names, "Non-party Living Room")

    crazy_mode(b, group_light_names, "Party Zone")


if __name__ == "__main__":
    main()