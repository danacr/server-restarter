# Server Restarter

Flask web app to restart my server using a usb relay.

Usb commands taken from https://github.com/zwizwa/usb_relay_ch551g

Setup service using: https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267

To run:
```bash
sudo python3 main.py
```

To trigger:
```bash
curl -X POST http://localhost
```

Ucreatefun USB Relay
![relay](./ucreatefun.jpg)