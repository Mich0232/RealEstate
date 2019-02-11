jQuery.ui.autocomplete.prototype._resizeMenu = function () {
    var ul = this.menu.element;
    ul.outerWidth(this.element.outerWidth());
};


$(window).ready(function () {
    data = {
        latlng: [50.068170, 19.945140]
    };
    var mymap = L.map('mapid').setView(data.latlng, 13);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 15,
        id: 'mapbox.streets',
        accessToken: map_box_access_token,
    }).addTo(mymap);

    var address_field = $('.address-field');
    address_field.on('input', function () {
        var term = address_field.val();
        if (term.length > 2) {
            $.ajax({
                url: '/api/geo/lookup/',
                method: 'GET',
                dataType: 'json',
                data: {
                    'term': term
                },
                success: function (response) {
                    var matches = response.names;
                    if (matches.length > 0) {
                        address_field.autocomplete({
                            source: matches
                        })
                    }
                }
            })
        }
    });
});
