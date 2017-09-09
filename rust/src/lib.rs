const AVERAGE_EARTH_RADIUS: f64 = 6371000.0;


#[no_mangle]
pub unsafe extern "C" fn haversine(lat1:f64, lon1:f64, lat2:f64, lon2:f64) -> f64 {
    let d_lat = (lat2 - lat1).to_radians();
    let d_lon = (lon2 - lon1).to_radians();
    let l1 = (lat1).to_radians();
    let l2 = (lat2).to_radians();

    let a = ((d_lat/2.0).sin()) * ((d_lat/2.0).sin()) + ((d_lon/2.0).sin()) * ((d_lon/2.0).sin()) * (l1.cos()) * (l2.cos());
    let c = 2.0 * ((a.sqrt()).atan2((1.0-a).sqrt()));

    return AVERAGE_EARTH_RADIUS * c;
}
