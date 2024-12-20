from PySide6 import QtWidgets
import socket
import uuid
import requests
import platform


class ComputerInfoApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(450, 300)
        self.setWindowTitle("Computer Information")
        self.create_layouts()
        self.create_widgets()
        self.add_widgets_to_layouts()
        self.populate_fields()

    def create_layouts(self):
        self.main_layout = QtWidgets.QVBoxLayout()

        self.hostname_layout = QtWidgets.QHBoxLayout()
        self.lan_ip_layout = QtWidgets.QHBoxLayout()
        self.mac_address_layout = QtWidgets.QHBoxLayout()
        self.wan_ip_layout = QtWidgets.QHBoxLayout()
        self.system_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        # Labels and LineEdits
        self.lbl_hostname = QtWidgets.QLabel("Hostname:")
        self.lineedit_hostname = QtWidgets.QLineEdit()
        self.lineedit_hostname.setReadOnly(True)

        self.lbl_lan_ip = QtWidgets.QLabel("LAN IP Address:")
        self.lineedit_lan_ip = QtWidgets.QLineEdit()
        self.lineedit_lan_ip.setReadOnly(True)

        self.lbl_mac_address = QtWidgets.QLabel("MAC Address:")
        self.lineedit_mac_address = QtWidgets.QLineEdit()
        self.lineedit_mac_address.setReadOnly(True)

        self.lbl_wan_ip = QtWidgets.QLabel("WAN IP Address:")
        self.lineedit_wan_ip = QtWidgets.QLineEdit()
        self.lineedit_wan_ip.setReadOnly(True)

        self.lbl_system = QtWidgets.QLabel("System:")
        self.lineedit_system = QtWidgets.QLineEdit()
        self.lineedit_system.setReadOnly(True)

        # Buttons
        self.btn_exit = QtWidgets.QPushButton("Exit")
        self.btn_exit.clicked.connect(self.close)

    def add_widgets_to_layouts(self):
        # Add widgets to individual layouts
        self.hostname_layout.addWidget(self.lbl_hostname)
        self.hostname_layout.addWidget(self.lineedit_hostname)

        self.lan_ip_layout.addWidget(self.lbl_lan_ip)
        self.lan_ip_layout.addWidget(self.lineedit_lan_ip)

        self.mac_address_layout.addWidget(self.lbl_mac_address)
        self.mac_address_layout.addWidget(self.lineedit_mac_address)

        self.wan_ip_layout.addWidget(self.lbl_wan_ip)
        self.wan_ip_layout.addWidget(self.lineedit_wan_ip)

        self.system_layout.addWidget(self.lbl_system)
        self.system_layout.addWidget(self.lineedit_system)

        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.btn_exit)

        # Add all layouts to the main layout
        self.main_layout.addLayout(self.hostname_layout)
        self.main_layout.addLayout(self.lan_ip_layout)
        self.main_layout.addLayout(self.mac_address_layout)
        self.main_layout.addLayout(self.wan_ip_layout)
        self.main_layout.addLayout(self.system_layout)
        self.main_layout.addLayout(self.buttons_layout)

        self.setLayout(self.main_layout)

    def populate_fields(self):
        """Populate fields with system information"""
        # Get hostname
        hostname = socket.gethostname()

        # Get LAN IP Address
        try:
            lan_ip = socket.gethostbyname(hostname)
        except socket.gaierror:
            lan_ip = "Unavailable"

        # Get MAC Address
        mac = uuid.getnode()
        mac_address = ':'.join(('%012X' % mac)[i:i+2] for i in range(0, 12, 2))

        # Get WAN IP Address
        try:
            wan_ip = requests.get("https://api64.ipify.org").text
        except requests.RequestException:
            wan_ip = "Unavailable"

        # Get System Information
        system_info = platform.system()

        # Populate the fields
        self.lineedit_hostname.setText(hostname)
        self.lineedit_lan_ip.setText(lan_ip)
        self.lineedit_mac_address.setText(mac_address)
        self.lineedit_wan_ip.setText(wan_ip)
        self.lineedit_system.setText(system_info)


# Application entry point
app = QtWidgets.QApplication([])
form = ComputerInfoApp()
form.show()
app.exec()
