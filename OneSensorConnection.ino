#include <Wire.h>

#define D6T_addr 0x0A
#define D6T_cmd 0x4C
byte rbuf[19]; 
float temp[9]; // amb + 8 temp_readings
int counter = 1;
boolean humanCheck = false;
int repeats = 0;
int people = 0;
void setup()
{
  Wire.begin();
  Serial.begin(9600);
  Serial.println("Serial Connected");
  Wire.beginTransmission(D6T_addr);
  Wire.write(D6T_cmd);
  Wire.endTransmission();
}
void loop()
{
  int i;
  
  Wire.requestFrom(D6T_addr,19);
  
  //delay(500); // < ------- 100MS DELAY
  for (i = 0; i < 19; i++) 
  {  
    while(!Wire.available());
    rbuf[i] = Wire.read(); 
  }
  for (i=0; i<9; i++)
  {
    temp[i]=(rbuf[(i*2)]+(rbuf[(i*2+1)]<<8))*0.1;
  }
  Serial.print("Run #");
  Serial.println(counter);
  counter += 1;
  humanCheck = false;
  if (temp[0]>0)
  {
    for (i=0; i<9; i++)
    {
      if (temp[i] > 30 && temp[i] < 34.5 && !humanCheck){
        humanCheck = true;
      }
      //printTemps(i, temp);
       
    }
  }
  

  if (humanCheck){
    /* human detected */
    repeats += 1;
    humanCheck = false;
  }
  else{
    /* no human detected */
    repeats = 0;
  }
  
  // if sensor was not tripped in last reading: add a person
  if (repeats == 1){
    people += 1;
  }
  else{
    //same person or no person in view of sensor
  }
  
  Serial.print("People = ");
  Serial.println(people);
  
  
  if (temp[0] <= 0) {
    Serial.print("Run returned a 0.00 or negative number");
  }
}

void printTemps(int i, float *temp){
    if (i == 0){
      Serial.print("Ptat =");
    }
    else { 
      Serial.print("P");
      Serial.print(i-1);
      Serial.print("= ");
    }
    
    
    Serial.print(temp[i]);
    if ( i < 8 ) {
      Serial.print( ", " );
    } 
    else if (i == 8) {
      Serial.println(" End");
    }
    else {
      Serial.println() ;
    }
    return;
      
} 
