"""
Bridge IP address is 192.168.1.189

Base URL: http://192.168.1.189/api/v1

Debug form accessible in browser: http://192.168.1.189/debug/clip.html

get ip and such: https://discovery.meethue.com/

To add a username
- go to xx
- URL: /api
- Message Body: {"devicetype":"nick#davidpc"}
- press bridge button, then click POST in the next 30 seconds
- username recieved: LImHWQImj1iO-HcOQAT6rEolcLaSvbhr62nAT-Ro

List all lights: /api/<username>/lights

Light 7 is hallway

Light controls
- off/on: /api/<username>/lights/7/state
    - message body: {"on":false}



colors:
- normal "bright": [0.459, 0.4103]

"""