import logging
import os
from threading import Thread
from time import sleep

import bluetooth

# TODO add in a variable
mac = "FC:A8:9A:00:0D:9E"


class Action(object):
    # def __init__(self):

    def wifi(self, enabled):
        try:
            self.blte = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.blte.connect((mac, 1))
            if enabled is True:
                self.blte.send("1")
            else:
                self.blte.send("0")
            print("Sent Message!")
            data = self.blte.recv(1024)
            logging.info("raw data: {}".format(data))
            self.blte.getsockname()
            self.blte.getpeername()
            self.blte.close()
            return True
        except Exception as e:
            logging.error('General error: ' + str(e))

        return False

    def shutdown(self):
        os.system('sudo shutdown -h now')

    def vpn(self):
        thread = Thread(target=self.__os_call, args=(
            'ssh pi@192.168.8.200 \'sudo -u bus sudo openvpn --config /home/bus/bora-bora.ovpn --daemon bus\'', ))
        thread.start()

        thread = Thread(target=self.__os_call, args=(
            'ssh pi@192.168.8.210 \'sudo -u bus sudo openvpn --config /home/bus/hiva-oa.ovpn --daemon bus\'', ))
        thread.start()

        thread = Thread(target=self.__os_call, args=(
            'sudo -u pi sudo openvpn --config /home/pi/raivavae.ovpn --daemon bus', ))
        thread.start()

    def over(self):
        thread = Thread(target=self.__os_call, args=(
            'ssh pi@192.168.8.200 \'sudo shutdown -h now\'', ))
        thread.start()

        thread = Thread(target=self.__os_call, args=(
            'ssh pi@192.168.8.210 \'sudo shutdown -h now\'', ))
        thread.start()

        thread = Thread(target=self.__os_call, args=(
            'sudo shutdown', ))
        thread.start()

    def __os_call(self, command):
        os.system(command)
