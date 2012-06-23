$("input#login-username").blur(function(){
        var username = $("input#login-username").val();
        if (username === '') {
            return false;
        }
        else {
            $.ajax({
                    url: "/auth/login/verify/username",
                    type: "post",
                    data: {"username":username},
                    success: function(msg) {
                        var popError = $("div#login-email-checker");
                        if(msg=="0") {
                            var errorInfo = $("p#error-info");
                            errorInfo[0].innerHTML = "The Email doesn't exist.";
                            if (popError.hasClass("hide")) {
                                popError.addClass("show");
                                popError.removeClass("hide");
                            }
                        }
                        else {
                            if (popError.hasClass("show")) {
                                popError.addClass("hide");
                                popError.removeClass("show");
                            }
                        }
                    }

                }
            );
        }
});


if ($("div#error")[0].innerHTML!=="") {
    var errorInfo = $("p#error-info");
    errorInfo[0].innerHTML = "Email doesn't match password.";
    var popError = $("div#login-email-checker");
    if (popError.hasClass("hide")) {
        popError.addClass("show");
        popError.removeClass("hide");
    }
}
