# Avalon Integration in LuminaOS

**Avalon** is the peer coordination and protocol layer of the Nexus ecosystem.

This directory links LuminaOS with the Avalon repository:

→ https://github.com/digitaldesignerjazz/avalon

## Transport

Seit 2026-08-30 läuft der Overlay-Transport über **NetBird** (`wt0`, Adressen `100.x`).
Avalon-Namen (47 Peers + 4 Hannover-Knoten) bleiben. Yggdrasil-Templates sind Legacy.

## What Avalon provides

- 47 named Peers (Agenten-Identitäten)
- 4 Hannover Nodes (Nord / Süd / West / Ost)
- Protocol Rounds & Direct Send
- Peer Public Key registry
- Legacy Yggdrasil templates (nicht mehr der aktive Pfad)

## Peer Connection (Live)

```python
from nexus.avalon_peers import AVALON_PEERS, peer_status_report, get_peer_by_name

print(peer_status_report())
```

File: `nexus/avalon_peers.py`

Geräte in Avalon onboarding:

```bash
netbird up --setup-key "$NETBIRD_SETUP_KEY"
```

## Integration Points

| LuminaOS Component       | Avalon Counterpart                     |
|--------------------------|----------------------------------------|
| NetBird Overlay          | Setup-Keys + Peer-Gruppen              |
| Agentenschwarm           | `nexus/avalon_peers.py` + `peers/list.md` |
| NodeInfo / Identity      | Avalon NodeInfo fields                 |
| Logging / Status         | `logs/protocol-round-*.md`             |
| Public Keys              | `peers/public-keys.md`                 |

## Status

- Avalon repository initialized: 2026-08-23
- Transport umgestellt auf NetBird: 2026-08-30
- Avalon Peer Connection layer active (`nexus/avalon_peers.py`)
