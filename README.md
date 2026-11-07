---
id: manufacturing-ai-week4/README.md
title: "충북대학교 제조 AI 실제 (8884023-01) - 4주차 실습 및 과제"
repo: joseki-korea/manufacturing-ai-week4
device_scope: all
doc_type: readme
tags:
  - readme
  - documentation
status: DRAFT
updated: '2026-11-07'
source_of_truth: README.md
---

# 충북대학교 제조 AI 실제 (8884023-01) - 4주차 실습 및 과제

- **작성자**: 2026154001 정용석
- **교과목**: 제조 AI 실제 (8884023-01, 충북대학교 산업인공지능연구센터 김영진 교수)
- **주제**: 지도학습 (Learning Strategies: Supervised Learning)

---

## 📚 4주차 실습 노트북 목록

| 번호 | 실습 노트북 | 핵심 내용 및 실습 과제 |
|:---:|:---|:---|
| **Lab 4-1** | [lab4_1_regression_activation_and_loss.ipynb](./2026154001_정용석_lab4_1_regression_activation_and_loss.ipynb) | 회귀(Regression) 출력 활성화함수(Linear, ReLU, Sigmoid, Tanh) 및 손실함수(MSE, MAE, Huber) 비교 실습 |
| **Lab 4-2** | [lab4_2_classification_activation_and_loss.ipynb](./2026154001_정용석_lab4_2_classification_activation_and_loss.ipynb) | 분류(Classification) Logits, 활성화함수(Sigmoid/Softmax), 손실함수(BCE/CE) 및 다중 라벨 복합 고장 진단 |
| **Lab 4-3** | [lab4_3_challenging_problems.ipynb](./2026154001_정용석_lab4_3_challenging_problems.ipynb) | 지도학습 4대 도전과제 (20층 망 기울기 소실, 과적합 모델 복잡도/데이터셋 크기, 클래스 불균형 착시) |
| **Lab 4-4** | [lab4_4_techniques_for_challenging_problems.ipynb](./2026154001_정용석_lab4_4_techniques_for_challenging_problems.ipynb) | 도전과제 극복 기법 (ResNet Residual Connection, L1/L2 정규화, Dropout, Balanced Data Augmentation, Class Weighting) |

---

## 🎯 주요 실습 및 질문 답변 요약

### 1. 회귀(Regression) 문제의 물리적 도메인과 손실함수
- 비음수 물리량(전력량, 토크 등)에는 `ReLU`, 정규화된 잔여수명 비율($0 \sim 1$)에는 `Sigmoid`를 적용하여 물리적 위반을 방지.
- 센서 글리치(Spike Noise)가 존재하는 환경에서는 MSE 대신 MAE의 이상치 강건성과 MSE의 매끄러운 수렴성을 겸비한 `Huber Loss`가 가장 적합.

### 2. 분류(Classification) 문제와 Logits
- 상호 배타적 단일 결함 진단에는 전체 합 1.0을 보장하는 `Softmax` + `CategoricalCrossentropy` 적용.
- 여러 결함이 동시 발생 가능한 복합 고장 진단에는 각 결함별 독립 확률을 출력하는 뉴런별 `Sigmoid` + `BinaryCrossentropy` 적용 (Softmax 적용 시 동시 고장이 상호 억제되어 결함 누락 발생).

### 3. 기울기 소실과 ResNet 구조
- Sigmoid 심층망(20층)에서는 연쇄 법칙에 의해 그래디언트가 $0.25^{20}$ 수준으로 소실되어 학습이 불가능.
- `ReLU` 전환 및 ResNet의 지름길 연결($F(x) + x$)을 통해 역전파 기울기 식에 $+1$ 항이 보존되어 깊은 층에서도 안정적 수렴 달성.

### 4. 클래스 불균형과 정확도의 착시
- 양품이 96%인 불균형 데이터셋에서는 단순 모델이 모두 정상으로만 예측해도 96%의 높은 정확도 착시(Accuracy Paradox)가 발생.
- 50:50 균형 테스트셋에서는 실제 성능이 50% 수준으로 폭락함을 확인하였으며, 소수 클래스 검출을 위해 `Balanced Data Augmentation` 및 `Class Weighting`을 적용하여 Recall 및 F1-Score를 대폭 개선.