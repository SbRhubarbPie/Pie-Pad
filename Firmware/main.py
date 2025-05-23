# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys

# This is the main instance of your keyboard
piepad = KMKKeyboard()

# Add the macro extension
macros = Macros()
piepad.modules.append(macros)
piepad.extensions.append(MediaKeys())

# Define your pins here!
PINS = [board.D28, board.D27, board.D26, board.D1, board.D2, board.D4, board.D3]

# Tell kmk we are not using a key matrix
piepad.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
piepad.keymap = [
    [KC.MPRV, KC.MPLY, KC.MNXT, KC.UP, KC.LEFT, KC.DOWN, KC.RIGHT]
]

# Start kmk!
if __name__ == '__main__':
    piepad.go()