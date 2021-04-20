def execute(eyetracker):
    if eyetracker is None:
        return
    # <BeginExample>
    filename = "saved_calibration.bin"

    # Save the calibration to file.
    with open(filename, "wb") as f:
        calibration_data = eyetracker.retrieve_calibration_data()

        # None is returned on empty calibration.
        if calibration_data is not None:
            print("Saving calibration to file for eye tracker with serial number {0}.".format(eyetracker.serial_number))
            f.write(eyetracker.retrieve_calibration_data())
        else:
            print("No calibration available for eye tracker with serial number {0}.".format(eyetracker.serial_number))

    # Read the calibration from file.
    with open(filename, "rb") as f:
        calibration_data = f.read()

        # Don't apply empty calibrations.
        if len(calibration_data) > 0:
            print("Applying calibration on eye tracker with serial number {0}.".format(eyetracker.serial_number))
            eyetracker.apply_calibration_data(calibration_data)
    # <EndExample>

    # Cleanup
    import os
    try:
        os.remove(filename)
    except OSError:
        pass
