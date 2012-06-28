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
        $('.profile-top-follow').live('click',function(){
                url = $(this).prop('href');
                if($(this).hasClass('btn-primary')) {
                    $.ajax({
                            context: this,
                            url: url,
                            type: 'post',
                            success: function(msg) {
                                if (msg==='1') {
                                    var newUrl = url.replace('follow', 'unfollow');
                                    $(this).prop('href', newUrl);
                                    $(this).addClass('btn-active');
                                    $(this).removeClass('btn-primary');
                                    $(this).html('following');
                                }
                            }
                    });
                }
                else {
                    $.ajax({
                            context: this,
                            url: $(this).prop('href'),
                            type: 'post',
                            success: function(msg) {
                                if (msg==='1') {
                                    var url = $(this).prop('href');
                                    var newUrl = url.replace('unfollow', 'follow');
                                    $(this).prop('href', newUrl);
                                    $(this).addClass('btn-primary');
                                    $(this).removeClass('btn-active');
                                    $(this).html('follow');
                                }
                            }
                    });
                }
                return false;
        });     
        $('.profile-top-follow').live({
                mouseenter: function() {
                    if ($(this).hasClass('btn-active')) {
                        $(this).addClass('btn-danger');
                        $(this).html('unfollow');
                    }
                    else if ($(this).hasClass('btn-primary')) {
                        $(this).addClass('btn-active');
                    }
                },
                mouseleave: function() {
                    $(this).removeClass('btn-danger');
                    if ($(this).hasClass('btn-primary')) {
                        $(this).html('follow');
                        $(this).removeClass('btn-active');
                    }
                    else {
                        $(this).html('following');
                    }
                }
        });
});
