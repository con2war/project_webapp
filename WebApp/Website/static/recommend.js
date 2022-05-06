$(function() {
    // Button will be disabled until we type anything inside the input field
    const source = document.getElementById('autoComplete');
    const inputHandler = function(e) {
      if(e.target.value==""){
        $('.phone-button').attr('disabled', true);
      }
      else{
        $('.phone-button').attr('disabled', false);
      }
    }
    source.addEventListener('input', inputHandler);
  
    $('.phone-button').on('click',function(){
      var phone = $('.phone').val();
      if (phone=="") {
        $('.results').css('display','none');
        $('.fail').css('display','block');
      }
      else{
        load_details(phone);
      }
    });
    $('.info-button').on('click',function(){
      var phone = $('.phone').val();
      if (phone=="") {
        $('.results').css('display','none');
        $('.fail').css('display','block');
      }
      else{
        load_details(phone);
      }
    });
  });
  
function phone_rec(model){
    $.ajax({
      type:'POST',
      url:"/recommendor",
      data:{'phone':model},
      success: function(recs){
        if(recs=="Sorry! The phone you requested is not in our database. Please check the spelling or try with some other phone"){
          $('.fail').css('display','block');
          $('.results').css('display','none');
          $("#loader").delay(500).fadeOut();
        }
        else {
          $('.fail').css('display','none');
          $('.results').css('display','block');
          var phone_arr = recs.split('---');
          var arr = [];
          for(const phone in phone_arr){
            arr.push(phone_arr[phone]);
          }
          get_phone_details(model);
        }
      },
      error: function(){
        alert("error recs");
        $("#loader").delay(500).fadeOut();
      },
    }); 
  }
