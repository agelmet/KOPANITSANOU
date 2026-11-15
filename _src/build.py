import json, re, os, shutil, html
S = os.path.dirname(os.path.abspath(__file__)); OUT = '/home/claude/kop/site'
FS = '/home/claude/tools/node_modules/@fontsource'
GR = 'U+0370-0377,U+037A-037F,U+0384-038A,U+038C,U+038E-03A1,U+03A3-03FF'
LA = 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'
FONTS = [('GFS Didot', 'gfs-didot', 400, 'normal'), ('Manrope', 'manrope', 400, 'normal'), ('Manrope', 'manrope', 600, 'normal'),
         ('Noto Serif Display', 'noto-serif-display', 300, 'italic')]
os.makedirs(OUT + '/assets/fonts', exist_ok=True)
ff = []
for fam, slug, w, st in FONTS:
    for sub, rng in (('greek', GR), ('latin', LA)):
        fn = f'{slug}-{sub}-{w}-{st}.woff2'
        shutil.copy(f'{FS}/{slug}/files/{fn}', f'{OUT}/assets/fonts/{fn}')
        ff.append(f"@font-face{{font-family:'{fam}';font-style:{st};font-weight:{w};font-display:swap;src:url(assets/fonts/{fn}) format('woff2');unicode-range:{rng}}}")
FONTCSS = '\n'.join(ff)

# ---------- logo ----------
psi = json.load(open(f'{S}/psi.json'))['Ψ']; s = 0.058; tx = 50 - (psi['b'][0] + psi['b'][2]) / 2 * s
SYMBOL = ('<svg xmlns="http://www.w3.org/2000/svg"><symbol id="mk" viewBox="0 0 100 120">'
          '<path d="M14 116V48a36 36 0 0 1 72 0v68z" fill="none" stroke="#B8955A" stroke-width="1.8"/>'
          '<path d="M21 109V49a29 29 0 0 1 58 0v60z" fill="none" stroke="#B8955A" stroke-width=".8" opacity=".75"/>'
          f'<path transform="translate({tx:.2f} 86) scale({s} -{s})" d="{psi["d"]}" style="fill:var(--mk-i,#15372B)"/>'
          '<path d="M50 92.5c3.2 4.6 4.6 7 4.6 9.2a4.6 4.6 0 0 1-9.2 0c0-2.2 1.4-4.6 4.6-9.2z" fill="#B8955A"/>'
          '</symbol></svg>')
icon = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120"><rect width="120" height="120" rx="26" fill="#15372B"/>'
        '<g transform="translate(14 4)"><path d="M18 108V50a28 28 0 0 1 56 0v58z" fill="none" stroke="#DCC48F" stroke-width="3.4"/>'
        f'<path transform="translate({46 - (psi["b"][0]+psi["b"][2])/2*0.062:.2f} 90) scale(0.062 -0.062)" d="{psi["d"]}" fill="#FBF8F2"/></g></svg>')
