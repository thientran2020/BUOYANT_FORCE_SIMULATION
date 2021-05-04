from PyQt5 import QtCore, QtWidgets
import sys
import os

# Main Window
class BuoyantForceWindow(object):

    # Define some parameters for main class
    def __init__(self):
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.title = QtWidgets.QLabel("BUOYANT FORCE SIMULATION", self.centralWidget)

        # Default style for central widget, block object and liquid object
        self.styleSheet = "color: white; font-size: 20px; font-family: Helvetica"
        self.blockStyleSheet = "background-color: white; color: blue;\
                font-family: Verdana; font-size: 20px; font-weight: bold"
        self.liquidStyleSheet = "background-color: white; color: red;\
                font-family: Verdana; font-size: 18px; font-weight:bold"

        # Default values
        self.wdHeight = 740             # Window Height
        self.wdWidth = 1200             # Window Width
        self.lbHeight = 50              # Label Height
        self.lbWidth = 120              # Label Width
        self.lqHeight = 270             # Liquid Height
        self.block_X = 630              # X_coordinate of the center of the block
        self.block_Y = 450              # Y_coordinate of the center of the block
        self.density_unit = "kg/m3"     # SI Unit for Density
        self.g = 9.81                   # g = 9.81 m/s^2
        self.block_raidus = 100         # default radius for sphere
        self.block_side = 100           # default side for cube

        # Dictionaries for lists of liquid density
        # {"liquid": ["density", "color in hex"]}
        self.density_list = {"Water": ["997", "D4F1F9"], "Oil": ["950", "FFBF00"],
                             "Sea Water": ["1020", "006994"],"Milk": ["1027", "FDFFF5"],
                             "Alcohol": ["789", "FFFFFF"], "Mercury": ["13593", "D5D2D1"],
                             "Honey": ["1360", "C58F00"]}

        # Dictionaries for lists of block density
        self.material_list = {"Wood": "99", "Iron": "7800", "Aluminum": "2700",
                              "Gold": "19300", "Platinum": "21400"}

        # Menu Bar
        self.menuBar = QtWidgets.QMenuBar(MainWindow)

        # Menu File
        # Include 2 actions:
        # @exit    TODO: quit the app
        # @clear   TODO: clear current set up
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.exitAction = QtWidgets.QAction(MainWindow)
        self.clearAction = QtWidgets.QAction(MainWindow)

        # Menu Help
        # Include 4 actions:
        # @analysic    TODO: open file analysis.docx
        # @textbook    TODO: open textbook website (Physics - OpenStax)
        # @video       TODO: open video for visualization
        # @about       TODO: open README.md
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.analysisAction = QtWidgets.QAction(MainWindow)
        self.textbookAction = QtWidgets.QAction(MainWindow)
        self.videoAction = QtWidgets.QAction(MainWindow)
        self.aboutAction = QtWidgets.QAction(MainWindow)

        # Formula label
        # TODO: display the manigtude buoyant force exerting on the object
        self.formula = QtWidgets.QLabel(self.centralWidget)

        # Attributes related to liquid
        # @liquid_background    TODO: display liqud color
        # @liquid_label         TODO: label "LIQUID"
        # @liquid_comboBox      TODO: combobox - list of liquids (water, oil, ...)
        # @liquid_density       TODO: label "DENSITY"
        # @liquid_density_text  TODO: display corresponding density with chosen liquid
        self.liquid_background = QtWidgets.QTextEdit(self.centralWidget)
        self.liquid_label = QtWidgets.QLabel(self.centralWidget)
        self.liquid_comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.liquid_density = QtWidgets.QLabel(self.centralWidget)
        self.liquid_density_text = QtWidgets.QLabel(self.centralWidget)

        # Attributes related to block
        # @block                    TODO: block object (either a cube or sphere in 2D)
        # @block_shape              TODO: label "BLOCK SHAPE"
        # @block_shape_comboBox     TODO: combobox - list of shapes (cube, sphere)
        # @block_material           TODO: label "BLOCK MATERIAL"
        # @block_material_comboBox  TODO: combobox - list of material (wood, iron, ...)
        # @block_density            TODO: label "BLOCK DENSITY"
        # @block_density_text       TODO: display corresponding density with chosen material
        # @volume_ratio             TODO: display fraction submerged V_sub / V_total
        self.block = QtWidgets.QLabel(self.centralWidget)
        self.block_shape = QtWidgets.QLabel(self.centralWidget)
        self.block_shape_comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.block_material = QtWidgets.QLabel(self.centralWidget)
        self.block_material_comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.block_density = QtWidgets.QLabel(self.centralWidget)
        self.block_density_text = QtWidgets.QLabel(self.centralWidget)
        self.volume_ratio = QtWidgets.QLabel(self.centralWidget)

        # Attributes for Sliders
        # @volume_slider                TODO: slider to increase or decrease volume of block
        # @volume_slider_text_start     TODO: minimum value for volume: 1 cm^3
        # @volume_slider_text_end       TODO: maximum value for volume: 1 m^3
        # @density_slider               TODO: slider to increase or decrease density of block
        # @density_slider_text          TODO: unit for density kg/m^3
        # @liquid_slider                TODO: slider to increase or decrease density of liquid
        self.volume_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.centralWidget)
        self.volume_slider_text_start = QtWidgets.QLabel(self.centralWidget)
        self.volume_slider_text_end = QtWidgets.QLabel(self.centralWidget)
        self.density_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.centralWidget)
        self.density_slider_text = QtWidgets.QLabel(self.centralWidget)
        self.liquid_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.centralWidget)

    # TODO: Setup the main window
    # TODO: Call others function to support setup
    def setupUI(self, MyWindow):
        MyWindow.setFixedSize(self.wdWidth, self.wdHeight)
        MyWindow.setWindowTitle("BUOYANT FORCE")
        MyWindow.setStyleSheet("background-color: black; color: white")
        self.centralWidget.resize(self.wdWidth, self.wdHeight)
        self.setupMenuBar(MyWindow)
        self.setupTitle_Formula()
        self.setupLiquid()
        self.setupBlock()
        self.setupSlider()

    # TODO: Setup Menu Bar
    # TODO: Set StyleSheet - Set Text - Add action - Event Handling
    def setupMenuBar(self, MyWindow):
        MyWindow.setMenuBar(self.menuBar)
        self.menuBar.setStyleSheet("font-size: 20px; color: white")
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.menuFile.addAction(self.clearAction)
        self.clearAction.setText("Clear")
        self.clearAction.setShortcut("Ctrl+C")
        self.clearAction.triggered.connect(lambda: self.clear())

        self.menuFile.setTitle("File")
        self.menuFile.addAction(self.exitAction)
        self.exitAction.setText("Exit")
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.triggered.connect(lambda: sys.exit(app.exec_()))

        self.menuHelp.setTitle("Help")
        self.menuHelp.addAction(self.videoAction)
        self.videoAction.setText("Visualization")
        self.videoAction.setShortcut('Ctrl+V')
        self.videoAction.triggered.connect(lambda: os.startfile("video.mp4"))

        self.menuHelp.addAction(self.analysisAction)
        self.analysisAction.setText("Analysis")
        self.analysisAction.setShortcut('Ctrl+A')
        self.analysisAction.triggered.connect(lambda: os.startfile("Analysis.docx"))

        self.menuHelp.addAction(self.textbookAction)
        self.textbookAction.setText("Textbook")
        self.textbookAction.setShortcut('Ctrl+T')
        self.textbookAction.triggered.connect(
            lambda: os.startfile("https://openstax.org/books/university-physics-volume-1/pages/14-4-archimedes-principle-and-buoyancy")
        )
        self.menuHelp.addAction(self.aboutAction)
        self.aboutAction.setText("About Us")
        self.aboutAction.triggered.connect(lambda: os.startfile("README.md"))

    # TODO: Setup Title, Formula Label and Volume_Ratio Label
    # TODO: Create text - Set stylesheet and coordinates
    def setupTitle_Formula(self):
        self.title.setStyleSheet("color: yellow; font-size: 40px;\
                                       font-family: Times New Roman; font-weight: bold")
        self.title.setGeometry(QtCore.QRect(300, 20, 1000, 70))

        self.formula.setText("F_b =  N")
        self.formula.setStyleSheet("color: white; font-size: 40px;\
                  font-family: Times New Roman; font-weight: bold")
        self.formula.setGeometry(QtCore.QRect(770, 160, 400, 140))
        self.formula.setAlignment(QtCore.Qt.AlignRight)

        self.volume_ratio.setStyleSheet("background-color: black; color: yellow; font-size: 40px;\
                  font-family: Times New Roman; font-weight: bold")
        self.volume_ratio.setText(" Fraction = ")
        self.volume_ratio.setGeometry(QtCore.QRect(self.wdWidth - 290, self.wdHeight - 70, 280, 60))

    # TODO: Setup 5 liquid objects
    # TODO: Create text - Set stylesheet and coordinates
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
        self.liquid_comboBox.addItem("")
        for item in self.density_list.keys():
            self.liquid_comboBox.addItem(item)
        self.liquid_comboBox.activated.connect(self.liquidClicked)

        self.liquid_density.setText("DENSITY p")
        self.liquid_density.setStyleSheet(self.styleSheet)
        self.liquid_density.setGeometry(QtCore.QRect(30, 570, self.lbWidth, self.lbHeight))
        self.liquid_density.setAlignment(QtCore.Qt.AlignCenter)

        self.liquid_density_text.setText("")
        self.liquid_density_text.setStyleSheet(self.liquidStyleSheet)
        self.liquid_density_text.setGeometry(QtCore.QRect(180, 570, self.lbWidth + 40, self.lbHeight))
        self.liquid_density_text.setAlignment(QtCore.Qt.AlignCenter)

    # TODO: Setup 6 blocks objects
    # TODO: Create text - Set stylesheet and coordinates
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
        self.block_shape_comboBox.addItem("")
        self.block_shape_comboBox.addItem("Sphere")
        self.block_shape_comboBox.addItem("Cube")
        self.block_shape_comboBox.activated.connect(self.shapeClicked)

        self.block_material.setText("BLOCK MATERIAL")
        self.block_material.setStyleSheet(self.blockStyleSheet)
        self.block_material.setGeometry(QtCore.QRect(30, 240, self.lbWidth * 2, self.lbHeight))
        self.block_material.setAlignment(QtCore.Qt.AlignCenter)

        self.block_material_comboBox.setGeometry(QtCore.QRect(320, 240, self.lbWidth, self.lbHeight))
        self.block_material_comboBox.setStyleSheet(self.liquidStyleSheet)
        self.block_material_comboBox.addItem("")
        for item in self.material_list.keys():
            self.block_material_comboBox.addItem(item)
        self.block_material_comboBox.activated.connect(self.materialClicked)

        self.block_density.setText("BLOCK DENSITY")
        self.block_density.setStyleSheet(self.blockStyleSheet)
        self.block_density.setGeometry(QtCore.QRect(30, 320, self.lbWidth * 2, self.lbHeight))
        self.block_density.setAlignment(QtCore.Qt.AlignCenter)

        self.block_density_text.setText("")
        self.block_density_text.setStyleSheet(self.liquidStyleSheet)
        self.block_density_text.setGeometry(QtCore.QRect(320, 320, self.lbWidth * 2, self.lbHeight))
        self.block_density_text.setAlignment(QtCore.Qt.AlignCenter)

    # TODO: Setup 3 main sliders objects (and its supported objects)
    # TODO: Create text - Set stylesheet and coordinates - Event Handling
    def setupSlider(self):
        self.volume_slider.setGeometry(490, 170, 230, 25)
        self.volume_slider.setMinimum(1)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.slideVolume)
        self.volume_slider.sliderPressed.connect(self.slideVolume)

        self.volume_slider_text_start.move(470, 200)
        self.volume_slider_text_start.setText("1 cm3")
        self.volume_slider_text_start.setStyleSheet(self.styleSheet)

        self.volume_slider_text_end.move(690, 200)
        self.volume_slider_text_end.setText("1 m3")
        self.volume_slider_text_end.setStyleSheet(self.styleSheet)

        self.density_slider.setGeometry(320, 390, 230, 25)
        self.density_slider.setMinimum(1)
        self.density_slider.setMaximum(100)
        self.density_slider.setValue(50)
        self.density_slider.valueChanged.connect(self.slideDensity)

        self.density_slider_text.move(320, 410)
        self.density_slider_text.setText("kg/m3")
        self.density_slider_text.setStyleSheet(self.styleSheet)

        self.liquid_slider.setGeometry(64, 640, 240, 25)
        self.liquid_slider.setMinimum(1)
        self.liquid_slider.setMaximum(100)
        self.liquid_slider.setValue(50)
        self.liquid_slider.valueChanged.connect(self.slideLiquid)

    # TODO: Display block (either cube or sphere depending what values passed)
    # @side             TODO: side of the cube
    # @radius           TODO: radius of the sphere
    # @(posX, posY)     TODO: coordinates of the center of the block
    def createShape(self, side = None, radius = None, posX = None, posY = None):
        if not posX and not posY:
            posX, posY = self.block_X, self.block_Y
        if radius is not None:
            self.block_radius = radius
            self.block.move(posX, posY - radius)
            self.block.resize(radius * 2, radius * 2)
            self.block.setStyleSheet("background-color: green; border-radius: " + str(radius))
        elif side is not None:
            self.block_side = side
            self.block.setStyleSheet("background-color: green;")
            self.block.setGeometry(QtCore.QRect(posX, posY - side // 3, side, side))

    # TODO: Clicked event handling when we change the material of the block
    def materialClicked(self):
        if self.block_material_comboBox.currentIndex() != 0:
            typ = self.block_material_comboBox.currentText()
            self.block_density_text.setText(
                self.material_list[typ] + " " + str(self.density_unit)
            )
            self.density_slider.setValue(50)
        else:
            self.block_density_text.setText("")

    # TODO: Liquid event handling when we change the liquid that the object immersered
    def liquidClicked(self):
        if self.liquid_comboBox.currentIndex() != 0:
            typ = self.liquid_comboBox.currentText()
            self.liquid_density_text.setText(
                self.density_list[typ][0] + " " + str(self.density_unit)
            )
            self.liquid_background.setStyleSheet("background-color: #" + self.density_list[typ][1])
            self.liquid_slider.setValue(50)
        else:
            self.liquid_density_text.setText("")

    # TODO: Shape event handling when we change the shape of the block (cube or sphere)
    def shapeClicked(self):
        idx = self.block_shape_comboBox.currentIndex()
        if  idx != 0:
            self.block.setVisible(True)
            shape = self.block_shape_comboBox.currentText()
            if shape == "Sphere":
                self.createShape(radius = self.volume_slider.value()*2 - 10)
            elif shape == "Cube":
                self.createShape(side = self.volume_slider.value()*3)
        else:
            self.clearBlock()

    # TODO: Check if there is buoyant force exerting on the block and return current condition
    # TODO: Return "NO" if not enough information, "FLOAT" if yes and "IMMERSE" if no
    def condition(self):
        liquid = self.liquid_comboBox.currentText()
        block = self.block_material_comboBox.currentText()
        if  liquid == "" or block == "":
            return "NO"
        p_liquid = float(self.density_list[liquid][0])
        p_block = float(self.material_list[block])
        if p_block < p_liquid:
            return "FLOAT"
        return "IMMERSE"

    # TODO: Return fraction submerged = V_submerged / V_total
    def getFraction(self):
        if self.block_material_comboBox.currentIndex() == 0 or self.liquid_comboBox.currentIndex() == 0:
            return ""
        p_object = float(self.block_density_text.text().split(" ")[0])
        p_liquid = float(self.liquid_density_text.text().split(" ")[0])
        return max(p_object / p_liquid, 0)

    # TODO: Move block all the way down into the liquid to display "IMMERSE" condition
    def makeImmersed(self):
        offsetY = self.block.size().height() + 10
        self.block.move(self.block_X, self.wdHeight - offsetY)
        self.volume_ratio.setText("  Fraction =  1")

    # TODO: Move the block vertically by @offsetY
    def moveBlock(self, offsetY):
        if self.block_shape_comboBox.currentText() == "Cube":
            current_X, current_Y = self.block_X, self.block_Y - self.block_side // 2
        elif self.block_shape_comboBox.currentText() == "Sphere":
            current_X, current_Y = self.block_X, self.block_Y - self.block_radius
        self.block.move(current_X, current_Y + offsetY)

    # TODO: Event handling for volume sliders
    # TODO: Update the buoyant force and size of block
    def slideVolume(self):
        condition = self.condition()
        F_buoyant = "0.0"
        if condition == "FLOAT":
            V = self.volume_slider.value() / 100
            material = self.block_material_comboBox.currentText()
            if material in self.material_list:
                p_object = float(self.material_list[material])
                F_buoyant = "{:.2f}".format(V * p_object * self.g)

            self.volume_ratio.setText(" Fraction = " + "{:.2f}".format(self.getFraction()))
            self.shapeClicked()
        elif condition == "IMMERSE":
            self.makeImmersed()
        self.formula.setText("F_b = " + F_buoyant + " N")

    # TODO: Event handling for block density sliders
    # TODO: Update the fraction submerged and new position of block (floated, immersed)
    def slideDensity(self, offset = 5):
        if self.block_density_text.text() == "" or self.condition() == "IMMERSE":
            return
        density = int(self.material_list[self.block_material_comboBox.currentText()])
        slider_dist = self.density_slider.value() - 50
        offset_density = max(density + offset*slider_dist, 0)

        self.block_density_text.setText(str(offset_density) + " " + str(self.density_unit))
        self.moveBlock(slider_dist)
        self.sliding(self.getFraction())

    # TODO: Event handling for liquid density sliders
    # TODO: Update the fraction submerged and new position of block (floated, immersed)
    def slideLiquid(self, offset = 5):
        if self.liquid_density_text.text() == "" or self.liquid_comboBox.currentText() == "" \
                or self.condition() == "IMMERSE":
            return
        density = int(self.density_list[self.liquid_comboBox.currentText()][0])
        slider_dist = self.liquid_slider.value() - 50
        offset_density = max(density + offset*slider_dist, 0)

        self.liquid_density_text.setText(str(offset_density) + " " + str(self.density_unit))
        self.moveBlock(-slider_dist)
        self.sliding(self.getFraction())

    # TODO: Event handling for changing density (either liquid or block)
    def sliding(self, fraction):
        if 0 < fraction < 1:
            self.block.setVisible(True)
            self.volume_ratio.setText(" Fraction = " + "{:.2f}".format(self.getFraction()))
        elif fraction == 0:
            self.block.setVisible(False)
        else:
            self.makeImmersed()

    # TODO: Clear all chosen information for block
    def clearBlock(self):
        self.block_material_comboBox.setCurrentIndex(0)
        self.block_shape_comboBox.setCurrentIndex(0)
        self.materialClicked()
        self.volume_slider.setValue(50)
        self.density_slider.setValue(50)
        self.formula.setText("F_b =  N")
        self.volume_ratio.setText(" Fraction =  ")
        self.block.setVisible(False)

    # TODO: Clear all chosen information for liquid
    def clearLiquid(self):
        self.liquid_comboBox.setCurrentIndex(0)
        self.liquid_density_text.setText("")

    # TODO: Event handling for Clear action on Menu File
    def clear(self):
        self.clearBlock()
        self.clearLiquid()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    simulator = BuoyantForceWindow()
    simulator.setupUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
