#!/usr/bin/python3

import argparse
import sys
import dns.resolver

def get_txt_records(domain):
    try:
        # TXT-Records abfragen
        records = dns.resolver.resolve(domain, 'TXT')
        # Alle TXT-Records in eine Liste speichern
        txt_records = [str(record) for record in records]
        return txt_records
    except dns.resolver.NoAnswer:
        print(f"Keine TXT-Records gefunden für die Domain: {domain}")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def find_spf_record(dns_record):
	spf_records = []
	for string in dns_record:
		if string.startswith("\"v=spf1"):
			print("Treffer")
			spf_records.append(string)
	return spf_records

domain=""

# ArgumentParser-Instanz erstellen
parser = argparse.ArgumentParser(description="Verarbeite eine übergebene Domain.")
# Argument für die Domain hinzufügen (-d)
parser.add_argument('-d', '--domain', type=str, help='Die Domain, die verarbeitet werden soll.', required=True)
    
# Argumente parsen
args = parser.parse_args()

# Überprüfen, ob die Domain angegeben wurde
if args.domain:
    domain=args.domain
else:
	print("Fehler: Keine Domain angegeben.")
	sys.exit(1)  # Beendet das Skript mit einem Fehlerstatus

print(f"Domain: {domain}")

txt_records = get_txt_records(domain)
#if txt_records:
#	print(f"TXT-Records für die Domain {domain}: {txt_records}")
#else:
#	print(f"Es wurden keine TXT-Records für die Domain {domain} gefunden.")


for record in find_spf_record(txt_records):
    print(record)
