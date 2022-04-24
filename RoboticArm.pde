import processing.net.*;
import g4p_controls.*;

Client myClient;

Server server;

boolean send;
String dataIn;
byte[] byteBuffer = new byte[1024];

void setup(){
  size(200, 200);
  createGUI();
  customGUI();
  
  myClient = new Client(this, "127.0.0.1", 50001);
}

void draw(){
  if (send == true){
    myClient.write("snap");
    println("Data successfully sent. Waiting for response");
    
    String data = myClient.readStringUntil('\n');
    println(data);
    
    send = false;
  } 
}

// Use this method to add additional statements
// to customise the GUI controls
public void customGUI(){

}
