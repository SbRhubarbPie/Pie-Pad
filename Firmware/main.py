import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.extensions.media_keys import MediaKeys

piepad = KMKKeyboard()

macros = Macros()
piepad.modules.append(macros)
piepad.extensions.append(MediaKeys())

PINS = [
    board.D7,   # SW1
    board.D8,   # SW2
    board.D9,   # SW3
    board.D10,  # SW4
    board.D2,   # SW5
    board.D1,   # SW6
    board.D0,   # SW7
    board.D5,   # encoder button
    board.D4,   # encoder A
    board.D3,   # encoder B
]

piepad.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

piepad.keymap = [
    [
        KC.UP, KC.LEFT, KC.DOWN, KC.RIGHT, KC.MPRV, KC.MPLY, KC.MNXT,
        KC.MUTE, KC.VOLD, KC.VOLU
    ]
]

if __name__ == '__main__':
        piepad.go()
