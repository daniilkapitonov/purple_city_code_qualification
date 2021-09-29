void setup() {
  for (int i=2; i<9; i++){
    pinMode(i, OUTPUT);
  }
  for (int i=2; i<9; i++){
    digitalWrite(i, HIGH);
  }
}

void loop() {
 for (int i=2; i<9; i++){
    digitalWrite(i, LOW);
    delay(300);
    digitalWrite(i, HIGH);
    delay(300);
  }
  for (int i=2; i<9; i++){
    digitalWrite(i, LOW);
    delay(100);
  }
    delay(1000);
  for (int i=2; i<9; i++){
    digitalWrite(i, HIGH);
  }
    delay(1000);
}
