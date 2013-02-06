
#!/usr/bin/env/python3

#see https://chromium.googlesource.com/chromiumos/platform/system_api.git/+/master/dbus/service_constants.h
# adn http://src.chromium.org/svn/trunk/src/chromeos/dbus/
from gi.repository import Gtk
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop


class flimflamService(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName('org.chromium.flimflam', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/')

    @dbus.service.method('org.chromium.flimflam.Manager.GetProperties')
    def GetProperties(self):
        return "/crash_me/for/real"

DBusGMainLoop(set_as_default=True)
myservice = flimflamService()
Gtk.main()
