- [iptv-tool](#)
	- [IPTV Setup instructions](#)
	- [Dependencies](#)
	- [Launching the tool](#)

iptv-tool
==========================================================================

A tool used to turn a Linux box (Raspberry Pi, probably) into a set-top box
for viewing internet TV. Developed for Debian (Raspbian) with Openbox.

IPTV Setup instructions
--------------------------------------------------------------------------

The main.py script has certain prerequisites that need to be fulfilled to
run it successfully. The script has to have effective group id that points
to group 'input' so that it can read keyboard/remote events, but it can't
be root, as Chromium has a problem running as root, and giving root 
privileges to random scripts is not a good idea.

Hence we have to create a user whose main group is 'input':
```
$ sudo adduser --system --ingroup input --no-create-home iptv
```
The user should have no password.
```
$ sudo passwd -d iptv
```
And the normal login user should be able to execute commands as the
iptv user without password prompts, so that the iptv background process
can be launched automatically on startup. Hence /etc/sudoers has to be
edited:
```
$ sudo visudo
```
And add to the end of file the following two lines:
```
# Let user 'user1' execute commands as user 'iptv' without prompts
user1	ALL=(iptv)	NOPASSWD: ALL
```

Dependencies
--------------------------------------------------------------------------

The script requires the 'evdev' python package to run. This is used
to catch the keyboard events. The 'evdev' package requires python
development package to compile. Hence:
```
$ sudo apt-get install python-pip
$ sudo apt-get install python-dev
$ pip install evdev
```
Launching the tool
--------------------------------------------------------------------------
There is a dedicated launch script that runs the script as 'iptv' user
that should be part of the 'input' group as per setup instructions. To 
launch the tool, give execute permissions to the launch script:
```
$ sudo chmod +x launcher.sh
```
And launch it:
```
./launcher.sh
```
