#include <PETEletrica.h>

int trigger = 3, echo = 2;
int IN1 = 4, IN2 = 5, IN3 = 6, IN4 = 7;
float d = 0;
SensorUltrassonico ultrassonico(trigger, echo);
Motores motor(IN1, IN2, IN3, IN4);

void setup() {
 Serial.begin(9600); 
 }

void loop() {

  long microsec = ultrassonico.timing();
  d = ultrassonico.convert(microsec, SensorUltrassonico::CM);
  delay(10);
  Serial.print("Distância: ");
  Serial.println(d);
  delay(250); 
  motor.set_motors(0, 100);

while (d < 5 ||  d > 18) {
  long microsec = ultrassonico.timing();
  d = ultrassonico.convert(microsec, SensorUltrassonico::CM);
  delay(10);
  Serial.print("Distância: ");
  Serial.println(d);
  delay(250); 
  motor.set_motors(0, 0);
}
}
