# doppelganger
A simple script bundle for X-Chat to mimic a mostly vanilla install of mIRC version 7.72, subvert some basic fingerprinting techniques and extend some needed functionality to the IRC client.

---

## Installation and usage
To load this bundle into XChat, you can use the following steps:
1. Save the popup script and ctcp script in separate files with the extension .py, for example, `ctcp.py` and `popups.py`.
2. Open XChat and connect to the desired IRC network and channel.
3. In XChat, go to the "Window" menu and select "Plugins and Scripts" or "List of Plugins" (depending on the version of XChat you are using).
4. In the "Plugins and Scripts" window, click on the "Load..." or "Add..." button.
5. Browse and select the .py files, and click "Open" to load the scripts.
6. Once the scripts are loaded, XChat will automatically execute them, and the aliases and popups will be available for use in the IRC channel and query windows.
7. You should now be able to access the context menus by right-clicking in the channel or query window and see the options that were defined in the scripts.
8. CTCP responses for VERSION will return mIRC version 7.72 and TIME will return the actual UTC +0, both formatted to mimic mIRC.

> Make sure you have the necessary permissions to load scripts in XChat, as some IRC networks or security settings may restrict loading external scripts.

---

## Included scripts
There are two scripts included in this repository, `popups.py`, and `ctcp.py`. The following subsections contain a detailed explanation of both:

---

### ctcp.py
The script is designed to provide specific functionalities within the X-Chat IRC client. The script provides selective CTCP handling, responding to specific commands while ignoring others, and disables DCC/XDCC functionality within the X-Chat IRC client.

The script registers a callback function called `ctcp_reply` for the CTCP event.
#### It responds to two CTCP commands:

#### TIME:
When a `CTCP TIME` command is received, the script
- Retrieves the current UTC time
- Formats the response to match that used by mIRC
- Sends a notice message containing the formatted time back to the sender.

#### VERSION:
When a `CTCP VERSION` command is received, the script sends the following response:
```
\x01VERSION mIRC v7.72 (Windows NT 6.3; WOW64) UK English\x01
```

The above can be considered plausible mIRC response.

> Future versions of doppelganger will implement a dynamic response based on user configuration.

### Ignoring Other CTCP Commands:
Any CTCP commands other than TIME and VERSION are ignored. The script consumes these commands without taking any further action.

### Disabling DCC/XDCC Functionality:
The script hooks into various DCC events (DCC CHAT, DCC SEND, DCC GET, DCC, XDCC) and registers a callback function called `disable_dcc`. This function simply consumes the events and prevents any action from being taken, effectively disabling DCC and XDCC functionality.

### Flowchart
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

---

### popups.py
`popups.ini` is a configuration file used by mIRC, to define and customize pop-up menus. These menus provide a way for users to interact with the client by executing specific commands or actions. Similarly, "popups.py" is a Python script that replicates the functionality of "popups.ini". It allows XChat users to create their own custom pop-up menus, tailored to their preferences, and enhances interactivity within the client by providing a flexible and extensible framework. The particular actions listed in these context menues follow that of a standard mIRC installation.

#### The actual popup menus
##### Channel Pop-up Menu (cpopup_menu):

- **Channel Modes:** Executes the command `/channel` in the IRC client.

##### Commands Pop-up Menu (bpopup_menu):

- **Commands:**
  - **Join channel:** Prompts the user to enter a channel name.
  - **Part channel:** Prompts the user to enter a channel name.
  - **Query user:** Prompts the user to enter a nickname and message.
  - **Send notice:** Prompts the user to enter a nickname and message.
  - **Whois user:** Prompts the user to enter a nickname.
- **Send CTCP:**
  - **Ping:** Prompts the user to enter a nickname.
  - **Time:** Prompts the user to enter a nickname.
  - **Version:** Prompts the user to enter a nickname.
- **Set Away:**
  - **On:** Prompts the user to enter an away message.
  - **Off:** Executes the command `/away` to unset the away status.
- **Invite user:** Prompts the user to enter a nickname and channel name.
- **Ban user:** Prompts the user to enter a channel name and nickname.
- **Kick user:** Prompts the user to enter a channel name and nickname.
- **Ignore user:** Prompts the user to enter a nickname.
- **Unignore user:** Prompts the user to enter a nickname.
- **Change nick:** Prompts the user to enter a new nickname.
- **Quit IRC:** Executes the command `/quit` to disconnect from the IRC server.

##### Server Pop-up Menu (mpopup_menu):

- **Server:**
  - **Lusers:** Executes the command `/lusers` in the IRC client.
  - **Motd:** Executes the command `/motd` in the IRC client.
  - **Time:** Executes the command `/time` in the IRC client.
- **Names:** 
  - **#mIRC:** Executes the command `/names #mirc` in the IRC client.
  - **#irchelp:** Executes the command `/names #irchelp` in the IRC client.
  - **?:** Prompts the user to enter a channel name.
