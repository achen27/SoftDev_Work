// Amanda "Amber" Chen
// SoftDev1 pd1
// K08 -- What is it saving the screen from?
// 2020-02-13

var startButton = document.getElementById('start');
var stopButton = document.getElementById('stop');
var movie = document.getElementById('dvd');
var canv= document.getElementById('canvas');
var contx=canv.getContext('2d');

//animate
var r = 10;
var i = true;
var ani;

//bounce
var x = 50;
var y = 50;
var dx = 1;
var dy = 1;
var ani2;

contx.strokeRect(0,0,600,600);
startButton.addEventListener('click',animate);
stopButton.addEventListener('click',stop);
movie.addEventListener('click',bounce);

function stop(){
  window.cancelAnimationFrame(ani);
  window.cancelAnimationFrame(ani2);
  x = 50;
  y = 50;
}

function animate(){
    window.cancelAnimationFrame(ani);
    contx.clearRect(0,0,600,600);
    contx.strokeRect(0,0,600,600);
    contx.beginPath()
    contx.arc(300, 300, r, 0, 2 * Math.PI);
    contx.fill();
    //console.log(r)
    if(r == 300 || r == 5){
      i = !i
    }
    if (i){
      r += 5
    } else {
      r -= 5
    }
    ani = window.requestAnimationFrame(animate);
}

function bounce(){
  window.cancelAnimationFrame(ani2);
  contx.clearRect(0,0,600,600);
  contx.strokeRect(0,0,600,600);
  contx.fillRect(x,y,50,30);
  // if (x == 0){
  //
  // }
  if (x+30 == 600){
    dx = -dx;
  }
  // if (y == 0){
  //
  // }
  // if (y == 600){
  //
  // }
  x += dx;
  y += dy;
  ani2 = window.requestAnimationFrame(bounce);
}

//var logo = new Image()
//logo.src = "logo_dvd.jpg"
//ctx.drawImage(?)
