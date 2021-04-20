def execute(address):
    # <BeginExample>
    import tobii_research as tr

    # address = "tet-tcp://12.13.14.15"
    eyetracker = tr.EyeTracker(address)

    print("Address: " + eyetracker.address)
    print("Model: " + eyetracker.model)
    print("Name (It's OK if this is empty): " + eyetracker.device_name)
    print("Serial number: " + eyetracker.serial_number)

    if tr.CAPABILITY_CAN_SET_DISPLAY_AREA in eyetracker.device_capabilities:
        print("The display area can be set on the eye tracker.")
    else:
        print("The display area can not be set on the eye tracker.")

    if tr.CAPABILITY_HAS_EXTERNAL_SIGNAL in eyetracker.device_capabilities:
        print("The eye tracker can deliver an external signal stream.")
    else:
        print("The eye tracker can not deliver an external signal stream.")

    if tr.CAPABILITY_HAS_EYE_IMAGES in eyetracker.device_capabilities:
        print("The eye tracker can deliver an eye image stream.")
    else:
        print("The eye tracker can not deliver an eye image stream.")

    if tr.CAPABILITY_HAS_GAZE_DATA in eyetracker.device_capabilities:
        print("The eye tracker can deliver a gaze data stream.")
    else:
        print("The eye tracker can not deliver a gaze data stream.")

    if tr.CAPABILITY_HAS_HMD_GAZE_DATA in eyetracker.device_capabilities:
        print("The eye tracker can deliver a HMD gaze data stream.")
    else:
        print("The eye tracker can not deliver a HMD gaze data stream.")

    if tr.CAPABILITY_CAN_DO_SCREEN_BASED_CALIBRATION in eyetracker.device_capabilities:
        print("The eye tracker can do a screen based calibration.")
    else:
        print("The eye tracker can not do a screen based calibration.")

    if tr.CAPABILITY_CAN_DO_MONOCULAR_CALIBRATION in eyetracker.device_capabilities:
        print("The eye tracker can do a monocular calibration.")
    else:
        print("The eye tracker can not do a monocular calibration.")

    if tr.CAPABILITY_CAN_DO_HMD_BASED_CALIBRATION in eyetracker.device_capabilities:
        print("The eye tracker can do a HMD screen based calibration.")
    else:
        print("The eye tracker can not do a HMD screen based calibration.")

    if tr.CAPABILITY_HAS_HMD_LENS_CONFIG in eyetracker.device_capabilities:
        print("The eye tracker can get/set the HMD lens configuration.")
    else:
        print("The eye tracker can not get/set the HMD lens configuration.")
    # <EndExample>
