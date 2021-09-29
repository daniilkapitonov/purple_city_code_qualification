// TCP клиент, передает данные из UART серверу, от сервера в UART
#include <Ethernet.h>

// определяем конфигурацию сети
byte macc[] = {0xAE, 0xB5, 0x36, 0xE7, 0x4A, 0x8C}; // MAC-адрес
byte ipp[] = {192, 168, 0, 104}; // IP-адрес клиента
byte ipServv[] = {192, 168, 0, 102}; // IP-адрес сервера

bool setting = true;
EthernetClient client; // создаем клиента

char massiv[] = "0000001";
void setup() {
  for (int i=2; i<9; i++){
    pinMode(i, OUTPUT);
  }
  for (int i=2; i<9; i++){
    digitalWrite(i, HIGH);
  }
  Serial.begin(9600);
  Ethernet.begin(macc, ipp); // инициализация контроллера
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
}

void loop() {
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
        strcpy(send, "house_");
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
    client.write("ok_", 3);
    
    client.flush();
    for (int i=0; i<7; i++){
    int num = test[i] -'0';
    if (num==1) {
      Serial.print(i);
      digitalWrite(i+2, LOW);
    } else{
      digitalWrite(i+2, HIGH);
    }
    delay(50);
    strcpy(test, "");
  }
  }


  // если сервер отключился, останавливаем клиент
  if (!client.connected()) {
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();
    while (true); // останавливается
  }
 
}
