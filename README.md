lightdm-login-chromiumos
===================

Installs Chromium OS Aura window manager to Ubuntu(64bit only), with embedded Chromium browser(canary snapshot). Binaries are downloaded from http://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html 

###Window mode (run with chromeos from terminal)
![alt text](http://screencloud.net/img/screenshots/671f8285738e0f54abbb29d7749f4efc.png "Windowed mode")

###Standalone mode (select at login screen)
![alt text](http://screencloud.net/img/screenshots/54573dd3fbb263b24e5984263d6fbf68.png "Standalone mode")

##How to install

    sudo add-apt-repository ppa:janez-troha/lightdm-login-chromiumos -y
    sudo apt-get update && sudo apt-get install lightdm-login-chromiumos

##FAQ

  https://github.com/dz0ny/lightdm-login-chromeos/issues?labels=faq

##What works: 
 
 - Login directly from LightDM (at login screen)
 - Sync, apps, bookmarks
 - Flash(install google-chrome-stable)
 - Talk(install google-talkplugin)
 - Java (icedtea-plugin)
 - Simple development for ChromeOS specific plugins/extensions(~/chrome-os/user)
 - HW acceleration
 - Tablet mode

##What doesn't work

 - Importing images from camera, other disks etc (missing dbus service, mtp deamon)
 - System controls, data is ignored and replaced with fake data ![alt text](http://screencloud.net/img/screenshots/ad06d7eb8b443e8ad2d650d65ea2d529.png "Fake date")
 - Guest login (missing cros subsystem)
 - Special "KIOSK" mode (switch still exists)
 - Auto-updates

##Computability with Ubuntu

  The plan is to port most functionality from ChromeOS (picture import, volume control etc.) BUt in order to do this, someone needs to write d-bus services(this is how chromeos ui communicates with system). Currently I'am writing services for sound(pulseaudio) and networking(networkmanager mashup). 

##Can I build my own version of ChromiumOS browser for Ubuntu?

  YES! Check http://www.chromium.org/developers/how-tos/build-instructions-chromeos

##Interesting stuff

If you login with `chronos` user you will get full experience, but you won't be able to get through with initial setup. Mainly because bunch of system services are not present. If you start this way you can entirely skip lightdm and start system like it is chromebook. 

##What this *deb does?

It simply downloads(official Google builds), chromiumos browser with aura WM. Sets `chromeos` command that launches chromiumos aura in windowed mode and for bonus, you can also login directly to chromiumos straight from login screen.

Thank Google for this :)