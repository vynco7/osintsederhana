🕸️ MuthairOSINT_Full.py - Modul OSINT Siluman Manual Penuh

Versi penuh untuk pencarian digital terdalam dan tersembunyi. Tanpa library tambahan. Tanpa jejak. Tanpa ampun.
Dirancang khusus bagi pelacak yang menginginkan akses manual penuh ke identitas, kebocoran data, file tersembunyi, dan jejak publik dari nama atau persona di internet.
🎯 Fitur Utama

    🔎 Pencarian Dork Siluman: Gunakan ratusan query canggih ke Google dengan rotasi User-Agent acak.

    📧 Pembentukan & Fingerprint Email: Buat varian realistis dari alamat email berdasarkan nama target.

    🔐 Simulator Kebocoran Data: Menyimulasikan kombinasi email + password yang biasa bocor.

    📂 Downloader PDF Otomatis: Mengunduh dan menyimpan dokumen PDF penting yang ditemukan.

    📜 Ekstraksi Metadata File: Ambil informasi tersembunyi dari file PDF (ukuran, hash, sumber).

    🕵️‍♂️ Reverse DNS Lookup: Lacak nama host dari alamat IP yang relevan.

    📁 Logging Cerdas Otomatis: Semua hasil disimpan ke dalam folder terstruktur (pdfs/, leaks/, metadata_logs/, dan dumps/).

    🧠 Total Manual. Tanpa Library Eksternal.: Bisa dijalankan langsung di Termux/Linux dengan Python default.

⚙️ Cara Pakai

$ python3 MuthairOSINT_Full.py
🧠 Masukkan nama target: John Doe

Semua hasil otomatis tersimpan di:

    dumps/ → hasil utama pencarian

    pdfs/ → file PDF yang berhasil diambil

    metadata_logs/ → metadata file PDF

    leaks/ → simulasi data bocor dari email

🔮 Rencana Integrasi Lanjutan

Modul berikut bisa ditambahkan ke sistem ini untuk membuatnya menjadi super suite OSINT sakti:

    GhostMailHunter.py → email-tracing berbasis MX dan SMTP ENUM

    FaceTrace.py → pencarian wajah dengan metode open-CV atau pencocokan hash visual

    DarkLeakScanner.py → pencarian siluman di .onion / layanan paste rahasia

⚠️ Peringatan Etika

Tool ini bukan untuk disalahgunakan. Digunakan hanya untuk edukasi, bug bounty, audit legal, atau pelatihan threat hunting.
Jangan gunakan untuk mengintai orang lain tanpa izin. Karma digital sangat cepat.
🧪 Catatan Teknis

    Dibangun dengan Python 3.x standar.

    Tidak memerlukan pip install sama sekali.

    Kompatibel dengan Termux, WSL, Linux Desktop, bahkan via SSH.

    Diuji pada koneksi rendah dan tetap stealth.
