### pip install torchinfo 필요
from torchinfo import summary
import torch
from ultralytics import YOLO
model = YOLO ('yolov8n.pt')

result = model.info()
print (result)

model = YOLO ('yolov8s.pt')

result = model.info()
print (result)
