var changeheading = function(e) {
  var h = document.getElementById("h");
  console.log(this);
  h.innerHTML = this.innerHTML;
}

var changeback = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = "Hello World!";
}

var removeItem = function(e) {
  //console.log(e);
  this.remove();
};

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++){
  lis[i].addEventListener('mouseover', changeheading);
  lis[i].addEventListener("mouseout", changeback);
  lis[i].addEventListener("click", removeItem);
}

var additem = function(e) {
  ////gets ordered list of items, creates a new element, appends it to the ordered list
  var list = document.getElementById("thelist");
  console.log(list);
  var item = document.createElement("li");
  item.addEventListener('mouseover', changeheading);
  item.addEventListener("mouseout", changeback);
  item.addEventListener("click", removeItem);
  item.innerHTML = "WORD";
  //console.log(lis);
  lis = document.getElementsByTagName("li");
  list.appendChild(item);
}

var button = document.getElementById("b");
button.addEventListener("click", additem);

var fib = function(n){
    if(n < 2) {
      return 1;
    }
    return fib(n-2)+fib(n-1);
};

var fibs = [0,1,1];

// var addfib = funtion(e){
//   console.log(e);
//
// }
