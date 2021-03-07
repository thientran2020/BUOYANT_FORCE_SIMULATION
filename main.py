from PyQt5 import QtCore, QtWidgets
import sys

# Main Window
class BuoyantForceWindow(object):

    # Define some parameters for main class
    def __init__(self):
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.title = QtWidgets.QLabel("BUOYANT FORCE SIMULATION", self.centralWidget)

        self.styleSheet = "color: white; font-size: 20px; font-family: Helvetica"
        self.blockStyleSheet = "background-color: white; color: green;\
                font-family: Verdana; font-size: 20px; font-weight: bold"
        self.liquidStyleSheet = "background-color: white; color: red;\
                font-family: Verdana; font-size: 18px; font-weight:bold"

        # Define some default sizes
        self.wdHeight = 700             # Window Height
        self.wdWidth = 1200             # Window Width
        self.lbHeight = 50              # Label Height
        self.lbWidth = 120              # Label Width
        self.lqHeight = 250             # Liquid Height
        self.block_X = 790              # X_coordinate of the block
        self.block_Y = 450              # Y_coordinate of the block
        self.density_unit = "kg/  m3"   # SI Unit for Density

        # Dictionaries for lists of liquid density and material density
        self.density_list = {"Water": ["997", "D4F1F9"], "Oil": ["950", "FFBF00"],
                             "Sea Water": ["1020", "006994"],"Milk": ["1027", "FDFFF5"],
                             "Alcohol": ["789", "FFFFFF"], "Mercury": ["13593", "D5D2D1"],
                             "Honey": ["1360", "C58F00"]}
        self.material_list = {"Wood": "99", "Iron": "7800", "Aluminum": "2700",
                              "Gold": "19300", "Platinum": "21400"}

        # Menu File
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.exitAction = QtWidgets.QAction(MainWindow)
        self.clearAction = QtWidgets.QAction(MainWindow)

        # Formula atrribute
        self.formula = QtWidgets.QLabel(self.centralWidget)

        # Attributes related to liquid
        self.liquid_background = QtWidgets.QTextEdit(self.centralWidget)
        self.liquid_label = QtWidgets.QLabel(self.centralWidget)
        self.liquid_comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.liquid_density = QtWidgets.QLabel(self.centralWidget)
        self.liquid_density_text = QtWidgets.QLabel(self.centralWidget)

        # Attributes related to block
        self.block = QtWidgets.QLabel(self.centralWidget)
        self.block_shape = QtWidgets.QLabel(self.centralWidget)
        self.block_shape_comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.block_material = QtWidgets.QLabel(self.centralWidget)
        self.block_material_comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.block_density = QtWidgets.QLabel(self.centralWidget)
        self.block_density_text = QtWidgets.QLabel(self.centralWidget)

        # Attributes related to shapes of the block: Sphere & Cube
        self.sphere_text = QtWidgets.QTextEdit(self.centralWidget)
        self.cube_text = QtWidgets.QTextEdit(self.centralWidget)
        self.sphere_button = QtWidgets.QPushButton(self.centralWidget)
        self.cube_button = QtWidgets.QPushButton(self.centralWidget)

    # Function to setup the main window
    # Call others function to support setup
    def setupUI(self, MyWindow):
        MyWindow.setFixedSize(self.wdWidth, self.wdHeight)
        MyWindow.setWindowTitle("BUOYANT FORCE")
        MyWindow.setStyleSheet("background-color: black; color: white")
        self.centralWidget.resize(self.wdWidth, self.wdHeight)
        self.setupMenuBar(MyWindow)
        self.setupTitle_Formula()
        self.setupLiquid()
        self.setupBlock()

    # Function to setup Menu
    def setupMenuBar(self, MyWindow):
        MyWindow.setMenuBar(self.menuBar)
        self.menuBar.setStyleSheet("font-size: 20px; color: red")
        self.menuBar.addAction(self.menuFile.menuAction())

        self.menuFile.setTitle("File")
        self.menuFile.addAction(self.exitAction)
        self.exitAction.setText("Exit")
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.triggered.connect(lambda: sys.exit(app.exec_()))

        self.menuFile.addAction(self.clearAction)
        self.clearAction.setText("Clear")
        self.clearAction.setShortcut("Ctrl+C")
        self.clearAction.triggered.connect(lambda: self.clear())

    # Function to setup the Formula object
    # Create text, stylesheet, and set coordinates
    def setupTitle_Formula(self):
        self.title.setStyleSheet("color: white; font-size: 36px;\
                                       font-family: Times New Roman; font-weight: bold")
        self.title.setGeometry(QtCore.QRect(310, 20, 1000, 70))

        self.formula.setText("F_buoyant = -pgV")
        self.formula.setStyleSheet("color: yellow; font-size: 40px;\
                  font-family: Times New Roman; font-style: italic; font-weight: bold")
        self.formula.setGeometry(QtCore.QRect(770, 180, 400, 50))

    # Function to setup liquid objects
    def setupLiquid(self):
        self.liquid_background.setGeometry(
            QtCore.QRect(0, self.wdHeight - self.lqHeight, self.wdWidth, self.lqHeight)
        )
        self.liquid_background.setStyleSheet("background-color: #D4F1F9")
        self.liquid_background.setReadOnly(True)

        self.liquid_label.setText("LIQUID")
        self.liquid_label.setStyleSheet(self.styleSheet)
        self.liquid_label.setGeometry(QtCore.QRect(30, 500, self.lbWidth, self.lbHeight))
        self.liquid_label.setAlignment(QtCore.Qt.AlignCenter)

        self.liquid_comboBox.setGeometry(QtCore.QRect(180, 500, self.lbWidth + 40, self.lbHeight))
        self.liquid_comboBox.setStyleSheet(self.liquidStyleSheet)
        self.liquid_comboBox.addItem("    ")
        for item in self.density_list.keys():
            self.liquid_comboBox.addItem(item)
        self.liquid_comboBox.activated.connect(self.liquidClicked)

        self.liquid_density.setText("DENSITY p")
        self.liquid_density.setStyleSheet(self.styleSheet)
        self.liquid_density.setGeometry(QtCore.QRect(30, 570, self.lbWidth, self.lbHeight))
        self.liquid_density.setAlignment(QtCore.Qt.AlignCenter)

        self.liquid_density_text.setText(" ")
        self.liquid_density_text.setStyleSheet(self.liquidStyleSheet)
        self.liquid_density_text.setGeometry(QtCore.QRect(180, 570, self.lbWidth + 40, self.lbHeight))
        self.liquid_density_text.setAlignment(QtCore.Qt.AlignCenter)

    # Function to setup the block
    def setupBlock(self):
        x_pos = 320
        y_pos = 160
        bt_height = 20
        offset_x = 160

        self.block_shape.setText("BLOCK SHAPE")
        self.block_shape.setStyleSheet(self.blockStyleSheet)
        self.block_shape.setGeometry(QtCore.QRect(30, y_pos, self.lbWidth * 2, self.lbHeight))
        self.block_shape.setAlignment(QtCore.Qt.AlignCenter)

        self.block_shape_comboBox.setGeometry(QtCore.QRect(x_pos, y_pos, self.lbWidth, self.lbHeight))
        self.block_shape_comboBox.setStyleSheet(self.liquidStyleSheet)
        self.block_shape_comboBox.addItem("    ")
        self.block_shape_comboBox.addItem("Sphere")
        self.block_shape_comboBox.addItem("Cube")
        self.block_shape_comboBox.activated.connect(self.shapeClicked)

        self.sphere_text.setText("")
        self.sphere_text.setPlaceholderText("R = 140 m")
        self.sphere_text.setStyleSheet(self.blockStyleSheet)
        self.sphere_text.setGeometry(QtCore.QRect(x_pos + offset_x, y_pos, self.lbWidth + 10, self.lbHeight))
        self.sphere_text.setVisible(False)

        self.sphere_button.setGeometry(QtCore.QRect(x_pos + 2*offset_x, y_pos, bt_height, self.lbHeight))
        self.sphere_button.setStyleSheet("background-color: yellow")
        self.sphere_button.setVisible(False)
        self.sphere_button.clicked.connect(lambda: self.changeSize("Sphere"))

        self.cube_text.setText("")
        self.cube_text.setPlaceholderText("S = 140 m")
        self.cube_text.setStyleSheet(self.blockStyleSheet)
        self.cube_text.setGeometry(QtCore.QRect(x_pos + offset_x, y_pos, self.lbWidth + 10, self.lbHeight))
        self.cube_text.setVisible(False)
        self.cube_button.setGeometry(QtCore.QRect(x_pos + 2*offset_x, y_pos, bt_height, self.lbHeight))
        self.cube_button.setStyleSheet("background-color: yellow")
        self.cube_button.setVisible(False)
        self.cube_button.clicked.connect(lambda: self.changeSize(self.block_shape_comboBox.currentText()))

        self.block_material.setText("BLOCK MATERIAL")
        self.block_material.setStyleSheet(self.blockStyleSheet)
        self.block_material.setGeometry(QtCore.QRect(30, 240, self.lbWidth * 2, self.lbHeight))
        self.block_material.setAlignment(QtCore.Qt.AlignCenter)

        self.block_material_comboBox.setGeometry(QtCore.QRect(320, 240, self.lbWidth, self.lbHeight))
        self.block_material_comboBox.setStyleSheet(self.liquidStyleSheet)
        self.block_material_comboBox.addItem("    ")
        for item in self.material_list.keys():
            self.block_material_comboBox.addItem(item)
        self.block_material_comboBox.activated.connect(self.materialClicked)

        self.block_density.setText("BLOCK DENSITY")
        self.block_density.setStyleSheet(self.blockStyleSheet)
        self.block_density.setGeometry(QtCore.QRect(30, 320, self.lbWidth * 2, self.lbHeight))
        self.block_density.setAlignment(QtCore.Qt.AlignCenter)

        self.block_density_text.setText(" ")
        self.block_density_text.setStyleSheet(self.liquidStyleSheet)
        self.block_density_text.setGeometry(QtCore.QRect(320, 320, self.lbWidth * 2, self.lbHeight))
        self.block_density_text.setAlignment(QtCore.Qt.AlignCenter)

    # Clicked event handling when we change the material of the block
    def materialClicked(self):
        if self.block_material_comboBox.currentIndex() != 0:
            typ = self.block_material_comboBox.currentText()
            self.block_density_text.setText(
                self.material_list[typ] + " " + str(self.density_unit)
            )
        else:
            self.block_density_text.setText(" ")

    # Liquid event handling when we change the liquid that the object immersered
    def liquidClicked(self):
        if self.liquid_comboBox.currentIndex() != 0:
            typ = self.liquid_comboBox.currentText()
            self.liquid_density_text.setText(
                self.density_list[typ][0] + " " + str(self.density_unit)
            )
            self.liquid_background.setStyleSheet("background-color: #" + self.density_list[typ][1])
        else:
            self.liquid_density_text.setText(" ")

    # Clicked event handling when we change the shape of the block
    # Either display Sphere or Rectangle object
    def shapeClicked(self):
        if self.block_shape_comboBox.currentIndex() != 0:
            shape = self.block_shape_comboBox.currentText()
            self.adjustShape(shape)
            if shape == "Sphere":
                self.sphere_text.setVisible(True)
                self.sphere_button.setVisible(True)
                self.cube_text.setText("")
                self.cube_text.setVisible(False)
            elif shape == "Cube":
                self.cube_text.setVisible(True)
                self.cube_button.setVisible(True)
                self.sphere_text.setText("")
                self.sphere_text.setVisible(False)
        else:
            self.sphere_text.setText("")
            self.sphere_text.setVisible(False)
            self.sphere_button.setVisible(False)
            self.cube_text.setText("")
            self.cube_text.setVisible(False)
            self.cube_button.setVisible(False)
        self.block.setVisible(True)

    # Button event handling we adjust the size for the shape of the current block
    # Default size: R = 140 for Sphere and SIDE = 140 for Box
    def adjustShape(self, shape, size=140):
        if shape == "Sphere":
            self.block.move(self.block_X, self.block_Y - size)
            self.block.resize(size*2, size*2)
            self.block.setStyleSheet("background-color: green; border-radius: " + str(size))
        elif shape == "Cube":
            self.block.setStyleSheet("background-color: green;")
            self.block.setGeometry(QtCore.QRect(self.block_X, self.block_Y - size//2, size, size))

    def changeSize(self, shape):
        size = "140"
        if shape == "Cube":
            size = self.cube_text.toPlainText()
        elif shape == "Sphere":
            size = self.sphere_text.toPlainText()
        if size.isdigit():
            self.adjustShape(shape, int(size))

    def clear(self):
        self.block_material_comboBox.setCurrentIndex(0)
        self.liquid_comboBox.setCurrentIndex(0)
        self.block_shape_comboBox.setCurrentIndex(0)
        self.shapeClicked()
        self.materialClicked()
        self.liquidClicked()
        self.block.setVisible(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    simulator = BuoyantForceWindow()
    simulator.setupUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
