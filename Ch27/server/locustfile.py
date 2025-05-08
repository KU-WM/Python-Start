# 가상환경에서 파일 위치가 있는 디렉토리로 cd
# locust -f locustfile.py
# locust -f (실행파일.py)

# Locust: 부하 테스트 프레임워크에서 필요한 클래스 임포트
from locust import HttpUser, TaskSet, task, between

# PIL을 사용하여 이미지 파일을 열기 위해 import
from PIL import Image
import io
import random  # (사용되지 않음. 필요시 제거 가능)

# 실제 테스트 작업들을 정의하는 클래스
class PredictTaskSet(TaskSet):
    # 테스트 시작 시 실행되는 초기화 함수
    def on_start(self):
        # 테스트에 사용할 이미지 파일을 미리 읽어와 메모리에 저장
        with open("C:\\Users\\human\\Downloads\\test2.jpg", "rb") as f:
            self.image_bytes = f.read()  # 이미지 바이트 저장

    # Locust가 호출할 작업(task)을 정의
    @task
    def predict(self):
        # multipart/form-data 형식으로 이미지 파일을 준비
        files = {
            "file": ("image.jpg", io.BytesIO(self.image_bytes), "image/jpeg")
        }

        # /predict 엔드포인트로 POST 요청 보내기 (catch_response=True로 수동 응답 체크)
        with self.client.post("/predict", files=files, catch_response=True) as response:
            if response.status_code != 200:
                # 상태 코드가 200이 아니면 실패로 간주
                response.failure(f"예상치 못한 상태 코드: {response.status_code}")
            else:
                data = response.json()
                if "confidence" not in data:
                    # 응답 JSON에 'results' 필드가 없으면 실패로 간주
                    response.failure("결과 필드 누락")
                else:
                    # 모든 조건을 만족하면 성공으로 표시
                    response.success()

# 실제 유저 시뮬레이션을 담당하는 클래스 정의
class WebsiteUser(HttpUser):
    tasks = [PredictTaskSet]         # 유저가 수행할 task 목록
    wait_time = between(1, 3)        # 각 요청 사이의 대기 시간 (초 단위) → 랜덤하게 1~3초
    host = "http://127.0.0.1:8000"   # 테스트할 FastAPI 서버 주소
