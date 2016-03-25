import denis


paris_lat_lng = (48.864716, 2.349014)
base = denis.Base(paris_lat_lng)


def test_orthogonals():
    a = base.make_point(x_y=(2, 5))
    b = base.make_point(x_y=(1, 3))

    vector_ab = denis.Vector(points=(a, b))
    vector_cd = vector_ab.get_direct_orthogonal()

    assert vector_ab * vector_cd == 0


def test_direct_orthogonals():
    a = base.make_point(x_y=(0, 0))
    b = base.make_point(x_y=(5, 5))

    vector_ab = denis.Vector(points=(a, b))
    vector_cd = vector_ab.get_direct_orthogonal()

    assert vector_cd._x == -5
    assert vector_cd._y == 5

    vector_ef = vector_cd.get_direct_orthogonal()

    assert vector_ef._x == -5
    assert vector_ef._y == -5
