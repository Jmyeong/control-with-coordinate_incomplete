#include <cvzone.h>

void setup() {
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()){
    char data = Serial.read();
    if(data == 'a') digitalWrite(9,HIGH);
    else if(data == 'b') digitalWrite(10,HIGH);
    else if(data == 'c') digitalWrite(11,HIGH);
    else if(data == 'd') digitalWrite(12,HIGH);
    delay(1000);
    digitalWrite(9,LOW);
    digitalWrite(10,LOW);
    digitalWrite(11,LOW);
    digitalWrite(12,LOW);
  }
}
