from kmk_firmware.kmk.kmk_keyboard import KMKKeyboard
from kmk_firmware.kmk.keys import KC
from kmk_firmware.kmk.scanners.keypad import KeysScanner
import board

keyboard = KMKKeyboard()

keyboard.matrix = [
    KeysScanner(
        pins=(board.D8,
              board.D9,
              board.D10,
              board.D11,)
    )
]