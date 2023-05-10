import xchat

def disable_ctcp_version(word, word_eol, userdata):
    if word[1].upper() == "VERSION":
        return xchat.EAT_ALL  # Ignore CTCP VERSION requests
    return xchat.EAT_NONE

def ctcp_version_reply(word, word_eol, userdata):
    if word[1].upper() == "VERSION":
        xchat.command("NOTICE {} :\x01VERSION mIRC v7.72\x01".format(word[0]))
        return xchat.EAT_ALL
    return xchat.EAT_NONE

xchat.hook_server("PRIVMSG", disable_ctcp_version)
xchat.hook_server("NOTICE", ctcp_version_reply)

print("Custom CTCP version reply script loaded.")
