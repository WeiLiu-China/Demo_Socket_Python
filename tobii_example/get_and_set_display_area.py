def execute(eyetracker):
    # <BeginExample>
    from tobii_research import DisplayArea

    display_area = eyetracker.get_display_area()

    print("Got display area from tracker with serial number {0}:".format(eyetracker.serial_number))

    print("Bottom Left: {0}".format(display_area.bottom_left))
    print("Bottom Right: {0}".format(display_area.bottom_right))
    print("Height: {0}".format(display_area.height))
    print("Top Left: {0}".format(display_area.top_left))
    print("Top Right: {0}".format(display_area.top_right))
    print("Width: {0}".format(display_area.width))

    # To set the display area it is possible to either use a previously saved instance of
    # the class Display area, or create a new one as shown bellow.
    new_display_area_dict = dict()
    new_display_area_dict['top_left'] = display_area.top_left
    new_display_area_dict['top_right'] = display_area.top_right
    new_display_area_dict['bottom_left'] = display_area.bottom_left

    new_display_area = DisplayArea(new_display_area_dict)

    eyetracker.set_display_area(new_display_area)
    # <EndExample>
