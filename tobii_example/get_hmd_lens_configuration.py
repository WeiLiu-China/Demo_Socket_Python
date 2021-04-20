def execute(eyetracker):
    # <BeginExample>
    lens_configuration = eyetracker.get_hmd_lens_configuration()

    print("Got HMD lens configuration from tracker with serial number {0}:".format(eyetracker.serial_number))

    print("Left: {0}".format(lens_configuration.left))
    print("Right: {0}".format(lens_configuration.right))
    # <EndExample>
