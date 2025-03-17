import streamlit as st
import openai
import requests

# OpenAI API 키 설정
OPENAI_API_KEY = "REST_API"
openai.api_key = OPENAI_API_KEY

# 카카오 로그인 설정
KAKAO_CLIENT_ID = "REST_API"
KAKAO_REDIRECT_URI = "http://localhost:8501/"
KAKAO_AUTH_URL = f"https://kauth.kakao.com/oauth/authorize?client_id={KAKAO_CLIENT_ID}&redirect_uri={KAKAO_REDIRECT_URI}&response_type=code"

# 세션 초기화
if "user_info" not in st.session_state:
    st.session_state.user_info = None

st.title("🌟 NBTI 성격 유형 검사")
st.markdown("---")

# 카카오 로그인
if st.session_state.user_info is None:
    st.markdown(f'<a href="{KAKAO_AUTH_URL}" target="_self"><button style="background-color:#FEE500; border:none; padding:10px; border-radius:5px; cursor:pointer;">카카오 로그인</button></a>', unsafe_allow_html=True)
else:
    if st.session_state.user_info and 'nickname' in st.session_state.user_info:
        st.write(f"👤 환영합니다, {st.session_state.user_info['nickname']}님!")
    else:
        st.write("사용자 정보를 불러올 수 없습니다.")
        st.write(st.session_state)

    # st.write(f"👤 환영합니다, {st.session_state.user_info['nickname']}님!")

# OAuth 인증 처리
query_params = st.query_params.to_dict()
if "code" in query_params:
    code = query_params["code"]
    token_url = "https://kauth.kakao.com/oauth/token"
    token_data = {
        "grant_type": "authorization_code",
        "client_id": KAKAO_CLIENT_ID,
        "redirect_uri": KAKAO_REDIRECT_URI,
        "code": code,
    }
    token_headers = {"Content-Type": "application/x-www-form-urlencoded"}
    token_response = requests.post(token_url, data=token_data, headers=token_headers)
    access_token = token_response.json().get("access_token")
    
    if access_token:
        user_info_url = "https://kapi.kakao.com/v2/user/me"
        user_info_headers = {"Authorization": f"Bearer {access_token}"}
        user_info_response = requests.get(user_info_url, headers=user_info_headers)
        st.session_state.user_info = user_info_response.json().get("kakao_account", {}).get("profile", {})
        st.rerun()

# 질문 리스트
questions = [
    {"text": "나는 새로운 사람을 만나는 것이 즐겁다.", "type": "E"},
    {"text": "나는 세부 사항보다 전체적인 그림을 보는 것을 좋아한다.", "type": "N"},
    {"text": "나는 결정을 내릴 때 감정보다 논리를 우선시한다.", "type": "T"},
    {"text": "나는 계획적으로 행동하는 것을 선호한다.", "type": "J"},
    {"text": "나는 혼자 있는 시간을 즐긴다.", "type": "I"},
    {"text": "나는 현실적인 정보를 중요하게 생각한다.", "type": "S"},
    {"text": "나는 감정을 중시하는 편이다.", "type": "F"},
    {"text": "나는 즉흥적으로 행동하는 편이다.", "type": "P"},
    {"text": "나는 빠른 결정을 내리는 것을 선호한다.", "type": "J"},
    {"text": "나는 아이디어를 떠올리는 것을 좋아한다.", "type": "N"}
]

# 상태 초기화
if "scores" not in st.session_state:
    st.session_state.scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "answers" not in st.session_state:
    st.session_state.answers = [None] * len(questions)

if not st.session_state.show_result:
    q = questions[st.session_state.current_question]
    progress = (st.session_state.current_question + 1) / len(questions)
    
    st.progress(progress)  # 진행률 표시
    
    with st.container():
        st.subheader(f"**{st.session_state.current_question + 1}. {q['text']}**")
        
        answer = st.radio("답변을 선택하세요:", ["1 - 전혀 아니다", "2 - 아니다", "3 - 보통이다", "4 - 그렇다", "5 - 매우 그렇다"], index=None if st.session_state.answers[st.session_state.current_question] is None else int(st.session_state.answers[st.session_state.current_question])-1)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅ 이전", disabled=st.session_state.current_question == 0):
            st.session_state.current_question -= 1
            st.rerun()
    
    with col2:
        if st.button("다음 ➡"):
            if answer is None:
                st.warning("답변을 선택해주세요.")
            else:
                prev_answer = st.session_state.answers[st.session_state.current_question]
                if prev_answer is not None:
                    st.session_state.scores[q["type"]] -= int(prev_answer)  # 이전 선택값 제거
                
                st.session_state.answers[st.session_state.current_question] = answer[0]  # 현재 선택 저장
                st.session_state.scores[q["type"]] += int(answer[0])  # 새로운 선택 반영
                
                st.session_state.current_question += 1
                if st.session_state.current_question >= len(questions):
                    st.session_state.show_result = True
                st.rerun()
