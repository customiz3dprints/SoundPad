from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.scanners.keypad import KeysScanner
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions import Extension
import adafruit_ssd1306
import board


class OLEDLayerDisplay(Extension):
    def __init__(self, display):
        self.display = display
        self.last_layer = -1

        self.display.fill(0)
        self.display.show()
        self.display = display
        self.last_layer = -1

    def after_matrix_scan(self, keyboard):
        layer = keyboard.active_layers[0]

        if layer != self.last_layer:
            self.last_layer = layer

            self.display.fill(0)
            self.display.text(["MEDIA", "OTHER"][layer], 0, 16, 1)
            self.display.show()
keyboard = KMKKeyboard()
layers = Layers()
encoder = EncoderHandler()
I2C_obj = board.I2C()
display = adafruit_ssd1306.SSD1306_I2C(
    128,
    32,
    I2C_obj
)
keyboard.extensions.append(OLEDLayerDisplay(display))
encoder.pins(board.D1, board.D0, None)
keyboard.modules.append(encoder)
keyboard.modules.append(layers)
keyboard.extensions.append(MediaKeys())
keyboard.matrix = [
    KeysScanner(
        pins=(board.D7,
              board.D8,
              board.D9,
              board.D10)
    )
]

keyboard.keymap = [
    [
        KC.MPRV,
        KC.MPLY,
        KC.MPNXT,
        KC.TO(1)
    ],
    [
        KC.F13,
        KC.F14,
        KC.F15,
        KC.TO(0)
    ]
]

encoder.map[
    ((KC.VOLD, KC.VOLU),),
    ]

if __name__ == "__main__":
    keyboard.go()