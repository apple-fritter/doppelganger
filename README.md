# doppelganger
X-Chat mIRC imposter, geographical cloak.

## Functions
This is a simple script bundle for X-Chat to mimic a mostly vanilla install of mIRC version 7.72, to subvert some basic fingerprinting techniques.

## Installation and usage
To load the aliases and popups into XChat, you can use the following steps:
1. Save the alias script and popup script in separate files with the extension .py, for example, ctcp.py and popups.py.
2. Open XChat and connect to the desired IRC network and channel.
3. In XChat, go to the "Window" menu and select "Plugins and Scripts" or "List of Plugins" (depending on the version of XChat you are using).
4. In the "Plugins and Scripts" window, click on the "Load..." or "Add..." button.
5. Browse and select the .py files, and click "Open" to load the scripts.
6. Once the scripts are loaded, XChat will automatically execute them, and the aliases and popups will be available for use in the IRC channel and query windows.
7. You should now be able to access the context menus by right-clicking in the channel or query window and see the options that were defined in the scripts.
8. CTCP responses for VERSION will return mIRC version 7.72 and TIME will return the actual UTC +0.

> Make sure you have the necessary permissions to load scripts in XChat, as some IRC networks or security settings may restrict loading external scripts.

## Included scripts

### ctcp.py
The script is designed to provide specific functionalities within the X-Chat IRC client. The script provides selective CTCP handling, responding to specific commands while ignoring others, and disables DCC/XDCC functionality within the X-Chat IRC client.

#### CTCP Handling:
##### The script registers a callback function called ctcp_reply for the CTCP event.
It responds to two CTCP commands:

###### TIME:
When a `CTCP TIME` command is received, the script retrieves the current UTC time and formats it to mimic the response format used by mIRC. It then sends a notice message containing the formatted time back to the sender.

###### VERSION:
When a `CTCP VERSION` command is received, the script responds with a notice message indicating the version of the mIRC client. Version response mimics the installation details of mIRC The response format resembles the typical format used by mIRC installations, including the string `"\x01VERSION mIRC v7.72 (Windows NT 6.3; WOW64) UK English\x01"`, which is a plausible mIRC response.

##### Ignoring Other CTCP Commands:
Any CTCP commands other than TIME and VERSION are ignored. The script consumes these commands without taking any further action.

##### Disabling DCC/XDCC Functionality:
The script hooks into various DCC events (DCC CHAT, DCC SEND, DCC GET, DCC, XDCC) and registers a callback function called disable_dcc. This function simply consumes the events and prevents any action from being taken, effectively disabling DCC and XDCC functionality.

#### Flowchart
```
Start
├─ Hook CTCP event to ctcp_reply function
│   ├─ CTCP Command = TIME
│   │   ├─ Get current UTC time
│   │   ├─ Format time to mimic mIRC response format
│   │   └─ Send notice message with formatted time to sender
│   ├─ CTCP Command = VERSION
│   │   └─ Send notice message with mIRC version to sender
│   └─ Ignore other CTCP commands
├─ Hook DCC CHAT event to disable_dcc function
├─ Hook DCC SEND event to disable_dcc function
├─ Hook DCC GET event to disable_dcc function
├─ Hook DCC event to disable_dcc function
├─ Hook XDCC event to disable_dcc function
│
└─ End CTCP subversion script

```

### popups.py
```
┌─ Start Alias/Popup .ini Script
│
├─ Load aliases.ini mimickery
│   └─ Define aliases from aliases.ini
│       └─ Create aliases in X-Chat
│
├─ Load popups.ini mimickery
│   └─ Create popups from popups.ini
│       └─ Create context menu popups in X-Chat
│           ├─ Channel Popup Menu (cpopup_menu)
│           ├─ Button Popup Menu (bpopup_menu)
│           └─ Main Popup Menu (mpopup_menu)
|
├─ Print confirmation message
│
├─ Program Execution
│   ├─ X-Chat event loop
│   │   └─ Execute appropriate actions based on user interaction
│   │
│   └─ End Program Execution
│
└─ End Alias/Popup Script
```
## Other IRC related repositories:

#### WeeChat
- [weechat.ban-evasion-detection](https://github.com/apple-fritter/weechat.ban-evasion-detection): Detect and prevent ban evasion. Python.
- [weechat.typo-aggregator](https://github.com/apple-fritter/weechat.typo-aggregator): Records misspelled words in a TSV (tab-separated values) file. Python.
- [weechat.whois-aggregator](https://github.com/apple-fritter/weechat.whois-aggregator): Aggregate whois data in a rolling CSV file. Python.
- [weechat.youtube-info](https://github.com/apple-fritter/weechat.youtube-info): Extract video information from a YouTube URL and post it back to the channel. Python.

#### IRCcloud
- [irccloud-to-weechat](https://github.com/apple-fritter/irccloud-to-weechat): Convert IRC logs from the IRCcloud format to the Weechat format. Rust.
- [irccloud-to-xchat](https://github.com/apple-fritter/irccloud-to-xchat): Convert IRC logs from the IRCcloud format to the XChat format. Rust.

#### X-Chat
- [xchat.channel-moderation](https://github.com/apple-fritter/xchat.channel-moderation): Moderate an IRC channel. Python.
- [doppelganger](https://github.com/apple-fritter/doppelganger): Masquerade X-Chat client as an out-of-the-box mIRC client. Python.

#### IRC General

- [driftwood](https://github.com/apple-fritter/driftwood): A unified IRC log format defined. Written in Rust.

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

## License

These files released under the [MIT License](LICENSE).
