# 블록 체인

## 블록 체인은 무엇인가요?
블록체인은 **데이터 분산 처리 기술**입니다. 즉, 네트워크에 참여하는 모든 사용자가 모든 거래 내역 등의 데이터를 분산, 저장하는 기술을 지칭하는 말입니다. 블록들을 체인 형태로 묶은 형태이기 때문에 블록체인이라는 이름이 붙었습니다. 블록체인에서 '블록'은 개인과 개인(P2P)의 데이터가 기록되는 장부가 됩니다. 이런 블록들은 형성된 후 시간의 흐름에 따라 순차적으로 연결된 '사슬(체인)'의 구조가 됩니다. 모든 사용자가 거래내역을 보유하고 있어 거래 내역을 확인할 때는 모든 사용자가 보유한 장부를 대조하고 확인해야 합니다. 이 때문에 블록체인은 '공공 거래장부' 또는 '분산 거래 장부'로 불리기도 합니다.

## 기존 거래와 블록 체인의 차이점은?
기존 거래 방식은 은행이 모든 거래 내역을 가지고 있었습니다. 만약 A가 B에게 10만원을 송금한다고 하면 현재 금융 시스템에서는 은행이 중간 역할을 합니다. 왜냐하면 A가 B에게 10만원을 줬다는 사실을 '증명'해 주어야 하기 때문이죠. 따라서 두 사람 사이에 안전하게 거래할 수 있도록 은행이 중간 역할을 해주는 것입니다.
<br><br>
블록체인도 거래 내역을 저장하고 증명합니다. 그러나 거래 내역을 은행이 아닌 여러명이 나눠서 저장을 합니다. 만약 한 네트워크에 10명이 참여하고 있다면 A와 B의 거래 내역을 10개의 블록을 생성해 10명 모두에게 전송, 저장합니다. 나중에 거래 내역을 확인할 때는 블록으로 나눠 저장한 데이터들을 연결해 확인합니다.

## 블록 체인의 특징은?
블록 체인은 **분산 저장**을 한다는 점이 특징입니다. 기존 거래 방식에서는 데이터를 위·변조하기 위해서는 은행의 중앙서버를 공격하면 가능했습니다. 최근 몇몇 은행 전산망 해킹 사건이 일어났다는 점을 생각해보면 현실적인 위협인 셈이죠. 그러나 블록체인은 여러 명이 데이터를 저장하기 때문에 위·변조가 어렵습니다. 블록 체인 네트워크를 위·변조하기 위해서는 참여자의 거래 데이터를 모두 공격해야 하기 때문에 사실상 해킹은 불가능하다고 여겨집니다.
<br><br>
또한 블록 체인은 **중앙 관리자가 없다**는 점도 특징으로 꼽힙니다. 은행이나 정부 등 중앙 기관이나 중앙 관리자가 필요했던 것은 공식적인 증명, 등기, 인증이 필요했기 때문이죠. 그러나 블록 체인은 다수가 데이터를 저장, 증명하기 때문에 중앙 관리자가 존재하지 않게 됩니다.

## 블록 체인, 비트 코인 탄생의 일등 공신
비트 코인과 같은 가상 화폐가 등장하게 된 것도 블록 체인 덕분입니다. 블록 체인을 사용하게 되면 중앙 기관의 역할이 필요 없어지기 때문에 '중앙 은행'이 없더라도 화폐 발행이 가능하게 된거죠. 비트 코인의 경우 이를 발행한 기관도 통제하는 기관도 없습니다. '나카모토 사토시'라는 개발자가 비트 코인 네트워크를 만들었을 뿐입니다. 비트코 인을 원하는 사람들이 직접 '채굴'을 통해 '발행'할 수 있죠. 이는 중앙 은행이 없이도 화폐 발행, 유통이 가능하다는 점을 실제로 보여줬습니다.
<br><br>
일각에서는 블록체인이 중앙 기관과 은행을 대체할 것이라는 극단적인 전망을 하기도 합니다. 하지만 당장 블록체인이 모든 중앙 기관을 대체하기에는 어려울 것으로 보입니다. 현재 비트 코인도 화폐 가치가 매일 몇 십만 단위로 오르락내리락 하면서 투기성이 지적되고 있는 등의 부정적인 측면이 발생하고 있기 때문이죠. 하지만 블록체인이 가진 높은 신뢰성과 보안성 덕분에 네트워크를 더 안전하게 만드는 기술로 산업 전분야에 확산될 것으로 보입니다.

------------------------------------------------------------------------------------------------------------------------------------------
# 블록 체인 클래스

## 시작하기 전에
 블록 체인은 변경 불가능하고 블록이라고 불리우는 기록의 연속된 체인이다. 블록체인에는 거래, 파일 그리고 당신이 원하는 데이터(그게 뭐든지)들을 포함하고 있다. 중요한 것은 "해쉬"를 이용해서 다 같이 "연결되어져" 있다는 것이다. 

## 블록은 어떻게 생겼는가?
각 블록은 인덱스, 타임스탬프(UNIX Time), 거래 내역, 증명 그리고 이전 블록의 해쉬를 가지고 있다. 각 블록은 이전 블록의 해쉬를 모두 포함하고 있다. 이 특징은 상당히 중요하다. 왜냐하면 위 코드가 바로 블록 체인에 **변경 불가능성**을 넣어주기 때문이다. 만약 공격자가 체인에서 특정 블록의 정보를 변경시키려고 한다면, 그에 부속된 모든 체인들이 잘못된 해쉬를 갖게될 것이다.

## 작업 증명(PoW: Proof of Work)에 대한 이해
작업 증명 알고리즘(PoW)는 어떻게 새 블록이 생성되고 채굴되는지를 보여주는 알고리즘이다. PoW의 목표는 문제를 푸는 숫자, 즉 답을 찾는 것이다. 그 숫자는 찾기 어렵지만, 네트워크 내의 누구에 의해서라도 증명은 쉬워야 할 것이다. 이것이 PoW의 핵심 아이디어이다.
<br><br>
이는 이전 proof의 값에 더하여 앞에서 0을 4개 갖는 해쉬 값을 갖게하는 새로운 proof 값을 구하여라 등과 같은 방법으로 구현할 수 있다.

------------------------------------------------------------------------------------------------------------------------------------------
# API 로서의 블록 체인






































