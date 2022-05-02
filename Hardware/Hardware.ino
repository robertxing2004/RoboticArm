#include <Stepper.h>
int stepsPerRevolution = 2048;
int motSpeed = 10;
Stepper motor1(stepsPerRevolution, 8, 10, 9, 11);
Stepper motor2(stepsPerRevolution, A0, A2, A1, A3);

void setup() {
  //Serial Setup
  Serial.begin(9600);
  Serial.setTimeout(10);
  motor1.setSpeed(motSpeed);
  motor2.setSpeed(motSpeed);
}

void loop() {
  while (!Serial.available()){} //Wait until incomming message
  int x = Serial.parseInt(); //Store the position value as x
  motor1.step(x);
  motor2.step(-x);
  
  Serial.println(x);
}
