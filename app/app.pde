import processing.net.*;
import g4p_controls.*;

// variables for the backend server stuff
Client myClient;
boolean send;
boolean sendToHardware;
String dataIn;
byte[] byteBuffer = new byte[1024];

String data;
int xLocation;

int picCounter; 

// variables for the front end stuff

public void setup(){
  // GUI code - front end guys 
  size(200, 200, JAVA2D);
  createGUI();
  customGUI();
  
  // initializing the client
  myClient = new Client(this, "127.0.0.1", 50001);
}

public void draw(){
  background(255);
  clientActions();
}

// Use this method to add additional statements
// to customise the GUI controls
public void customGUI(){

}
