//Pin connected to ST_CP of 74HC595
#define latchPin 8
//Pin connected to SH_CP of 74HC595
#define clockPin 12
////Pin connected to DS of 74HC595
#define dataPin 11

byte input[256];

void setup() {
  //Start Serial for debuging purposes  
  Serial.begin(9600);
  //set pins to output because they are addressed in the main loop
  pinMode(latchPin, OUTPUT);
}

void loop() {
}

void shiftOut(int myDataPin, int myClockPin) {
  // This shifts 32 bits out MSB first, 
  //on the rising edge of the clock,
  //clock idles low

//internal function setup
  pinMode(myClockPin, OUTPUT);
  pinMode(myDataPin, OUTPUT);

 //clear everything out just in case to
 //prepare shift register for bit shifting
  digitalWrite(myDataPin, 0);
  digitalWrite(myClockPin, 0);
  
  for(int bytes = 3; bytes>=0; bytes--){
    for(int bits = 0; bits<=7; bits++){
      digitalWrite(myClockPin, 0);
      
      //Sets the pin to HIGH or LOW depending on pinState
      if(input[bytes] & (1<<bits)){
        digitalWrite(myDataPin, 1);
      }
      else{
        digitalWrite(myDataPin, 0);
      }
      //register shifts bits on upstroke of clock pin  
      digitalWrite(myClockPin, 1);
      //zero the data pin after shift to prevent bleed through
      digitalWrite(myDataPin, 0);
    }
  }
  //stop shifting
  digitalWrite(myClockPin, 0);
}

void writeBytes(){
    digitalWrite(latchPin, 0);
    shiftOut(dataPin, clockPin);
    digitalWrite(latchPin, 1);
}

void serialEvent(){
  Serial.readBytes(input, 4);
  writeBytes();
}
