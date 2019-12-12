var changeheading = function(e) {
  var h = document.getElementById("h");
  console.log(e);
  h.innerHTML = e.target.innerHTML;
}

var removeItem = function(e) {

};

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++){
  lis[i].addEventListener('mouseover', changeheading);
  lis[i].addEventListener("mouseout", changeheading);
}
