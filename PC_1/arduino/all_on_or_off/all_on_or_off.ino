void setup() {
  for (int i=2; i<18 ; i++){
    pinMode(i, OUTPUT);
  }
  for (int i=2; i<18; i++){
    digitalWrite(i, HIGH);
  }
  Serial.begin(9600);
}

void loop() {
  Serial.println(123);
  for (int i=2; i<18; i++){
    digitalWrite(i, LOW);
    delay(700);
  }
    delay(2000);
  for (int i=2; i<18; i++){
    digitalWrite(i, HIGH);
  }
    delay(2000);
}
