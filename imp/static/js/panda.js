$(document).ready(function(){
        //add action to follow button
        $(".follow-item-button").live('click', function(){
                if($(this).hasClass('follow-item-active')) {
                    $(this).removeClass('follow-item-active');
                }
                else {
                    $(this).addClass('follow-item-active');
                }

                return false;
                
        });



        $("ul#category-tab li a").click(function() {
                //change the current tab to active state
                $('#content-items')[0].innerHTML = '';
                $("ul#category-tab li a").removeClass("active");
                $(this).addClass("active");

                //get the id of the tab
                var category = $(this).prop('id');
                var callbackUrl = '/content/provider/get'+category+'s';
                var mode = 1;

                if (category === 'all') {
                    callbackUrl = '/content/provider/getrecentall';
                    mode = 1;
                }

                else if (category === 'people') {
                    callbackUrl = '/content/provider/getpeople';
                }


                //send ajax to get the events/offer/needs
                $.ajax({
                        url: callbackUrl,
                        type: 'post',
                        data: {'cursor':0,'mode':mode},
                        success: function(contentJson) {
                            contentJson = JSON.parse(contentJson);
                            if (category === 'people') {
                                /*showPeople(contentJson);*/
                                showContent(contentJson, category);
                            }

                            else {
                                showContent(contentJson, category);
                            }
                        }
                });
                return false;
        });

        function showPeople(contentJson) {
            /*$('#content-items')[0].innerHTML = '';*/
            var i = contentJson.length-1;
            for (i;i>=0;i--) {
            }
        }

        function showContent(contentJson, category) {
            if (contentJson === 'null') {
                $('#content-items')[0].innerHTML = "<p>No items in the database.</p>";
            }

            else {
                var i = contentJson.length-1;
                for (i;i>=0;i--) {
                    var people = 0;
                    if (contentJson[i]._type == 'People') {
                        people = 1;
                    }
                    var item = contentJson[i];
                    showEachContent(item, category, people);
                }
            }
        }

        function showEachContent(item, category, people) {
            var authorName = item.author.first_name+' '+item.author.last_name;
            var contentItem = $('<div class="content-item"></div>');

            //parse the user info box
            var userContainer = $('<div class="user-container grid_3 omega"></div>');
            var userInfo = $('<div class="user-info"></div>');
            var avatarWrap = $('<a class="avatar-wrap" href=""></a>');
            avatarWrap.prop('href', '/profile/'+item.author.user_id);
            var avatarImg = $('<img class="avatar"></img>');
            avatarImg.prop('src', '/static/img/avatar_big.jpg');
            avatarWrap.append(avatarImg);
            var followPeople = $('<a class="profile-top-follow btn btn-primary"></a>');
            if (item.my_user_id!==item.author.user_id) {
                if (item.author.is_followed === '0') {
                    followPeople.prop('href', '/action/people/follow/'+item.author.user_id);
                    followPeople.html('follow');
                }
                else {
                    followPeople.prop('href', '/action/people/unfollow/'+item.author.user_id);
                    followPeople.removeClass('btn-primary');
                    followPeople.addClass('btn-active');
                    followPeople.html('following');
                }
                followPeople.prop('name', 'people-follow-'+item.author.user_id);
                avatarWrap.append(followPeople);
            }
            var pName = $('<p class="name">Name</p>');
            pName.html(item.author.first_name+' '+item.author.last_name);
            var pLocation = $('<p>Location</p>');
            pLocation.html(item.author.location);
            userInfo.append(avatarWrap);
            avatarWrap.append(pName);
            userInfo.append(pLocation);
            userContainer.append(userInfo);

            //parse the content details
            var itemDetails = $('<div class="item-details grid_9 alpha"></div');
            var itemDetailMain = $('<div class="item-details-main"></div>');
            if (!people) {
                var followLink = $('<a href="#" class="follow-item-button"></a>');
                itemDetailMain.append(followLink);
            }

            var generalInfo = $('<div class="general-info"></div');
            var itemHeaderLink = $('<a></a>');
            if (people) {
                itemHeaderLink.prop('href', '/profile/'+item.author.user_id);
            }
            else if(category==='all'){
                itemHeaderLink.prop('href', '/'+item._type.split('s')[0].toLowerCase()+'/'+item.id);
            }
            else {
                itemHeaderLink.prop('href', '/'+category+'/'+item.id);
            }
            var itemHeader = $('<h3 class="item-title"></h3>');
            if (category==='all') {
                if (!people) {
                    itemHeader.html('['+item._type+']'+item.title);
                }
                else {
                    itemHeader.html('[People]'+authorName);
                }
            }
            else {
                if (!people) {
                    itemHeader.html(item.title);
                }
                else {
                    itemHeader.html(authorName);
                }
            }
            itemHeaderLink.append(itemHeader);
            generalInfo.append(itemHeaderLink);
            if (category === 'event') {
                var itemTime = $('<p class="item-time">May-2123 to May-23</p>');
                itemTime.html(item.start_date+'-'+item.end_date);
                generalInfo.append(itemTime);
            }
            itemDetailMain.append(generalInfo);

            var descriptionWrap = $('<div class="item-description-wrap"></div>');
            var itemDescription = $('<p class="item-description"></p>');
            itemDescription.html(item.description);

            descriptionWrap.append(itemDescription);
            itemDetailMain.append(descriptionWrap);
            itemDetails.append(itemDetailMain);

            var itemTags = $('<div class="item-details-tags"></div>');
            itemDetails.append(itemTags);
            contentItem.append(itemDetails);
            contentItem.append(userContainer);

            /*var clearFix = $('<div class="clearfix"></div>');*/

            /*clearFix.append(contentItem);*/
            $('#content-items').append(contentItem);
            var clearDiv = $('<div></div>');
            clearDiv.css('clear','both');
            clearDiv.css('padding-bottom','20px');
            $('#content-items').append(clearDiv);

        }
        $('#all').trigger('click');
});