open(f'{OUT}/assets/img/akrivi-kopanitsanou-logo-icon.svg', 'w').write(icon)
logo = SYMBOL.replace('<symbol id="mk" viewBox="0 0 100 120">', '').replace('</symbol></svg>', '').replace('<svg xmlns="http://www.w3.org/2000/svg">', '')
open(f'{OUT}/assets/img/akrivi-kopanitsanou-logo.svg', 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 120">' + logo.replace('var(--mk-i,#15372B)', '#15372B') + '</svg>')

# ---------- reviews (doctoranytime, verbatim) ----------
REVIEWS = [
 ('Χαρά', 'Ιούνιος 2025', 'Είχα την τύχη να συνεργαστώ με την Ακριβή για δύο χρόνια. Μέσα από αυτή τη διαδρομή κατάφερα να κατανοήσω βαθύτερα τον εαυτό μου και να αντιμετωπίζω τους φόβους μου χωρίς να τους φοβάμαι. Με ενσυναίσθηση, συνέπεια και σεβασμό, δημιούργησε έναν χώρο ασφάλειας όπου ένιωσα ελεύθερη να εκφραστώ. Η συμβολή της στην προσωπική μου εξέλιξη ήταν καθοριστική. Τη συστήνω ανεπιφύλακτα. Ευχαριστώ Βιβή μου για ολα..ειμαι ευγνώμων που βρέθηκες στον δρόμο μου. ολα ειναι εδω και ολοι ειμαστε εδω...Χαρά'),
 ('Ναταλία', 'Φεβρουάριος 2026', 'Εξαιρετικη επαγγελματίας! Ενεπνευσε εμπιστοσύνη ανθρωπιά και κατανόηση τη συστήνω ανεπιφύλακτα αξίζει!!'),
 ('ΘΕΟΔΩΡΑ', 'Ιούνιος 2025', 'Εξαιρετική επαγγελματίας, άρτια καταρτιστισμενη, με σεβασμο στον ανθρωπο και διορατικη σκεψη που σε βοηθά να νιώσεις ασφαλής από τις πρώτες συναντησεις'),
 ('Σταματια', 'Μάρτιος 2026', 'Πολύ καλή Επαγγελματίας με εμπειρία.εμπιστοσύνη από τν πρώτη στιγμή..'),
 ('PANOS', 'Ιούνιος 2025', 'ΕΠΑΓΓΕΛΜΑΤΙΑΣ ΜΕ ΟΛΗ ΤΗΝ ΣΗΜΑΣΙΑ ΤΗΣ ΛΕΞΗΣ.ΑΚΟΥΕΙ ΚΑΙ ΔΙΝΕΙ ΠΡΟΣΟΧΗ ΣΕ ΑΥΤΑ ΠΟΥ ΤΗΣ ΛΕΣ.ΚΑΝΕΙ ΣΤΟΧΕΥΜΕΝΕΣ ΕΡΩΤΗΣΕΙΣ ΚΑΙ ΣΕ ΔΙΕΥΚΟΛΥΝΕΙ ΝΑ ΠΕΙΣ ΑΥΤΑ ΠΟΥ ΝΙΩΘΕΙΣ.ΧΡΗΣΙΜΟΠΟΙΕΙ ΚΑΙΝΟΤΟΜΕΣ ΠΡΑΚΤΙΚΕΣ ΓΙΑ ΝΑ ΥΠΑΡΧΕΙ ΜΙΑ ΑΠΟΔΟΤΙΚΗ ΚΑΙ ΧΡΗΣΙΜΗ ΕΠΙΚΟΙΝΩΝΙΑ.ΤΗΝ ΠΡΟΤΕΙΝΩ ΑΝΕΠΙΦΥΛΑΧΤΑ!!!'),
 ('Nikos', 'Ιούλιος 2025', 'Ανα πάσα στιγμή που χρειάστηκα την βοήθεια της κ την γνώμη της ήταν εκεί για εμένα....'),
 ('Eirini G', 'Φεβρουάριος 2023', 'Πολυ καλή δουλειά! Ενιωσα ότι με καταλαβαίνει και οι συμβουλές ηταν στοχευμενες Η καθοδήγηση της ηταν διακριτικη και ένιωσα άμεσα οικεία. Την συστήνω ανεπιφύλακτα'),
 ('Μιτσι', 'Ιούλιος 2025', 'Άνθρωπος εμπιστοσύνης με άμεσα αποτελέσματα !!'),
 ('Elli', 'Φεβρουάριος 2023', 'Εξαιρετικη επαγγελματιας κ ανθρωπος ταυτοχρονα!Με την εμπειρια της κ την γλυκεια προσεγγιση της μας βοηθησες αρκετα!'),
 ('Παναγιώτα', 'Φεβρουάριος 2023', 'Εξαιρετική επιστήμονας!.αισθάνθηκα αμέσως άνετα και οικεία!..'),
 ('Eleni', 'Φεβρουάριος 2023', 'Αισθάνθηκα ασφάλειας και κατανόηση σε ότι συζητήσαμε την προτείνω ανεπιφύλακτα'),
]
rv = []
for n, d, t in REVIEWS:
    cls = ' class="long"' if len(t) > 260 else ''
    rv.append(f'<article class="rv"><span class="st" aria-label="5 αστέρια" data-en-aria="5 stars"><span>★</span><span>★</span><span>★</span><span>★</span><span>★</span></span>'
              f'<blockquote{cls}>{html.escape(t, quote=False)}</blockquote><div class="rv-f"><b>{html.escape(n)}</b><span>doctoranytime · {d}</span></div></article>')
REV = '\n        '.join(rv)

# ---------- FAQ ----------
FAQ = [
 ('Χρειάζεται να ξέρω ζωγραφική;', 'Do I need to know how to draw?',
  'Όχι. Η Εικαστική Ψυχοθεραπεία δεν προϋποθέτει καλλιτεχνικές γνώσεις ή δεξιότητες· τα εικαστικά υλικά είναι ένα ακόμη μέσο έκφρασης, δίπλα στον λόγο.',
  'No. Art Psychotherapy does not require any artistic knowledge or skills; art materials are simply another means of expression, alongside words.'),
 ('Με ποιους δουλεύετε;', 'Who do you work with?',
  'Με παιδιά, εφήβους και ενήλικες, σε ατομικές συνεδρίες και σε ομάδες. Συναντώ επίσης γονείς, ατομικά ή σε ομάδες γονέων.',
  'Children, adolescents and adults, in individual sessions and in groups. I also meet parents, individually or in parent groups.'),
 ('Πόσο διαρκεί μια συνεδρία;', 'How long is a session?',
  '60 λεπτά για την ατομική συνεδρία. Οι ομάδες γονέων και οι ομάδες προσωπικής ανάπτυξης διαρκούν 120 λεπτά και τα ομαδικά βιωματικά εργαστήρια 180 λεπτά.',
  '60 minutes for an individual session. Parent groups and personal-development groups last 120 minutes, and experiential group workshops 180 minutes.'),
 ('Πού βρίσκεται το γραφείο;', 'Where is the practice?',
  'Στην Αλ. Παπαναστασίου 42, στο Νέο Ψυχικό (154 51), περίπου 600 μέτρα από τον σταθμό μετρό Πανόρμου. Κοντά υπάρχουν οι στάσεις λεωφορείου «Βούρη» και «Λητώ».',
  'At 42 Al. Papanastasiou, Neo Psychiko (154 51), about 600 metres from Panormou metro station. The «Vouri» and «Lito» bus stops are close by.'),
 ('Πώς κλείνω ραντεβού;', 'How do I book an appointment?',
  'Τηλεφωνικά στο 694 769 3984 ή online μέσα από το doctoranytime, όπου φαίνονται οι διαθέσιμες ώρες.',
  'By phone on 694 769 3984, or online on doctoranytime, where the available times are shown.'),
 ('Πώς γίνεται η πληρωμή;', 'How do I pay?',
  'Στο γραφείο, με κάρτα ή μετρητά.', 'At the practice, by card or in cash.'),
 ('Μπορώ να ακυρώσω ένα ραντεβού;', 'Can I cancel an appointment?',
  'Ναι, έως 24 ώρες πριν από την ώρα της συνεδρίας.', 'Yes, up to 24 hours before the session.'),
 ('Τι σημαίνει ECP;', 'What does ECP mean?',
  'Είναι το Ευρωπαϊκό Πιστοποιητικό Ψυχοθεραπείας (European Certificate of Psychotherapy) της Ευρωπαϊκής Ένωσης Ψυχοθεραπείας (EAP), της οποίας είμαι μέλος.',
  'It is the European Certificate of Psychotherapy of the European Association for Psychotherapy (EAP), of which I am a member.'),
]
fq = []
for q, qe, a, ae in FAQ:
    fq.append(f'<details class="qa"><summary data-en="{html.escape(qe)}">{html.escape(q)}</summary><div class="qa-a"><p data-en="{html.escape(ae)}">{html.escape(a)}</p></div></details>')
FAQH = '\n      '.join(fq)

body = open(f'{S}/body.html').read().replace('{{REVIEWS}}', REV).replace('{{FAQ}}', FAQH).replace('{{SYMBOL}}', SYMBOL)
css = open(f'{S}/style.css').read()
css += '\n.ft .brand-mk{--mk-i:#FBF8F2}.in-mk{--mk-i:#15372B}'
import subprocess
js = subprocess.run(['/home/claude/tools/node_modules/.bin/terser', f'{S}/script.js', '-c', '-m'], capture_output=True, text=True, check=True).stdout

BOOK = 'https://www.doctoranytime.gr/d/Symvoulos-psychikis-ygeias/kopanitsanou-akrivi'
IMG = 'assets/img/akrivi-kopanitsanou-eikastiki-psychotherapeftria-neo-psychiko-portreto-900.webp'
ld = {"@context": "https://schema.org", "@graph": [
  {"@type": "MedicalBusiness", "@id": "#practice", "name": "Ακριβή (Βιβή) Κοπανιτσάνου — Εικαστική Ψυχοθεραπεία",
   "alternateName": ["Akrivi (Vivi) Kopanitsanou — Art Psychotherapy", "Βιβή Κοπανιτσάνου Εικαστική Ψυχοθεραπεύτρια"],
   "description": "Εικαστική Ψυχοθεραπεία και συμβουλευτική ψυχικής υγείας για παιδιά, εφήβους, ενήλικες και ομάδες στο Νέο Ψυχικό, από την Ακριβή (Βιβή) Κοπανιτσάνου, πιστοποιημένη Εικαστική Ψυχοθεραπεύτρια (ECP-h), M.Sc.",
   "image": IMG, "telephone": "+30 694 769 3984", "email": "akrivikop@gmail.com",
   "address": {"@type": "PostalAddress", "streetAddress": "Αλ. Παπαναστασίου 42", "addressLocality": "Νέο Ψυχικό", "postalCode": "154 51", "addressRegion": "Αττική", "addressCountry": "GR"},
   "geo": {"@type": "GeoCoordinates", "latitude": 38.0054352, "longitude": 23.7808102},
   "hasMap": "https://www.google.com/maps/search/?api=1&query=38.0054352,23.7808102",
   "areaServed": ["Νέο Ψυχικό", "Ψυχικό", "Αμπελόκηποι", "Πανόρμου", "Αθήνα"],
   "knowsAbout": ["Εικαστική Ψυχοθεραπεία", "Ψυχοθεραπεία μέσω τέχνης", "Εικαστική ψυχοθεραπεία ενηλίκων", "Εικαστική ψυχοθεραπεία παιδιών και εφήβων", "Ομαδική εικαστική ψυχοθεραπεία", "Συμβουλευτική γονέων", "Ομάδες γονέων", "Ομάδες προσωπικής ανάπτυξης και αυτογνωσίας", "Βιωματικά εργαστήρια", "Παιδοψυχολογία", "Art Psychotherapy"],
   "sameAs": [BOOK, "https://www.icps.edu.gr/academics/akrivi-kopanitsanoy/"],
   "paymentAccepted": "Κάρτα, Μετρητά", "founder": {"@id": "#person"},
   "aggregateRating": {"@type": "AggregateRating", "ratingValue": 10, "bestRating": 10, "worstRating": 1, "ratingCount": 14}},
  {"@type": "Person", "@id": "#person", "name": "Ακριβή Κοπανιτσάνου",
   "alternateName": ["Ακριβή (Βιβή) Κοπανιτσάνου", "Βιβή Κοπανιτσάνου", "Akrivi Kopanitsanou", "Vivi Kopanitsanou"],
   "jobTitle": "Εικαστική Ψυχοθεραπεύτρια (ECP-h) · Σύμβουλος Ψυχικής Υγείας", "image": IMG, "telephone": "+30 694 769 3984", "email": "akrivikop@gmail.com",
   "worksFor": {"@id": "#practice"}, "affiliation": {"@type": "CollegeOrUniversity", "name": "ICPS – Κολλέγιο Ανθρωπιστικών Επιστημών"},
   "alumniOf": [{"@type": "CollegeOrUniversity", "name": "University of Central Lancashire (UCLan)"}, {"@type": "CollegeOrUniversity", "name": "Εθνικό και Καποδιστριακό Πανεπιστήμιο Αθηνών"}],
   "hasCredential": [{"@type": "EducationalOccupationalCredential", "name": "European Certificate of Psychotherapy (ECP)", "credentialCategory": "certification"},
                     {"@type": "EducationalOccupationalCredential", "name": "M.Sc. Psychology of Child Development", "credentialCategory": "degree"}],
   "memberOf": [{"@type": "Organization", "name": "Ελληνικός Σύλλογος Εικαστικών Ψυχοθεραπευτών (ΕΣΕΨ)"}, {"@type": "Organization", "name": "European Association for Psychotherapy (EAP)"}, {"@type": "Organization", "name": "European Federation of Art Therapy (EFAT)"}],
   "knowsLanguage": ["el"], "sameAs": [BOOK, "https://www.icps.edu.gr/academics/akrivi-kopanitsanoy/"]},
  {"@type": "WebSite", "@id": "#website", "name": "Ακριβή Κοπανιτσάνου — Εικαστική Ψυχοθεραπεία", "alternateName": ["Akrivi Kopanitsanou", "Βιβή Κοπανιτσάνου"], "inLanguage": ["el", "en"]},
  {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, qe, a, ae in FAQ]}]}

