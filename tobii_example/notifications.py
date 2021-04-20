def execute(eyetracker):
    if eyetracker is not None:
        notifications(eyetracker)


# <BeginExample>
import tobii_research as tr


def notification_callback(notification, data):
    print("Notification {0} received at time stamp {1}.".format(notification, data.system_time_stamp))


def notifications(eyetracker):
    all_notifications = \
        (tr.EYETRACKER_NOTIFICATION_CONNECTION_LOST,
         tr.EYETRACKER_NOTIFICATION_CONNECTION_RESTORED,
         tr.EYETRACKER_NOTIFICATION_CALIBRATION_MODE_ENTERED,
         tr.EYETRACKER_NOTIFICATION_CALIBRATION_MODE_LEFT,
         tr.EYETRACKER_NOTIFICATION_CALIBRATION_CHANGED,
         tr.EYETRACKER_NOTIFICATION_TRACK_BOX_CHANGED,
         tr.EYETRACKER_NOTIFICATION_DISPLAY_AREA_CHANGED,
         tr.EYETRACKER_NOTIFICATION_GAZE_OUTPUT_FREQUENCY_CHANGED,
         tr.EYETRACKER_NOTIFICATION_EYE_TRACKING_MODE_CHANGED,
         tr.EYETRACKER_NOTIFICATION_DEVICE_FAULTS,
         tr.EYETRACKER_NOTIFICATION_DEVICE_WARNINGS)

    # Subscribe to all notifications.
    for notification in all_notifications:
        eyetracker.subscribe_to(notification,
                                lambda x, notification=notification: notification_callback(notification, x))
        print("Subscribed to {0} for eye tracker with serial number {1}.".
              format(notification, eyetracker.serial_number))

    # Trigger some notifications
    calibration = tr.ScreenBasedCalibration(eyetracker)

    calibration.enter_calibration_mode()

    calibration.leave_calibration_mode()

    # Unsubscribe from notifications.
    for notification in all_notifications:
        eyetracker.unsubscribe_from(notification)
        print("Unsubscribed from {0}.".format(notification))
# <EndExample>
