// TCP клиент, передает данные из UART серверу, от сервера в UART
#include <Ethernet.h>

// определяем конфигурацию сети
byte macc[] = {0xAE, 0xB1, 0x32, 0xE0, 0x9A, 0x8C}; // MAC-адрес
byte ipp[] = {192, 168, 0, 105}; // IP-адрес клиента
byte ipServv[] = {192, 168, 0, 100}; // IP-адрес сервера

bool setting = true;
EthernetClient client; // создаем клиента

unsigned long period_time = 100;
// переменная таймера, максимально большой целочисленный тип (он же uint32_t)
unsigned long my_timer;

const int up = 2;
const int down = 3;
const int right = 4;
const int left = 5;

int movetime;
 int num;

//   abc
/*
 * a-повороты
 * 1-направо
 * 0-налево
 * 2-прямо
 * 
 * b-направление
 * 1-вперед
 * 0-стоп
 * 2-назад
 * 
 * с-время 
 * время=с*100+50 мс
 */

void setup() {
  Ethernet.begin(macc, ipp); // инициализация контроллера
  Serial.begin(9600);
  pinMode(up,OUTPUT);
  pinMode(down,OUTPUT);
  pinMode(right,OUTPUT);
  pinMode(left,OUTPUT);
  digitalWrite(up,1);
  digitalWrite(down,1);
  digitalWrite(right,1);
  digitalWrite(left,1);
  pinMode(A0,INPUT);
  pinMode(A1,INPUT);
  pinMode(A2,INPUT);
  pinMode(A3,INPUT);
  pinMode(A4,INPUT);
  pinMode(A5,INPUT);
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
        strcpy(send, "energycar_");
        client.write(send,sizeof(send)+10); 
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

  int udset;
  int rlset;
  int movespeed;
  int buf;

    
    // все, что приходит с сервера, печатаем в UART
 if (client.available() and not setting) {
    //int num = Serial.parseInt();
    char test[8];// = client.read();
    strcpy(test, "");
    client.read(test, 8);
    num = atoi(test);
    Serial.print("Получены данные - ");
    Serial.print(test);
    
    //setting = true; 
    if (test != 999){
      buf=num%10;
      movespeed=buf;
      num=num/10;
    
      buf=num%10;
      udset=buf;
      num=num/10;
    
      buf=num%10;
      rlset=buf;
      
      Serial.print(" rlset=");
      Serial.print(rlset); 
      Serial.print(" udset=");
      Serial.print(udset);
      Serial.print(" movespeed=");
      Serial.print(movespeed);
      Serial.println(); 
      my_timer=millis();
      period_time=movespeed*100+50;
      while (millis() - my_timer <= period_time){
        //***********Повороты*************
        if(rlset==1){
          digitalWrite(right,0);
          digitalWrite(left,1);
        }
        if(rlset==0){
          digitalWrite(right,1);
          digitalWrite(left,0);
        }
        if(rlset==2){
          digitalWrite(right,1);
          digitalWrite(left,1);
        }
       //********Вперед и стоп***********
         if(udset==1){
          digitalWrite(up,0);
          digitalWrite(down,1);
        }
        if(udset==0){
          digitalWrite(up,1);
          digitalWrite(down,1);
        }
        if(udset==2){
          digitalWrite(up,1);
          digitalWrite(down,0);
        }
        
      }
    
      if(udset==1){
        my_timer=millis();
        period_time=100;
        while (millis() - my_timer <= period_time){
          digitalWrite(down,0); 
          digitalWrite(up,1);  
          }
      }
    }
    client.write("ok_", 3);
    digitalWrite(up,1);
    digitalWrite(down,1);
    digitalWrite(right,1);
    digitalWrite(left,1);
    int CUR_SOL;
    CUR_SOL=analogRead(A4)-analogRead(A5);
    if (abs(CUR_SOL) < 150)
    {
      CUR_SOL = 0;
    } else
    {
      CUR_SOL = abs(CUR_SOL);
    }
    strcpy(test,"");
    char en_str[8];
    sprintf(en_str,"%d",CUR_SOL);
    strcat(test,en_str);
    strcat(test,"+1+1+");
    //strcpy(test,"1+1+1+");
    client.write(test, sizeof(test));
//    while (not client.available()){
//      
//    }
//    char read_c[16];
//    client.read(read_c,16);
//    num = atoi(read_c);
//    Serial.print("Получена команда - ");
//    Serial.println(num);
//    if (num ==102){
//      Serial.println();
//      Serial.println("Сервер отключил устройство");
//      client.stop();
//      while (true); // останавливается
//    }
//    if (num ==404){
//      Serial.println();
//      Serial.println("Сервер перезагружает устройство");
//      client.stop();
//      setup();
//    }
//    if (num ==167){
//      Serial.println();
//      Serial.println("Сервер инициализировал устройство. Начало работы.");
//      setting = false;
//    }
    client.flush();
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
