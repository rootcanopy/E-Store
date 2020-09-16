// UPDATE CART QTY

var fadeTime = 300;
// ASSIGN ACTIONS
$('.quantity input').change(function() {
    updateQuantity(this);
});

$('.remove button').click(function() {
    removeProduct(this);
});

$(document).ready(function() {
    updateProductSums();
});

// RECALCULATE CART
function recalculateCart(onlyTotal) {
    var subtotal = 0;

    // SUM UP ROW TOTALS
    $('.cart-product').each(function() {
        subtotal += parseFloat($(this).children('.subtotal').text());
    });
    // CALCULATE TOTALS
    var total = subtotal;

    // IF SWITCH FOR UPDATE ONLY TOTAL, UPDATE ONLY TOTAL DISPLAY
    if (onlyTotal) {
        //UPDATE TOTAL DISPLAY
        $('.total-value').fadeOut(fadeTime, function() {
            $('#grand-total').html(total.toFixed(2));
            $('.total-value').fadeIn(fadeTime);
        });
    } else {
        // UPDATE SUMMARY DISPLAY
        $('.final-value').fadeOut(fadeTime, function() {
            $('#grand-subtotal').html(subtotal.toFixed(2));
            $('#grand-total').html(total.toFixed(2));
            if (total == 0) {
                $('.checkout-cta').fadeOut(fadeTime);
            } else {
                $('.checkout-cta').fadeIn(fadeTime);
            }
            $('.final-value').fadeIn(fadeTime);
        });
    }
}

// UPDATE QTY
function updateQuantity(quantityInput) {
    //CALC LINE PRICE
    var productRow = $(quantityInput).parent().parent();
    var price =
    parseFloat(productRow.children('price').text());
    var quantity = $(quantityInput).val();
    var linePrice = price * quantity;

    // UPDATE LINE PRICE TOTALS & RECALC CART TOTALS
    productRow.children('.subtotal').each(function() {
        $(this).fadeOut(fadeTime, function() {
            $(this).text(linePrice.toFixed(2));
            recalculateCart();
            $(this).fadeIn(fadeTime);
        });
    });

    productRow.find('.product-quantity').text(quantity);
    updateProductSums();
}

function updateProductSums() {
    var productSums = 0;
    $('.quantity input').each(function() {
        productSums += parseInt($(this).val());
    });
    $('.total-products').text(productSums);
}

// REMOVE ITEM FROM CART
function removeProduct(removeButton) {
    // REMOVE ROW FROM DOM & RECALC CART TOTAL
    var productRow = $(removeButton).parent().parent();
    productRow.slideUp(fadeTime, function() {
        productRow.remove();
        recalculateCart();
        updateProductSums();
        
    });
}
console.log('i am here');