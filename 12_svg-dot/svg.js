// Amanda "Amber" Chen
// SoftDev1 pd1
// K #012: Connect the Dots
// 2020-03-29

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

function draw(e) {
    var newx = e.offsetX;
    var newy = e.offsetY;
    //dot
    var dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    dot.setAttribute("cx",newx);
    dot.setAttribute("cy",newy);
    dot.setAttribute("r","5");
    dot.setAttribute("fill","black");
    pic.appendChild(dot);
    //line
    if (x != -1){
      var line = document.createElementNS("http://www.w3.org/2000/svg", "line");
      line.setAttribute("x1",x);
      line.setAttribute("y1",y);
      line.setAttribute("x2",newx);
      line.setAttribute("y2",newy);
      line.setAttribute("stroke","black");
      pic.appendChild(line);
    }
    x = newx
    y = newy
}

clearButton.addEventListener('click', clear);
pic.addEventListener('click', draw);
