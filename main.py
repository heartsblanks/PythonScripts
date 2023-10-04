import sys
import subprocess
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

class PackageInstaller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Package Installer")
        self.setGeometry(100, 100, 600, 400)

        # List widget to display package installation status
        self.package_list = QtWidgets.QListWidget(self)
        self.package_list.setGeometry(50, 50, 300, 200)

        # Progress bar
        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setGeometry(50, 270, 300, 20)

        # Start installation button
        self.start_button = QtWidgets.QPushButton("Start Installation", self)
        self.start_button.setGeometry(50, 310, 120, 30)
        self.start_button.clicked.connect(self.install_packages)

    def install_packages(self):
        packages_to_install = ["package1", "package2", "package3"]  # Replace with your package list
        total_packages = len(packages_to_install)
        successful_installs = 0

        for package in packages_to_install:
            try:
                # Execute pip install command
                result = subprocess.run(["pip", "install", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

                # Update list widget with success status
                item = QtWidgets.QListWidgetItem(f"{package} - Installed", self.package_list)
                item.setIcon(QtGui.QIcon("green_tick_icon.png"))  # Replace with your green tick icon path
                successful_installs += 1

            except subprocess.CalledProcessError as e:
                # Update list widget with failure status
                item = QtWidgets.QListWidgetItem(f"{package} - Failed to install", self.package_list)
                item.setIcon(QtGui.QIcon("red_x_icon.png"))  # Replace with your red X icon path

            # Update progress bar
            progress_percent = (successful_installs / total_packages) * 100
            self.progress_bar.setValue(progress_percent)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = PackageInstaller()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()