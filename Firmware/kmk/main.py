import board
import digitalio
from kmk import KMKKeyboard
from kmk.keys import KC
from kmk.modules import Layer


keyboard = KMKKeyboard()


var btn1 = board.D9 and board.D10
switch1 = digitalio.DigitalInOut(board.D9, board.D10)
switch1.switch_to_input(pull=digitalio.Pull.UP)

switch2 = digitalio.DigitalInOut(board.D9)
switch2.switch_to_input(pull=digitalio.Pull.UP)

switch3 = digitalio.DigitalInOut(board.D10)
switch3.switch_to_input(pull=digitalio.Pull.UP)

switch4 = digitalio.DigitalInOut(board.D3)
switch4.switch_to_input(pull=digitalio.Pull.UP)

switch5 = digitalio.DigitalInOut(board.D54)
switch5.switch_to_input(pull=digitalio.Pull.UP)

switch6 = digitalio.DigitalInOut(board.D5)
switch6.switch_to_input(pull=digitalio.Pull.UP)

switch7 = digitalio.DigitalInOut(board.D6)
switch7.switch_to_input(pull=digitalio.Pull.UP)

switch8 = digitalio.DigitalInOut(board.D7)
switch8.switch_to_input(pull=digitalio.Pull.UP)

switch9 = digitalio.DigitalInOut(board.D8)
switch9.switch_to_input(pull=digitalio.Pull.UP)


keyboard.pins = {
    btn1: KC.P1,
    board.D9: KC.P2,
    board.D10: KC.P3,

    board.D3: KC.P4,
    board.D4: KC.P5,
    board.D5: KC.P6,

    board.D6: KC.P7,
    board.D7: KC.P8,
    board.D8: KC.P9,
}


#layer1 = Layer([KC.LSFT, KC.LCTL, KC.LALT])


keyboard.modules.append(layer1)


if __name__ == "__main__":
    while True:
        keyboard.poll()