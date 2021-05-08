$(document).ready(function (){
    
    $('form#sign-form').validate({
            
        highlight: function(element, errorClass){
            $(element).add($(element).parent()).addClass("invalidElem");
            
        },
        unhighlight: function(element, errorClass){
            $(element).add($(element).parent()).removeClass('invalidElem');
            
        },
        submitHandler: function (form) {
            $.ajax({
                url: '/reg',
                type: 'post',
                data: $('form#sign-form').serialize(),
                success: function(data) {
                           if (data.redirect){
                               console.log(data.redirect);
                               window.location = data.redirect;
                           }
                           if (data.Fail == '-1'){
                               console.log("Exist");
                               $('form#sign-form').each(function () {
                                    $('.test').remove();
                                    $(this).addClass($(this).append("<div class= 'test'>Такой пользователь уже есть. Воспользуйтесь формой восстановления пароля. <a href = ''>Восстановить</a></div>"));
                                 });
                           }
                         }
            });
          },
        errorElement: "div",
        errorClass: "errorMsg",
    });
    $('.sign-email').each(function(index, elem){
        $(elem).rules("add", {
            email:true,
            required:true,
            messages: {
                required: "Пожалуйста введите Email",
                email: "Вы ввели не email"
            }
        })
    });
    $('.sign-login').each(function(index, elem){
        $(elem).rules("add", {
            required:true,
            minlength: 4,
            messages:{
                required: "Пожалуйста введите Login",
                minlength: "Login должен быть не менее 4-х символов"
            }
        })
    });
    $('.sign-password').each(function(index, elem){
        $(elem).rules("add", {
            required: true,
            minlength: 6,
            messages:{
                required: "Пожалуйста введите пароль",
                minlength: "Пароль должен быть не менее 6 символов"
            }
        })
    });
});