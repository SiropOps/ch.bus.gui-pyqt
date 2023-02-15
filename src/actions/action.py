import logging
from time import sleep
import os

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
        logging.info("vpn click")
        # TODO
    
    def over(self):
        os.system('ssh pi@192.168.8.200 \'sudo shutdown -h now\'')
        os.system('ssh pi@192.168.8.210 \'sudo shutdown -h now\'')
        self.shutdown()
