$(document).ready(function(){

    var iconCart = $('.icon-cart');
    iconCart.on('click', function () {
        $('.shopping-cart-content').toggleClass('cart-visible');
    });

    /* Cart search */
    $(".account-satting-active , .search-active").on("click", function (e) {
        e.preventDefault();
        $(this).parent().find('.account-dropdown , .search-content').slideToggle('medium');
    });

});