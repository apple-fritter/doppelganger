# doppelganger
A simple script bundle for X-Chat to mimic a mostly vanilla install of mIRC version 7.72, to subvert some basic fingerprinting techniques.

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
The script registers a callback function called ctcp_reply for the CTCP event.
##### It responds to two CTCP commands:

###### TIME:
> When a `CTCP TIME` command is received, the script retrieves the current UTC time and formats it to mimic the response format used by mIRC. It then sends a notice message containing the formatted time back to the sender.

###### VERSION:
> When a `CTCP VERSION` command is received, the script responds that response mimics mIRC

> The string `"\x01VERSION mIRC v7.72 (Windows NT 6.3; WOW64) UK English\x01"` is a plausible mIRC response.

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
│   │
│   ├─ CTCP Command = VERSION
│   │   └─ Send notice message with mIRC version to sender
│   │
│   └─ Ignore other CTCP commands
│
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

## Considerations
When working with this script bundle, there are several important considerations to keep in mind.

### Philosophy of use
It's important to note that the script attempts to mimic the format and details of a standard mIRC version response.
- The response may not precisely match the exact details of a real mIRC installation.
- Adjustments may be needed to fine-tune the response to better match the expected appearance of an mIRC client, or to better match the user's intended use cases.

### Foster a positive and inclusive environment
#### Ensure that your usage of the script aligns with the hosting IRC platform's guidelines
- Familiarize yourself with the rules and policies set forth by the platform regarding script usage, automation, and acceptable behavior.
- Comply with the ToS and respect any limitations or restrictions imposed by the platform.
- Creates a positive and respectful experience for everyone involved.

#### Respect the rights and dignity of other users and their preferences
It's essential to consider the rights and dignity of other users, which are foundational concepts of the Internet Relay Chat ecosystem.  
- Maintain a polite and courteous demeanor in all interactions.
  - Avoid engaging in inappropriate or offensive behavior:
    - derogatory or inflammatory language or dialogue
    - obscene, triggering, or revolting content
    - harassment
    - personal attacks.
- Obtain user consent before interacting with them or sending responses.
  - Be respectful of other users' privacy
  - Do not invade their personal space without their explicit permission.

### Respect the host platform

Avoid interfering with the normal flow of conversation in the IRC channel. Your script should respond to CTCP requests without causing disruptions or inconveniencing other users. Implement mechanisms to prevent spamming or flooding the channel with unnecessary messages. It is therefore crucial to handle errors gracefully to prevent unintended behavior or disruptions. Implement error handling mechanisms to ensure the script fails gracefully and does not cause instability or interfere with the IRC platform or other users' experiences.

### Ensure compatibility
Remember that the script aims to be agnostic to the actual host platform. While it provides a consistent response format, certain platform-specific functionalities may not be available or accurate on all platforms. Keep in mind the potential variations in behavior across different operating systems.

The script relies on the xchat library, which is specific to the XChat IRC client.
> It should go, without saying, that you should be sure you are using XChat or a compatible IRC client that supports the xchat library.

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
- [doppelganger](https://github.com/apple-fritter/doppelganger): X-Chat mIRC imposter. Fingerprint subversion. Python bundle.

#### IRC General

- [driftwood](https://github.com/apple-fritter/driftwood): A unified IRC log format defined. Written in Rust.

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

## License

These files released under the [MIT License](LICENSE).
