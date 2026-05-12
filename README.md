# zika-ubuntu

Scripts and systemd services for maintaining Ubuntu Linux for elderly people.

## What's included

### autofocus-gnome-signal
Signal Desktop on Linux/Wayland does not raise its window when an incoming call
arrives — it just sends a system notification. This service monitors DBus for
incoming call notifications and automatically brings Signal to the foreground.

- `signal.service` — runs Signal Desktop as a systemd user service
- `signal-call-raiser.service` — monitors DBus and raises Signal on incoming calls
- `bin/signal-call-raiser.py` — the DBus monitor script

### ssh-tunnel
Maintains a persistent reverse SSH tunnel from the home machine to a remote
server, allowing remote access from anywhere in the world even when the home
machine is behind NAT.

- `reverse-tunnel.service` — systemd system service that keeps the tunnel alive
- `reverse-tunnel.conf.example` — configuration template

Once the tunnel is established, an expert user can:
- **SSH** directly into the home machine from anywhere
- **VPN** using WireGuard tunneled over SSH for full network access
- **RDP** for full graphical remote desktop access

## Requirements

- Ubuntu 24.04
- GNOME (X11 or Wayland)
- Signal Desktop (apt version, not snap)
- `dbus-monitor` (usually pre-installed)
- `python3`

## Installation

See README in each subdirectory for installation instructions.

## License

Copyright (c) 2026 Zoran Dimitrijevic and Claude (Anthropic)  
BSD 3-Clause License — see [LICENSE](LICENSE) for details.
