#!/usr/bin/python
from subprocess import call, check_output


def set_volume(volume):
    volume = int(volume)
    if volume < 0 or volume > 100:
        raise ValueError("Volume should worth between 0 and 100.")
    # if the new volume is the same with the old one, we do nothing.
    if volume == int(check_output('osascript -e "output volume of (get volume settings)"', shell=True)):
        return False
    cmd = "/usr/bin/osascript -e \"set volume output volume {0}\"".format(volume)
    call(cmd, shell=True)
    return True


def set_volume_with_notification(volume):
    from notify import post_notification
    if set_volume(volume):
        post_notification("Setting volume - " + volume, "Mac volume has been set to " + volume)


if __name__ == '__main__':
    import sys
    set_volume_with_notification(sys.argv[1])
