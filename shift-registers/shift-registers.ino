//**************************************************************//
//  Name    : shiftOutCode, Dual Binary Counters                 //
//  Author  : Carlyn Maw, Tom Igoe                               //
//  Date    : 25 Oct, 2006                                       //
//  Version : 1.0                                                //
//  Notes   : Code for using a 74HC595 Shift Register            //
//          : to count from 0 to 255                             //
//**************************************************************//

//Pin connected to ST_CP of 74HC595
int latchPin = 8;
//Pin connected to SH_CP of 74HC595
int clockPin = 12;
////Pin connected to DS of 74HC595
int dataPin = 11;



void setup() {
  //Start Serial for debuging purposes  
  Serial.begin(9600);
  //set pins to output because they are addressed in the main loop
  pinMode(latchPin, OUTPUT);
}

void loop() {
    digitalWrite(latchPin, 0);
    //count up on GREEN LEDs
    //count down on RED LEDs
    shiftOut(dataPin, clockPin, 0);
    //return the latch pin high to signal chip that it 
    //no longer needs to listen for information
    digitalWrite(latchPin, 1);
    delay(100);
    digitalWrite(latchPin, 0);
    //count up on GREEN LEDs
    //count down on RED LEDs
    shiftOut(dataPin, clockPin, 1);
    //return the latch pin high to signal chip that it 
    //no longer needs to listen for information
    digitalWrite(latchPin, 1);
    delay(100);
}

void shiftOut(int myDataPin, int myClockPin, int pinState) {
  // This shifts 8 bits out MSB first, 
  //on the rising edge of the clock,
  //clock idles low

//internal function setup
  pinMode(myClockPin, OUTPUT);
  pinMode(myDataPin, OUTPUT);

 //clear everything out just in case to
 //prepare shift register for bit shifting
  digitalWrite(myDataPin, 0);
  digitalWrite(myClockPin, 0);
  
  for(int i = 0; i<32; i++){
    //Sets the pin to HIGH or LOW depending on pinState
    digitalWrite(myDataPin, pinState);
    //register shifts bits on upstroke of clock pin  
    digitalWrite(myClockPin, 1);
    //zero the data pin after shift to prevent bleed through
    digitalWrite(myDataPin, 0);
  }

  //stop shifting
  digitalWrite(myClockPin, 0);
}
