def execute(eyetracker):
    # <BeginExample>
    track_box = eyetracker.get_track_box()

    print("Got track box from tracker with serial number {0} with corners:".format(eyetracker.serial_number))

    print("Back Lower Left: {0}".format(track_box.back_lower_left))
    print("Back Lower Right: {0}".format(track_box.back_lower_right))
    print("Back Upper Left: {0}".format(track_box.back_upper_left))
    print("Back Upper Right: {0}".format(track_box.back_upper_right))
    print("Front Lower Left: {0}".format(track_box.front_lower_left))
    print("Front Lower Right: {0}".format(track_box.front_lower_right))
    print("Front Upper Left: {0}".format(track_box.front_upper_left))
    print("Front Upper Right: {0}".format(track_box.front_upper_right))
    # <EndExample>
