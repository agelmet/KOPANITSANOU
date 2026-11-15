#!/bin/bash
set -e
S=/home/claude/kop/site; T=/home/claude/tools/advon; export ADVON_TOOLS=/home/claude/tools/cache
python3 /home/claude/kop/src/build.py
python3 $T/privacy/privacy_fix.py apply $S >/dev/null
sed -i 's/ είναι Ακριβή Κοπανιτσάνου/ είναι η Ακριβή Κοπανιτσάνου/' $S/privacy.html
python3 $T/seo_live.py fix $S | tail -1
python3 $T/favicon.py make $S assets/img/akrivi-kopanitsanou-logo-icon.svg --tile none --preview /tmp/fav.png | tail -1
python3 $T/seo_rank.py en $S | tail -1
python3 $T/ai_seo.py fix $S | tail -1
