void clientActions(){
  if (send == true){
    myClient.write("snap");
    println("Data successfully sent. Waiting for response");
    
    String data = myClient.readStringUntil('\n');
    println(data);
    
    send = false; 
  } 
}
