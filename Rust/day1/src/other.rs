pub const GOOD_WEIGHT: f32 = 1.0;
pub const BAD_WEIGHT: f32 = 2.0;

pub fn is_nice(good_deeds: u32, bad_deeds: u32) -> bool {
    // Calculate the ratio of good deeds to total deeds
    // Any ratio greater than or equal to 0.75 is considered nice
    // e.g. 10 good deeds and 2 bad deeds =
    // (10 * 1) / ((10 * 1) + (2 * 2)) = 10 / 14 = 0.714... (not nice)
    // If both good and bad deeds are 0, the child is naughty

    if good_deeds == 0 && bad_deeds == 0{
        return false;
    }

    let ratio = good_deeds / (good_deeds + (2 * bad_deeds));

    return ratio >= 0.75;

}