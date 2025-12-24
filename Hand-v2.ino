#include <Wire.h>                     // Подключаем библиотеку Wire
#include <Adafruit_PWMServoDriver.h>  // Подключаем библиотеку Adafruit_PWMServoDriver

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40);  // Установка адреса I2C 0x40

#define SERVOMIN 150  // Минимальная длительность импульса для сервопривода
#define SERVOMAX 600  // Максимальная длина импульса для сервопривода
#define SERVO_0 0     // Номер порта (0 - 15)
#define SERVO_1 1
#define SERVO_2 2
#define SERVO_3 3
#define SERVO_4 4
#define SERVO_5 5
#define SERVO_6 6
#define SERVO_7 7

String c;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pwm.begin();         // Инициализация
  pwm.setPWMFreq(60);  // Частота следования импульсов 60 Гц
  delay(10);           // Пауза
  Serial.begin(115000);
  char c = Serial.read();
  for (uint16_t pulselen = SERVOMIN; pulselen < SERVOMAX; pulselen++) {
    pwm.setPWM(SERVO_0, 0, pulselen);
    pwm.setPWM(SERVO_1, 0, pulselen);
    pwm.setPWM(SERVO_2, 0, pulselen);
    pwm.setPWM(SERVO_3, 0, pulselen);
    pwm.setPWM(SERVO_4, 0, pulselen);
    pwm.setPWM(SERVO_5, 0, pulselen);
    pwm.setPWM(SERVO_6, 0, pulselen);
    pwm.setPWM(SERVO_7, 0, pulselen);
  }
}


void loop() {
  if (Serial.available() > 0) {
    c = Serial.readString();
  }
  char a1 = c[0];
  char a2 = c[1];
  char a3 = c[2];
  digitalWrite(LED_BUILTIN, HIGH);
  if (a1 == '1') {
    digitalWrite(LED_BUILTIN, LOW);
    int pulselen = SERVOMIN;
    pwm.setPWM(SERVO_0, 0, pulselen);
    pwm.setPWM(SERVO_1, 0, pulselen);
    pwm.setPWM(SERVO_2, 0, pulselen);
    pwm.setPWM(SERVO_3, 0, pulselen);
    pwm.setPWM(SERVO_4, 0, pulselen);
  };
  if (a1 == '0') {
    digitalWrite(LED_BUILTIN, LOW);
    int pulselen = SERVOMAX;
    pwm.setPWM(SERVO_0, 0, pulselen);
    pwm.setPWM(SERVO_1, 0, pulselen);
    pwm.setPWM(SERVO_2, 0, pulselen);
    pwm.setPWM(SERVO_3, 0, pulselen);
    pwm.setPWM(SERVO_4, 0, pulselen);
  };
  if (a1 == '2') {
    digitalWrite(LED_BUILTIN, LOW);
    int pulselen = SERVOMIN;
    pwm.setPWM(SERVO_0, 0, pulselen/2);
    pwm.setPWM(SERVO_1, 0, pulselen/2);
    pwm.setPWM(SERVO_2, 0, pulselen/2);
    pwm.setPWM(SERVO_3, 0, pulselen/2);
    pwm.setPWM(SERVO_4, 0, pulselen/2);
  };
  if (a2 == '1') {
    int pulselen = SERVOMIN;
    pwm.setPWM(SERVO_5, 0, pulselen);
  };
  if (a2 == '0') {
    int pulselen = SERVOMAX;
    pwm.setPWM(SERVO_5, 0, pulselen);
  };
    if (a2 == '2') {
    int pulselen = SERVOMIN;
    pwm.setPWM(SERVO_5, 0, pulselen/2);
  };
  if (a3 == '1') {
    int pulselen = SERVOMIN;
    pwm.setPWM(SERVO_6, 0, pulselen);
  };
  if (a3 == '0') {
    int pulselen = SERVOMAX;
    pwm.setPWM(SERVO_6, 0, pulselen);
  }
    if (a3 == '2') {
    int pulselen = SERVOMIN;
    pwm.setPWM(SERVO_6, 0, pulselen/2);
  };
}