def execute(eyetracker):
    # <BeginExample>
    initial_eye_tracking_mode = eyetracker.get_eye_tracking_mode()

    print("The eye tracker's initial eye tracking mode is {0}.".format(initial_eye_tracking_mode))

    try:
        for eye_tracking_mode in eyetracker.get_all_eye_tracking_modes():
            eyetracker.set_eye_tracking_mode(eye_tracking_mode)
            print("Eye tracking mode set to {0}.".format(eye_tracking_mode))
    finally:
        eyetracker.set_eye_tracking_mode(initial_eye_tracking_mode)
        print("Eye tracking mode reset to {0}.".format(initial_eye_tracking_mode))
    # <EndExample>
