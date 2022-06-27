# AT90CAN

내가 사용한 것은 Atmel사의 AVR 시리즈

### AVR 개발 환경 및 IO 제어를 통한 보드 사용법

##### 개발 환경

AVRstudio, Toolchain, USBtoSerial Driver

##### 기본적인 IO 제어

DDRx, PORTx 레지스터 제어를 통한 기본적인 IO 동작 이해

### 

### Micro Processor 및 Micro Controller 개념

##### Micro Processor

- 프로세서를 하나의 칩안에 집적하여 넣은 소형 형태
- 컴퓨터의 발전과 함꼐 고성능의 프로세서로 발전



##### Micro Controller Unit

개념

- 지능의 소형화를 위하여, 마이크로 프로세서에 메모리와 주변장치 제어 모듈을 함께 넣은 칩
- 마이크로 프로세스 코어, 여러가지 크기와 다양한 종류의 메모리, 여러 종류의 주변장치. 여러 종류의 입출력 포트를 하나의 칩에 집적
- 여러 응용 분야에 필요한 주변 장치 제어 모듈 제공

특징

- 주변 장치를 센싱 및 제어 하기 위한 I/O능력 강화
- Timer/Counter, 통신포트 내장 및 인터럽트 처리 능력 보유
- Bit 조작 강화
- 저렴, 소형, 경향, 융통성 및 확장성 용이(by 프로그램 변경), 신뢰성



##### AVR MC

개념

- ATMEL사가 1997년 발표한 8비트 제어용 마이크로 프로세서

특징

- RISC(Reduced Instruction Set Computer) 구조
- 32개의 8비트 범용 레지스터를 가지는 레지스터 중심형 구조
- CMOS 기술 채택으로 소비전력이 적고, 동작 전압이 1.8~5.5로 큼



##### AT98CAN128 Micro Controller

개념

- Atmel 사의 8-bit RISC기반 Micro Controller
- 16MHz Operatining frequency
- CAN 통신 가능

특징

- 고성능 저전력



### 사용한 모듈

##### CDS/Temp Sensor

- 조도 및 온도 감지
- 빛의 세기가 커질수록 저항의 크기는 작아지는 광 가변저항



##### DC motor/Servo motor

- Servo motor란 모터와 제어구동 모드(내부 제어 회로와 알고리즘)를 포함하는 것으로 명령에 따라 정확한 위치와 속도를 맞출 수 있다. 이때 모터가 회전하는 정도는 모터에게 가하는 PWM 신호에 의해 결정된다.
- Dc motor란 들어오는 두 입력이 서로 다를 경우 돌아가게 되는 일반적인 모터이다.



##### Ultrasonic Sensor

- 초음파, 거리 센서

##### 

##### Joystick

- 조이스틱을 작동할 시, 그 내부에 있는 저항의 값이 바뀌게 되는데, 이로 인해 전압 값에도 영향을 주어 그 변한 값이 각각 JS_1과 JS_2으로 들어가게 되어 그 변한 값을 읽어낼 수가 있게 된다. 이 때, 하나는 x축, 다른 하나는 y축을 담당하게 된다. 즉, 두 개의 가변저항이라고 여길 수도 있다.



##### 3D Accelerator, LED



# GPIO

### 개념

- General Purpose Input Output

- 범용으로 사용되는 입출력 포트
- 입출력 마음대로 선택, 0과 1로 출력 신호를 임의로 만들어 줄 수 있는 구조
- 입력으로 사용할 경우, 외부 인터럽트를 처리할 수 있도록 하는 경우 많음
- 입출력 방향 전환용 레지스터와, 입출력 데이터 레지스터 등이 필요
- 대부분 핀들은 GPIO로 설정

### 입출력 포트 제어용 레지스터

##### DDRx 레지스터

- 입출력의 방향 설정을 하기 위한 레지스터
- DDRA~DDRG 레지스터의 해방 비트에 1-출력, 0-입력으로 설정

##### PORTx 레지스터

- 데이터를 출력하기 위한 레지스터
- 출력을 원하는 데이터 값을 PORTx 레지스터에 넣음

##### PIN 레지스터

- 데이터 입력용 레지스터
- PINx 레지스터에 해당하는 값을 읽으면 해당 핀의 값이 읽어진다.



# PWM

### 개념

- Pulse width Modulation
- 펄스폭 변조로써, on/off 비율을 변화시켜 제어하는 방식
- DC모터 속도 제어, LED 조명의 광량 제어등



# USART 직렬 통신 포트

### 개념

- Universal Synchronous and Asynchronous Receiver and Transmitter
- 동기 및 비동기 전송 모드에서 전이중 통신 가능(full-duplex)



### UsART0 I/O Data Register

- UDRn으로 명명



### Control and Status Register A

- UCSRnA로 명명
- 송 수신 동작을 제어하거나 송수신 상태를 저장

##### RXCn(Receive Complete)

- 수신 버퍼에 읽혀지지 않은 수신 문자가 들어있음 1

##### TXCn(Transmit Complete)

- 송신 시프트 레지스터에 있는 송신 데이터가 모두 송신되고 UDRn 송신
- 버퍼에 송신데이터가 라이트 되지 않은 상태 1

##### UDREn(Data Register Empty)

- UDRn의 송신 버퍼가 비어있으면 1

##### FEn(Frame Error)

- UDRn의 수신 버퍼에 현재 저장되어 있는 데이터를 수신하는 동안 프레임 에러 발생 시, (스톱 비트가 0으로 검출되면 발생)

##### DORn(USARTn Data Overrun Error)

- 수신 동작에서 오버런 에러가 발생시

##### UPEn(Parity Error)

- 패러티 에러 발생시

##### U2Xn(Double the USARTn Transmission Speed)

- 비동기 모드에서만 유효, 클럭 분주비를 16->8로 전송 속도 2배

##### MPCMn(Multi-Processor Communication Mode)

- 멀티 프로세서 통신 모드 설정

...많다



# CAN 통신

### 개념

- Controller Area Network

- USART는 일대일 통신이므로, 서로 다른 다수의 통신 방식으로 적합하지 않아 다중 통신 방식이 요구되어 개발

### 특징

- 경제적 솔루션
- 우수한 신뢰성
- 표준화
- 실시간성, 전송 요청과 실제 전송 시작 사이의 짧은 지연 시간
- 유연성, Multi-Master 구조 가능, 모든 노드들이 독립적, 노드 연결/분리 용이
- 다중 전송/방송 성능 , 모든 노드에 메시지 전송, 모두 수신 가능

### 

### 송신

1. 초기화
2. Message Object 설정
3. 채널 스캔(가장 우선권을 높은 Mob를 찾는다)
   - 불가 모드
   - 전송 모드
   - 수신 모드
   - 자동응답 모드
   - 프레임 버퍼 수신 모드
4. 전송완료 인터럽트 발생
5. 대기



### 수신

1. 초기화
2. Mob 설정
3. 채널 스캔
4. Mob 갱신
5. 수신완료 인터럽트 발생
6. 대기



# MATLAB SIMULINK

Finite State Machine으로 디자인된 시스템

몇 개의 스테이트와 그 사이의 트랜지션으로 구성

