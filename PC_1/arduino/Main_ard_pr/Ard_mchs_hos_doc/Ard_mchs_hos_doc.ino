// TCP клиент, передает данные из UART серверу, от сервера в UART
#include <Ethernet.h>

// определяем конфигурацию сети
byte macc[] = {0xAE, 0xB3, 0x35, 0xE7, 0x1A, 0x1C}; // MAC-адрес
byte ipp[] = {192, 168, 0, 157}; // IP-адрес клиента
byte ipServv[] = {192, 168, 0, 100}; // IP-адрес сервера

bool setting = true;
EthernetClient client; // создаем клиента

void setup() {
  Ethernet.begin(macc, ipp); // инициализация контроллера
  Serial.begin(9600);
  Serial.println("connecting...");
  for(int i=0;i<16;i++){
      if (i>9){
        pinMode(i+5,OUTPUT);
        digitalWrite(i+5,1);
      }
    pinMode(i+2,OUTPUT);
    digitalWrite(i+2,1);
  }
  //pinMode(1,OUTPUT);
  //digitalWrite(2,0);
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
}

void loop() {
  // все, что приходит с сервера, печатаем в UART

  if (client.available() and setting) {
    //char chr = client.read();
    char test[8];
    client.read(test, 8);
    //client.write(chr);
    int num = atoi(test);
    Serial.print("Получены данные - ");
    Serial.print(num);
    Serial.println();
    setting = true;
    if (num == 666){
        Serial.println("Запрос на место работы устройства");
        char send[20];
        strcpy(send, "mchsdochospital_");
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
  if (client.available() and not setting) {
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
      setup();
      //while (true); // останавливается
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
    
    client.flush();
    Serial.println();
    int k=0;
     for(int i=0;i<16;i++){
      if (i>7){
        k=6;
      } else{
        k=2;
      }
      if (i==15){
       //k=-14;
      }
      Serial.print(test[i]);
      int val;
      val=test[i]-'0';
      Serial.print(val);
      Serial.print("  ");
      if(val==1){
        digitalWrite(i+k,0);
         Serial.print(i);
        Serial.print("OFF");
        Serial.print("  ");
      }
      if(val==0){
        Serial.print(i);
        Serial.print("ON");
        Serial.print("  ");
        digitalWrite(i+k,1);
      }
      
     }
    strcpy(test, "");
    Serial.println();
  }
  // если сервер отключился, останавливаем клиент
  if (!client.connected()) {
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();
    setup();
    //while (true); // останавливается
  }
 
}