TITLE = 'Εικαστική Ψυχοθεραπεία Νέο Ψυχικό | Ακριβή Κοπανιτσάνου'
DESC = 'Ακριβή (Βιβή) Κοπανιτσάνου, Εικαστική Ψυχοθεραπεύτρια (ECP-h) και Σύμβουλος Ψυχικής Υγείας στο Νέο Ψυχικό. Παιδιά, έφηβοι, ενήλικες και ομάδες.'
head = f'''<!DOCTYPE html>
<html lang="el">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#F7F3EC">
<meta name="color-scheme" content="light only">
<meta property="og:type" content="website">
<meta property="og:locale" content="el_GR">
<meta property="og:locale:alternate" content="en_GB">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:image" content="assets/img/og.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Ακριβή (Βιβή) Κοπανιτσάνου, Εικαστική Ψυχοθεραπεύτρια στο Νέο Ψυχικό">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{DESC}">
<meta name="twitter:image" content="assets/img/og.jpg">
<link rel="image_src" href="{IMG}">
<link rel="preload" href="assets/fonts/gfs-didot-greek-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" as="image" href="{IMG}" imagesrcset="assets/img/akrivi-kopanitsanou-eikastiki-psychotherapeftria-neo-psychiko-portreto-640.webp 640w, {IMG} 900w" imagesizes="(max-width:900px) 92vw, 42vw">
<script>(function(h){{h.classList.add('js');try{{if(!sessionStorage.getItem('kop-intro')&&!matchMedia('(prefers-reduced-motion:reduce)').matches&&!document.hidden)h.classList.add('js-intro')}}catch(e){{}}}})(document.documentElement)</script>
<style id="advon-fonts">
{FONTCSS}
</style>
<style>
{css}
</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
'''
page = head + body + '\n<script>' + js + '</script>\n</body>\n</html>\n'
open(f'{OUT}/index.html', 'w').write(page)
open(f'{OUT}/robots.txt', 'w').write('User-agent: *\nAllow: /\n')
open(f'{OUT}/sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>\n')
open(f'{OUT}/.nojekyll', 'w').write('')
print('ok', len(page), len(TITLE), len(DESC))
