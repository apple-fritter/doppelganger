import xchat

def execute_command(word, word_eol, userdata):
    command = word[0][1:]  # Remove the leading dot (.)
    xchat.command(command)
    return xchat.EAT_ALL

def create_popup_menu(menu_items, menu_number):
    for item in menu_items:
        xchat.command("menu -p%s add \"%s\" \"%s\"" % (menu_number, item.split(":")[0], item.split(":")[1]))

cpopup_menu = [
    "Channel Modes:/channel"
]

bpopup_menu = [
    "Commands",
    "Join channel:/join #$?=\"Enter channel name:\"",
    "Part channel:/part #$?=\"Enter channel name:\"",
    "Query user:/query $1=\"Enter nickname and message:\"",
    "Send notice:/notice $1=\"Enter nickname and message:\"",
    "Whois user:/whois $1=\"Enter nickname:\"",
    "Send CTCP",
    ".Ping:/ctcp $1=\"Enter nickname:\" ping",
    ".Time:/ctcp $1=\"Enter nickname:\" time",
    ".Version:/ctcp $1=\"Enter nickname:\" version",
    "Set Away",
    ".On:/away $1=\"Enter away message:\"",
    ".Off:/away",
    "Invite user:/invite $1=\"Enter nickname and channel:\"",
    "Ban user:/ban $1=\"Enter channel and nickname:\"",
    "Kick user:/kick $1=\"Enter channel and nickname:\"",
    "Ignore user:/ignore $1=\"Enter nickname:\"",
    "Unignore user:/ignore -r $1=\"Enter nickname:\"",
    "Change nick:/nick $1=\"Enter new nickname:\"",
    "Quit IRC:/quit"
]

mpopup_menu = [
    "Server",
    ".Lusers:/lusers",
    ".Motd:/motd",
    ".Time:/time",
    "Names",
    ".#mIRC:/names #mirc",
    ".#irchelp:/names #irchelp",
    ".names ?:/names #$?=\"Enter a channel name:\"",
    "Join",
    ".#mIRC:/join #mirc",
    ".#irchelp:/join #irchelp",
    ".join ?:/join #$?=\"Enter a channel to join:\"",
    "Query",
    ".query ?:/query $1=\"Enter nickname to talk to:\"",
    "Other",
    ".Whois ?:/whois $1=\"Enter a nickname:\"",
    ".Query:/query $1=\"Enter a nickname:\"",
    ".Nickname:/nick $1=\"Enter your new nickname:\"",
    ".Away",
    "..Set Away...:/away $1=\"Enter your away message:\"",
    "..Set Back:/away",
    ".List Channels:/list",
    "-",
    "Edit Notes:/run notepad.exe notes.txt",
    "Quit IRC:/quit Leaving"
]

create_popup_menu(cpopup_menu, 1)
create_popup_menu(bpopup_menu, 2)
create_popup_menu(mpopup_menu, 0)

xchat.hook_command("", execute_command)

print("mIRC-like popups loaded.")
