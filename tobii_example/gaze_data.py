def execute(eyetracker):
    gaze_data(eyetracker)


    # <BeginExample>


import time
import tobii_research as tr

global_gaze_data = None


def gaze_data_callback(gaze_data):
    global global_gaze_data
    global_gaze_data = gaze_data


def gaze_data(eyetracker):
    global global_gaze_data

    print("Subscribing to gaze data for eye tracker with serial number {0}.".format(eyetracker.serial_number))
    eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

    # Wait while some gaze data is collected.
    time.sleep(2)

    eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
    print("Unsubscribed from gaze data.")

    print("Last received gaze package:")
    print(global_gaze_data)
# <EndExample>
