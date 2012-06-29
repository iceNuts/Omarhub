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
        $('#home-nav').removeClass("active");

        if (pathList[1] !== "home") {
            if (pathList[1] == "profile") {
                $('#profile-nav').addClass("active");
            }
            else if (pathList[1] == "tags") {
                $('#tags-nav').addClass("active");
            }
        }
        else if (pathList[1] === "home") {
        $('#home-nav').addClass("active");
    }
});


$(document).ready(function() {
        $('.profile-top-follow').live('click',function(){
                url = $(this).prop('href');
                name = $(this).prop('name');
                if($(this).hasClass('btn-primary')) {
                    $.ajax({
                            context: this,
                            url: url,
                            type: 'post',
                            success: function(msg) {
                                if (msg==='1') {
                                    var newUrl = url.replace('follow', 'unfollow');
                                    var allUserLink = $('a[name="'+name+'"]');
                                    allUserLink.prop('href', newUrl);
                                    allUserLink.addClass('btn-active');
                                    allUserLink.removeClass('btn-primary');
                                    allUserLink.html('following');
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
                                    var newUrl = url.replace('unfollow', 'follow');
                                    var allUserLink = $('a[name="'+name+'"]');
                                    allUserLink.prop('href', newUrl);
                                    allUserLink.addClass('btn-primary');
                                    allUserLink.removeClass('btn-active');
                                    allUserLink.html('follow');
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
