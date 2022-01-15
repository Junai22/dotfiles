import os
from typing import List  
from libqtile import layout, bar
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

os.system("sh /home/$(whoami)/.config/qtile/autostart.sh &")

mod = "mod4"
terminal = guess_terminal()

keys = [
    

    # -------------------- My Shortcuts ------------------------------  # 
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "l", lazy.spawn("betterlockscreen -l"), desc="Lock the screen"),
    Key([mod], "c", lazy.spawn("chromium"), desc="Launch Chromium"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "s", lazy.spawn("spotify"), desc="Launch Spotify"),
    Key([mod], "Print", lazy.spawn("flameshot gui"), desc="Launch Screenshot App"),
    Key([mod], "m", lazy.spawn("lunarclient &"), desc="Launch Minecraft | Lunar Client"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play and Pause button"),
    Key([], "XF86AudioMedia", lazy.spawn("spotify")),


    Key([], "XF86AudioMute", lazy.spawn("/usr/bin/pactl set-sink-mute alsa_output.pci-0000_14.2.analog-stereo toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("/usr/bin/pactl set-sink-volume alsa_output.pci-0000_14.2.analog-stereo -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("/usr/bin/pactl set-sink-volume alsa_output.pci-0000_14.2.analog-stereo +5%")),    

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config")
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    layout.Max(),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

def init_screens():
    return [Screen(bottom=bar.Gap(size=35),
                    top=bar.Gap(size=35))
    ]
screens = init_screens()

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

auto_minimize = True
wmname = "qtile"
