# AD-project 


## 프로젝트 주제 : GUI기반 2인 텍사스 홀덤


### 요구사항 분석
  기능
   * 자신의 차례, 소유 칩의 수, 패, 베팅 금액을 알 수 있어야한다.
   * GUI상 입력 공간이 헷갈리지 않아야한다.
   * 텍사스 홀덤 규칙 및 카드 게임 규칙에 반하는 버튼은 누르지 못하여야 한다.(미해결)
   
   로직
   * 필드에 배치되는 카드 및 플레이어의 카드 모두 랜덤값을 통해 예측 불가능한 값이여야 한다.
   * 불가능한 입력일 경우 입력을 받지 않고 메세지를 출력한다.(미해결)
   * 베팅은 한사람이 한번에 두번이상 하지 않도록 한다.

### 구조설계

|모듈|클래스|역할|
|------|---|---|
|cardlist.py|Cardlist|텍사스 홀덤 내 사용되는 카드를 생성|
|poker.py|Poker| 위젯 표시 및 텍사스 홀덤 내 기능 구현|
|user.py|User|cardlist의 카드를 필드, 유저에게 추출, 카드를 화면에 표시 할 수 있도록 반환|  

인터페이스 설계

|클래스|메서드|기능|
|------|---|---|
|Cardlist|-|카드 리스트 생성|
|Poker|clickCheak|베팅을 하지 않고 상대에게 턴을 넘김|
||clickCall|카드 리스트 생성|
||clickFold|해당 플레이어 게임 포기|
||clickRaise|베팅 금액을 올림|
||betting|clickCall, clickRaise에서 입력된 칩을 처리|
||startGame|게임 시작|
|User|playerChoice|베팅|
||flop|처음 3장의 카드 추출|
||turn|4번째 카드 추출|
||river|마지막 카드 추출|
||displayCard|플레이어 카드를 순서에 맞게 반환|
||displayField|필드 카드를 반환|

#### 테스트
  User부분의 간단한 입출력 밖에 테스트하지 못하였음

|Testcase|UUT|기능|Results|
|------|---|---|---|
|UT-1-1|self.player1|실행 시 제대로 생성 되는지 테스트|pass|
|UT-1-2|self.player2|실행 시 제대로 생성 되는지 테스트|pass|
|UT-1-3|self.player1|실행 시 제대로 생성 되는지 테스트|pass|
|UT-1-4|self.field|실행 시 제대로 생성 되는지 테스트|pass|
|UT-2-1|playerChoice()|실행 시 제대로 생성 되는지 테스트|pass|
|UT-2-1|flop()|실행 시 리스트 안에 값이 저장되는지, 상황에 맞게 작동하는지|pass|
|UT-2-1|turn()|실실행 시 리스트 안에 값이 저장되는지, 상황에 맞게 작동하는지|pass|
|UT-2-1|river()|실행 시 리스트 안에 값이 저장되는지, 상황에 맞게 작동하는지|pass|



동작영상 https://youtu.be/CYsnLkad1t8


