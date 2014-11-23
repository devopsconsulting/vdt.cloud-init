vdt.cloud-init
==============

Cloud init scripts for deployment.

How does it work?
-----------------

cloudinit is a script executed on boot once (when a new vm is created to setup the vm) and can communicate with cloud hypervisors like cloudstack, opencloud and others.
However, cloudinit can also be used with "no cloud management vm's", like Xen or KVM.
In this case you can use the "nocloud" plugin of cloudinit, and pass on some parameters to setup the VM using the kernel commandline. For example:

    <cmdline>root=/dev/vda1 ro ds=nocloud-net;s=http://repos.devopsconsulting.nl:8080/vdt.cloud-init/cloud-init.cfg.d/vdt.cloudinit-</cmdline>

Then cloudinit will download two files:
* vdt.cloudinit-metadata (used for general setup of the host)
* vdt.cloudinit-userdata (used for customizing the host by it need)

See the example in this repository.
