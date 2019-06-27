$(document).ready(function(){
      $( ".form-group" ).wrap( "<div class='col-md-6'></div>" );
      $("#id_time").attr('class', 'form-control col-md-10');
      $("#id_date").attr('class', 'form-control col-md-10');
      $("#id_name").attr('placeholder', 'Your Name');
      $("#id_email").attr('placeholder', 'Your Email');
      $("#id_phone").attr('placeholder', 'Your Phone');
});