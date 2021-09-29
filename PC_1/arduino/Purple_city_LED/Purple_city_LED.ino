// TCP клиент, передает данные из UART серверу, от сервера в UART
#include <SPI.h>
#include <Ethernet.h>
unsigned long period_time = 1000;
unsigned long my_timer;
uint8_t  array1[2];
char test[7]="0000000";
char test1[7]="0000000";
// определяем конфигурацию сети
byte mac[] = {0xAE, 0xB5, 0x36, 0xE7, 0x4A, 0x5C}; // MAC-адрес
byte ip[] = {192, 168, 0, 104}; // IP-адрес клиента
byte ipServ[] = {192, 168, 0, 100}; // IP-адрес сервера
bool flag = true;
EthernetClient client; // создаем клиента

void setup() {
  for(int i=0;i<7;i++){
    pinMode(i+2,OUTPUT);
  }
  pinMode(A0,INPUT);
  my_timer = millis();
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
 // client.write("Ard_1_", 6);
}

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
  
    client.read(test, 8);
    //client.write(chr);
    
    Serial.print("Получены данные - ");
    
    Serial.println(test);
    for (int i=0; i<7; i++){
      test1[i] = test[i];
    }
   
    Serial.print("Отправка данных - ");
    
    
    client.write(test,sizeof(test));
    Serial.print(test);
    Serial.println();
    for (int i=0; i<7; i++){
      test[i] = "";
    }
    client.flush();
    
  }

  // все, что приходит из UART, передаем серверу
 /* while (Serial.available() > 0) {
    char inChr = Serial.read();
    if (client.connected()) {
      client.print(inChr);
    }
  }
*/
  // если сервер отключился, останавливаем клиент
  if (!client.connected()) {
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();
    while (true); // останавливается
  }

if (millis() - my_timer >= period_time) 
{
       my_timer = millis();
   Serial.println(test1);
     for(int i=0;i<7;i++){
      Serial.print(test1[i]);
      int val;
      val=test1[i]-'0';
      Serial.print(val);
      if(val==1){
        digitalWrite(i+2,0);
         Serial.print(i);
        Serial.println("OFF");
      }
      if(val==0){
        Serial.print(i);
        Serial.println("ON");
        digitalWrite(i+2,1);
      }
     }
}

  
}
