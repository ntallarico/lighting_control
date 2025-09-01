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
b.set_light(7, 'xy', [random.random(), random.random()])
# b.set_light(7, 'xy', [1, 1])

# change brightness
b.set_light(7, 'bri', 254)
