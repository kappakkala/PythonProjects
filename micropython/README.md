# MicroPython with ESP8266


## 1. Prerequisites

### 1. Software Requirements

Install esptool using `pip install esptool`

Download latest firmware from https://micropython.org/download/esp8266/ and move it to project directory

Install the pymakr extension in visual studio code. 
### 2. Hardware Requirements 

#### Option 1 : Command Line Interface
**a. Erase flash memory**

Before flashing the MicroPython firmware, you need to erase the ESP8266 flash memory. So, with your ESP8266 connected to your computer, hold-down the “BOOT/FLASH” button in your ESP8266 board.

![Query selection1 flash_button](./images/01_esp8266_flash.png?raw=true "flash_button")

While holding down the “BOOT/FLASH” button, run the following command to erase the ESP8266 flash memory:

`python -m esptool --chip esp8266 erase_flash`

When the “Erasing” process begins, you can release the “BOOT/FLASH” button. After a few seconds, the ESP8266 flash memory will be erased.

![Query selection1 flash_button](./images/02_erase_flash.png?raw=true "erase_flash")

**b. Flash the firmware**

Hold down the “BOOT/FLASH“ and run 

`python -m esptool --chip esp8266 --port COM8 write_flash --flash_mode dio --flash_size detect 0x0 esp8266-20220618-v1.19.1.bin` 

The terminal displays the following

![Query selection1 firmware_flashing](./images/03_firmware_flashing.png?raw=true "firmware_flashing")


Source: https://randomnerdtutorials.com/flashing-micropython-firmware-esptool-py-esp32-esp8266/

#### Option 2 : Thonny IDE

Alternatively, it is possible to erase and flash the firmware using Thonny IDE. In this case, there is no need for holding down the “BOOT/FLASH“ button.

Go to **Tools** > **Options** and select the **Interpreter** tab. Make sure you’ve selected the right interpreter for your board as well as the COM port.

![Query selection1 thonny_init](./images/13_thonny_init.png?raw=true "thonny_init")

Click on **Install or update MicroPython**.

![Query selection1 thonny_init2](./images/14_thonny_init2.png?raw=true "thonny_init2")

After selecting the correct Port and the downloaded firmware, click on **Install**.

Once installed, click on **Close** followed by **OK**.

![Query selection1 thonny_init3](./images/15_thonny_init3.png?raw=true "thonny_init3")

Source: https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/

## 2. Running a project

### 1. Create a project

Create a new pymakr project inside the parent directory.

![Query selection1 new_project](./images/04_pymakr_new_project.png?raw=true "new_project")

Enter the project name

![Query selection1 project_name](./images/05_project_name.png?raw=true "project_name")

Select the path *parent_dir/project_name*

![Query selection1 path_select](./images/06_path_select.png?raw=true "path_select")

Select empty template

![Query selection1 empty_template](./images/07_empty_template.png?raw=true "empty_template")

Select COM Port and click OK

![Query selection1 com_port](./images/08_com_port.png?raw=true "com_port")

### 2. Edit *main.py*

Go to the newly created project folder and edit main.py

**[Option 1 - Pymakr]**
### 3. Connect device

Click on the Pymakr extension and connect the device to the selected com port

![Query selection1 connect_device](./images/09_connect_device.png?raw=true "connect_device")

Once the connection is succesfull, the blended icons appears for selection

![Query selection1 connection_success](./images/10_connection_success.png?raw=true "connection_success")

If not, disconnect the device, reconnect the esp8266 and try connecting again.

### 4. Project upload

Upload the *main.py* file to the device using pymakr.

![Query selection1 upload_code](./images/11_upload_code.png?raw=true "upload_code")

Select the COM port and destination. The status can be seen on the lower right corner of the window.

![Query selection1 uploading](./images/12_uploading.png?raw=true "uploading")

Once uploaded, right click on the *main.py* file, go to pymakr options and select *Run file on device*. See the image *11_upload_code.png*. Select the COM port again and file starts running on the device.

**[Option 2 - Thonny IDE]**

### 3. Project upload

Open *main.py* in Thonny and go to **File** > **Save As**. Select **Micropython device**.

![Query selection1 thonny_upload](./images/16_thonny_upload.png?raw=true "thonny_upload")

Name the file as *main.py* and click **OK**. The *boot.py* file is created by default when you burn MicroPython firmware.

![Query selection1 thonny_upload2](./images/17_thonny_upload2.png?raw=true "thonny_upload2")

Press the on-board **RST/EN** button so that the board restarts and starts running the uploaded code.