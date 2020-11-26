(function($) {

  $('#reset').on('click', function(){
      $('#register-form').reset();
  });

})(jQuery);

// Edit Employee

$('.edit_emp').click(function(e){
  //  alert('hhhh')
  // e.preventDefault();
  console.log($(this).attr('id'))
  div_id=$(this).attr('id')
  console.log($('.emp_name').val())
  
  if($(this).val()== 'Edit')
  {
  $('#'+div_id).closest('div').find('.editfield').prop('readonly', false);
   $('#'+div_id).closest('div').find('.pic_div').append('<form method="POST" enctype="multipart/form-data" class="image_emp"><input type="file" name="propic" class="up_img" ></form>')
  
  // $('#'+div_id).closest('div').find('.editfield').css({'border-color':'orange'})  
  $('#'+div_id).closest('div').find('.edit_emp').val('Update')
  }
  else{
    emp_name=$('#'+div_id).closest('div').find('.emp_name').val()
    emp_email=$('#'+div_id).closest('div').find('.emp_email').val()
    emp_phone=$('#'+div_id).closest('div').find('.emp_phone').val()
    emp_profile=$('#'+div_id).closest('div').find('.emp_profile').val()
    emp_address=$('#'+div_id).closest('div').find('.emp_address').val()
    emp_state=$('#'+div_id).closest('div').find('.emp_state').val()
    emp_city=$('#'+div_id).closest('div').find('.emp_city').val()
    emp_pincode=$('#'+div_id).closest('div').find('.emp_pincode').val()
    console.log(emp_email)
   
    var pic=$('#'+div_id).closest('div').find('.image_emp')[0];
    
    console.log(pic)
    var data = new FormData(pic);
    console.log(data)

    
         data.append('user_id', div_id);
         data.append('csrfmiddlewaretoken', window.CSRF_TOKEN);
         $.ajax({
             type:"POST",
             enctype: 'multipart/form-data',
             url: "/data_image_upload",
             async:false,
             data:data,
             processData: false,
             contentType: false,
             cache: false,
             timeout: 60000,
             success: function( data ){
               console.log(data);
             }
         });

         
            
                $.ajax({
                    type:"POST",
                    url: "/update_data",
                    async:false,
                    
                    data:{csrfmiddlewaretoken: window.CSRF_TOKEN,name:emp_name,user_id:div_id,email:emp_email,phone:emp_phone,
                              profile:emp_profile,address:emp_address,state:emp_state,city:emp_city,pincode:emp_pincode},
                      
                    success: function(data){
                    console.log(data.data);
                    new Noty({
                      type: 'success',
                      layout: 'topRight',
                      theme: 'metroui',
                      text: 'Data updated successfully',
                      timeout: '3000',
                      progressBar: true,
                      closeWith: ['click'],
                      killer: true,
                   }).show();

                    }
        
                });
                    setTimeout(function(){
                            location.reload();
                          }, 2000);

  }



});


 // TO DELETE emp

 $('.delete_emp').click(function(){
  row_id=$(this).attr('id')
  $.ajax({
    type:"POST",
    url: "/delete_data",
    async:false,
    data:{csrfmiddlewaretoken: window.CSRF_TOKEN,div_id:row_id},
      
    success: function(data){
    console.log(data.data);
    new Noty({
      type: 'success',
      layout: 'topRight',
      theme: 'metroui',
      text: 'Data deleted successfully',
      timeout: '2000',
      progressBar: true,
      closeWith: ['click'],
      killer: true,
   }).show();
    }

});
    setTimeout(function(){
            location.reload();
          }, 2000);

})
// TO DELETE 