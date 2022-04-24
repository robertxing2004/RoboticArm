import processing.net.*;
import g4p_controls.*;

Client myClient;

boolean send;
String dataIn;
byte[] byteBuffer = new byte[10];

void setup(){
  size(200, 200);
  createGUI();
  customGUI();
  
  myClient = new Client(this, "Stevens-MacBook-Pro.local", 50000);
}

void draw(){
  if (send == true){
    // send a snapshot, and wait for a response
    myClient.write("snap");
    send = false;
    
    // wait for a response
  } 
}

// Use this method to add additional statements
// to customise the GUI controls
public void customGUI(){

}
