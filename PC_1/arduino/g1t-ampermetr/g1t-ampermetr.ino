
const int analogIn1 = A0;
const int analogIn2 = A1;
int mVperAmp = 100; // use 185 for 5A Module, 100 for 20A Module, 66 for 30A Module
int RawValue1 = 0;
int RawValue2 = 0;
int ACSoffset = 2500; 
double Voltage1 = 0;
double Amps1 = 0;
double mA1 = 0;
double Voltage2 = 0;
double Amps2 = 0;
double mA2 = 0;

void setup(){ 
 Serial.begin(9600);
}

void loop(){
 
 RawValue1 = analogRead(analogIn1);
 Voltage1 = (RawValue1 / 1024.0) * 5000; // Gets you mV
 Amps1 = ((Voltage1 - ACSoffset) / mVperAmp);
 mA1 = Amps1 * 1000;
 if (mA1 < 0){
   mA1 = 0;
 }

 RawValue2 = analogRead(analogIn2);
 Voltage2 = (RawValue2 / 1024.0) * 5000; // Gets you mV
 Amps2 = ((Voltage2 - ACSoffset) / mVperAmp);
 mA2 = Amps2 * 1000;
 if (mA2 < 0){
   mA2 = 0;
 }
 

 Serial.print("1 = "); 
 Serial.print(RawValue1);
 Serial.print("\t mV1 = "); 
 Serial.print(Voltage1);
 Serial.print("\t mA1 = "); 
 Serial.print(mA1);
 Serial.print("\t 2 = "); 
 Serial.print(RawValue2);
 Serial.print("\t mV2 = "); 
 Serial.print(Voltage2);
 Serial.print("\t mA2 = "); 
 Serial.println(mA2);
 delay(500); 
 
}
