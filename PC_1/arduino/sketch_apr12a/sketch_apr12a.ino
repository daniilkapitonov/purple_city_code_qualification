// TCP клиент, передает данные из UART серверу, от сервера в UART
#include <SPI.h>
#include <Ethernet.h>

// определяем конфигурацию сети
byte mac[] = {0xAE, 0xB2, 0x26, 0xE4, 0x4A, 0x5C}; // MAC-адрес
byte ip[] = {192, 168, 0, 103}; // IP-адрес клиента
byte ipServ[] = {192, 168, 0, 100}; // IP-адрес сервера

EthernetClient client; // создаем клиента

void setup() {
  
  Ethernet.begin(mac, ip); // инициализация контроллера
  Serial.begin(9600);
  Serial.println("connecting...");
  // устанавливаем соединение с сервером
  while (!client){
    if (client.connect(ipServ, 10000)) {
      Serial.println("connected"); // успешно
      client.flush();
    }
    else {
      Serial.println("connection failed"); // ошибка
    }
    delay (1000);
  }
}
bool flag = true;
void loop() {
  // все, что приходит с сервера, печатаем в UART
  while (flag){
    client.write("1",1);
    char r[1];
    client.read(r,1);
    int cash = atoi(r);
    Serial.println(cash);
    if (cash=1){
      flag = false;
      Serial.println("Получен ответ");
    }
  }
  if (client.available()) {
    //char chr = client.read();
    char test[8];
    client.read(test, 8);
    //client.write(chr); 
    int num = atoi(test);
    Serial.print("Получены данные - ");
    Serial.print(num);
    Serial.println();
    Serial.print("Отправка данных - ");
    char send[8];
    sprintf(send, "%d", num);
    client.write(send,sizeof(send));
    Serial.print(send);
    Serial.println();
    for (int i=0; i<8; i++){
      test[i] = "";
    }
    client.flush();
    
  }

  // все, что приходит из UART, передаем серверу
  while (Serial.available() > 0) {
    char inChr = Serial.read();
    if (client.connected()) {
      client.print(inChr);
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
