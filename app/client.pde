void clientActions(){
  if (send == true){
    myClient.write("snap");
    println("Data successfully sent. Waiting for response");
    
    data = myClient.readStringUntil('\n');

    xLocation = int(data);

    println(data);
    
    send = false; 
  } 
}
