import base64
import os
import subprocess

uuid = subprocess.check_output(["/usr/sbin/dmidecode", "-s", "system-uuid"]).strip()
with open("/etc/UUID.conf", "wb") as f:
    f.write(uuid)
os.rename("/etc/hosts", "/etc/hosts.bak")
with open("/etc/hosts", "wb") as f:
    f.write("127.0.0.1    localhost\n127.0.1.1    %(uuid)s.local %(uuid)s\n" % locals())
with open("/etc/hostname", "wb") as f:
    f.write("%(uuid)s.local" % locals())

with open("/proc/cmdline", "r") as f:
    cmdline = f.read()
    cmdline = cmdline.strip()
    userdata = [x.split('=')[1] for x in cmdline.split(' ') if x.find('userdata=') == 0][0]
    userdata = base64.urlsafe_b64decode(userdata + '=' * (4 - len(userdata) % 4)).split("\n")
for x in userdata:
    key, value = x.split("=")
    with open("/etc/environment", "a") as f:
        f.write("FACTER_%s=%s\n" % (key, value))
