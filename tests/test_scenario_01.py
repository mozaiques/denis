import denis


harbor_center_coords = (43.65274668444309, -1.4359748644615138)
base = denis.Base(harbor_center_coords)


start = base.make_point(lat_lng=(43.650857105523244, -1.4347123977510705))
end = base.make_point(lat_lng=(43.65064272349392, -1.4356604255036132))


def test_scenario_01():
    pp_line = denis.Line(start, end).get_perpendicular_at(start)

    top_fake_start = pp_line.get_point_at_distance(-3, start)
    top_start = pp_line.get_perpendicular_at(top_fake_start)\
        .get_point_at_distance(-3, top_fake_start)

    bottom_fake_start = pp_line.get_point_at_distance(3, start)
    bottom_start = pp_line.get_perpendicular_at(bottom_fake_start)\
        .get_point_at_distance(-3, bottom_fake_start)

    assert denis.Line(start, end).is_perpendicular_to(denis.Line(top_start, bottom_start))
