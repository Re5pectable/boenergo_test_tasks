$( "form" ).submit(function( event ) {
  event.preventDefault();
  $.ajax({
        url: '/',
        type: 'POST',
        data: $(this).serialize(),
        success: function (response) {
        $(".result-wrapper").empty()
        console.log(response)
           if (response === false) {alert("Ошибка. Скорее всего вы ввели некорректные значения. Помните, что А не должно равняться нулю. В таком случае это не квадратное уравнение и решается оно иначе")}
           	else if (response === '') {$(".result-wrapper").append("<h3>У этого уравнения нет ответа</h3>")}
           		else {
           			for (var i = 0; i < response.length; i++) {
           				{$(".result-wrapper").append(`<h3>${i+1}) Ответ: <span>${response[i]}</h3>`)}	
           			}
           		}
        },
        error: function (response) {
            
        }
    });
});


function resizeInput() {
  console.log($('input[type="text"]').width())
   if ($(this).width() + 15 <= 250) {
      $(this).css({"width": 5 + $(this).val().length*15 + "px"})
    } else {return}
    if ($(this).val() == "") {
      $(this).css({"width": "20px"})
  }
}


$('input[type="text"]').keyup(resizeInput)

let info = "Любое квадратное уравнение можно представить в виде трех слагаемых, где A, B, C - их множители. В случае, если многочлен не имеет какого-то слагаемого, то на месте его коэффициента просто поставьте 0."
$("img").attr("title", info)