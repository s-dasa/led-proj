pin = {"red": 27, "green": 22, "blue": 17, "white": 10}
values = {"white":[255, 255, 255], "red": [255, 0, 0], "orange":[255, 127, 0], "yellow":[255, 255, 0], "green":[0, 255, 0], "blue":[0, 0, 255], "indigo":[39, 9, 5], "violet":[139, 0, 255]}
def getValue(color):
    return values[color]
