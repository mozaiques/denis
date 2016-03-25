import math

import denis


paris_lat_lng = (48.864716, 2.349014)


def test_pythagore():
    base = denis.Base(paris_lat_lng)
    somewhere1 = base.make_point(x_y=(10, 0))
    somewhere2 = base.make_point(x_y=(0, 10))

    distance = denis.Segment(somewhere1, somewhere2).length
    assert denis.is_zero(distance - math.sqrt(200))


def test_parallels():
    base = denis.Base(paris_lat_lng)

    a = base.make_point(x_y=(0, 0))
    b = base.make_point(x_y=(10, 0))

    c = base.make_point(x_y=(0, 10))
    d = base.make_point(x_y=(10, 10))

    ab = denis.Line(a, b)
    cd = denis.Line(c, d)
    assert ab.is_parallel_to(cd)


def test_perpendicular():
    base = denis.Base(paris_lat_lng)

    a = base.make_point(x_y=(0, 0))
    b = base.make_point(x_y=(10, 0))
    c = base.make_point(x_y=(0, 10))

    ab = denis.Line(a, b)
    ac = denis.Line(a, c)
    assert ab.is_perpendicular_to(ac)


def test_perpendicular_scenario():
    base = denis.Base(paris_lat_lng)
    a = base.make_point(x_y=(0, 0))
    b = base.make_point(x_y=(10, 0))

    ab = denis.Line(a, b)
    bc = ab.get_perpendicular_at(b)
    c = bc.get_point_at_distance(10, b)

    assert c._x == 10
    assert c._y == 10

    cd = bc.get_perpendicular_at(c)
    d = cd.get_point_at_distance(20, c)

    assert d._x == -10
    assert d._y == 10
