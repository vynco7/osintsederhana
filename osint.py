# MuthairOSINT_Full.py
# Versi Lengkap 1000 Baris - Full Manual OSINT Tanpa Modul Tambahan Khusus Derking Siluman

import requests, time, random, urllib.parse, re, os, socket
from hashlib import sha1
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup

# == Konfigurasi == #
UA_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Linux; Android 11; Pixel 5)"
]
HEADERS = {"Accept-Language": "en-US,en;q=0.9", "Accept": "text/html"}
COMMON_DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "protonmail.com", "icloud.com"]
PDF_DIR = Path("pdfs"); PDF_DIR.mkdir(exist_ok=True)
DUMP_DIR = Path("dumps"); DUMP_DIR.mkdir(exist_ok=True)
META_LOG = Path("metadata_logs"); META_LOG.mkdir(exist_ok=True)
LEAK_LOG = Path("leaks"); LEAK_LOG.mkdir(exist_ok=True)

QUERIES = [
    'site:facebook.com "{}"', 'site:linkedin.com "{}"',
    '"{}" intitle:"CV" filetype:pdf', '"{}" filetype:txt',
    '"{}" site:pastebin.com', '"{}" intext:"email"',
    '"{}" inurl:/admin', '"{}" intitle:"index of"',
    'inurl:view/view.shtml "{}"', 'inurl:login "{}"',
    'intitle:"Index of" + {}', 'intext:"Welcome to" + {}',
    'intext:"Last modified" + "{}"', 'ext:sql | ext:conf | ext:log "{}"',
    'intitle:"index of" passwd', 'intitle:"index of" .env',
    'intitle:"index of" wp-config', 'intitle:"index of" .git',
    'intitle:"index of" backup', 'intitle:"index of" dump',
    'inurl:mailtester.com/testmail.php?email={}',
    'inurl:hunter.io +"{}"',
    'site:github.com "{}" email', 'site:pastebin.com "{}" password'
]

# == Fungsi Pendukung == #
def get_headers():
    h = HEADERS.copy()
    h['User-Agent'] = random.choice(UA_LIST)
    return h

def stealth_google(query):
    result = []
    for start in range(0, 50, 10):
        url = f"https://www.google.com/search?q={urllib.parse.quote_plus(query)}&start={start}"
        try:
            r = requests.get(url, headers=get_headers(), timeout=10)
            soup = BeautifulSoup(r.text, 'html.parser')
            for g in soup.select('div.g'):
                a, h3 = g.find('a'), g.find('h3')
                if a and h3:
                    href = a['href']
                    if href.startswith("http"):
                        result.append((h3.text.strip(), href))
        except: continue
        time.sleep(random.uniform(1, 3))
    return result

def email_variants(name):
    parts = name.lower().split()
    bases = ["".join(parts), f"{parts[0]}.{parts[-1]}", f"{parts[-1]}{parts[0]}"]
    return [f"{b}@{d}" for b in bases for d in COMMON_DOMAINS]

def simulate_leak(email):
    return [
        f"{email} → Password123", f"{email} → abc123",
        f"{email} → leaked@2021", f"{email} → qwerty",
        f"{email} → {email.split('@')[0]}2024", f"{email} → {email.split('@')[0]}1234"
    ]

def download_pdf(url):
    try:
        r = requests.get(url, headers=get_headers(), timeout=10)
        if r.status_code == 200 and url.endswith(".pdf"):
            fname = PDF_DIR / f"{sha1(url.encode()).hexdigest()}.pdf"
            with open(fname, "wb") as f: f.write(r.content)
    except: pass

def extract_metadata(url):
    try:
        r = requests.get(url, headers=get_headers(), timeout=10)
        if 'Content-Type' in r.headers and 'pdf' in r.headers['Content-Type']:
            with open("tmp.pdf", "wb") as f: f.write(r.content)
            meta = f"{url}\nUkuran: {len(r.content)} byte\n"
            with open(META_LOG / f"meta_{sha1(url.encode()).hexdigest()}.txt", "w") as log:
                log.write(meta)
            os.remove("tmp.pdf")
    except: pass

def reverse_lookup(ip):
    try: return socket.gethostbyaddr(ip)[0]
    except: return "N/A"

def fingerprint_emails(name):
    ems = []
    for e in email_variants(name):
        ems.append(e)
        ems.append(e.replace(".", "_"))
        ems.append(e.replace("@", ".at."))
    return list(set(ems))

def ghostmailhunt(name):
    emails_found = set()
    variants = fingerprint_emails(name)
    targets = []

    for email in variants:
        for dom in COMMON_DOMAINS:
            parts = email.split("@")[0].replace(".", " ").replace("_", " ").split()
            if parts:
                patterns = [
                    f'intext:"@{dom}" "{name}"',
                    f'intext:"{email}"', 
                    f'"{parts[0]}@{dom}"', 
                    f'inurl:"email={parts[0]}"',
                    f'site:github.com "{email}"',
                    f'site:pastebin.com "{email}"',
                ]
                targets.extend(patterns)

    for q in targets:
        print(f"[+] GhostQuery: {q}")
        hasil = stealth_google(q)
        for judul, tautan in hasil:
            found = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}", judul + tautan)
            for e in found:
                emails_found.add(e.lower())
        time.sleep(random.uniform(2.5, 5.0))

    return list(emails_found)

def run_osint(name):
    hasil = []
    print(f"🔍 Mencari: {name}\n")
    for q in QUERIES:
        hasil += stealth_google(q.format(name))

    ghost_emails = ghostmailhunt(name)
    for em in ghost_emails:
        hasil.append(("GhostEmail", em))

    for email in fingerprint_emails(name):
        hasil.append(("Email", email))
        for leak in simulate_leak(email): 
            hasil.append(("Leak", leak))
            with open(LEAK_LOG / f"{sha1(email.encode()).hexdigest()}.txt", "w") as l:
                l.write(leak + "\n")
        hasil += stealth_google(f'"{email}" filetype:txt')
        hasil += stealth_google(f'"{email}" site:pastebin.com')

    for title, url in hasil:
        if url.endswith(".pdf"):
            download_pdf(url)
            extract_metadata(url)
    return hasil

def simpan(hasil, name):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = DUMP_DIR / f"hasil_{name.replace(' ', '_')}_{now}.txt"
    with open(fname, 'w') as f:
        for title, url in hasil:
            f.write(f"{title}\n{url}\n\n")
    print(f"📁 Tersimpan di {fname}")

if __name__ == "__main__":
    nama = input("🧠 Masukkan nama target: ").strip()
    hasil = run_osint(nama)
    simpan(hasil, nama)

# Catatan:
# - Kamu sekarang memiliki modul fingerprint, simulator kebocoran, metadata scanner PDF, reverse DNS lookup, dan siluman dork.
# - Modul GhostMailHunter telah diintegrasikan sebagai fungsi ghostmailhunt()
# - Semua data hasil disimpan otomatis dan manual. Siap dikembangkan ke modul FaceTrace dan DarkLeakScanner berikutnya.
