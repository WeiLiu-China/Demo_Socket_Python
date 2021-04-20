def execute(eyetracker):
    # <BeginExample>
    initial_gaze_output_frequency = eyetracker.get_gaze_output_frequency()

    print("The eye tracker's initial gaze output frequency is {0} Hz.".format(initial_gaze_output_frequency))

    try:
        for gaze_output_frequency in eyetracker.get_all_gaze_output_frequencies():
            eyetracker.set_gaze_output_frequency(gaze_output_frequency)
            print("Gaze output frequency set to {0} Hz.".format(gaze_output_frequency))
    finally:
        eyetracker.set_gaze_output_frequency(initial_gaze_output_frequency)
        print("Gaze output frequency reset to {0} Hz.".format(initial_gaze_output_frequency))
    # <EndExample>
