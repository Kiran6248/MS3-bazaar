$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
  });

// -------------------------------------------------------------------- footer copyright
function copyrightYear() {
    var d = new Date();
    var y = d.getFullYear();
    document.getElementById("copyright").innerHTML = y;
}
copyrightYear();