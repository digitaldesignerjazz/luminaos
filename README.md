# LuminaOS

**Agentic Operating System** for the Nexus stack.

## Components

| Layer | Description |
|-------|-------------|
| **Orchestrator** | Central task decomposition and agent coordination |
| **Agentenschwarm** | Perception, Planner, Executor, Critic, Memory |
| **Mesh** | Yggdrasil (IPv6 overlay) + Headscale (WireGuard coordination) |
| **Avalon** | Peer coordination layer (47 Peers + 4 Hannover Nodes) |
| **LuminaOS** | Boot orchestrator tying mesh + swarm + Avalon together |

## Quick Start

```bash
# Agentenschwarm
python3 nexus/agent_swarm.py

# Full LuminaOS boot (mesh status + swarm)
python3 lumina/luminaos.py

# Yggdrasil
cp config/yggdrasil.conf.example /etc/yggdrasil/yggdrasil.conf
# Set your PrivateKey (yggdrasil -genconf)
./nexus/start_yggdrasil.sh
```

## Avalon Integration

Avalon is the peer & protocol layer of the Nexus ecosystem.

→ Repository: https://github.com/digitaldesignerjazz/avalon  
→ Local docs: [`avalon/README.md`](avalon/README.md)

Avalon provides:
- 47 named Peers
- Hannover Nord / Süd / West / Ost nodes
- Yggdrasil config templates for the four nodes
- Protocol Rounds & Direct Send logging

## Structure

```
luminaos/
├── lumina/
│   └── luminaos.py          # Main boot / status
├── nexus/
│   ├── agent_swarm.py       # Multi-agent system
│   └── start_yggdrasil.sh   # Mesh helper
├── avalon/
│   └── README.md            # Avalon integration
└── config/
    ├── yggdrasil.conf.example
    └── headscale.yaml.example
```

## License

Experimental – Nexus ecosystem (Esslinger / Hannover).
