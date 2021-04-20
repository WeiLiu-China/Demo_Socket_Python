def execute(eyetracker):
    if eyetracker is not None:
        external_signal(eyetracker)
    else:
        print("No tracker with external signal to run example.")


    # <BeginExample>


import time
import tobii_research as tr


def external_signal_callback(external_signal_data):
    print(external_signal_data)


def external_signal(eyetracker):
    print("Subscribing to external signal for eye tracker with serial number {0}.".format(eyetracker.serial_number))
    eyetracker.subscribe_to(tr.EYETRACKER_EXTERNAL_SIGNAL, external_signal_callback, as_dictionary=True)

    # Wait for external signal.
    time.sleep(2)

    eyetracker.unsubscribe_from(tr.EYETRACKER_EXTERNAL_SIGNAL, external_signal_callback)
    print("Unsubscribed from external signal.")
# <EndExample>
