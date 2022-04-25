import processing.net.*;
import g4p_controls.*;

// variables for the backend server stuff
Client myClient;
boolean send;
String dataIn;
byte[] byteBuffer = new byte[1024];

// variables for the front end stuff

void setup(){
  // GUI code - front end guys 
  size(200, 200);
  createGUI();
  customGUI();
  
  // initializing the client
  myClient = new Client(this, "127.0.0.1", 50001);
}

void draw(){
  clientActions();
}

// Use this method to add additional statements
// to customise the GUI controls
public void customGUI(){

}
