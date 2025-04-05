#include <libudev.h>
#include <iostream>
#include <cstdlib>
#include <string>

void handle_device(const std::string& devNode) {
    std::cout << "[+] USB Device Detected: " << devNode << std::endl;
    
    // Notify Python orchestrator - for now, call script with device path
    std::string command = "python3 ../python/sandbox_manager.py " + devNode;
    system(command.c_str());
}

int main() {
    struct udev *udev = udev_new();
    if (!udev) {
        std::cerr << "Cannot create udev context.\n";
        return 1;
    }

    struct udev_monitor *mon = udev_monitor_new_from_netlink(udev, "udev");
    udev_monitor_filter_add_match_subsystem_devtype(mon, "block", "disk");
    udev_monitor_enable_receiving(mon);

    int fd = udev_monitor_get_fd(mon);

    std::cout << "[*] USB Firewall Listener Started\n";

    while (true) {
        fd_set fds;
        FD_ZERO(&fds);
        FD_SET(fd, &fds);

        if (select(fd+1, &fds, nullptr, nullptr, nullptr) > 0) {
            struct udev_device *dev = udev_monitor_receive_device(mon);
            if (dev) {
                std::string action = udev_device_get_action(dev);
                std::string devnode = udev_device_get_devnode(dev);
                if (action == "add") {
                    handle_device(devnode);
                }
                udev_device_unref(dev);
            }
        }
    }

    udev_unref(udev);
    return 0;
} 