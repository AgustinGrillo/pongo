import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5n')

# Images
imgs = ['test.jpeg', 'test_people.jpeg', 'test_street.jpeg', 'test_street2.jpeg' ]  

# Inference
results = model(imgs)
results.show()  
