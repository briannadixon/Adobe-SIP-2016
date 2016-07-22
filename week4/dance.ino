#include <Servo.h>

Servo servoRight;
Servo servoLeft;

void forward() {
 servoLeft.writeMicroseconds(1700);
 servoRight.writeMicroseconds(1300);
}

void back() {
 servoLeft.writeMicroseconds(1300);
 servoRight.writeMicroseconds(1700);
}

void left() {
 servoLeft.writeMicroseconds(1700);
 servoRight.writeMicroseconds(1700);
}

void right() {
 servoLeft.writeMicroseconds(1300);
 servoRight.writeMicroseconds(1300);
}

void bot_stop() {
 servoLeft.writeMicroseconds(1500);
 servoRight.writeMicroseconds(1500);
}

void beginning(){
  forward();
  delay(300);
  right();
  delay(300);
}

void work(){
  left();
}
void setup() {
  // put your setup code here, to run once:
  servoLeft.attach(12);
  servoRight.attach(11);
}


void loop() {
  for (int j = 0; j <30; j++) {
    left();
    delay(60);
    forward();
    delay(100);
    right();
    delay(30);
    back();
    delay(30);
  }
  for (int i = 0; i<10; i++){
    forward();
    delay(300);
    right();
    delay(300);
  }
  for (int j = 0; j <30; j++) {
    left();
    delay(60);
    forward();
    delay(100);
    right();
    delay(60);
    back();
    delay(30);
    }
 
  for (int b =0; b<10; b++) {
    forward();
    delay(50);
    back();
    delay(30);
    }
  
}
