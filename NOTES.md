Notes
=====

Currently I'm launching Chrome natively and then using xdotool to interact with
the created window. This is how I can do double click to maximize the player,
etc.

The problem with this approach is that there is no way how to set change the URL
of a running browser process, wich is suboptimal. So, I have to kill a browser
window and then make a new one just when switching channels.

A lot better would be to somehow create a Browser instance and then change the
URL of a running instance. It seems like 'selenium' package from pip can be used
to achieve this.
