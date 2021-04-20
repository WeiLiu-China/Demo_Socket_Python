def execute(eyetracker):
    old_lens_configuration = eyetracker.get_hmd_lens_configuration()

    # <BeginExample>

    from tobii_research import HMDLensConfiguration

    lens_configuration = HMDLensConfiguration(left=(0.0, 0.0, 0.0), right=(0.0, 0.0, 0.0))

    eyetracker.set_hmd_lens_configuration(lens_configuration)

    # <EndExample>

    eyetracker.set_hmd_lens_configuration(old_lens_configuration)
