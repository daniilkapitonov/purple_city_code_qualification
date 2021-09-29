// TCP клиент, передает данные из UART серверу, от сервера в UART
#include <Ethernet.h>

// определяем конфигурацию сети
byte macc[] = {0xAE, 0xB1, 0x96, 0xE6, 0x4A, 0x6C}; // MAC-адрес
byte ipp[] = {192, 168, 0, 176}; // IP-адрес клиента
byte ipServv[] = {192, 168, 0, 100}; // IP-адрес сервера

bool setting = true;
EthernetClient client; // создаем клиента

void setup() {
  Ethernet.begin(macc, ipp); // инициализация контроллера
  Serial.begin(9600);
  Serial.println("connecting...");
  
  pinMode(5,OUTPUT);
  digitalWrite(5,0);
  pinMode(4,OUTPUT);
  digitalWrite(4,0);
  pinMode(9,OUTPUT);
  //pinMode(1,OUTPUT);
  //digitalWrite(0,0);
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
        char send[8];
        strcpy(send, "ges_");
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
    Serial.println(analogRead(9));
    client.write("ok_", 3);
    
    client.flush();
    Serial.println();
    int k=0;
     for(int i=0;i<2;i++){
      Serial.print(test[i]);
      int val;
      val=test[i]-'0';
      Serial.print("  ");
      Serial.print(val);
      Serial.print("  ");
      if(val==1){
        digitalWrite(i+4,0);
        Serial.print(i);
        Serial.print("OFF");
        Serial.print("  ");
      }
      if(val==0){
        Serial.print(i);
        Serial.print("ON");
        Serial.print("  ");
        digitalWrite(i+4,1);
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
