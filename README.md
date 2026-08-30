# LuminaOS

**Agentic Operating System** for the Nexus stack.

Mesh-Transport seit 2026-08-30: **NetBird** (WireGuard overlay, Cloud-Control-Plane).
Yggdrasil und Headscale bleiben als Legacy-Referenz in `config/`.

## Components

| Layer | Description |
|-------|-------------|
| **Orchestrator** | Central task decomposition and agent coordination |
| **Agentenschwarm** | Perception, Planner, Executor, Critic, Memory |
| **Mesh** | NetBird (`wt0`, `100.x` CGNAT overlay) |
| **Avalon** | Peer coordination layer (47 Peers + 4 Hannover Nodes) |
| **LuminaOS** | Boot orchestrator tying mesh + swarm + Avalon together |

## Quick Start

```bash
# NetBird Client (einmal)
curl -fsSL https://pkgs.netbird.io/install.sh | sh
netbird up
# oder headless:
# netbird up --setup-key "$NETBIRD_SETUP_KEY"

# Mesh-Helper
./nexus/start_netbird.sh

# Agentenschwarm
python3 nexus/agent_swarm.py

# Full LuminaOS boot (NetBird status + swarm)
python3 lumina/luminaos.py
```

Dashboard: https://app.netbird.io

## Avalon Integration

Avalon bleibt die Namens- und Peer-Schicht. Der Transport darunter ist NetBird.

→ Repository: https://github.com/digitaldesignerjazz/avalon  
→ Local docs: [`avalon/README.md`](avalon/README.md)

## Structure

```
luminaos/
├── lumina/
│   └── luminaos.py          # Main boot / status (NetBird-aware)
├── nexus/
│   ├── agent_swarm.py       # Multi-agent system
│   ├── avalon_peers.py      # Named Avalon peers
│   ├── start_netbird.sh     # Mesh helper (aktiv)
│   └── start_yggdrasil.sh   # Legacy
├── avalon/
│   └── README.md
└── config/
    ├── netbird.env.example
    ├── yggdrasil.conf.example   # Legacy
    └── headscale.yaml.example   # Legacy
```

## License

Experimental – Nexus ecosystem (Esslinger / Hannover).
