const char OFF = 'o';
const char UVON = 'U';
const char UVOFF = 'u';
const char HEATERON = 'H';
const char HEATEROFF = 'h';

int uvpin1 = 8;
int heaterpin1 = 9;


void setup() {
  pinMode(uvpin1, OUTPUT);
  pinMode(heaterpin1, OUTPUT);
  digitalWrite(uvpin1, HIGH);
  digitalWrite(heaterpin1, LOW);
  Serial.begin(115200);
}
void loop() {

  if (Serial.available() > 0) {
    int incomingByte = Serial.read(); // read the incoming byte:

//    Serial.print("Recieved: ");
//    Serial.println(incomingByte, DEC);
    if (incomingByte == UVON) {
//        Serial.println("yeehaw");
        digitalWrite(uvpin1, LOW);
        delay(2000);
    }
    if (incomingByte == UVOFF) {
//      Serial.println("yeehaw");
        digitalWrite(uvpin1, HIGH);
        delay(2000);
    }
    if (incomingByte == HEATERON) {
//      Serial.println("yeehaw");
        digitalWrite(heaterpin1, HIGH);
        delay(2000);
    }
    if (incomingByte == HEATEROFF) {
//      Serial.println("yeehaw");
        digitalWrite(heaterpin1, LOW);
        delay(2000);
    }
    
    if (incomingByte == OFF) {
//      Serial.println("yeehaw");
        digitalWrite(heaterpin1, LOW);
        digitalWrite(uvpin1, HIGH);
        delay(2000);
    }
  }

  
}
