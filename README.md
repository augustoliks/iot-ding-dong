# iot-ding-dong

Smart doorbell, ding dong in your Telegram.

> Workflow:
> _Doorbell Push Button > ESP32 > HTTP Request > Telegram Bot Endpoint > Notify Channel_

This project consists of an ESP32 module that is connected to a network. This module is formatted with the Micropython Firmware. When Pin 22 is not closed circuit, a message is sent to a telegram channel via bot.

## Requirements

Hardware Components: 

- [ESP32](https://pt.wikipedia.org/wiki/ESP32)
- [MB102 Breadboard 3.3V/5V Power Supply](https://www.amazon.com/CorpCo-Breadboard-Supply-Arduino-Solderless/dp/B00ZO9YB1G)
- 7DC 12DC power supply

System Packages:

- python3-pyserial
- micropython
- ampy

## Configuration

```python
NET_SSID = "<YOUR NET_SSID>"
NET_PASSWD = "<YOUR NET_PASSWD>"

TELEGRAM_BOT_TOKEN = "<YOUR TELEGRAM BOT TOKEN>"
TELEGRAM_CHAT_ID = "<YOUR TELEGRAM CHAT ID>"
```

To discovery `TELEGRAM_CHAT_ID`, in order to get the group chat id, do as follows:

- Add the Telegram Bot to the group
- Get the list of updates for your Bot:
    - `curl -s -XGET https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdateS`
- Check `chat.id` value.


## How To Run

First step, it's install micropython firmware in ESP32. Check latest firwmare version on https://micropython.org/download/esp32/. At the time of release of this project, the latest firmware is `esp32-20220117-v1.18.bin`

```bash
wget https://micropython.org/resources/firmware/esp32-20220117-v1.18.bin
sudo chmod 777 /dev/ttyUSB0
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin
```

> `/dev/ttyUSB0` value may change depending on other USB peripherals connected on the machine.

Next, upload source code to 

```bash
git clone https://github.com/augustoliks/iot-ding-dong
ampy --port /dev/ttyUSB0 put src/main.py /main.py
```
