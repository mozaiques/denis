import denis


paris_lat_lng = (48.864716, 2.349014)
base = denis.Base(paris_lat_lng)


def test_xy_to_latlng():
    p1 = base.make_point(x_y=(10.5, 10.5))
    p2 = base.make_point(lat_lng=(p1.latitude, p1.longitude))

    assert denis.is_zero(p2._x - 10.5)
    assert denis.is_zero(p2._y - 10.5)


def test_latlng_to_xy():
    p1 = base.make_point(lat_lng=(48.865, 2.3486))
    p2 = base.make_point(x_y=(p1._x, p1._y))

    assert denis.is_zero(p2.latitude - 48.865)
    assert denis.is_zero(p2.longitude - 2.3486)
