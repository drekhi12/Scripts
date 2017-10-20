import dbus
sys_bus = dbus.SystemBus()
hal_srvc = sys_bus.get_object('org.freedesktop.Hal',
                              '/org/freedesktop/Hal/devices/computer')
pwr_mgmt =  dbus.Interface(hal_srvc,
                'org.freedesktop.Hal.Device.SystemPowerManagement')
shutdown_method = pwr_mgmt.get_dbus_method("Shutdown")
shutdown_method()

