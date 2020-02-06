// Amanda "Amber" Chen
// SoftDev1 pd1
// K05 -- ...and I want to Paint It Better
// 2020-02-06

var clearButton = document.getElementById('clearB');
var toggleButton = document.getElementById('toggleB');
var canv= document.getElementById('slate');
var contx=canv.getContext('2d');
var brushMode=0;

contx.strokeRect(0,0,600,600);

clearButton.addEventListener('click',clear);
toggleButton.addEventListener('click',function(e){toggle()});

function clear(){
    console.log('clear');
    contx.clearRect(0,0,600,600);
    contx.strokeRect(0,0,600,600);
}
function toggle(){
    console.log('toggle')
    if(brushMode){
        brushMode = 0
    }
    else{
        brushMode = 1
    }
}

canv.addEventListener("click", draw);
function draw(event) {
    var r = 10;
    console.log(event.clientX +",",event.clientY);
    if (brushMode){
        contx.beginPath();
        contx.arc(event.clientX - 8, event.clientY - 8, r, 0, 2 * Math.PI);
        contx.fill();
    }
    else{
        contx.fillRect(event.clientX - 8, event.clientY - 8, 2*r, 2*r);
        console.log( (event.client - 8) + "," + (event.clientY - 8) + "," + 2*r+","+ 2*r);
    }
}

//e.preventDefault();
//The preventDefault() method cancels the event if it is cancelable, meaning
//that the default action that belongs to the event will not occur.
//For example, this can be useful when:
//    Clicking on a "Submit" button, prevent it from submitting a form
//    Clicking on a link, prevent the link from following the URL
//Note: Not all events are cancelable. Use the cancelable property to find out
//  if an event is cancelable.
//Note: The preventDefault() method does not prevent further propagation of an
//  event through the DOM. Use the stopPropagation() method to handle this.

//ctx.beginPath();
//The beginPath() method begins a path, or resets the current path.
//For example, the method can called before beginning a second line, so that
//they may be drawn with different colors.

//e.offsetX / e.offsetY
//The offsetX property returns the x-coordinate / y-coordinate of the mouse
//pointer, relative to the target element.
//Note: This property is read-only.
