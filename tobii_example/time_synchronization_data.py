def execute(eyetracker):
    time_synchronization_data(eyetracker)


# <BeginExample>
import time
import tobii_research as tr


def time_synchronization_data_callback(time_synchronization_data):
    print(time_synchronization_data)


def time_synchronization_data(eyetracker):
    print("Subscribing to time synchronization data for eye tracker with serial number {0}.".
          format(eyetracker.serial_number))
    eyetracker.subscribe_to(tr.EYETRACKER_TIME_SYNCHRONIZATION_DATA,
                            time_synchronization_data_callback, as_dictionary=True)

    # Wait while some time synchronization data is collected.
    time.sleep(2)

    eyetracker.unsubscribe_from(tr.EYETRACKER_TIME_SYNCHRONIZATION_DATA,
                                time_synchronization_data_callback)
    print("Unsubscribed from time synchronization data.")
# <EndExample>
