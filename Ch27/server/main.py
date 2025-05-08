# 가상환경에서 파일 위치가 있는 디렉토리로 cd
# uvicorn main:app --reload
# uvicorn (실행파일:앱 이름) --reload

import io
import numpy as np
from typing import Union
import torch
from fastapi import FastAPI, UploadFile, File   # 파일 업로드를 위한 모듈
from PIL import Image
import cv2  # 얼굴 인식 할때 사용하기 위해서 불러옴
from transformers import AutoImageProcessor, AutoModelForImageClassification

model_name = 'C:\\Users\\human\\ku-python\\Ch27\\server\\emotion5-model'

processor = AutoImageProcessor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)  
model.eval()

id2label = model.config.id2label

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                     'haarcascade_frontalface_default.xml')

app = FastAPI()

# 1. 동시 접속자 수가 많아도 감당 가능한 API -> 멀티 스레드 + 비동기 처리 or 멀티 프로세싱
#       - cpu bound인지 I/O bound인지에 따라 전랙이 달라짐

# 2. 얼굴 인식 모델 + 감정 인식 모델 동시 추론  -> 물체인식으로 예측한 ROI를 분류 모델로 다시 추론
# 3. 웹 클라이언트에서 파일 입력받기
# 4. 예측값이 없을때 예외처리
#       - 입력 파일 형식이 안맞을때
#       - 예측값이 없을때
#       - 예측값의 신회도가 낮을때
#       - 예측값이 허용범위가 아닐때
#       - 두 모델의 결과가 같이 나와야 하는지, 따로 나와야 하는지 결정해서 예외 처리

# 5. 얼굴 위치 좌표와 감정 인식 결과를 이미지에 표시하고 화면에 표시

# async def + await -> 비동기 처리
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # predict api 비동기 처리로 구현 -> 동시 요청 대응에 강하고 I/O(입출력 처리) 처리가 긴 작업에 유리
    
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")
    input_image = processor(image, return_tensors="pt")
    
    try:
        # 얼굴 감지
        
        # RGB -> BGR 변환
        BGR_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        # PIL 이미지를 Gray scale로 변환
        gray_image = cv2.cvtColor(BGR_image, cv2.COLOR_BGR2GRAY)
        
        # 얼굴 위치 예측
        face_position = face_cascade.detectMultiScale(gray_image, 1.1, 5)
        
        # x, y, width, height
        x, y, w, h = face_position[0]
        
        # 감정추론
        with torch.no_grad():
            outputs = model(**input_image)
            logits = outputs.logits
            prob = torch.softmax(logits, dim=1)
            pred_id = prob.argmax(dim=-1).item()    # (Batch, class_num)
            
            confidence = prob[0, pred_id].item()
            
            if confidence < 0.2:
                return {"Message": "예측 신뢰도가 너무 낮습니다."}
            
        return {"label" : id2label[pred_id], 
                "confidence": confidence,
                "position": [int(x), int(y), int(x + w), int(y + h)]}
    except Exception as e:
        return {"Error": "No Face",
                "Error_code": e}
