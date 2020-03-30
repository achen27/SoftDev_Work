// Amanda "Amber" Chen
// SoftDev1 pd1
// K #013: Ask Circles [Change || Die]
// 2020-03-30

var pic = document.getElementById("vimage")
var clearButton = document.getElementById("clear");
var x = -1;
var y = -1;

function clear(){
    while (pic.lastChild){
      pic.removeChild(pic.lastChild);
    }
    x = -1;
    y = -1;
}

function firstdot(e) {
    x = e.clientX
    y = e.clientY
    if (e.target.id == "vimage") {
        var cir = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        cir.setAttribute("cx",x-10);
        cir.setAttribute("cy",y-10);
        cir.setAttribute("r","20");
        cir.setAttribute("fill","red");
        cir.setAttribute("stroke","black");
        pic.appendChild(cir);
    }
}

function changecolor(e){
  var node = e.target
  if (node.getAttribute("fill") == "red") {
    node.setAttribute("fill","blue");
  }
}

function move(e){
  var node = e.target
  if (node.getAttribute("fill") == "blue") {
    pic.removeChild(node);
    var cir = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    cir.setAttribute("id","circle");
    cir.setAttribute("cx", Math.random() * 500);
    cir.setAttribute("cy", Math.random() * 500);
    cir.setAttribute("r","20");
    cir.setAttribute("fill","red");
    cir.setAttribute("stroke","black");
    pic.appendChild(cir);
  }
}

clearButton.addEventListener('click', clear);
pic.addEventListener('click', firstdot);
pic.addEventListener('click', move);
pic.addEventListener('click', changecolor);
