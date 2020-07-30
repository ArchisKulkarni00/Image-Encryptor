from PyQt5 import QtWidgets,QtCore,QtGui
import sys
from Encryptor import *
import PhotoDispla
import Menu
import os
import cv2
import numpy as np
import pickle5 as pickle

Address = None
imlist = None

###Seperates image and filename after reading from file
'''Args: .fuck file
   Returns: name and image(numpy array) '''
def seperateImage(file):
    with open(file, 'rb') as infile:
        loadingDict = pickle._load(infile)
    name = loadingDict['name']
    image = loadingDict['image']
    return name,image

###Reads files from folder specified by Address variable. Reads normal image for false anf fuckfiles for true
'''Args: fuck_files = false'''
def getFiles(fuck_files = False):
    global imlist
    if fuck_files:
        imlist = [filename for filename in os.listdir(Address) if filename[-5:] in [".fuck", '.FUCK']]
    else:
        imlist = [filename for filename in os.listdir(Address) if filename[-4:] in [".jpg", '.JPG','.png','.PNG']]



###Menu Class
class MenuD(Menu.Ui_Menu,QtWidgets.QMainWindow):
    def __init__(self):
        super(MenuD,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.encrypt)
        # self.pushButton_2.clicked.connect(self.Decrypt)
        self.pushButton_3.clicked.connect(self.Display)
        self.checkBox.stateChanged.connect(self.checkBox1)
        self.toolButton.clicked.connect(self.getAddress)
    ###Display the Gallery
    def Display(self):
        seed = self.lineEdit_2.text() #Read seed value to be passed to display class
        self.window = PhotoDisplay(seed)
        self.window.show()

    ###Sets the Address parameter to address of current working directory if checked and clears if unchecked
    def checkBox1(self):
        global Address
        global imlist
        if self.checkBox.isChecked():
            Address = os.getcwd() + '/'
            Address=Address.replace("\\",'/')
            self.lineEdit.clear()
            self.lineEdit.setText(Address)
        else:
            self.lineEdit.clear()

    ###Reads address using tool button and file select dialogbox
    def getAddress(self):
        global Address
        global imlist
        Address = str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Select source')) + '/'
        self.lineEdit.setText(Address)

    ###Used to encrypt files read in imlist specified by Address end with jpg or png
    def encrypt(self):
        global Address
        getFiles()
        self.seed = self.lineEdit_2.text()
        self.save_path = Address + 'Encrypted/'
        os.mkdir(self.save_path)
        for i in range(len(imlist)):
            image = cv2.imread(Address+imlist[i])
            np.random.seed(int(self.seed))
            self.noise_gen = np.random.uniform(4, 255, image.shape).astype(np.uint8)
            encrypted = cv2.bitwise_xor(image,self.noise_gen)
            saving_dict = {'name':imlist[i],'image':encrypted}
            with open( self.save_path+imlist[i]+'.fuck','wb') as outfile:
                pickle._dump(saving_dict, outfile)
        self.lineEdit.clear()
        self.lineEdit_2.clear()

###Gallery Class
class PhotoDisplay(PhotoDispla.Ui_PhotoDisplay,QtWidgets.QMainWindow):
    def __init__(self,seed):
        super(PhotoDisplay,self).__init__()
        self.setupUi(self)
        self.threshold = 1000
        getFiles(True)
        self.num_images = len(imlist)
        self.seed = seed
        self.displayImage(0)
        self.index = 0
        self.pushButton_2.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.previous)

    ###Loads next image
    def next(self):
        global imlist
        if self.index < self.num_images-1:
            self.index += 1
            self.displayImage(self.index)

    ###Loads previous image
    def previous(self):
        global imlist
        if self.index > 0:
            self.index -= 1
            self.displayImage(self.index)

    ###Displays image with indedx
    def displayImage(self,index):
        global Address
        global imlist

        name, image = seperateImage(Address + imlist[index])
        np.random.seed(int(self.seed))
        self.noise_gen = np.random.uniform(4, 255, image.shape).astype(np.uint8)
        decrypted = cv2.bitwise_xor(image, self.noise_gen)


        height, width, channel = decrypted.shape
        bytesperline = 3 * width
        qimg = QtGui.QImage(decrypted,width,height,bytesperline,QtGui.QImage.Format_RGB888).rgbSwapped()

        self.pixmap = QtGui.QPixmap(qimg)
        self.Image.setPixmap(self.pixmap)
        self.Image.setScaledContents(True)
        self.Image.resize(self.pixmap.width(), self.pixmap.height())
        self.pixmap1 = self.pixmap
        if self.pixmap.width() > self.threshold or self.pixmap.height() > self.threshold:
            if self.pixmap.width() > self.pixmap.height():
                height = int(self.threshold * self.pixmap.height() / self.pixmap.width())
                self.pixmap1 = self.pixmap.scaled(self.threshold, height)
            else:
                width = int(self.threshold * self.pixmap.height() / self.pixmap.width())
                self.pixmap1 = self.pixmap.scaled(width, self.threshold)
        print('Index:',index)
        if self.pixmap1.width()+60 <560:
            self.setFixedSize(560, self.pixmap1.height()+60)
        else:
            self.setFixedSize(self.pixmap1.width(), self.pixmap1.height() + 60)
        self.frame.resize(self.width(), self.frame.height())
        self.Image.resize(self.pixmap1.width(), self.pixmap1.height())

        self.label.setText(str(index+1)+'/'+str(self.num_images))
        self.label_2.setText(str(name))


###Starting Window
class Window(Ui_Login,QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.exit)

    ###Display the menu
    def newWindow(self):
        self.window = MenuD()
        self.window.show()

    ###Verify credentials and login
    def login(self):
        if self.lineEdit.text():
            self.newWindow()
        else:
            print('not welcome here')

    ###Exit the application
    def exit(self):
        print('bye')
        sys.exit()

app=QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())