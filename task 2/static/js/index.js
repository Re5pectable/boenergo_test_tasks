$( "form" ).submit(function( event ) {
  event.preventDefault();
  $.ajax({
        url: '/',
        type: 'POST',
        data: $(this).serialize(),
        success: function (response) {
          $(".result-wrapper").empty()
          if (response === false) {alert("Некорректные данные.")}
            else {
                  $(".result-wrapper").append(`<span>${response}</span>`)
                }
        },
        error: function (response) {
            
        }
    });
});