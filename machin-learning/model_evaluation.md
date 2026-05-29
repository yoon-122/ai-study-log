# Model Evaluation

머신러닝 모델은 보통 데이터를 다음과 같이 나눠서 사용한다.

- Training Data
- Validation Data
- Test Data

## Training Data
모델이 실제로 학습하는 데이터.

예를 들어:
- 문제 풀이 연습
- 패턴 학습

---

## Validation Data
모델 성능을 조정하기 위한 데이터.

학습률, 은닉층 수 같은
하이퍼파라미터를 조정할 때 사용한다.

즉: 모델 튜닝용 데이터.

---

## Test Data
모델이 처음 보는 데이터.

실제 성능을 평가하는 단계에서 사용한다.

책에서는:
- Training = 문제집
- Validation = 모의고사
- Test = 수능

느낌으로 설명했다.

---

## 느낀 점
처음에는 그냥 학습시키고 테스트만 하면 되는 줄 알았는데,
검증 데이터가 따로 존재하는 필요성과 이유를 이해하게 됐다.