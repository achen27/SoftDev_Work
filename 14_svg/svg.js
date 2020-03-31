// Amanda "Amber" Chen
// SoftDev1 pd1
// K #014: Ask Circles [Change || Die] While Moving, etc.
// 2020-03-31

var pic = document.getElementById("vimage")
var clearButton = document.getElementById("clear");
var moveButton = document.getElementById("move");
var stopButton = document.getElementById('stop');
var ani;

function clear(){
    while (pic.lastChild){
      pic.removeChild(pic.lastChild);
    }
}

function firstdot(e) {
  console.log(pic)
    x = e.clientX
    y = e.clientY
    if (e.target.id == "vimage") {
        var cir = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        cir.setAttribute("cx",x-10);
        cir.setAttribute("cy",y-10);
        cir.setAttribute("r","20");
        cir.setAttribute("fill","red");
        cir.setAttribute("stroke","black");
        cir.setAttribute("dx",1);
        cir.setAttribute("dy",1);
        pic.appendChild(cir);
    }
}

function changecolor(e){
  var node = e.target
  if (node.getAttribute("fill") == "red") {
    node.setAttribute("fill","blue");
  }
}

function teleport(e){
  var node = e.target
  if (node.getAttribute("fill") == "blue") {
    pic.removeChild(node);
    var cir = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    cir.setAttribute("id","circle");
    cir.setAttribute("cx", Math.round(Math.random() * 500));
    cir.setAttribute("cy", Math.round(Math.random() * 500));
    cir.setAttribute("r","20");
    cir.setAttribute("fill","red");
    cir.setAttribute("stroke","black");
    cir.setAttribute("dx",1);
    cir.setAttribute("dy",1);
    pic.appendChild(cir);
  }
}

function bounce(){
  window.cancelAnimationFrame(ani);
  var allChildren = pic.children
  var i;
  for (i = 0; i < allChildren.length; i++) {
    var cir = allChildren[i].cloneNode(true);
    var oldx = parseInt(cir.getAttribute("cx"));
    var oldy = parseInt(cir.getAttribute("cy"));

    if (oldx-20 <= 0 || oldx+20 >= 500){
      cir.setAttribute("dx", -parseInt(cir.getAttribute("dx")));
    }
    if (oldy-20 <= 0 || oldy+20 >= 500){
      cir.setAttribute("dy", -parseInt(cir.getAttribute("dy")));
    }

    cir.setAttribute("cx", oldx + parseInt(cir.getAttribute("dx")));
    cir.setAttribute("cy", oldy + parseInt(cir.getAttribute("dy")));

    pic.removeChild(allChildren[i]);
    pic.appendChild(cir);
  }
  ani = window.requestAnimationFrame(bounce);
}

function stop(){
  window.cancelAnimationFrame(ani);
}

clearButton.addEventListener('click', clear);
pic.addEventListener('click', firstdot);
pic.addEventListener('click', teleport);
pic.addEventListener('click', changecolor);
moveButton.addEventListener('click', bounce);
stopButton.addEventListener('click', stop)
