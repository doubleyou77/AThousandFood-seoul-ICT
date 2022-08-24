import os
import shutil
from flask import Flask, render_template, request
import torch
import pandas as pd
from recipe import Crawling
from material import engToKor


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ai", methods=['POST'])
def ai():
    results_recipe = []

    image = request.files['image']
    image.save('static/upload/'+image.filename)
    # 인공지능으로 이미지 처리

    img = image.filename

    startDir = 'runs/detect/exp/'
    endDir = 'static/output/'

    results = model(img)
    results_name = results.pandas().xyxy[0]['name'].to_list()
    results.save(img)
    
    shutil.move(startDir+img, endDir+img)
    shutil.rmtree(startDir.replace('/exp', ''))
    # 처리한 이미지를 저장

    for name in results_name:
        results_recipe.append(Crawling(engToKor(name)))
    
    
    return render_template("result.html", image_path=img, materials=results_name, recipes=results_recipe )

if __name__ == "__main__":
    # 모델을 불러오는 부분
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='static/models/best.pt')
    app.run(host='0.0.0.0', port=8000)
