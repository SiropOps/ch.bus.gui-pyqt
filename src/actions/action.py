import logging
from time import sleep

import bluetooth

# TODO add in a variable
mac = "FC:A8:9A:00:0D:9E"


class Action(object):
    # def __init__(self):

    def wifi(self, enabled):
        try:
            driver_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            driver_socket.connect((mac, 1))
            sleep(1)
            if enabled is True:
                driver_socket.send("1")
            else:
                driver_socket.send("0")
            print("Sent Message!")
            data = driver_socket.recv(1024)
            logging.info("raw data: {}".format(data))
            driver_socket.getsockname()
            driver_socket.getpeername()
            driver_socket.close()
            return True
        except Exception as e:
            logging.error('General error: ' + str(e))

        return False
