def execute(eyetracker):
    if eyetracker is None:
        return

    # <BeginExample>
    import time
    import tobii_research as tr

    calibration = tr.HMDBasedCalibration(eyetracker)

    # Enter calibration mode.
    calibration.enter_calibration_mode()
    print("Entered calibration mode for eye tracker with serial number {0}.".format(eyetracker.serial_number))

    # Define the points on the HMD we should calibrate at.
    # The coordinates are are in the HMD coordinate system.
    points_to_calibrate = [(0.0, 0.0, 100.0), (20.0, 0.0, 100.0), (0.0, 20.0, 100.0)]

    for point in points_to_calibrate:
        print("Show a point on the HMD at {0}.".format(point))

        # Wait a little for user to focus.
        time.sleep(0.7)

        print("Collecting data at {0}.".format(point))
        if calibration.collect_data(point[0], point[1], point[2]) != tr.CALIBRATION_STATUS_SUCCESS:
            # Try again if it didn't go well the first time.
            # Not all eye tracker models will fail at this point, but instead fail on ComputeAndApply.
            calibration.collect_data(point[0], point[1], point[2])

    print("Computing and applying calibration.")
    calibration_result = calibration.compute_and_apply()
    print("Compute and apply returned {0} and collected at {1} points.".
          format(calibration_result.status, len(calibration_result.calibration_points)))

    # The calibration is done. Leave calibration mode.
    calibration.leave_calibration_mode()

    print("Left calibration mode.")
    # <EndExample>
