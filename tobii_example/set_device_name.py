def execute(eyetracker):
    current_device_name = eyetracker.device_name

    # <BeginExample>
    import tobii_research as tr

    print("The current name of the eye tracker is {0}".format(eyetracker.device_name))

    try:
        eyetracker.set_device_name("A new name")
        print("The eye tracker changed name to {0}".format(eyetracker.device_name))
    except tr.EyeTrackerFeatureNotSupportedError:
        print("This eye tracker doesn't support changing the device name.")
    except tr.EyeTrackerLicenseError:
        print("You need a higher level license to change the device name.")
    # <EndExample>

    try:
        eyetracker.set_device_name(current_device_name)
    except Exception:
        pass
