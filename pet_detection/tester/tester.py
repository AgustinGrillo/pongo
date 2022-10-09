import torch
import os

file_path = os.path.dirname(os.path.abspath(__file__))

# Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5n')
model = torch.hub.load('ultralytics/yolov5', 'custom', path=os.path.join(file_path, 'best.pt'), force_reload=True) 

# Images
imgs = ['test.jpeg', 'test_people.jpeg', 'test_street.jpeg', 'test_street2.jpeg' ]  

# Inference
results = model(imgs)
results.show()  
