
 
void setup() {
// put your setup code here, to run once: 
  Serial.begin(9600);
  pinMode(5,OUTPUT);
  pinMode(4,OUTPUT);
  
}
 
void loop() {
// put your main code here, to run repeatedly:
int voltage_value0 = analogRead(5);
int voltage_value1 = analogRead(4);
 
 int subraction_value =(voltage_value0 - voltage_value1) ;
 float temp_val = (subraction_value*0.00488);
 
 float current_value = (temp_val/1);
 Serial.print ("Amper - ");
 Serial.println(current_value);
 
 delay(1000);
}
