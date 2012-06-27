$(document).ready(function(){
        $("#top-filter a").click(function() {
            $("#top-filter a").removeClass("active");
            $(this).addClass("active");

            if($(this).prop('id') === 'event') {
                var readyToHide = $(".profile-info>div.show");
                readyToHide.addClass("hide");
                readyToHide.removeClass("show");

                var readyToShow = $("#create-event");
                readyToShow.addClass("show");
                readyToShow.removeClass("hide");
            }
            else if($(this).prop('id') === 'offer') {
                var readyToHide = $(".profile-info>div.show");
                readyToHide.addClass("hide");
                readyToHide.removeClass("show");

                var readyToShow = $("#create-offer");
                readyToShow.addClass("show");
                readyToShow.removeClass("hide");
            }
            else if($(this).prop('id') === 'need') {
                var readyToHide = $(".profile-info>div.show");
                readyToHide.addClass("hide");
                readyToHide.removeClass("show");

                var readyToShow = $("#create-need");
                readyToShow.addClass("show");
                readyToShow.removeClass("hide");
            }
        });
});
