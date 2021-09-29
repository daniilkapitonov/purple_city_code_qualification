
unsigned long period_time = 1000;
unsigned long my_timer;

#include <SPI.h>
#include <Ethernet.h>
bool flag = true;

#include <TroykaCurrent.h>
ACS712 dataI(A2);
// определяем конфигурацию сети
byte mac[] = {0xAE, 0xB5, 0x14, 0xE3, 0x6A, 0x5C}; // MAC-адрес
byte ip[] = {192, 168, 0, 107}; // IP-адрес клиента
byte ipServ[] = {192, 168, 0, 100}; // IP-адрес сервера

EthernetClient client; // создаем клиента

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);

  Ethernet.begin(mac, ip); // инициализация контроллера
  Serial.begin(9600);
  Serial.println("connecting...");
  // устанавливаем соединение с сервером
  while (!client) {
    if (client.connect(ipServ, 10001)) {
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

  while (flag) {
    client.write("2", 1);
    char r[1];
    client.read(r, 1);
    int cash = atoi(r);
    Serial.println(cash);
    if (cash = 1) {
      flag = false;
      Serial.println("Получен ответ");
    }
  }

  if (0 > 1) { // (client.available()) {
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
    client.write(send, sizeof(send));
    Serial.print(send);
    Serial.println();
    for (int i = 0; i < 8; i++) {
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

  if  (client.available()){ //(millis() - my_timer >= period_time and not flag) {
    
    char cash12[3];
    
    client.read(cash12,3);
    Serial.print("Massage come");
    Serial.println(cash12);
    if (atoi(cash12) >0){
      client.flush();
      my_timer = millis();
      char str1[14];
      char str2[4];
      char str3[4];
  
      //int number1 = analogRead(A0) - 270;
      //if (number1 < 0)number1 = 0;
      //int number2 = map(analogRead(A1), 700, 950, 0, 100);
      //int number3 = dataI.readCurrentDC();
      int number1 = abs(100-analogRead(A0));
      int number2 = analogRead(A1);
      int number3 = dataI.readCurrentDC();
      sprintf(str1, "%d", number1);
      sprintf(str2, "%d", number2);
      sprintf(str3, "%d", number3);
  
      strcat(str1, "_");
      strcat(str1, str2);
      strcat(str1, "_");
      strcat(str1, str3);
      strcat(str1, "_");
      client.write(str1, 14);
      Serial.println(str1);
      client.flush();
      /*  for(int i=0;i<11;i++){
         str[i]="";
        }*/
    }
  }
}
