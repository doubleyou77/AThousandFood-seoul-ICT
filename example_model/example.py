from unittest import result
import torch
import pandas as pd

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='static/models/best.pt')   # or yolov5n - yolov5x6, custom

# Images
img = 'gogi.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
# print(results)
df = results.pandas().xyxy[0]  # or .show(), .save(), .crop(), .pandas(), etc.
#print(results.pandas().names)
results.show()
results.save('gogi_r.jpg')
print(df['name'])

