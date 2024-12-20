from PySide6 import QtWidgets, QtGui, QtCore
import sys


class VideoCalculateApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video_calculate")
        self.resize(400, 300)

        self.create_layouts()
        self.create_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_layouts(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.radio_layout = QtWidgets.QHBoxLayout()
        self.input_layout = QtWidgets.QVBoxLayout()  # Layout global pour tous les champs
        self.button_layout = QtWidgets.QHBoxLayout()

        # Layout principal pour les champs et l'image alignés horizontalement
        self.fields_layout = QtWidgets.QHBoxLayout()

        self.duration_layout = QtWidgets.QHBoxLayout()

        self.days_layout = QtWidgets.QVBoxLayout()
        self.hours_layout = QtWidgets.QVBoxLayout()
        self.minutes_layout = QtWidgets.QVBoxLayout()
        self.seconds_layout = QtWidgets.QVBoxLayout()

    def create_widgets(self):
        self.radio_duration = QtWidgets.QRadioButton("Durée")
        self.radio_hdd = QtWidgets.QRadioButton("HDD")
        self.radio_duration.setChecked(True)

        self.label_size = QtWidgets.QLabel("Taille")
        self.input_size = QtWidgets.QLineEdit()

        self.label_ips = QtWidgets.QLabel("ips")
        self.input_ips = QtWidgets.QLineEdit()

        self.label_hdd = QtWidgets.QLabel("Hdd")
        self.input_hdd = QtWidgets.QLineEdit()

        self.label_duration = QtWidgets.QLabel("Durée")
        self.label_days = QtWidgets.QLabel("Jour")
        self.result_days = QtWidgets.QLineEdit()
        self.result_days.setDisabled(True)

        self.label_hours = QtWidgets.QLabel("Heures")
        self.result_hours = QtWidgets.QLineEdit()
        self.result_hours.setDisabled(True)

        self.label_minutes = QtWidgets.QLabel("Minutes")
        self.result_minutes = QtWidgets.QLineEdit()
        self.result_minutes.setDisabled(True)

        self.label_seconds = QtWidgets.QLabel("Secondes")
        self.result_seconds = QtWidgets.QLineEdit()
        self.result_seconds.setDisabled(True)

        self.button_calculate = QtWidgets.QPushButton("Calculer")
        self.button_exit = QtWidgets.QPushButton("Quitter")
        self.button_exit.clicked.connect(self.close)

        # Image de la caméra
        self.image_label = QtWidgets.QLabel()
        self.pixmap = QtGui.QPixmap("camera.png")
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)  # Centrer l'image si nécessaire

    def add_widgets_to_layouts(self):
        self.radio_layout.addWidget(self.radio_duration)
        self.radio_layout.addWidget(self.radio_hdd)

        # Créer un layout horizontal pour chaque champ (label + line edit)
        self.size_layout = QtWidgets.QHBoxLayout()
        self.size_layout.addWidget(self.label_size)
        self.size_layout.addWidget(self.input_size)

        self.ips_layout = QtWidgets.QHBoxLayout()
        self.ips_layout.addWidget(self.label_ips)
        self.ips_layout.addWidget(self.input_ips)

        self.hdd_layout = QtWidgets.QHBoxLayout()
        self.hdd_layout.addWidget(self.label_hdd)
        self.hdd_layout.addWidget(self.input_hdd)

        # Ajouter les layouts des champs dans un layout global
        self.input_layout.addLayout(self.size_layout)
        self.input_layout.addLayout(self.ips_layout)
        self.input_layout.addLayout(self.hdd_layout)

        # Ajouter l'image à côté des champs dans le même layout horizontal
        self.fields_layout.addLayout(self.input_layout)  # Champs (label + line edit)
        self.fields_layout.addWidget(self.image_label)  # Image à côté des champs

        # Durée (jours, heures, minutes, secondes)
        self.days_layout.addWidget(self.label_days)
        self.days_layout.addWidget(self.result_days)

        self.hours_layout.addWidget(self.label_hours)
        self.hours_layout.addWidget(self.result_hours)

        self.minutes_layout.addWidget(self.label_minutes)
        self.minutes_layout.addWidget(self.result_minutes)

        self.seconds_layout.addWidget(self.label_seconds)
        self.seconds_layout.addWidget(self.result_seconds)

        self.duration_layout.addLayout(self.days_layout)
        self.duration_layout.addLayout(self.hours_layout)
        self.duration_layout.addLayout(self.minutes_layout)
        self.duration_layout.addLayout(self.seconds_layout)

        # Boutons
        self.button_layout.addWidget(self.button_calculate)
        self.button_layout.addWidget(self.button_exit)

        # Ajouter tout au layout principal
        self.main_layout.addLayout(self.radio_layout)
        self.main_layout.addLayout(self.fields_layout)  # Champs + image alignés
        self.main_layout.addLayout(self.duration_layout)
        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)

    def setup_connections(self):
        self.radio_duration.toggled.connect(self.toggle_duration_fields)
        self.button_calculate.clicked.connect(self.calculate)

    def toggle_duration_fields(self):
        if self.radio_duration.isChecked():
            self.input_size.setDisabled(False)
            self.input_ips.setDisabled(False)
            self.input_hdd.setDisabled(False)

            self.result_days.setDisabled(True)
            self.result_hours.setDisabled(True)
            self.result_minutes.setDisabled(True)
            self.result_seconds.setDisabled(True)

        elif self.radio_hdd.isChecked():
            self.input_size.setDisabled(False)
            self.input_ips.setDisabled(False)
            self.result_days.setDisabled(False)
            self.result_hours.setDisabled(False)
            self.result_minutes.setDisabled(False)
            self.result_seconds.setDisabled(False)
            self.input_hdd.setDisabled(True)

    def calculate(self):
        try:
            if self.radio_duration.isChecked():

                size = float(self.input_size.text())
                ips = float(self.input_ips.text())
                hdd = float(self.input_hdd.text())

                duration_seconds = (hdd * 1024 * 1024) / (size * ips)

                days = duration_seconds // (24 * 3600)
                hours = (duration_seconds % (24 * 3600)) // 3600
                minutes = (duration_seconds % 3600) // 60
                seconds = duration_seconds % 60

                self.result_days.setText(str(int(days)))
                self.result_hours.setText(str(int(hours)))
                self.result_minutes.setText(str(int(minutes)))
                self.result_seconds.setText(str(int(seconds)))

            elif self.radio_hdd.isChecked():

                size = float(self.input_size.text())
                ips = float(self.input_ips.text())
                days = float(self.result_days.text())
                hours = float(self.result_hours.text())
                minutes = float(self.result_minutes.text())
                seconds = float(self.result_seconds.text())

                total_seconds = (days * 24 * 3600) + (hours * 3600) + (minutes * 60) + seconds

                hdd_size = (size * ips * total_seconds) / (1024 * 1024)

                self.input_hdd.setText(f"{hdd_size:.2f} Go")

        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Erreur", "Veuillez entrer des valeurs valides.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VideoCalculateApp()
    window.show()
    sys.exit(app.exec())
