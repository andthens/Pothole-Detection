# Imports
import sys
import platform
import time
import os
import threading
import geocoder
import cv2 as cv
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from subprocess import *
from mainWindow import Ui_mainWindow  # Importing mainWindow.py
from SplashScreen import Ui_SplashScreen  # Importing SplashScreen.py
counter = 0

# Splashscreen class
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.main_window = MainWindow()
        self.ui.setupUi(self)

        # Remove titlebar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Dropshadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.show()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        # Timer in millisecond
        self.timer.start(35)

    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEN AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main_window.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


# MainWindow class
class MainWindow(QMainWindow):
    def __init__(self):
        # Shadow+Other functions
        QMainWindow.__init__(self)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.ui.dropshadowFrame.setGraphicsEffect(self.shadow)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # Setting frameless window
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Setting frame border

        # Window control buttons
        self.ui.minButton.clicked.connect(lambda: self.showMinimized())  # Minimize on click
        self.ui.closeButton.clicked.connect(lambda: self.close())  # Close on click

        # Titlebar dragging
        self.ui.titleBar.mouseMoveEvent = self.moveWindow

        # About page function
        self.file_label = QLabel(self)
        self.file_label.setGeometry(10, 10, 480, 50)

        # Page swap functions

        # To scanpage from homepage
        self.ui.scanFrame.mousePressEvent = self.switch_file
        self.ui.updateFrame.setEnabled(False)
        # To updatepage from homepage
        self.ui.updateFrame.mousePressEvent = self.switch_detection
        # To aboutpage from homepage
        self.ui.aboutLabel.mousePressEvent = self.switch_about
        # To homepage from aboutpage
        self.ui.homeButtonAbout.clicked.connect(self.switch_home)


    # Mouse drag event handler
    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # invoke the select_file method
    def switch_file(self, event):
        self.select_file()
    #invoke the detection
    def switch_detection(self, event):
        self.start_detection()

    def switch_home(self):
        self.ui.stackedHome.setCurrentWidget(self.ui.pageHome)

    def switch_about(self, event):
        self.ui.stackedHome.setCurrentWidget(self.ui.pageAbout)

    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_filter = "Video files (*.mp4 *.avi);;Image files (*.jpg *.png)"
        filepath, _ = QFileDialog.getOpenFileName(self, "Select file", "", file_filter, options=options)
        if filepath:
            self.filepath = filepath
            self.file_label.setText(self.filepath)
            self.ui.updateFrame.setEnabled(True)
        else:
            self.filepath = None
            self.file_label.setText("")
            self.ui.updateFrame.setEnabled(False)

    def start_detection(self):
        if self.filepath is None:
            return
        if self.filepath.endswith(('.mp4', '.avi')):
            video_detection = VideoDetection(self.filepath)
            video_detection.detect()
        elif self.filepath.endswith(('.jpg', '.png')):
            image_detection = ImageDetection(self.filepath)
            image_detection.detect()
        else:
            # Show error message
            print('Invalid file type')   

class VideoDetection:
    def __init__(self, file_path):
        self.filepath = file_path

    def detect(self):
    
       # Run the detection code with the selected file path
        class_name = []
        with open(os.path.join("project_files", 'obj.names'), 'r') as f:
            class_name = [cname.strip() for cname in f.readlines()]

        net1 = cv.dnn.readNet('project_files/yolov4_tiny.weights', 'project_files/yolov4_tiny.cfg')
        net1.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
        net1.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)
        model1 = cv.dnn_DetectionModel(net1)
        model1.setInputParams(size=(640, 480), scale=1 / 255, swapRB=True)

        cap = cv.VideoCapture(self.filepath)
        width = cap.get(3)
        height = cap.get(4)
        result = cv.VideoWriter('result.avi',
                                cv.VideoWriter_fourcc(*'MJPG'),
                                10, (int(width), int(height)))

        g = geocoder.ip('me')
        result_path = "pothole_coordinates"
        starting_time = time.time()
        Conf_threshold = 0.5
        NMS_threshold = 0.4
        frame_counter = 0
        i = 0
        b = 0

        while True:
            ret, frame = cap.read()
            frame_counter += 1
            if ret == False:
                break

            classes, scores, boxes = model1.detect(frame, Conf_threshold, NMS_threshold)
 
            for (classid, score, box) in zip(classes, scores, boxes):
                label = "pothole"
                x, y, w, h = box
                recarea = w*h
                area = width*height
                #drawing detection boxes on frame for detected potholes and saving coordinates txt and photo
                if(len(scores)!=0 and scores[0]>=0.7):
                    if((recarea/area)<=0.1 and box[1]<600):
                        cv.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 1)
                        cv.putText(frame, "%" + str(round(scores[0]*100,2)) + " " + label, (box[0], box[1]-10),cv.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
                        if(i==0):
                            cv.imwrite(os.path.join(result_path,'pothole'+str(i)+'.jpg'), frame)
                            with open(os.path.join(result_path,'pothole'+str(i)+'.txt'), 'w') as f:
                                f.write(str(g.latlng))
                                i=i+1
                        if(i!=0):
                            if((time.time()-b)>=2):
                                cv.imwrite(os.path.join(result_path,'pothole'+str(i)+'.jpg'), frame)
                                with open(os.path.join(result_path,'pothole'+str(i)+'.txt'), 'w') as f:
                                    f.write(str(g.latlng))
                                    b = time.time()
                                    i = i+1
                #writing fps on frame
                endingTime = time.time() - starting_time
                fps = frame_counter/endingTime
                cv.putText(frame, f'FPS: {fps}', (20, 50),
                cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
                #showing and saving result
                cv.imshow('frame', frame)
                result.write(frame)
                key = cv.waitKey(1)
                if key == ord('q'):
                    break
        #end
        cap.release()
        result.release()
        cv.destroyAllWindows()


class ImageDetection:
    def __init__(self, file_path):
        self.filepath = file_path

    def detect(self):
        if self.filepath is None:
            return
        img = cv.imread(self.filepath) #image name

        #reading label name from obj.names file
        with open(os.path.join("project_files",'obj.names'), 'r') as f:
            classes = f.read().splitlines()

        #importing model weights and config file
        net = cv.dnn.readNet('project_files/yolov4_tiny.weights', 'project_files/yolov4_tiny.cfg')
        model = cv.dnn_DetectionModel(net)
        model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
        classIds, scores, boxes = model.detect(img, confThreshold=0.6, nmsThreshold=0.4)

        #detection 
        for (classId, score, box) in zip(classIds, scores, boxes):
            cv.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                        color=(0, 255, 0), thickness=2)
        
        cv.imshow("pothole",img)
        cv.imwrite("result1"+".jpg",img) #result name
        cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())
