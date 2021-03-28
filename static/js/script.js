$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('.tooltipped').tooltip();
     $('select').formSelect();
  });

// -------------------------------------------------------------------- footer copyright
function copyrightYear() {
    var d = new Date();
    var y = d.getFullYear();
    document.getElementById("copyright").innerHTML = y;
}
copyrightYear();