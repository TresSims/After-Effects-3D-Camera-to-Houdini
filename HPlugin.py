import hou
from hutil.Qt import QtCore
from PySide2 import QtCore, QtUiTools, QtWidgets


class Choser(QtWidgets.QWidget):
    def __init__(self):
        super(Choser, self).__init__()
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)
        # Edit the file location to the location of your HoudiniInterface.ui
        ui_file = 'D:/Dropbox/CG Art/After-Effects-3D-Camera-to-Houdini/HoudiniInterface.ui'
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)

        self.fileChooser = hou.qt.FileChooserButton()
        self.fileChooser.fileSelected.connect(self.fileChosen)
        self.nodeChooser = hou.qt.NodeChooserButton()
        self.nodeChooser.nodeSelected.connect(self.nodeChosen)

        self.ui.gridLayout.addWidget(self.fileChooser, 0, 2)
        self.ui.gridLayout.addWidget(self.nodeChooser, 1, 2)

        self.ui.keyframeFile.textChanged.connect(self.fileTextSelected)
        self.ui.cameraObject.textChanged.connect(self.cameraTextSelected)
        self.ui.scaleValue.textChanged.connect(self.scaleTextSelected)

        self.ui.import_2.clicked.connect(self.readAndSet)

        self.filename = "C:/Documents/CameraData.txt"
        self.cam = "/obj/cam1"
        self.scale = 0.01

        # self.readAndSet()

    def fileChosen(self, file):
        self.ui.keyframeFile.setText(file)

    def fileTextSelected(self, text):
        self.filename = text

    def cameraTextSelected(self, text):
        self.cam = text

    def scaleTextSelected(self, text):
        self.scale = float(text)

    def nodeChosen(self, node):
        self.ui.cameraObject.setText(node.path())

    def readAndSet(self):
        state = "crap"
        ignoreLine = False
        with open(self.filename, "rU") as ff:
            for theLine in ff:
                elements = theLine.strip().split("\t")
                ignoreLine = False
                if len(elements) == 0:
                    state = "crap"
                    ignoreLine = True
                else:
                    if elements.count("X degrees") > 0:
                        state = "orientation"
                        ignoreLine = True
                    if elements.count("X pixels") > 0:
                        state = "translate"
                        ignoreLine = True
                    if ignoreLine is False:
                        if len(elements) == 4:
                            theFrame = elements[0]
                            theXValue = elements[1]
                            theYValue = elements[2]
                            theZValue = elements[3]
                        if state == "translate":
                            print("At frame "+theFrame+" translate to: " +
                                  theXValue)
                            setKey = hou.Keyframe()
                            setKey.setFrame(int(theFrame))
                            setKey.setValue(float(theXValue)*self.scale)
                            print("{}tx".format(self.cam))
                            testCh = hou.parm("{}/tx".format(self.cam))
                            testCh.setKeyframe(setKey)

                            setKey = hou.Keyframe()
                            setKey.setFrame(int(theFrame))
                            setKey.setValue(-float(theYValue)*self.scale)
                            testCh = hou.parm("{}/ty".format(self.cam))
                            testCh.setKeyframe(setKey)

                            setKey = hou.Keyframe()
                            setKey.setFrame(int(theFrame))
                            setKey.setValue(-float(theZValue)*self.scale)
                            testCh = hou.parm("{}/tz".format(self.cam))
                            testCh.setKeyframe(setKey)

                        if state == "orientation":
                            print ("At frame "+theFrame+" orient to: "
                                   + theXValue)

                            setKey = hou.Keyframe()
                            setKey.setFrame(int(theFrame))
                            setKey.setValue(float(theXValue))
                            testCh = hou.parm("{}/rx".format(self.cam))
                            testCh.setKeyframe(setKey)
                            setKey = hou.Keyframe()
                            setKey.setFrame(int(theFrame))
                            setKey.setValue(-float(theYValue))
                            testCh = hou.parm("{}/ry".format(self.cam))
                            testCh.setKeyframe(setKey)

                            setKey = hou.Keyframe()
                            setKey.setFrame(int(theFrame))
                            setKey.setValue(-float(theZValue))
                            testCh = hou.parm("{}/rz".format(self.cam))
                            testCh.setKeyframe(setKey)


c = Choser()
c.show()
