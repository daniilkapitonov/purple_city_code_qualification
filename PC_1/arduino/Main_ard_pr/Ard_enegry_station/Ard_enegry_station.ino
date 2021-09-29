// TCP клиент, передает данные из UART серверу, от сервера в UART
#include <Ethernet.h>

// определяем конфигурацию сети
byte macc[] = {0xAE, 0xB1, 0x32, 0xE0, 0x9A, 0x8C}; // MAC-адрес
byte ipp[] = {192, 168, 0, 105}; // IP-адрес клиента
byte ipServv[] = {192, 168, 0, 101}; // IP-адрес сервера

bool setting = true;
EthernetClient client; // создаем клиента

unsigned long period_time = 3000;
// переменная таймера, максимально большой целочисленный тип (он же uint32_t)
unsigned long my_timer;

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


void setup() {
  Ethernet.begin(macc, ipp); // инициализация контроллера
  Serial.begin(9600);
  
  Serial.println("connecting...");
  // устанавливаем соединение с сервером
  while (!client){
    if (client.connect(ipServv, 10000)) {
      Serial.println("connected"); // успешно
      client.flush();
    }
    else {
      Serial.println("connection failed"); // ошибка
    }
    delay (1000);
  }
  my_timer = millis();
  client.flush();
}

void loop() {
  // все, что приходит с сервера, печатаем в UART
  
  if (client.available() and setting) {
    //char chr = client.read();
    char test[8];
    strcpy(test, "");
    client.read(test, 8);
    //client.write(chr);
    int num = atoi(test);
    Serial.print("Получены данные - ");
    Serial.print(test);
    Serial.println();
    setting = true;
    if (num == 666){
        Serial.println("Запрос на место работы устройства");
        char send[8];
        strcpy(send, "energy_");
        client.write(send,sizeof(send)); 
        Serial.print(send);
        Serial.println();
        strcpy(test, "");
        client.flush();
    }
    if (num ==102){
      Serial.println();
      Serial.println("Сервер отключил устройство");
      client.stop();
      while (true); // останавливается
    }
    if (num ==404){
      Serial.println();
      Serial.println("Сервер перезагружает устройство");
      client.stop();
      setup();
    }
    if (num ==167){
      Serial.println();
      Serial.println("Сервер инициализировал устройство. Начало работы.");
      setting = false;
    }
    
  }

  if ((millis() - my_timer >= period_time) and not setting) {
    char test[16];   
    int num=0;
    char c_ma1[8], c_ma2[8];   
    RawValue1 = analogRead(analogIn1);
    Voltage1 = (RawValue1 / 1024.0) * 5000; // Gets you mV
    Amps1 = ((Voltage1 - ACSoffset) / mVperAmp);
    mA1 = Amps1 * 1000;
    if (mA1 < 200){
     mA1 = 0;
    }
    sprintf(c_ma1,"%d",mA1);
    
    RawValue2 = analogRead(analogIn2);
    Voltage2 = (RawValue2 / 1024.0) * 5000; // Gets you mV
    Amps2 = ((Voltage2 - ACSoffset) / mVperAmp);
    mA2 = Amps2 * 1000;
    if (mA2 < 200){
     mA2 = 0;
    }
    sprintf(c_ma2,"%d",mA2);
    int amp_energy_gen, wat_enegry_gen;
    amp_energy_gen = round(random(0,5000) / 1000 * 15);
    wat_enegry_gen = amp_energy_gen * 5;
    char war_en_c[20];
    sprintf(war_en_c,"%d",wat_enegry_gen);
    Serial.print("Send 1 ");     
    Serial.print("\t mA1 = "); 
    Serial.print(c_ma1);
    Serial.print("\t Send 2 "); 
    Serial.print("\t mA2 = "); 
    Serial.println(c_ma2);
    Serial.print("\t Send 3 "); 
    Serial.print("\t wat_gen = "); 
    Serial.println(war_en_c);
    strcpy(test, c_ma1);
    strcat(test, "+");
    strcat(test, c_ma2);
    strcat(test, "+");
    strcat(test, war_en_c);
    strcat(test, "_");
    Serial.print("Send_all ");
    Serial.println(test);
    client.write(test, sizeof(test));
    while (not client.available()){
      
    }
    char read_c[16];
    client.read(read_c,16);
    num = atoi(read_c);
    Serial.print("Получена команда - ");
    Serial.println(num);
    if (num ==102){
      Serial.println();
      Serial.println("Сервер отключил устройство");
      client.stop();
      while (true); // останавливается
    }
    if (num ==404){
      Serial.println();
      Serial.println("Сервер перезагружает устройство");
      client.stop();
      setup();
    }
    if (num ==167){
      Serial.println();
      Serial.println("Сервер инициализировал устройство. Начало работы.");
      setting = false;
    }
    
    strcpy(test, "");
    strcpy(c_ma1, "");
    strcpy(c_ma2, "");
    client.flush();
    my_timer = millis();
  }
  
  if (false) {
    //char chr = client.read();
    char test[16];
    client.read(test, 16);
    //client.write(chr);
    int num = atoi(test);
    Serial.print("Получены данные - ");
    Serial.print(test);
    Serial.print("Служебная команда - ");
    Serial.print(num);
    Serial.println();
    if (num ==102){
      Serial.println();
      Serial.println("Сервер отключил устройство");
      client.stop();
      while (true); // останавливается
    }
    if (num ==404){
      Serial.println();
      Serial.println("Сервер перезагружает устройство");
      client.stop();
      setup();
    }
    if (num ==167){
      Serial.println();
      Serial.println("Сервер инициализировал устройство. Начало работы.");
      setting = false;
    }
    client.write("ok_", 3);
    strcpy(test, "");
    client.flush();
  }


  // если сервер отключился, останавливаем клиент
  if (!client.connected()) {
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();
    while (true); // останавливается
  }
 
}
