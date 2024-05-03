$(function () {
  // var dropArea = $("#drop-area");

  // dropArea.on({
  //   dragover: function(e) {
  //     e.preventDefault();
  //     $(this).addClass("highlight");
  //   },
  //   dragleave: function() {
  //     $(this).removeClass("highlight");
  //   },
  //   drop: function(e) {
  //     e.preventDefault();
  //     $(this).removeClass("highlight");
  //     var file = e.originalEvent.dataTransfer.files[0];
  //     readURL(file);
  //   }
  // });

  $('#upload').on('change', function () {
    readURL(this.files[0]);
  });
});

function readURL(file) {
  if (file && file.type.match(/^image\//)) {
    var reader = new FileReader();
    reader.onload = function (e) {
      $('#imageResult')
        .attr('src', e.target.result);
      $('#upload-label')
        .removeClass('hidden')
        .text('File name: ' + file.name);
    };
    reader.readAsDataURL(file);
  } else {
    alert("Not Supported File Image");
  }
}


function replay() {
  audio = document.getElementById("sound")
  audio.pause() // important!!!
  audio.currentTime = 0
  audio.play()
}

function change(){
  content = document.getElementById("content")
  load = document.getElementById("load")
  content.classList.add('hidden'); 
  load.classList.remove('hidden');
  console.log("HELLO")
}