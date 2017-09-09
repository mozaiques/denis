import denis


some_lat_lng = [
    (48.864716, 2.349014),
    (37.773972, -122.431297),
    (55.751244, 37.618423),
    (60.192059, 24.945831),
    (-54.8, -68.3),
]


def test_improved_reverse_haversine():
    for lat_lng in some_lat_lng:
        kx, ky = denis.improved_reverse_haversine(lat_lng)
        dx = denis.haversine(lat_lng, (lat_lng[0] + ky, lat_lng[1]))
        dy = denis.haversine(lat_lng, (lat_lng[0], lat_lng[1] + kx))
        assert denis.is_zero(dx - 1)
        assert denis.is_zero(dy - 1)
