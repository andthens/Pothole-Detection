import sys
import os
import cv2 as cv
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QLabel, QPushButton
import geocoder
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.filepath = None

    def initUI(self):
        self.setWindowTitle("Pothole Detection")
        self.setGeometry(100, 100, 500, 300)

        # Added a label to display selected file path
        self.file_label = QLabel(self)
        self.file_label.setGeometry(10, 10, 480, 50)

        # Added a button to select a file
        self.file_button = QPushButton("Select file", self)
        self.file_button.setGeometry(10, 70, 480, 50)
        self.file_button.clicked.connect(self.select_file)

        # Add a button to start detection
        self.detect_button = QPushButton("Start detection", self)
        self.detect_button.setGeometry(10, 130, 480, 50)
        self.detect_button.clicked.connect(self.start_detection)

    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_filter = "Video files (*.mp4 *.avi);;Image files (*.jpg *.png)"
        filepath, _ = QFileDialog.getOpenFileName(self, "Select file", "", file_filter, options=options)
        if filepath:
            self.filepath = filepath
            self.file_label.setText(self.filepath)

    def start_detection(self):
        if self.filepath is None:
            return
        if self.filepath.endswith(('.mp4', '.avi')):
            self.start_video_detection()
        elif self.filepath.endswith(('.jpg', '.png')):
            self.start_image_detection()
        else:
            # Show error message
            print('Invalid file type')


    def start_video_detection(self):

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

    def start_image_detection(self):
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
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
