#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DionaeaFR.settings")

    from django.core.management import execute_from_command_line

    pid = str(os.getpid())
    pidfile = "/var/run/dionaeafr/dionaeafr.pid"
    file(pidfile, 'w').write(pid)

    execute_from_command_line(sys.argv)
