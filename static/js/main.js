$(document).ready(function(){

    var iconCart = $('.icon-cart');
    iconCart.on('click', function () {
        $('.shopping-cart-content').toggleClass('cart-visible');
    });

    $.scrollUp({
        scrollDistance: 300,
        scrollSpeed: 300,
        scrollFrom: 'bottom',
        easingType: 'linear',
        animation: 'fade',
        animationSpeed: 200,
        zIndex: 2147483647,
    });

    /* Cart search */
    $(".account-satting-active , .search-active").on("click", function (e) {
        e.preventDefault();
        $(this).parent().find('.account-dropdown , .search-content').slideToggle('medium');
    });

});