// TCP клиент, передает данные из UART серверу, от сервера в UART
#include <SPI.h>
#include <Ethernet.h>

// определяем конфигурацию сети
byte mac[] = {0xAE, 0xB2, 0x26, 0xE4, 0x4A, 0x5C}; // MAC-адрес
byte ip[] = {192, 168, 0, 103}; // IP-адрес клиента
byte ipServ[] = {192, 168, 0, 100}; // IP-адрес сервера
unsigned long period_time = 50;
// переменная таймера, максимально большой целочисленный тип (он же uint32_t)
unsigned long my_timer;
EthernetClient client; // создаем клиента

void setup() {
  my_timer = millis();   // "сбросить" таймер
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
    client.flush();
    client.write("2",1);
    char r[1];
    client.read(r,1);
    int cash = atoi(r);
    Serial.println(cash);
    if (cash=1){
      flag = false;
      Serial.println("Получен ответ");
    }
  }
  if (1>0) {
    //char chr = client.read();
    my_timer = millis();
    //client.read(test, 8);
    //client.write(chr); 
    //int num = atoi(test);
    //Serial.print("Получены данные - ");
    //Serial.print(num);
    char text[30];
    //Serial.println("Begin");
    char cash[30];
    strcpy(text, "");
    sprintf(cash, "%d", rand()%1000+1000);
    strcat(text,cash);
    strcat(text,"_");
    sprintf(cash, "%d", rand()%1000+1000);
    strcat(text,cash);
    strcat(text,"_");
    sprintf(cash, "%d", rand()%10+90);
    strcat(text,cash);
    strcat(text,"_");
    Serial.println();
    Serial.print("Отправка данных - ");
    client.write(text,sizeof(text));
    Serial.print(text);
    Serial.println();
    for (int i=0; i<8; i++){
      text[i] = "";
    }
    client.flush();
    delay(5000);
    
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
