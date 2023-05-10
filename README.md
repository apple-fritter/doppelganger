# doppelganger
X-Chat mIRC imposter, geographical cloak.

## Functions
This is a simple script for X-Chat to mimic the out-of-the-box popup/context menu functionality of mIRC. I have also included a very basic script to subvert CTCP fingerprinting.

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

## Flowchart
#### ctcp.py
```
┌─ Start CTCP Script
│
├─ Define disable_ctcp_version function
│
├─ Define ctcp_version_reply function
│   ├─ Check for CTCP VERSION request
│   └─ Send custom CTCP VERSION reply
│   |   └─ Send custom NOTICE message with mIRC version
│   |
│   ├─ Check for CTCP TIME request
│   └─ Send custom CTCP TIME reply
│       └─ Send custom NOTICE message with UTC + 0
│
├─ Register event hooks for CTCP version reply functions
│
├─ Print confirmation message
│
├─ Program Execution
│   ├─ X-Chat event loop
│   │   ├─ Handle incoming messages and events
│   │   └─ Execute appropriate actions based on events
│   │
│   └─ End Program Execution
│
└─ End CTCP Script
```

#### popups.py
```
┌─ Start Alias/Popup Script
│
├─ Load aliases.ini
│   └─ Define aliases from aliases.ini
│       └─ Create aliases in X-Chat
│
├─ Load popups.ini
│   └─ Create popups from popups.ini
│       └─ Create context menu popups in X-Chat
│           ├─ Channel Popup Menu (cpopup_menu)
|           ├─ Button Popup Menu (bpopup_menu)
|           └─ Main Popup Menu (mpopup_menu)
|
├─ Print confirmation message
│
├─ Program Execution
│   ├─ X-Chat event loop
│   │   └─ Execute appropriate actions based on events
│   └─ End Program Execution
│
└─ End Alias/Popup Script
```

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

## License

These files released under the [MIT License](LICENSE).
