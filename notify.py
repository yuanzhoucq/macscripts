#!/usr/bin/python
from subprocess import call


def post_notification(title, msg):
    cmd = "/usr/bin/osascript -e \"display notification \\\"{0}\\\" with title \\\"{1}\\\"\"" \
        .format(msg, title)
    call(cmd, shell=True)


if __name__ == '__main__':
    import sys
    post_notification(sys.argv[1], sys.argv[2])
