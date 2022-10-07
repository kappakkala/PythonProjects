# MicroPython with ESP8266


## Prerequisites

### 1. Install esptool

`pip install esptool`

### 2. Download latest firmware from https://micropython.org/download/esp8266/ and move it to project directory

### 3. Erase flash memory

Before flashing the MicroPython firmware, you need to erase the ESP8266 flash memory. So, with your ESP8266 connected to your computer, hold-down the “BOOT/FLASH” button in your ESP8266 board.

![Query selection1 flash_button](./images/01_esp8266_flash.png?raw=true "flash_button")

While holding down the “BOOT/FLASH” button, run the following command to erase the ESP8266 flash memory: `python -m esptool --chip esp8266 erase_flash`

When the “Erasing” process begins, you can release the “BOOT/FLASH” button. After a few seconds, the ESP8266 flash memory will be erased.

![Query selection1 flash_button](./images/02_erase_flash.png?raw=true "erase_flash")

### 4. Flashing the firmware

Hold down the “BOOT/FLASH“ and run `python -m esptool --chip esp8266 --port COM8 write_flash --flash_mode dio --flash_size detect 0x0 esp8266-20220618-v1.19.1.bin` 

![Query selection1 firmware_flashing](./images/03_firmware_flashing.png?raw=true "firmware_flashing")



References: https://randomnerdtutorials.com/flashing-micropython-firmware-esptool-py-esp32-esp8266/
