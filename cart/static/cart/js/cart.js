// QTY INPUT BOX
/*
$(document).ready(function() {
  const minus = $('.decrement_qty');
  const plus = $('.increment_qty');
  const input = $('.qty_input');
  minus.click(function(e) {
    e.preventDefault();
    var value = input.val();
    if (value > 1) {
      value --;
    }
    input.val(value);
  });
  
  plus.click(function(e) {
    e.preventDefault();
    var value = input.val();
    value ++;
    input.val(value);
  })
});
*/

// SET VALUES
var promoCode;
var promoPrice;
var fadeTime = 300;

// ASSIGN ACTIONS
$('.quantity input').change(function() {
  updateQuantity(this);
});

$('.remove-link').click(function() {
  removeItem(this);
});

$(document).ready(function() {
  updateSumItems();
});

// PROMO DISCOUNT ELEMENT
$('.promo-code-cta').click(function() {
  promoCode = $('#promo-code').val();

  if (promoCode == '10off' || promoCode == '10OFF') {
    // IF PROMO PRICE HAS NO VALUE, SET IT AS 10 FOR 10OFF PROMOPRICE 
    if (!promoPrice) {
      promoPrice = 10;
    } else if (promoCode) {
      promoPrice = promoPrice * 1;
    }
  } else if (promoCode != '') {
    alert("Invalid Promo Code");
    promoPrice = 0;
  }
  // IF THERE IS A PROMOPRICE THAT HAS BEEN SET (it means there is a valid promoCode input) show promo
  if (promoPrice) {
    $('.summary-promo').removeClass('hide');
    $('.promo-value').text(promoPrice.toFixed(2));
    recalculateCart(true);
  }
});

$(document).ready(function(){
  var quantitiy = 0;
     $('.increment_qty').click(function(e){
        // STOP ACTING LIKE A BUTTON
        e.preventDefault();
        // GET THE QTY FIELD
        var quantity = parseInt($('#id_qty_').val());
        // IF ITEM != UNDEFINED
          $('#quantity').val(quantity + 1);
          // INCREMENT
      });
      $('.decrement_qty').click(function(e){
      // STOP ACTING LIKE A BUTTON
      e.preventDefault();
      // GET THE QTY FIELD
      var quantity = parseInt($('#id_qty_').val());
      // IF ITEM != UNDEFINED
      // DECREMENT
      if(quantity > 0){
        $('#quantity').val(quantity - 1);
    }
  });
});

// RECALCULATE CART
function recalculateCart(onlyTotal) { 
  var subtotal = 0;
  // SUM UP ROW TOTALS
  $('.basket-product').each(function() {
    subtotal += parseFloat($(this).children('.subtotal').text());
  });
  // CALCULATE TOTALS
  var total = subtotal;
  // IF VALID PROMOCODE = 10, AND SUBTOTAL < 10 SUBTRACT FROM TOTAL
  var promoPrice = parseFloat($('.promo-value').text());
  if (promoPrice) {
    if (subtotal >= 10) {
      total -= promoPrice;
    } else {
      alert('Order must be more than €10 for Promo code to apply.');
      $('.summary-promo').addClass('hide');
    }
  }

  // IF SWITCH FOR UPDATE ONLY TOTAL, UPDATE ONLY DISPLAY
  if (onlyTotal) {
    // UPDATE TOTAL DISPLAY
    $('.total-value').fadeOut(fadeTime, function() {
      $('#basket-total').html(total.toFixed(2));
      $('.total-value').fadeIn(fadeTime);
    });
  } else {
    // UPDATE SUMMARY DISPLAY
    $('.final-value').fadeOut(fadeTime, function() {
      $('#basket-subtotal').html(subtotal.toFixed(2));
      $('#basket-total').html(total.toFixed(2));
      if (total == 0) {
        $('.checkout-cta').fadeOut(fadeTime);
      } else {
        $('.checkout-cta').fadeIn(fadeTime);
      }
      $('.final-value').fadeIn(fadeTime);
    });
  }
}

// UPDATE QUANTITY
function updateQuantity(quantityInput) {
  // CALCULATE LINE PRICE
  // var productRow = $(quantityInput).closest('.input-group').find('.qty-input')[0];
  var productRow = $(quantityInput).parent().parent().parent();
  var price = parseFloat(productRow.children('.price').text());
  var quantity = $(quantityInput).val();
  var linePrice = price * quantity;

  // UPDATE LINE PRICE TOTAL & RECALC CART TOTALS
  productRow.children('.subtotal').each(function() {
    $(this).fadeOut(fadeTime, function() {
      $(this).text(linePrice.toFixed(2));
      recalculateCart();
      $(this).fadeIn(fadeTime);
    });
  });
  productRow.find('.item-quantity').text(quantity);
  updateSumItems();
}


function updateSumItems() {
  var sumItems = 0;
  $('.quantity input').each(function() {
    sumItems += parseInt($(this).val());
  });
  $('.total-items').text(sumItems);
}


// REMOVE PRODUCT FROM CART
function removeItem(removeButton) {
  // REMOVE ROW FROM DOM AND RECALC TOTALS
  var productRow = $(removeButton).parent();
  productRow.slideUp(fadeTime, function() {
    productRow.remove();
    recalculateCart();
    updateSumItems();
  });
}

// REMOVE
$('.remove-link').click(function(e) {
  var csrfToken = "{{ csrf_token }}";
  var productId = $(this).attr('id').split('remove_')[1];
  var url = `/cart/remove/${productId}/`;
  var data = {'Csrfmiddlewaretoken': csrfToken, 'quantity': quantity};

  $.post(url)
  .done(function() {
    location.reload();
  });
})

// UPDATE CART 
$('.adjust_cart_qty_').change(function(e) {
  e.preventDefault();
  var closestInput = $(this).closestInput('.input').find('.adjust_cart_qty')[0];
  var currentValue = parseInt($(closestInput).val())
  $(closestInput).value(currentValue +1 || -1);
  var productId = $(this).data('product_id');
});

// UPDATE FORM
$('.update-link').click(function(e) {
  var form = $(this).prev('.update-form');
  form.submit();
})

console.log('im here cart.js')