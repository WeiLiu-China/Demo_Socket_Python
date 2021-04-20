def execute(eyetracker):
    stream_errors(eyetracker)


# <BeginExample>
import time
import tobii_research as tr


def stream_error_callback(stream_error_data):
    print(stream_error_data)


def eye_image_callback(data):
    pass


def stream_errors(eyetracker):
    print("Subscribing to stream errors for eye tracker with serial number {0}.".format(eyetracker.serial_number))
    eyetracker.subscribe_to(tr.EYETRACKER_STREAM_ERRORS, stream_error_callback, as_dictionary=True)

    # Trigger an error by subscribing to something not supported.
    eyetracker.subscribe_to(tr.EYETRACKER_EYE_IMAGES, eye_image_callback)
    time.sleep(1)
    eyetracker.unsubscribe_from(tr.EYETRACKER_EYE_IMAGES, eye_image_callback)

    eyetracker.unsubscribe_from(tr.EYETRACKER_STREAM_ERRORS, stream_error_callback)
    print("Unsubscribed from stream errors.")
# <EndExample>
