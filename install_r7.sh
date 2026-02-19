#!/bin/sh

URL="https://eu.storage.endpoint.ingress.rapid7.com/public.razor-prod-0.eu-central-1.insight.rapid7.com/endpoint/agent/1770062320/linux/x86_64/rapid7-insight-agent_4.0.21.45-1_amd64.deb"
OUTPUT="/tmp/r7.deb"

if command -v curl >/dev/null 2>&1; then
    echo "curl trovato, avvio download..."
    curl -fsSL "$URL" -o "$OUTPUT"

    if [ $? -eq 0 ]; then
        echo "Download completato: $OUTPUT"
    else
        echo "Errore durante il download"
    fi
else
    echo "curl non presente"
fi

apt-get install /tmp/r7.deb -y
cd /opt/rapid7/ir_agent/components/insight_agent/4.0.21.45
/opt/rapid7/ir_agent/components/insight_agent/4.0.21.45/configure_agent.sh --token=eu:d7bfca37-6f50-4382-b090-ff99d144d072 -v --start

systemctl status ir_agent.service
