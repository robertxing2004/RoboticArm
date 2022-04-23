
// testing
// if you have a mac running mojave+ (robert), you have to use processing 4
// if you have anything else, it should run fine in processing 3

import processing.video.*;

Capture video;

void setup() {
  size(1280, 720); // this is TOP of video 
  video = new Capture(this, 1280, 720, 30); //return img, w, h, fps
  video.start(); // start webcam
}

void draw(){
  pushMatrix();
  scale(-1,1);
  image(video,-width,0);
  popMatrix();
}

// change this event to control snapshots (take snapshot when bot isnt on, every 5 seconds for speed)
void captureEvent(Capture video){
  video.read();
}
