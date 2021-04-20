def execute(eyetracker):
    hmd_gaze_data(eyetracker)


# <BeginExample>
import time
import tobii_research as tr

global_hmd_gaze_data = None


def hmd_gaze_data_callback(hmd_gaze_data):
    global global_hmd_gaze_data
    global_hmd_gaze_data = hmd_gaze_data


def hmd_gaze_data(eyetracker):
    global global_hmd_gaze_data

    print("Subscribing to gaze data for eye tracker with serial number {0}.".format(eyetracker.serial_number))
    eyetracker.subscribe_to(tr.EYETRACKER_HMD_GAZE_DATA, hmd_gaze_data_callback, as_dictionary=True)

    # Wait while some HMD gaze data is collected.
    time.sleep(2)

    eyetracker.unsubscribe_from(tr.EYETRACKER_HMD_GAZE_DATA, hmd_gaze_data_callback)
    print("Unsubscribed from HMD gaze data.")

    print("Last received HMD gaze package:")
    print(global_hmd_gaze_data)
# <EndExample>
