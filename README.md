# LuminaOS

**Agentic Operating System** for the Nexus stack.

## Components

| Layer | Description |
|-------|-------------|
| **Orchestrator** | Central task decomposition and agent coordination |
| **Agentenschwarm** | Perception, Planner, Executor, Critic, Memory |
| **Mesh** | Yggdrasil (IPv6 overlay) + Headscale (WireGuard coordination) |
| **LuminaOS** | Boot orchestrator tying mesh + swarm together |

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

## Structure

```
luminaos/
├── lumina/
│   └── luminaos.py          # Main boot / status
├── nexus/
│   ├── agent_swarm.py       # Multi-agent system
│   └── start_yggdrasil.sh   # Mesh helper
└── config/
    ├── yggdrasil.conf.example
    └── headscale.yaml.example
```

## License

Experimental – Nexus ecosystem (Esslinger / Hannover).
