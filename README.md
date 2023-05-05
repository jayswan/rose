# rose
A braindead simple CLI lookup for Microsoft Threat Intel group names.

Based on: https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json

Case insensitive and matches on any simple string:

```
> rose blizzard

{"Previous name": "ACTINIUM", "New name": "Aqua Blizzard", "Origin/Threat": "Russia", "Other names": ["UNC530", "Primitive Bear", "Gamaredon"]}
{"Previous name": "BROMINE", "New name": "Ghost Blizzard", "Origin/Threat": "Russia", "Other names": ["Energetic Bear", "Crouching Yeti"]}
{"Previous name": "IRIDIUM", "New name": "Seashell Blizzard", "Origin/Threat": "Russia", "Other names": ["Sandworm"]}
{"Previous name": "KRYPTON", "New name": "Secret Blizzard", "Origin/Threat": "Russia", "Other names": ["Venomous Bear", "Turla", "Snake"]}
{"Previous name": "NOBELIUM", "New name": "Midnight Blizzard", "Origin/Threat": "Russia", "Other names": ["APT29", "Cozy Bear"]}
{"Previous name": "SEABORGIUM", "New name": "Star Blizzard", "Origin/Threat": "Russia", "Other names": ["Callisto", "Reuse Team"]}
{"Previous name": "STRONTIUM", "New name": "Forest Blizzard", "Origin/Threat": "Russia", "Other names": ["APT28", "Fancy Bear"]}
{"Previous name": "DEV-0586", "New name": "Cadet Blizzard", "Origin/Threat": "Russia", "Other names": []}
{"Previous name": "DEV-0665", "New name": "Sunglow Blizzard", "Origin/Threat": "Russia", "Other names": []}
```