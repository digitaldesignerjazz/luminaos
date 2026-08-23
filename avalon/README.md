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

## Integration Points

| LuminaOS Component       | Avalon Counterpart                     |
|--------------------------|----------------------------------------|
| Yggdrasil Mesh           | `nodes/yggdrasil-hannover-*.conf`      |
| Agentenschwarm           | `peers/list.md` (47 named peers)       |
| NodeInfo / Identity      | Avalon NodeInfo fields                 |
| Logging / Status         | `logs/protocol-round-*.md`             |
| Public Keys              | `peers/public-keys.md`                 |

## How to use

1. Clone or reference the Avalon repository alongside LuminaOS.
2. Use the Avalon Yggdrasil configs for the four Hannover nodes.
3. Map Avalon peer names into the Agentenschwarm identities.
4. Feed protocol round results into LuminaOS monitoring.

## Status

- Avalon repository initialized: 2026-08-23
- Yggdrasil configs for all four Hannover nodes available
- First Protocol Round logged
- Ready for deep integration with `nexus/agent_swarm.py` and `lumina/luminaos.py`
