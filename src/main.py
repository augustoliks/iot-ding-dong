from machine import Pin
import network
from time import sleep

# input variales
NET_SSID = "<YOUR NET_SSID>"
NET_PASSWD = "<YOUR NET_SSID>"

TELEGRAM_BOT_TOKEN = "<YOUR TELEGRAM BOT TOKEN>"
TELEGRAM_CHAT_ID = "<YOUR TELEGRAM CHAT ID>"

TELEGRAM_MSG_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
TELEGRAM_MSG_PAYLOAD = {"chat_id": TELEGRAM_CHAT_ID, "text": "knock knock heaven`s door"}

ESP_PORT_BUTTON = 22

print(">>> ports setup")
print(">>> - PORT_RELAY: {}".format(PORT_RELAY))
print(">>> - ESP_PORT_BUTTON: {}".format(ESP_PORT_BUTTON))

net_station = network.WLAN(network.STA_IF)
port_relay = Pin(PORT_RELAY, Pin.OUT)  # 0 up | 1 down
port_button = Pin(ESP_PORT_BUTTON, Pin.IN, Pin.PULL_UP)

requirements = ("urequests",)

def net_keep_connect():
    while not net_station.isconnected():
        print(">>> try wifi connection")
        net_station.active(True)
        try:
            net_station.connect(ssid, NET_PASSWD)
        except Exception as e:
            print(">>> wifi connection error: " + str(e))
            sleep(10)

net_keep_connect()

print(">>> install urequests")
try:
    import urequets
except ImportError as e:
    import upip
    for requiment in requirements:
        upip.install(requirement)
    import urequests


def main_loop_routine():
    button_pressed = 1

    while True:
        sleep(0.1)
        net_keep_connect()

        if port_button.value() == button_pressed:
            print(">>> button pressed")

            try:
                response = urequests.post(TELEGRAM_MSG_URL, json=TELEGRAM_MSG_PAYLOAD)
                response.close()
                print("message sent to telegram")
            except Exception as e:
                print(">>> error on send message to telegram {}".format(e))

            sleep(1)
            

if __name__ == '__main__':
    print(">>> start main loop routine")
    main_loop_routine()
