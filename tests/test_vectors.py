import denis


paris_lat_lng = (48.864716, 2.349014)
base = denis.Base(paris_lat_lng)


def test_direct_orthogonals():
    a = base.make_point(x_y=(0, 0))
    b = base.make_point(x_y=(10, 0))

    vector_ab = denis.Vector(points=(a, b))
    vector_cd = vector_ab.get_direct_orthogonal()

    assert vector_cd._x == 0
    assert vector_cd._y == 10

    vector_ef = vector_cd.get_direct_orthogonal()

    assert vector_ef._x == -10
    assert vector_ef._y == 0
