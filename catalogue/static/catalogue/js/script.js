$(document).ready(function () {
    var temp, denomination = [1, 2, 3, 5, 10, 20, 25, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000,
        50000, 100000, 200000, 500000, 100000, 200000, 500000, 1000000, 2000000];
    for (var i = 0; i < denomination.length; i++) {
        temp = document.createElement('option');
        $(temp).attr('value', denomination[i]).html(denomination[i]);
        $('#from').append(temp);
    }

    for (var i = denomination.length - 1; i >= 0; i--) {
        temp = document.createElement('option');
        $(temp).attr('value', denomination[i]).html(denomination[i]);
        $('#to').append(temp);
    }

    $('#from, #to').change(function () {
        if (parseInt($('#from').val()) > parseInt($('#to').val())) {
            temp = $('#to').val();
            $('#to').val($('#from').val());
            $('#from').val(temp);
        }
    });

    $('.toggle-menu').click(function () {
        if ($(this.lastChild).hasClass('fa-chevron-up')) {
            $(this.lastChild).removeClass('fa-chevron-up').addClass('fa-chevron-down');
        } else $(this.lastChild).removeClass('fa-chevron-down').addClass('fa-chevron-up');
    });

    $('#id_year_0, #id_year_1').change(function () {
        var val1 = parseInt($('#id_year_0').val()),
            val2 = parseInt($('#id_year_1').val()),
            rs = $('.range-slider').children();
        console.log("val1 = " + val1 + ", val2 = " + val2);
        if (val1 > 2017) val1 = 2017;
        if (val2 > 2017) val2 = 2017;
        if (val1 < 1917) val1 = 1917;
        if (val2 < 1917) val2 = 1917;
        if (val1 > val2) {
            var temp = val2;
            val2 = val1;
            val1 = temp;
        } else if (val1 === val2) {
            if (val1 === 2017) val1 -= 1;
            else if (val1 === 1917) val2 += 1;
            else val1 += 1;
        }

        $('#id_year_0').attr('value', val1);
        $('#id_year_1').attr('value', val2);

        rs[0].value = parseInt(val1);
        rs[1].value = parseInt(val2);
        test();
    });
});

function showcontent(id) {
    $(id).slideToggle('fast');
}

/*        slider           */
function getVals() {
    // Get slider values
    var parent = this.parentNode;
    var slides = parent.getElementsByTagName("input");
    var slide1 = parseFloat(slides[0].value);
    var slide2 = parseFloat(slides[1].value);
    // Neither slider will clip the other, so make sure we determine which is larger
    if (slide1 > slide2) {
        var tmp = slide2;
        slide2 = slide1;
        slide1 = tmp;
    }
    $('#id_year_0').attr('value', slide1);
    $('#id_year_1').attr('value', slide2);
}

window.onload = function test() {
    // Initialize Sliders
    var sliderSections = document.getElementsByClassName("range-slider");
    for (var x = 0; x < sliderSections.length; x++) {
        var sliders = sliderSections[x].getElementsByTagName("input");
        for (var y = 0; y < sliders.length; y++) {
            if (sliders[y].type === "range") {
                sliders[y].oninput = getVals;
                // Manually trigger event first time to display values
                sliders[y].oninput();
            }
        }
    }
};
/*         more slider      */
  // var body = document.body,
  //     html = document.documentElement,
  //     height = Math.max( body.scrollHeight, body.offsetHeight,
  //         html.clientHeight, html.scrollHeight, html.offsetHeight );
  // console.log(height);
  // if(height <= html.clientHeight){
  //     $('footer').css('position', 'absolute');
  //   } else $('footer').css('position', 'relative');