$('#header .header-icon').each(function(index, eachOne) {
        $(eachOne).hover(
            function() {
                $(eachOne).next().addClass('show');
                $(eachOne).next().removeClass('hide');
                $(eachOne).addClass('hover');

            },
            function() {
                $(eachOne).next().addClass('hide');
                $(eachOne).next().removeClass('show');
                $(eachOne).removeClass('hover');
            }
        )
});
$('#header .hiden-list').each(function(index, eachOne) {
        $(eachOne).hover(
            function() {
                $(eachOne).addClass('show');
                $(eachOne).removeClass('hide');
                $(eachOne).prev().addClass('hover');

            },
            function() {
                $(eachOne).addClass('hide');
                $(eachOne).removeClass('show');
                $(eachOne).prev().removeClass('hover');
            }
        );
});


$(document).ready(function() {
        var path = document.location.pathname;
        pathList = path.split("\/");
        if (pathList[1] !== "home") {
            if (pathList[1] == "profile") {
                $('#home-nav').removeClass("active");
                $('#profile-nav').addClass("active");
            }
            else if (pathList[1] == "tags") {
                $('#home-nav').removeClass("active");
                $('#tags-nav').addClass("active");
            }
        }

});


$(document).ready(function() {
        $('.profile-top-follow').click(function(){
                if($(this).hasClass('btn-primary')) {
                    $(this).addClass('btn-active');
                    $(this).removeClass('btn-primary');
                    $(this).html('following');
                }
                else {
                    $(this).addClass('btn-primary');
                    $(this).removeClass('btn-active');
                    $(this).html('follow');
                }
        });     
});