- **Join:**
  - **#mIRC:** Executes the command `/join #mirc` in the IRC client.
  - **#irchelp:** Executes the command `/join #irchelp` in the IRC client.
  - **?:** Prompts the user to enter a channel.
- **Query:**
  - **?:** Prompts the user to enter a nickname.
- **Other:**
  - **Whois ?:** Prompts the user to enter a nickname.
  - **Query ?:** Prompts the user to enter a nickname.
  - **Nickname ?:** Prompts the user to enter a new nickname.
- **Away:**
  - **Set Away... ?:** Prompts the user to enter an away message.
  - **Set Back:** Executes the command `/away` to unset the away status.
- **List Channels:** Executes the command `/list` in the IRC client.
- **Edit Notes:** Executes the command `/py exec nano ~/notes.txt` to open the "notes.txt" file in nano.
- **Quit IRC:** Executes the command `/quit` to disconnect from the IRC server.

#### Flowchart
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
│
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

---

## 🤪 IRC Meta
### [@apple-fritter](https://github.com/apple-fritter)'s IRC Repositories:

---

#### WeeChat
- [weechat.driftwood](https://github.com/apple-fritter/weechat.driftwood): Natively log WeeChat messages in the driftwood standard. (Python.)
- [weechat.ban-evasion-detection](https://github.com/apple-fritter/weechat.ban-evasion-detection): Detect and prevent ban evasion. (Python)
- [weechat.typo-aggregator](https://github.com/apple-fritter/weechat.typo-aggregator): Record misspelled words in a TSV (tab-separated values) file. (Python)
- [weechat.whois-aggregator](https://github.com/apple-fritter/weechat.whois-aggregator): Aggregate whois data in a rolling CSV file. (Python)
- [weechat.youtube-info](https://github.com/apple-fritter/weechat.youtube-info): Deprecated. Extract video information from a YouTube URL and post it back to the channel. (Python)
- [weechat.youtube-api](https://github.com/apple-fritter/weechat.youtube-api): Extract video information from a YouTube URL and post it back to the channel. (Python)

---

#### IRCcloud
- [irccloud-to-weechat](https://github.com/apple-fritter/irccloud-to-weechat): Convert IRC logs from IRCcloud format to Weechat format. (Rust)
- [irccloud-to-xchat](https://github.com/apple-fritter/irccloud-to-xchat): Convert IRC logs from IRCcloud format to XChat format. (Rust)

---

#### X-Chat
- [xchat.channel-moderation](https://github.com/apple-fritter/xchat.channel-moderation): Moderate an IRC channel. (Python)
- [doppelganger](https://github.com/apple-fritter/doppelganger): X-Chat mIRC imposter. Fingerprint subversion. (Python bundle)

---

#### Other
- [driftwood](https://github.com/apple-fritter/driftwood): A unified IRC log format definition. (Rust)
- [jetsam](https://github.com/apple-fritter/jetsam): Flag lines of driftwood formatted IRC logs for sanitization, moderation, or further review. (Rust)
- [scrimshaw](https://github.com/apple-fritter/scrimshaw): Create a quoteslist of any given user, from your driftwood formatted logs. (Rust)

---

### IRC usage considerations
When working with any project involving IRC (Internet Relay Chat), it's important to keep the following considerations in mind to ensure a positive and respectful environment for all participants.

#### Philosophy of Use
Tailor your project's behavior and responses to align with the expected norms and conventions of IRC. Take into account the preferences and expectations of IRC users, ensuring that your project provides a seamless and familiar experience within the IRC ecosystem.

#### Foster a Positive and Inclusive Environment
Respect and adhere to the guidelines and policies of the IRC platform you are using. Familiarize yourself with the platform's rules regarding script usage, automation, and acceptable behavior. Comply with the platform's Terms of Service, and be mindful of any limitations or restrictions imposed by the platform. Strive to create an inclusive and welcoming environment where all users can engage respectfully and comfortably.

#### Respect the Rights and Dignity of Other Users
Maintain a polite and courteous demeanor in all interactions. Uphold the fundamental principles of respect, avoiding engagement in illegal, inappropriate, or offensive behavior. This includes refraining from using derogatory or inflammatory language, sharing explicit, triggering, or offensive content, engaging in harassment, or launching personal attacks. Obtain explicit consent before interacting with other users or sending automated responses. Respect the privacy of other users and avoid invading their personal space without their permission.

#### Respect the IRC Community and Channels
Avoid disrupting the normal flow of conversation within IRC channels. Ensure that your project's actions and responses do not cause unnecessary disruptions or inconvenience to other users. Implement mechanisms to prevent spamming or flooding the channel with excessive or irrelevant messages. Handle errors gracefully, preventing unintended behavior or disruptions to the IRC platform or the experiences of other users.

#### Ensure Compatibility
Consider the potential variations in behavior across different IRC platforms and clients. While aiming for compatibility, be aware that certain functionalities may not be available or consistent across all platforms. Test your project on multiple IRC platforms and clients to ensure compatibility and provide the best possible experience for users.

---

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

---

## License

These files released under the [MIT License](LICENSE).
