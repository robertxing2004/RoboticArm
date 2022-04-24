import processing.net.*;
import g4p_controls.*;

Client frontClient;

boolean send;

void setup(){
  size(200, 200);
  createGUI();
  customGUI();
  
  frontClient = new Client(this, "Stevens-MacBook-Pro.local", 50000);
}

void draw(){
  
  if (send == true){
    frontClient.write("your mother");
    send = false;
  }
  
}

// Use this method to add additional statements
// to customise the GUI controls
public void customGUI(){

}
