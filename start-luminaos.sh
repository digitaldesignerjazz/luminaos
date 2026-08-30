#!/usr/bin/env bash
# start-luminaos.sh — Boot-Orchestrator für LuminaOS
# Nexus / Esslinger & Co. — Sir, dein gehorsamer Startknopf.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

BANNER='LuminaOS — Agentic Operating System (Nexus Stack)'
echo "============================================================"
echo "  $BANNER"
echo "  Boot: $(date -Iseconds)"
echo "============================================================"

# 1) Mesh-Transport (NetBird) — aktiv, Yggdrasil/Headscale nur Legacy
if [[ "${SKIP_MESH:-0}" != "1" ]]; then
  echo ""
  echo "🌐 MESH LAYER"
  echo "------------------------------------------------------------"
  if [[ -x "$ROOT/nexus/start_netbird.sh" ]]; then
    bash "$ROOT/nexus/start_netbird.sh" || echo "  NetBird-Helper meldete einen Fehler — weiter ohne Mesh."
  else
    echo "  start_netbird.sh fehlt — überspringe Mesh-Boot."
  fi
else
  echo "  Mesh-Boot übersprungen (SKIP_MESH=1)."
fi

# 2) Nexus-Proxy (lokaler Token-Halter) — nur wenn im lumina-Repo vorhanden
PROXY_DIR="${LUMINA_REPO:-$ROOT/../lumina}"
if [[ -f "$PROXY_DIR/nexus-proxy.py" && "${SKIP_PROXY:-0}" != "1" ]]; then
  if ! curl -sf "http://127.0.0.1:8787/" >/dev/null 2>&1; then
    echo ""
    echo "🔐 NEXUS-PROXY"
    echo "------------------------------------------------------------"
    echo "  Starte nexus-proxy.py im Hintergrund..."
    (cd "$PROXY_DIR" && nohup python3 nexus-proxy.py > /tmp/nexus-proxy.log 2>&1 &) || true
    sleep 1
    if curl -sf "http://127.0.0.1:8787/" >/dev/null 2>&1; then
      echo "  Proxy läuft auf http://127.0.0.1:8787"
    else
      echo "  Proxy noch nicht erreichbar — siehe /tmp/nexus-proxy.log"
    fi
  else
    echo "  Proxy läuft bereits."
  fi
fi

# 3) Agentenschwarm + Status (Haupt-Boot)
echo ""
echo "🤖 AGENTENSCHWARM + STATUS"
echo "------------------------------------------------------------"
exec python3 "$ROOT/lumina/luminaos.py" "$@"
