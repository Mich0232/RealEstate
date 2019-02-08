$(window).on('resize', function () {
    var map_column = $('#map-column');
    var adverts_column = $('#advert-list-column');
    var screen_width = $(window).width();

    if(screen_width >= 992){
        // Large screen
        map_column.show();
        map_column.removeClass('col-12');
        adverts_column.removeClass('col-12');

        map_column.addClass('col-6');
        adverts_column.addClass('col-6');
        return;
    }

    if(screen_width < 992 && screen_width >= 768)
    {
        // Medium screen
        map_column.show();
        map_column.removeClass('col-6');
        adverts_column.removeClass('col-6');

        map_column.addClass('col-12');
        adverts_column.addClass('col-12');
        return;
    }

    if(screen_width < 768){
        // small screen
        map_column.hide();
        adverts_column.addClass('col-12')

    }

}).resize();
