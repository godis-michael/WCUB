$(document).ready(function () {
    setTimeout(function () {
        $('#animated-feedback').append('<p class="animated rollIn">' + "З'явилось запитання?" + '</p>');
        setTimeout(function () {
            $('#animated-feedback').append('<p class="animated rollIn" style="margin-left: 1vw;">' + "Знайшли несправність на сайті?" + '</p>');
            setTimeout(function () {
                $('#animated-feedback').append('<p class="animated rollIn" style="margin-left: 2vw;">' + "Є ідеї або пропозиції щодо роботи порталу?" + '</p>');
                setTimeout(function () {
                    $('#animated-feedback').append('<p class="animated fadeIn" style="margin-left: 3vw; margin-top: 13%;">' + "Напиши нам про це" + '</p>');
                    $('#animated-feedback').append('<a href = "#feedback-section" ><i class = "fa fa-angle-double-down" style = "color: #5f82a6; font-size: 48px; margin-left: 50%;" ></i></a>'
                    )
                    ;
                }, 1000);
            }, 1000);
        }, 1000);
    }, 1000);

    var temp, denomination = [1, 2, 3, 5, 10, 20, 25, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000,
        50000, 100000, 200000, 500000, 100000, 200000, 500000, 1000000];

    $('#id_year_0').attr('value', 1917);
    $('#id_year_1').attr('value', 2017);

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

    $('#id_year_0, #id_year_1').change(function () {
        if (parseInt($('#id_year_0').val()) > parseInt($('#id_year_1').val())) {
            temp = $('#id_year_1').val();
            $('#id_year_1').val($('#id_year_0').val());
            $('#id_year_0').val(temp);
        }
    });

    $('.toggle-menu').click(function () {
        if ($(this.lastChild).hasClass('fa-chevron-up')) {
            $(this.lastChild).removeClass('fa-chevron-up').addClass('fa-chevron-down');
        } else $(this.lastChild).removeClass('fa-chevron-down').addClass('fa-chevron-up');
    });

    $("#zoom_07").elevateZoom({
        zoomType: "lens",
        lensShape: "round",
        lensSize: 200
    });
});

function showcontent(id) {
    $(id).slideToggle('fast');
}

$(Window).scroll(function () {
    if($(document).scrollTop() > 100){
        $('.scroll_up').fadeIn('slow').css('opacity','1');
    }else $('.scroll_up').fadeOut('slow');
});

/*         more slider      */
// var body = document.body,
//     html = document.documentElement,
//     height = Math.max( body.scrollHeight, body.offsetHeight,
//         html.clientHeight, html.scrollHeight, html.offsetHeight );
// console.log(height);
// if(height <= html.clientHeight){
//     $('footer').css('position', 'absolute');
//   } else $('footer').css('position', 'relative');