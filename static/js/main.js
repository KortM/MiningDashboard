function send_form(event){
    event.preventDefault();
    console.log("send");
    console.log($('form#sign-form').serialize());
    $.ajax({
        url: '/reg',
        type: 'post',
        data: $('form#sign-form').serialize(),
        success: function(data) {
                   // ... do something with the data...
                 }
    });
}