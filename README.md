# workspace-switcher

## A problem:

This script is my solution to the problem:
I have a Logitech MX Master 2S mouse but I can't find the key mapper program for the Ubuntu to map some keys as I like.
Most of the keys are bound well but two keys I want to remap, the 8 and 9 buttons - they are near the horizontal scroll wheel.

The script binds the buttons near the horizontal scroll to move to the next/previous workspace in Ubuntu (Gnome).

### Prerequisites
python3
- pynput you can run `pip requirements.txt`
- [wmctrl](https://linux.die.net/man/1/wmctrl) you can install it with the `sudo apt-get install wmctrl` command

There are some common bindings for these keys, for example in the Chrome browser.
To remove they I use [xbindkeys](https://www.nongnu.org/xbindkeys/xbindkeys.html#configuration):
- install: `sudo apt-get install xbindkeys`
- create a .xbindkeysrc file in home directory: `touch .xbindkeysrc`
- and add to it these lines:
```
"NoCommand"
b:8

"NoCommand"
b:9
```

Now you can run the main.py script and switch between workspaces with the mouse buttons! 
