# Only needed for access to command line arguments
import sys
import logging

from PyQt5.QtWidgets import QApplication, QWidget

from windows.window import MainWindow


logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()

window.showMaximized()
# window.showFullScreen()

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
