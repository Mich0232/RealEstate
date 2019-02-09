var markers = [];

$(window).ready(function () {
    var mymap = L.map('mapid').setView([50.064651, 19.944981], 13);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 15,
        id: 'mapbox.streets',
        accessToken: map_box_access_token,
    }).addTo(mymap);

    $.ajax({
        url: '/pin_locations/',
        method: 'GET',
        dataType: 'json',
        success: function (data) {
            if(data.success){
                var cords = data.cords;
                cords.forEach(function (item) {
                    var newMarker = L.marker(item).addTo(mymap);
                    markers.push(newMarker);
                })
            }
            console.log(markers);
        },
        error: function (data) {
        }
    });
});




$(window).on('resize', function () {
    var map_column = $('#map-column');
    var adverts_column = $('#advert-list-column');
    var screen_width = $(window).width();

    if (screen_width >= 992) {
        // Large screen
        map_column.show();
        map_column.removeClass('col-12');
        adverts_column.removeClass('col-12');

        map_column.addClass('col-6');
        adverts_column.addClass('col-6');
        return;
    }

    if (screen_width < 992 && screen_width >= 768) {
        // Medium screen
        map_column.show();
        map_column.removeClass('col-6');
        adverts_column.removeClass('col-6');

        map_column.addClass('col-12');
        adverts_column.addClass('col-12');
        return;
    }

    if (screen_width < 768) {
        // small screen
        map_column.hide();
        adverts_column.addClass('col-12')

    }

}).resize();
