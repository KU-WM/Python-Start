const questions = [
    "나는 사교적이고 외향적인 성격이다.",
    "나는 계획을 세우고 그것을 실행하는 것을 좋아한다.",
    "나는 새로운 아이디어에 관심이 많다.",
    "나는 타인의 감정을 잘 이해한다.",
    "나는 사실과 세부 사항을 중요시한다.",
    "나는 도전적인 문제를 해결하는 것을 즐긴다.",
    "나는 내 감정과 직관에 따라 행동하는 경우가 많다.",
    "나는 체계적이고 정리 정돈을 잘 한다.",
    "나는 결정을 내릴 때 논리적으로 생각한다.",
    "나는 규칙을 따르기보다는 자유롭게 행동하는 것을 선호한다."
];

const results = {
    E: "외향적인 성격으로, 사교적이고 에너지가 넘칩니다.",
    I: "내향적인 성격으로, 깊이 사고하고 조용한 환경을 선호합니다."
};

let currentQuestion = 0;
let scores = { E: 0, I: 0 };

document.getElementById("start-button").addEventListener("click", () => {
    document.getElementById("main-page").style.display = "none";
    document.getElementById("test-page").style.display = "block";
    loadQuestion();
});

document.getElementById("next-button").addEventListener("click", () => {
    const answer = document.querySelector('input[name="answer"]:checked');
    if (answer) {
        const score = parseInt(answer.value);
        scores.E += score; // 예: E 유형을 증가
        scores.I += 6 - score; // 반대 유형 계산
        currentQuestion++;
        if (currentQuestion < questions.length) {
            loadQuestion();
        } else {
            showResult();
        }
    } else {
        alert("답변을 선택해주세요!");
    }
});

document.getElementById("retry-button").addEventListener("click", () => {
    currentQuestion = 0;
    scores = { E: 0, I: 0 };
    document.getElementById("result-page").style.display = "none";
    document.getElementById("main-page").style.display = "block";
});

function loadQuestion() {
    document.getElementById("question-number").innerText = currentQuestion + 1;
    document.getElementById("question-text").innerText = questions[currentQuestion];
    document.querySelectorAll('input[name="answer"]').forEach(input => input.checked = false);
}

function showResult() {
    const resultType = scores.E > scores.I ? "E" : "I";
    document.getElementById("test-page").style.display = "none";
    document.getElementById("result-page").style.display = "block";
    document.getElementById("result-text").innerText = results[resultType];
}
