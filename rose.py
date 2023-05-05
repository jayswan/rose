#! /usr/bin/env python3
import json
import sys
import requests

def main():
    r = requests.get('https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json')
    r.raise_for_status()
    d = json.loads(r.text)
    search_term = sys.argv[1].lower()
    for item in d:
        for k,v in item.items():
            if isinstance(v, list):
                for i in v:
                    if search_term in i.lower():
                        print(json.dumps(item))
            elif search_term in v.lower():
                print(json.dumps(item))

if __name__ == "__main__":
    main()