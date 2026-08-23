# Avalon Integration in LuminaOS

**Avalon** is the peer coordination and protocol layer of the Nexus ecosystem.

This directory links LuminaOS with the Avalon repository:

→ https://github.com/digitaldesignerjazz/avalon

## What Avalon provides

- 47 named Peers (Agenten-Identitäten)
- 4 Hannover Nodes (Nord / Süd / West / Ost)
- Protocol Rounds & Direct Send
- Yggdrasil config templates specialized for Avalon nodes
- Peer Public Key registry

## Peer Connection (Live)

The Avalon peers are now programmatically available inside LuminaOS:

```python
from nexus.avalon_peers import AVALON_PEERS, peer_status_report, get_peer_by_name

print(peer_status_report())
```

File: `nexus/avalon_peers.py`

## Integration Points

| LuminaOS Component       | Avalon Counterpart                     |
|--------------------------|----------------------------------------|
| Yggdrasil Mesh           | `nodes/yggdrasil-hannover-*.conf`      |
| Agentenschwarm           | `nexus/avalon_peers.py` + `peers/list.md` |
| NodeInfo / Identity      | Avalon NodeInfo fields                 |
| Logging / Status         | `logs/protocol-round-*.md`             |
| Public Keys              | `peers/public-keys.md`                 |

## Status

- Avalon repository initialized: 2026-08-23
- Yggdrasil configs for all four Hannover nodes available
- First Protocol Round logged
- **Avalon Peer Connection layer active** (`nexus/avalon_peers.py`)
- Ready for deeper binding into `agent_swarm.py` and `luminaos.py`
