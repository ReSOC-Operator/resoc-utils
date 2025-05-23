import os
import dns
import requests
import socket
from requests.auth import HTTPBasicAuth


FRESH_API_KEY = os.getenv("FRESH_API_KEY")

# Verifica il dominio Fresh Service
def dominio_con_cname(dominio):
    try:
        # Verifica che il dominio si risolva
        socket.gethostbyname(dominio)
        # Verifica se ha un record CNAME
        answers = dns.resolver.resolve(dominio, 'CNAME', raise_on_no_answer=False)
        if answers.rrset is not None:
            if ("routing.freshservice.com" in str(answers.response)):
                print(f"{dominio} ha un record CNAME.")
                return True
            else:
                print(f"{dominio} non ha 'routing.freshservice.com'.")
                return False
        else:
            print(f"{dominio} non ha record CNAME.")
            return False
 
    except (socket.gaierror, dns.exception.DNSException) as e:
        print(f"Errore con {dominio}: {e}")
        return False
 
# Scelta di dominio Fresh Service
def scegli_dominio_con_cname():
    domini = ["helpdeskrelatech.freshservice.com", "mediatechsrlhelpdesk.freshservice.com"]
    for dominio in domini:
        if dominio_con_cname(dominio):
            return dominio
 
    return None

# Aggiornamento ticket ed invio email
def update_fresh_ticket_email_to_and_cc_emails(id_ticket,email_to,list_cc_email):
    dominio = scegli_dominio_con_cname()
    linkFresh = f'https://{dominio}/api/v2'
    get_ticket_link = linkFresh + f"/tickets/{id_ticket}"
    auth = HTTPBasicAuth(FRESH_API_KEY, 'X')
    headers = {'Content-Type': 'application/json'}
    data = {
        "email":email_to,
        "cc_emails":list_cc_email
        }
    #print(data)
    r = requests.put(get_ticket_link, headers=headers, auth=auth, json=data, timeout=15)
    #r.raise_for_status()
    json_response = r.json()
    #print(json_response)
    return (json_response,r.status_code)