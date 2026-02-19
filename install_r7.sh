wget https://eu.storage.endpoint.ingress.rapid7.com/public.razor-prod-0.eu-central-1.insight.rapid7.com/endpoint/agent/1770062320/linux/x86_64/rapid7-insight-agent_4.0.21.45-1_amd64.deb
apt-get install ./rapid7-insight-agent_4.0.21.45-1_amd64.deb -y
cd /opt/rapid7/ir_agent/components/insight_agent/4.0.21.45
/opt/rapid7/ir_agent/components/insight_agent/4.0.21.45/configure_agent.sh --token=eu:ab23ad3a-68c9-4fe1-b448-1d5083739129 -v --start
systemctl status ir_agent.service