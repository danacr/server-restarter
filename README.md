# Server Restarter

![working](images/working.gif)

Completely overkill solution to restart my NAS using an external relay. All of this could have been solved with one ethernet connected relay, but I happened to have all the other parts in a storage box collecting dust. (Except for the relay, thank you very much [@Jogi](https://github.com/jogi-k)!

I reused the flask web app from [busylight](https://github.com/danacr/busylight) with a different button (and api call) to restart my server.

This is all hosted on a [Radxa Rock Pi S](https://wiki.radxa.com/RockpiS) which I have left over from the [flying Kubernetes cluster project](https://github.com/danacr/Kubernetes-The-Fun-Way/tree/master/02-kubernetes-operator-for-drones).

The [QYF-UR01 USB HID relay board](https://de.aliexpress.com/i/4000280363602.html?gatewayAdapt=glo2deu) is not really documented, so I took the bytes that I need to pipe to `/dev/hidraw0` from [here](https://github.com/zwizwa/usb_relay_ch551g).

The `systemctl` service was setup using [this guide](https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267)

To run:
```bash
sudo python3 main.py
```

To trigger:
```bash
curl -X POST http://localhost
```

### Everything is stuck using double-sided tape in an old iPhone box, the reset cables coming through the cdrom slot:
![iPhone box](images/IMG_0462.jpeg)

### To keep the functionality of the existing reset button, I just tied the cables together using scotch tape
![Cables](images/IMG_0463.jpeg)

### The final result
![final](images/IMG_0467.jpeg)