import xchat
import time

def ctcp_reply(word, word_eol, userdata):
    command = word[1]
    sender = word[0]

    if command == "TIME":
        current_time = time.strftime("%a %b %d %H:%M:%S %Y", time.gmtime())
        xchat.command("NOTICE {} :\x01TIME {}\x01".format(sender, current_time))
    elif command == "VERSION":
        xchat.command("NOTICE {} :\x01VERSION mIRC v7.72\x01".format(sender))

    return xchat.EAT_XCHAT

xchat.hook_server("CTCP", ctcp_reply)
