import sys
from PyQt5.QtWidgets import QApplication
from interface import ImageCompressorApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageCompressorApp()
    window.show()
    sys.exit(app.exec_())