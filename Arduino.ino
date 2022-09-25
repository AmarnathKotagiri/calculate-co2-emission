#include <LiquidCrystal.h>



// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;



//temperature sensor setup/declaration:
int led = 13; // define the LED pin
int digitalPin = 8; // KY-028 digital interface
int analogPin = A0; // KY-028 analog interface
int digitalVal; // digital readings
long analogVal; //analog readings



//summation of ppm setup:
int arr[600];
int x = 0;
int count;
int i;
int sum;
int avg;



LiquidCrystal lcd(rs, en, d4, d5, d6, d7);



void setup() {
  //temperature sensor setup
  pinMode(led, OUTPUT);
  pinMode(digitalPin, INPUT);
  //pinMode(analogPin, OUTPUT);
  Serial.begin(9600);
  
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("CO2: ");
}



void loop() {
  // Read the digital interface
  digitalVal = digitalRead(digitalPin);
  if(digitalVal == HIGH) // if temperature threshold reached
  {
    digitalWrite(led, HIGH); // turn ON Arduino's LED
  }
  else
  {
    digitalWrite(led, LOW); // turn OFF Arduino's LED
  }
  // Read the analog interface
  analogVal = analogRead(analogPin);
  //Serial.println(analogVal); // print analog value to serial
  arr[x] = analogVal;



 //30 second average:
  sum = 0;
  count = 0;
  for (i = x; i >= 0 && i > x - 30; --i) {
    ++count;
    sum = sum + arr[i];
  }
  avg = sum / count;



 //output avg every 30 seconds, not including 0
  if (x % 30 == 0 && x > 0) {
    Serial.println(avg);
  }
  
  //lcd:
  lcd.setCursor(6,0);
  lcd.print(analogVal);
  lcd.print(" PPM");
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  lcd.setCursor(0, 1);
  // print the number of seconds since reset:
  lcd.print("30s avg: ");
  lcd.print(avg);
  lcd.print("PPM");



 //delay, increase time variable (x)
  delay(1000);
  x = x + 1;



}
