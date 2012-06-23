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
        )
});
