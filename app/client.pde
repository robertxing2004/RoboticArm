void clientActions(){
  if (send == true){
    
    // server-client comm stuff
    
    myClient.write("snap");
    println("Data successfully sent. Waiting for response");
    
    while (data == null){
      data = myClient.readStringUntil('p');
    }
    
    data = data.substring(0, data.length() - 1);
    xLocation = int(data);
    data = null;
    println(xLocation);
    picCounter = picCounter + 1; 
     
    // update slider code 
    
    LocationSlider.setValue(xLocation);
    
    // your mom
    
    send = false;
  } 
}





void confirmActions(){
  
  if (sendToHardware  == true){
    
    newLocation = str(xLocation) + "p";
    
    myClient.write("move");
    println("");
    delay(100);
    myClient.write(newLocation);
    println("command successfully sent");
    
    sendToHardware = false;
  }
  
}
