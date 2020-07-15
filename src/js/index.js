require('../../node_modules/bootstrap/dist/js/bootstrap.js');


$(document).ready(function () {
    $('.js-slick').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        prevArrow: '.js-prev',
        nextArrow: '.js-next'
    });
});

$(document).ready(function () {
    $('.js-member-slick').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        prevArrow: '.js-member-prev',
        nextArrow: '.js-member-next'
    });
});

$('.js-show-avator').click(function () {
    $('.js-avator-nav-item').removeClass('d-none');
    $(this).hide();
});

$('.js-oh-my-tab').click(function (){
    var targetId = $(this).data('target');

    $('.js-oh-my-tab-content > div').hide();
    $(targetId).fadeIn();
    
    $('.js-oh-my-tab').removeClass('text-primary');
    $(this).addClass('text-primary');
    
})