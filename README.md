🕵️‍♂️ Muthair OSINT Full — Derking Siluman Edition

Versi penuh OSINT tanpa modul tambahan eksternal. Dibuat khusus untuk penelusuran target yang mendalam, stealth, dan efisien. Cocok untuk investigator digital, bug bounty hunter, atau praktisi keamanan siber garis halus.
✨ Fitur Utama

    🔍 Stealth Google Dorking: Menelusuri data tersembunyi di web menggunakan ratusan dork pencarian siluman.

    📧 GhostMailHunter: Pencarian email tersembunyi dari berbagai varian dan domain umum, termasuk pola unik dan hasil tersembunyi.

    🧠 Fingerprint Email Generator: Membangun seluruh kemungkinan email berdasarkan nama target.

    🛑 Simulasi Kebocoran Data: Mendeteksi kemungkinan password default yang bocor dari fingerprint email.

    📄 Scanner Metadata PDF: Mengunduh PDF target dan memindai metadata dasar.

    🌍 Reverse DNS Lookup: Menelusuri hostname berdasarkan alamat IP.

    🧾 Penyimpanan Otomatis: Semua hasil disimpan otomatis ke folder dump dengan timestamp.

🧪 Cara Pakai

$ python3 osint.py
🧠 Masukkan nama target: John Doe

Semua hasil dork, email, kebocoran, metadata, dan PDF akan disimpan otomatis.
📁 Struktur Folder

    pdfs/ → File PDF hasil unduhan otomatis.

    dumps/ → Ringkasan hasil investigasi (per target).

    leaks/ → Hasil simulasi kebocoran berdasarkan email.

    metadata_logs/ → Metadata dari file PDF.

⚠️ Catatan Penting

    Tidak menggunakan modul tambahan eksternal — 100% bisa dijalankan di Termux, Kali, atau Python bare-metal.

    Semua pencarian dilakukan dengan delay acak dan header acak agar siluman dan tidak diblokir.

    Cocok untuk OSINT skala pribadi, investigasi, atau rekonstruksi jejak digital.
