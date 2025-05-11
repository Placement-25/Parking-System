#include <Servo.h>
Servo Serv;
String myCmd;
int echoPin = 9;  // IR sensor digital pin
int pinServo = 6; // Servo motor pin
int trigPin = 10;
int ledPin = 3;
int duration;
int distance;
String one = "1";
String zero = "0";

void setup() {
  Serv.attach(pinServo);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration * 0.034 / 2);
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.print(" cm");
  Serial.println();
  while (Serial.available() == 0) {
  }
  myCmd = Serial.readStringUntil('\n');
  myCmd.trim(); // Remove leading/trailing white space
  Serial.println(myCmd);
  if (myCmd == one) {
    if (distance < 12) {
      Serv.write(0);
      digitalWrite(ledPin, HIGH);
      delay(100);
    } else {
      Serv.write(90);
      digitalWrite(ledPin, LOW);
      delay(100);
    }
  }
}
