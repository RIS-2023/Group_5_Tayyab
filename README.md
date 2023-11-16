# <div align=center>duckduckgopls</div>
#### <div align="center">" This repository is created for object recognition and computing safe distance with Duckiebot, </div>
#### <div align="center"> which using the camera node of a duckiebot, detects the objects, the distance between them and gives a warning if objects are too close. "</div>
***

### Run the program
1. Object Detection
        
      - In shell 1:
     
       $ rosrun image_transport republish compressed in:=/duckduckgopls/camera_node/image raw out:=/duckduckgopls/camera_node/image/raw
       
       
      - In shell 2:
     
       $ roscd duckduckgopls/scripts/
       $ python detect_and_publish.py
       
      - In shell 3:
       
       $ dts start_gui_tools duckduckgopls
       # rqt_image_view
       
2. Safe Distance Alarm
      - In shell 4:

       $ python safe_distance.py
      
       
       

# Training
- Our Model has been trained on 4151 images and 100 epochs, with an overall accuracy of 0.817
 

# Dataset
- The Dataset has been provided by https://github.com/duckietown/duckietown-objdet


# NOTE
- Current Models/Utils might not work with latest yolov5 models so make sure to update all files accordingly in order to reproduce results.

***


