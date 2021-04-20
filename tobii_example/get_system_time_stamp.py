def execute():
    # <BeginExample>
    import tobii_research as tr

    system_time_stamp = tr.get_system_time_stamp()

    print("The system time stamp in microseconds is {0}.".format(system_time_stamp))
    # <EndExample>
