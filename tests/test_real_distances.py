import math

from haversine import haversine

import denis


paris_lat_lng = (48.864716, 2.349014)


def test_short_distance():
    base = denis.Base(paris_lat_lng)
    paris = base.make_point(lat_lng=paris_lat_lng)
    somewhere = base.make_point(x_y=(10, 0))

    h_distance = haversine(
        (paris.latitude, paris.longitude),
        (somewhere.latitude, somewhere.longitude),
    ) * 1000
    assert denis.is_zero(h_distance - 10)


def test_intermediate_distance():
    base = denis.Base(paris_lat_lng)
    paris = base.make_point(lat_lng=paris_lat_lng)
    somewhere = base.make_point(x_y=(100, 0))

    h_distance = haversine(
        (paris.latitude, paris.longitude),
        (somewhere.latitude, somewhere.longitude),
    ) * 1000
    assert denis.is_zero(h_distance - 100)


def test_long_distance():
    base = denis.Base(paris_lat_lng)
    paris = base.make_point(lat_lng=paris_lat_lng)
    somewhere = base.make_point(x_y=(1000, 0))

    h_distance = haversine(
        (paris.latitude, paris.longitude),
        (somewhere.latitude, somewhere.longitude),
    ) * 1000
    assert denis.is_zero(h_distance - 1000)


def test_pythagore():
    base = denis.Base(paris_lat_lng)
    somewhere1 = base.make_point(x_y=(10, 0))
    somewhere2 = base.make_point(x_y=(0, 10))

    h_distance = haversine(
        (somewhere1.latitude, somewhere1.longitude),
        (somewhere2.latitude, somewhere2.longitude),
    ) * 1000
    assert denis.is_zero(h_distance - math.sqrt(200))
