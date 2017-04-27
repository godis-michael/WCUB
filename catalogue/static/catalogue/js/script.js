$(document).ready(function () {
  var temp, denomination = [1,2,3,5,10,20,25,50,100,200,500,1000,2000,5000,10000,20000,
      50000,100000,200000,500000,100000,200000,500000,1000000,2000000];
  for(var i = 0; i < denomination.length; i++){
      temp = document.createElement('option');
      $(temp).attr('value', denomination[i]).html(denomination[i]);
      $('#from').append(temp);
  }

  for(var i = denomination.length - 1; i >= 0; i--){
      temp = document.createElement('option');
      $(temp).attr('value', denomination[i]).html(denomination[i]);
      $('#to').append(temp);
  }

  $('#from, #to').change(function () {
      if(parseInt($('#from').val()) > parseInt($('#to').val())){
          temp = $('#to').val();
          $('#to').val($('#from').val());
          $('#from').val(temp);
      }
  });

  $('.toggle-menu').click(function () {
      console.log(this.lastChild);
      if($(this.lastChild).hasClass('fa-chevron-up')){
          $(this.lastChild).removeClass('fa-chevron-up').addClass('fa-chevron-down');
      } else $(this.lastChild).removeClass('fa-chevron-down').addClass('fa-chevron-up');
  });

});

function showcontent(id) {
    $(id).slideToggle('fast');
}

/*        slider           */
function getVals(){
  // Get slider values
  var parent = this.parentNode;
  var slides = parent.getElementsByTagName("input");
    var slide1 = parseFloat( slides[0].value );
    var slide2 = parseFloat( slides[1].value );
  // Neither slider will clip the other, so make sure we determine which is larger
  if( slide1 > slide2 ){ var tmp = slide2; slide2 = slide1; slide1 = tmp; }

  $('#firstPer').attr('value', slide1);
  $('#secPer').attr('value', slide2);
}

window.onload = function(){
  // Initialize Sliders
  var sliderSections = document.getElementsByClassName("range-slider");
      for( var x = 0; x < sliderSections.length; x++ ){
        var sliders = sliderSections[x].getElementsByTagName("input");
        for( var y = 0; y < sliders.length; y++ ){
          if( sliders[y].type ==="range" ){
            sliders[y].oninput = getVals;
            // Manually trigger event first time to display values
            sliders[y].oninput();
          }
        }
      }
};
/*         more slider      */
