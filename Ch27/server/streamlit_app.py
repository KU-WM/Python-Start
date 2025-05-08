# 가상환경에서 파일 위치가 있는 디렉토리로 cd
# streamlit run streamlit_app.py
# streamlit run (실행파일.py)

import streamlit as st
import requests
from PIL import Image, ImageDraw, ImageFont
import io
import unicodedata

font_path = "C:/Windows/Fonts/malgun.ttf"  # 맑은 고딕
font = ImageFont.truetype(font_path, 8)

# 페이지 구성
st.set_page_config(page_title="이미지 분석", layout="centered")

# Bootstrap 스타일 적용
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .container {
            margin-top: 50px;
        }
        .result {
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="container">', unsafe_allow_html=True)

st.title("이미지 업로드 및 분석")

# 이미지 업로드
uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])
image_placeholder = st.empty()

if uploaded_file is not None:
    # 업로드한 이미지 표시
    image = Image.open(uploaded_file)
    image_placeholder.image(image, caption='업로드한 이미지', use_container_width=True)

    # 버튼 클릭 시 API 전송
    if st.button("API로 전송"):
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        
        # API 호출 준비
        files = {"file": (uploaded_file.name, img_bytes, uploaded_file.type)}
        try:
            response = requests.post("http://127.0.0.1:8000/predict", files=files)
            if response.status_code == 200:
                data = response.json()
                label = data.get("label", "없음")
                confidence = data.get("confidence", "없음")
                position = data.get("position", "없음")
                
                image_with_box = image.copy()
                draw = ImageDraw.Draw(image_with_box)
                if position and isinstance(position, list) and len(position) == 4:
                    x1, y1, x2, y2 = position

                    # 사각형 그리기
                    draw.rectangle([x1, y1, x2, y2], outline="red", width=3)

                    # 확률 텍스트
                    label = unicodedata.normalize("NFC", label)
                    confidence_text = f"감정: {label}, 확률: {confidence:.2%}"

                    # 텍스트 박스 배경 위치
                    text_height = 20
                    draw.rectangle([x1, y1 - text_height, x1 + 100, y1], fill="red")

                    # 텍스트 그리기
                    draw.text((x1 + 5, y1 - text_height + 2), confidence_text, fill="black", font=font)

                    # Streamlit에 표시
                    image_placeholder.image(image_with_box, caption=f"감정: {label}, 확률: {confidence:.2%}", use_container_width=True)
                else:
                    # 좌표 없을 경우 원본 그대로 표시
                    image_placeholder.image(image, caption=f"감정: {label}, 확률: {confidence:.2%}", use_container_width=True)
            else:
                st.error("API 요청 실패: 상태 코드 " + str(response.status_code))
        except Exception as e:
            st.error(f"API 요청 중 오류 발생: {e}")

st.markdown('</div>', unsafe_allow_html=True)
