import xchat
import time

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
        xchat.command("NOTICE {} :\x01VERSION mIRC v7.72\x01".format(sender))
    else:
        # Ignore other CTCP commands
        return xchat.EAT_XCHAT

    return xchat.EAT_XCHAT

def disable_dcc(word, word_eol, userdata):
    return xchat.EAT_XCHAT

# Hook the CTCP event to the ctcp_reply function
xchat.hook_server("CTCP", ctcp_reply)

# Hook the DCC events to the disable_dcc function
xchat.hook_server("DCC CHAT", disable_dcc)
xchat.hook_server("DCC SEND", disable_dcc)
xchat.hook_server("DCC GET", disable_dcc)
xchat.hook_server("DCC", disable_dcc)
xchat.hook_server("XDCC", disable_dcc)
