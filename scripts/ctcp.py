def ctcp_reply(word, word_eol, userdata):
    command = word[1]
    sender = word[0]

    if command == "TIME":
        # Get the current UTC time
        current_utc_time = time.gmtime()

        # Format the time to mimic mIRC's response format
        formatted_time = time.strftime("%a %b %d %H:%M:%S %Y", current_utc_time)

        # Send the response to the sender
        xchat.command("NOTICE {} :\x01TIME {}\x01".format(sender, formatted_time))
    elif command == "VERSION":
        # Construct the version response to mimic mIRC's installation details
        version_response = "\x01VERSION mIRC v7.72 Khaled Mardam-Bey\x01"

        # Send the response to the sender
        xchat.command("NOTICE {} :{}".format(sender, version_response))

    return xchat.EAT_XCHAT
