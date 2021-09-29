 int red = 200;
 int green = 0;
 int blue = 100;
 int r = 11;
 int g = 10;
 int b = 9;
 void setup() {
  pinMode(r, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(b, OUTPUT);

  analogWrite(r, red);
  analogWrite(g, green);
  analogWrite(b, blue);
  
}

void loop() {
  
}
