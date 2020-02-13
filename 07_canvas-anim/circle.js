// Amanda "Amber" Chen
// SoftDev1 pd1
//K07 -- They lock us in the tower whenever we get caught ...which is often
// 2020-02-11

var startButton = document.getElementById('start');
var stopButton = document.getElementById('stop');
var canv= document.getElementById('canvas');
var contx=canv.getContext('2d');
var r = 10;
var i = true;

contx.strokeRect(0,0,600,600);
startButton.addEventListener('click',start);

function stop(){
  startButton.addEventListener('click',start);
  ani = window.cancelAnimationFrame(ani);
}


function start(event){
  startButton.removeEventListener('click',start);
  stopButton.addEventListener('click',stop);
  ani = window.requestAnimationFrame(animate);
  console.log(ani);
}

function animate(){
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

// canv.addEventListener("click", draw);
// function draw(event) {
//     var r = 5;
//     console.log(event.clientX +",",event.clientY);
//     //dot
//     contx.beginPath()
//     contx.arc(event.clientX - 8, event.clientY - 8, r, 0, 2 * Math.PI);
//     contx.fill();
//     //line
//     if (x != 0){
//       contx.beginPath();
//       contx.moveTo(x,y);
//       contx.lineTo(event.clientX-8,event.clientY-8);
//       contx.stroke()
//     }
//     x=event.clientX-8;
//     y=event.clientY-8;
// }
