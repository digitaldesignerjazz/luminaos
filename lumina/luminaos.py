#!/usr/bin/env python3
"""
LuminaOS – Agentic Operating System Prototype
Nexus Layer: Orchestrator + Agentenschwarm + Mesh Awareness
"""
import asyncio
import subprocess
from datetime import datetime

def run_cmd(cmd):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
        return r.stdout.strip() or r.stderr.strip()
    except Exception as e:
        return str(e)

async def mesh_status():
    print("\n🌐 MESH LAYER")
    print("-" * 40)
    hs = run_cmd("curl -s http://127.0.0.1:8080/health 2>/dev/null || curl -sk https://headscale.esslinger.consulting/health 2>/dev/null")
    print(f"  Headscale: {hs or 'offline'}")
    ygg = run_cmd("yggdrasilctl -endpoint=tcp://127.0.0.1:9001 getSelf 2>/dev/null | head -10")
    if "IPv6 address" in ygg or "Build name" in ygg:
        print("  Yggdrasil: online")
        for line in ygg.splitlines():
            if "IPv6 address" in line or "Build version" in line or "Public key" in line:
                print(f"    {line.strip()}")
    else:
        print("  Yggdrasil: offline / no admin")
    peers = run_cmd("yggdrasilctl -endpoint=tcp://127.0.0.1:9001 getPeers 2>/dev/null | grep -c 'Up' || echo 0")
    print(f"  Yggdrasil Peers Up: {peers}")

async def swarm_status():
    print("\n🤖 AGENTENSCHWARM")
    print("-" * 40)
    print("  Orchestrator: bereit")
    print("  Agents: Perception, Planner, Executor, Critic, Memory")
    import sys
    sys.path.insert(0, "nexus")
    try:
        from agent_swarm import SharedMemory, Orchestrator, PerceptionAgent, PlannerAgent, ExecutorAgent, CriticAgent, MemoryAgent
        memory = SharedMemory()
        swarm = Orchestrator(memory)
        for cls, name, role in [
            (PerceptionAgent, "Perception", "Wahrnehmung"),
            (PlannerAgent, "Planner", "Planung"),
            (ExecutorAgent, "Executor", "Ausführung"),
            (CriticAgent, "Critic", "Kritiker"),
            (MemoryAgent, "Memory", "Gedächtnis"),
        ]:
            swarm.register_agent(cls(name, role, memory))
        await swarm.run("LuminaOS Boot – Mesh + Swarm Status erfassen und Nexus bereit melden")
    except Exception as e:
        print(f"  Swarm Fehler: {e}")

async def main():
    print("=" * 60)
    print("  LUMINA OS  –  Agentic Operating System")
    print(f"  Boot: {datetime.now().isoformat()}")
    print("=" * 60)
    await mesh_status()
    await swarm_status()
    print("\n" + "=" * 60)
    print("  LUMINA OS online – Nexus Stack bereit")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())
