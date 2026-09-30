# -*- coding: utf-8 -*-
"""Bahasa Melayu copy. Each page has en_path so the two language versions are linked with hreflang."""
from content import tbl

SERVICES = [
    {"path": "perkhidmatan/setiausaha-syarikat/", "en_path": "services/company-secretary/", "title": "Setiausaha Syarikat", "cta": "Perkhidmatan setiausaha syarikat",
     "desc": "Pematuhan berkanun dan dokumentasi di bawah Akta Syarikat 2016.",
     "items": ["Pendaftaran Sdn Bhd, LLP & syarikat asing", "Penyata tahunan, AGM & resolusi",
               "Daftar berkanun & pemilikan benefisial", "Perubahan pengarah, saham & alamat"]},
    {"path": "perkhidmatan/perakaunan-simpan-kira/", "en_path": "services/accounting-bookkeeping/", "title": "Perakaunan & Simpan Kira", "cta": "Perkhidmatan perakaunan",
     "desc": "Akaun yang tepat dan tepat masa untuk membantu anda mengurus perniagaan dengan lebih baik.",
     "items": ["Simpan kira bulanan & penyesuaian bank", "Akaun pengurusan & laporan",
               "Penyata kewangan akhir tahun", "Gaji, KWSP, PERKESO & SIP"]},
    {"path": "perkhidmatan/audit/", "en_path": "services/audit/", "title": "Audit & Jaminan", "cta": "Perkhidmatan audit",
     "desc": "Audit bebas bagi memenuhi keperluan berkanun dan kawal selia.",
     "items": ["Audit berkanun penyata kewangan", "Persediaan & penyelarasan audit",
               "Semakan bertujuan khas", "Cadangan kawalan dalaman"]},
    {"path": "perkhidmatan/ejen-cukai/", "en_path": "services/tax-agent/", "title": "Ejen Cukai & Nasihat", "cta": "Perkhidmatan cukai",
     "desc": "Kekal patuh kepada LHDN dan optimumkan kedudukan cukai anda.",
     "items": ["Penyerahan cukai korporat & individu", "Anggaran cukai CP204", "Pendaftaran & penyata SST",
               "Perancangan cukai & pertanyaan LHDN"]},
]

PERSONAS = [
    {"id": "start", "label": "Memulakan syarikat", "sub": "Belum berdaftar", "label_l": "sedang memulakan syarikat",
     "headline": "Sediakan Sdn Bhd anda dengan betul, kali pertama.",
     "intro": "Kebanyakan penalti tahun pertama datang daripada langkah yang pengasas tidak tahu wujud. Kami uruskan kesemuanya.",
     "needs": ["Carian nama & pendaftaran SSM", "Perlembagaan & resolusi lembaga pertama",
               "Pelantikan setiausaha syarikat dalam 30 hari (Akta Syarikat 2016)", "Pendaftaran fail cukai LHDN",
               "Dokumen pembukaan akaun bank"],
     "plan": "Launch", "planDesc": "Pemerbadanan serta pematuhan tahun pertama anda.",
     "includes": ["Semua yang diperlukan untuk pemerbadanan", "Setiausaha syarikat 12 bulan", "Penyediaan simpan kira", "Pendaftaran fail cukai LHDN"],
     "alt": "Hanya perlukan pendaftaran? Tanya tentang pakej Incorporate.", "need": ["Daftar syarikat baharu"], "stage": "Belum berdaftar"},
    {"id": "run", "label": "Mengendalikan Sdn Bhd", "sub": "Sudah beroperasi, mahu diuruskan", "label_l": "mengendalikan sebuah Sdn Bhd",
     "headline": "Serahkan keseluruhan kitaran pematuhan tahunan.",
     "intro": "Satu pasukan mengurus setiausaha, akaun, audit dan cukai bersama — supaya tiada yang terlepas antara dua firma.",
     "needs": ["Penyata tahunan & penyata kewangan kepada SSM", "Simpan kira bulanan & gaji (KWSP, PERKESO, SIP)",
               "Penyelarasan audit berkanun", "Borang C dan CP204 kepada LHDN"],
     "plan": "Full compliance", "planDesc": "Setiausaha, akaun, audit dan cukai — satu pasukan.",
     "includes": ["Setiausaha syarikat yang dikenali", "Simpan kira bulanan", "Penyelarasan audit", "Penyerahan Borang C & CP204"],
     "alt": "Hanya perlukan setiausaha? Tanya tentang pakej Secretarial.",
     "need": ["Setiausaha syarikat", "Perakaunan", "Audit", "Cukai"], "stage": "Beroperasi lebih 2 tahun"},
    {"id": "foreign", "label": "Pengasas luar negara", "sub": "Cawangan, LLP atau subsidiari", "label_l": "pengasas luar negara",
     "headline": "Masuk ke Malaysia dengan urusan dokumen diselesaikan.",
     "intro": "Kami bantu anda memilih struktur yang sesuai, kemudian mendaftar dan memastikan ia patuh dari sini.",
     "needs": ["Memilih antara cawangan, LLP atau Sdn Bhd", "Semakan & pengesahan dokumen",
               "Ejen pemastautin atau pegawai pematuhan", "Senarai semak selepas pendaftaran"],
     "plan": "Foreign company / LLP", "planDesc": "Untuk pengasas dan perkongsian luar negara.",
     "includes": ["Pendaftaran cawangan atau LLP", "Semakan & pengesahan dokumen", "Ejen pemastautin / pegawai pematuhan",
                  "Senarai semak selepas pendaftaran"],
     "alt": "Tidak pasti struktur mana? Kami nasihatkan dalam panggilan pertama.", "need": ["Daftar syarikat baharu"],
     "stage": "Belum berdaftar"},
    {"id": "behind", "label": "Tertunggak penyerahan", "sub": "Atau tidak berpuas hati dengan firma anda", "label_l": "tertunggak penyerahan",
     "headline": "Kembali ke landasan — tanpa tekanan.",
     "intro": "Penyata tertunggak memang berlaku. Kami kumpulkan rekod anda, selesaikan yang tertunggak dan pastikan ia kekal bersih selepas itu.",
     "needs": ["Rekod dikumpulkan daripada firma terdahulu", "Semakan pematuhan", "Penyerahan tertunggak diselesaikan",
               "Kemudian pakej yang sesuai"],
     "plan": "Switch to us", "planDesc": "Bertukar daripada firma lain? Kami permudahkan.",
     "includes": ["Serahan rekod diuruskan untuk anda", "Semakan pematuhan penuh", "Penyerahan lewat diselesaikan",
                  "Pakej berterusan selepas itu"],
     "alt": "Hubungi kami sebelum kompaun seterusnya tiba.", "need": ["Belum pasti"], "stage": "Tertunggak penyerahan"},
]

QUIZ = [
    {"q": "Adakah syarikat anda telah melantik setiausaha syarikat yang berlesen?",
     "fix": "Lantik setiausaha syarikat yang berlesen (diwajibkan di bawah Akta Syarikat 2016)."},
    {"q": "Adakah penyata tahunan terakhir anda difailkan dengan SSM tepat pada masanya?",
     "fix": "Failkan penyata tahunan yang tertunggak dan selesaikan yang lewat."},
    {"q": "Adakah akaun beraudit terkini anda diedarkan dan difailkan tepat pada masanya?",
     "fix": "Kembalikan pemfailan audit dan penyata kewangan mengikut jadual."},
    {"q": "Adakah Borang C terakhir anda diserahkan dalam tempoh 7 bulan selepas akhir tahun kewangan?",
     "fix": "Serahkan Borang C dan semak anggaran CP204 anda dengan LHDN."},
    {"q": "Adakah buku akaun anda dikemas kini sekurang-kurangnya setiap bulan?",
     "fix": "Sediakan simpan kira bulanan supaya akhir tahun tidak menjadi kelam-kabut."},
]

HOME_FAQS = [
    ("Adakah setiap Sdn Bhd perlu mempunyai setiausaha syarikat?",
     "Ya. Di bawah Akta Syarikat 2016, setiap syarikat mesti melantik sekurang-kurangnya seorang setiausaha syarikat dalam tempoh 30 hari selepas pemerbadanan. Setiausaha mesti berlesen atau berdaftar dengan SSM."),
    ("Adakah syarikat persendirian saya perlu diaudit?",
     "Kebanyakannya perlu, walaupun SSM membenarkan syarikat tertentu yang tidak aktif (dorman), tiada hasil atau kecil yang memenuhi ambang layak untuk dikecualikan. Kami akan menyemak sama ada syarikat anda layak sebelum mencadangkan audit."),
    ("Bilakah pulangan cukai syarikat saya perlu diserahkan?",
     "Borang C mesti diserahkan kepada LHDN dalam tempoh tujuh bulan selepas akhir tahun kewangan anda. Anggaran cukai (CP204) perlu dikemukakan 30 hari sebelum bermulanya setiap tempoh asas, dengan ansuran dibayar setiap bulan."),
    ("Apa akan berlaku jika penyerahan lewat?",
     "SSM dan LHDN boleh mengenakan kompaun dan penalti ke atas syarikat dan pegawainya. Jika anda sudah mempunyai penyerahan tertunggak, kami boleh membantu menyelesaikannya apabila anda bertukar kepada kami."),
    ("Bolehkah saya menggunakan satu perkhidmatan sahaja?",
     "Sudah tentu. Ramai pelanggan bermula dengan setiausaha atau perakaunan sahaja dan menambah audit serta cukai kemudian. Harga fleksibel dan dibina mengikut keperluan anda."),
    ("Di mana CCM Secretarial berpangkalan, dan adakah anda melayani PKS di luar Shah Alam?",
     "Pejabat kami di Elmina, Shah Alam, Selangor. Kebanyakan urusan SSM dan LHDN dibuat secara dalam talian, jadi kami menyokong PKS di seluruh Lembah Klang dan Malaysia melalui telefon, WhatsApp dan bersemuka."),
]

PAGES = []

PAGES.append({
    "path": "perkhidmatan/setiausaha-syarikat/", "en_path": "services/company-secretary/",
    "crumb": "Perkhidmatan setiausaha syarikat", "eyebrow": "Setiausaha syarikat · Malaysia",
    "title": "Perkhidmatan Setiausaha Syarikat Malaysia | CCM",
    "desc": "Setiausaha syarikat berlesen untuk Sdn Bhd & LLP: penyata tahunan SSM, daftar berkanun, resolusi dan perubahan pengarah. Yuran tetap. Shah Alam.",
    "h1": "Perkhidmatan setiausaha syarikat untuk PKS Malaysia",
    "lead": "Seorang setiausaha syarikat yang anda kenali, yang memastikan Sdn Bhd, LLP atau syarikat asing anda patuh kepada Akta Syarikat 2016 dan SSM — supaya penyerahan tidak pernah lewat.",
    "box_title": "Apa yang termasuk", "box": ["Pelantikan setiausaha syarikat", "Penyerahan penyata tahunan kepada SSM", "Daftar berkanun & buku minit",
                                         "Perubahan pengarah, pemegang saham & alamat", "Rekod pemilikan benefisial", "Peringatan tarikh akhir, setiap tahun"],
    "faq_h": "Soalan tentang setiausaha syarikat",
    "body": """
<h2>Mengapa setiap syarikat di Malaysia memerlukan setiausaha syarikat</h2>
<p>Di bawah Akta Syarikat 2016, setiap syarikat yang diperbadankan di Malaysia mesti melantik sekurang-kurangnya seorang setiausaha syarikat dalam tempoh 30 hari selepas pemerbadanan. Setiausaha mestilah individu yang lazimnya bermastautin di Malaysia dan berlesen atau layak di bawah Akta. Bagi kebanyakan PKS, mengambil setiausaha sepenuh masa tidak masuk akal — sebab itu menggunakan firma setiausaha syarikat adalah kebiasaan.</p>
<h2>Apa yang dilindungi oleh perkhidmatan setiausaha syarikat kami</h2>
<ul>
<li><strong>Penyerahan penyata tahunan</strong> — disediakan dan difailkan dengan SSM dalam tempoh 30 hari selepas ulang tahun pemerbadanan anda.</li>
<li><strong>Mesyuarat dan resolusi</strong> — resolusi lembaga dan pemegang saham, notis dan minit AGM, serta pengedaran akaun beraudit.</li>
<li><strong>Daftar berkanun</strong> — pengarah, ahli, caj dan rekod lain yang diwajibkan Akta disimpan di pejabat berdaftar anda.</li>
<li><strong>Perubahan butiran syarikat</strong> — melantik atau menyingkirkan pengarah, pindahan saham, menukar alamat berdaftar, aktiviti perniagaan atau nama syarikat.</li>
<li><strong>Pemilikan benefisial</strong> — memastikan daftar pemilik benefisial anda tepat dan difailkan dengan SSM.</li>
<li><strong>Setiausaha syarikat untuk Sdn Bhd, LLP dan syarikat asing</strong> — termasuk urusan ejen pemastautin atau pegawai pematuhan untuk pengasas luar negara.</li>
</ul>
<h2>Setiausaha yang dikenali, bukan barisan tiket</h2>
<p>Anda mendapat seorang wakil yang mengenali syarikat, pengarah dan akhir tahun kewangan anda. Kami menjejak setiap tarikh akhir SSM untuk anda dan mengingatkan anda sebelum ia tiba, supaya anda tidak mengetahui penyata tahunan yang terlepas melalui notis kompaun.</p>
<h2>Tarikh akhir SSM utama yang kami uruskan</h2>
""" + tbl(["Kewajipan", "Tarikh akhir lazim"], [
        ["Melantik setiausaha syarikat", "Dalam 30 hari selepas pemerbadanan"],
        ["Penyata tahunan kepada SSM", "Dalam 30 hari selepas ulang tahun pemerbadanan"],
        ["Mengedarkan penyata kewangan beraudit", "Dalam 6 bulan selepas akhir tahun kewangan"],
        ["Memfailkan penyata kewangan dengan SSM", "Dalam 30 hari selepas pengedaran"],
        ["Perubahan pengarah / alamat", "Biasanya dalam 14 hari selepas perubahan"]]) + """
<p>Lihat <a href="../../panduan/kalendar-pematuhan-sdn-bhd-malaysia/">kalendar pematuhan Sdn Bhd</a> kami yang lengkap, termasuk tarikh LHDN.</p>
<h2>Mahu menukar setiausaha syarikat?</h2>
<p>Jika setiausaha anda sekarang perlahan, tidak memberi respons atau anda mempunyai penyerahan tertunggak, kami uruskan serahan rekod dan menyelesaikan penyata yang lewat. <a href="../tukar-setiausaha-syarikat/">Ketahui cara pertukaran berfungsi</a>.</p>
""",
    "faqs": [
        ("Berapakah kos setiausaha syarikat di Malaysia?", "Yuran bergantung kepada jenis syarikat, bilangan pengarah dan penyerahan yang terlibat. Kami beri sebut harga yuran tetap selepas panggilan ringkas, supaya anda tahu kos tahunan sebelum kami mula."),
        ("Bolehkah saya menjadi setiausaha syarikat saya sendiri?", "Hanya jika anda orang yang layak di bawah Akta Syarikat 2016 — contohnya ahli badan profesional yang ditetapkan atau dilesenkan oleh SSM. Kebanyakan pemilik perniagaan melantik setiausaha syarikat berlesen."),
        ("Adakah anda melayani LLP dan perniagaan milik tunggal?", "Ya. Kami menyokong Sdn Bhd, LLP dan syarikat asing, dan boleh membantu pemilik tunggal mendaftar atau menukar kepada Sdn Bhd."),
        ("Apa berlaku jika penyata tahunan difailkan lewat?", "SSM boleh mengeluarkan kompaun terhadap syarikat dan pegawainya. Kami boleh membantu menyelesaikan penyata tertunggak dan mengembalikan penyerahan anda mengikut jadual."),
    ],
})

PAGES.append({
    "path": "perkhidmatan/perakaunan-simpan-kira/", "en_path": "services/accounting-bookkeeping/",
    "crumb": "Perakaunan & simpan kira", "eyebrow": "Perakaunan · Malaysia",
    "title": "Perakaunan & Simpan Kira untuk PKS Malaysia | CCM",
    "desc": "Simpan kira bulanan, akaun pengurusan, gaji (KWSP, PERKESO, SIP) dan penyata kewangan akhir tahun untuk Sdn Bhd dan PKS. Yuran tetap. Shah Alam.",
    "h1": "Perkhidmatan perakaunan & simpan kira untuk PKS Malaysia",
    "lead": "Buku bulanan yang tepat, gaji dan penyata kewangan akhir tahun — disediakan mengikut piawaian Malaysia dan sedia untuk audit serta LHDN.",
    "box_title": "Apa yang termasuk", "box": ["Simpan kira bulanan & penyesuaian bank", "Akaun pengurusan & laporan",
                                         "Penyata kewangan akhir tahun", "Gaji: KWSP, PERKESO, SIP & PCB", "Sokongan kesediaan SST dan e-Invois",
                                         "Rekod sedia untuk audit"],
    "faq_h": "Soalan tentang perakaunan",
    "body": """
<h2>Simpan kira yang memastikan anda patuh sepanjang tahun</h2>
<p>Kebanyakan masalah cukai dan audit PKS bermula daripada buku yang dikemas kini setahun sekali, dalam keadaan tergesa-gesa. Kami memastikan rekod anda sentiasa terkini setiap bulan, supaya penyata kewangan, audit dan Borang C anda dibina atas angka yang bersih — bukan dibina semula daripada timbunan resit.</p>
<h2>Apa yang kami lakukan setiap bulan</h2>
<ul>
<li>Merekod jualan, pembelian dan perbelanjaan daripada invois, resit dan penyata bank anda.</li>
<li>Menyesuaikan akaun bank dan pembayaran anda serta menjejak dokumen yang tiada.</li>
<li>Menyediakan akaun pengurusan — untung rugi, kunci kira-kira dan pandangan ringkas aliran tunai.</li>
<li>Menjalankan gaji dan menyerahkan caruman <strong>KWSP, PERKESO dan SIP</strong> serta potongan cukai bulanan (PCB).</li>
<li>Menyediakan dan menyerahkan penyata SST jika anda berdaftar SST.</li>
</ul>
<h2>Penyata kewangan akhir tahun</h2>
<p>Pada akhir tahun, kami menyediakan penyata kewangan mengikut rangka kerja pelaporan kewangan Malaysia yang terpakai, sedia untuk juruaudit, pengarah dan SSM anda. Oleh kerana buku disimpan setiap bulan, persediaan audit lebih pantas dan kurang mengganggu.</p>
<h2>e-Invois dan kesediaan digital</h2>
<p>Keperluan e-Invois (MyInvois) LHDN dilaksanakan secara berperingkat mengikut perolehan perniagaan. Kami membantu PKS menyemak fasa yang terpakai, menyediakan perisian perakaunan atau aliran kerja portal yang betul, dan menyimpan rekod dalam format yang dikehendaki LHDN. Hubungi kami untuk mengetahui kedudukan perniagaan anda.</p>
<h2>Mengapa PKS memilih satu pasukan untuk akaun, audit dan cukai</h2>
<p>Apabila firma yang menyimpan buku anda juga menyelaras <a href="../audit/">audit berkanun</a> dan menyerahkan <a href="../ejen-cukai/">cukai korporat</a>, tiada yang terlepas antara dua pembekal dan akhir tahun tidak lagi kelam-kabut.</p>
""",
    "faqs": [
        ("Berapa kerap buku kami dikemas kini?", "Sekurang-kurangnya setiap bulan. Anda hantar dokumen melalui WhatsApp, e-mel atau folder kongsi, dan kami menyesuaikan serta melapor setiap bulan."),
        ("Adakah anda menggunakan perisian perakaunan seperti AutoCount, SQL atau Xero?", "Kami bekerja dengan platform biasa yang digunakan PKS Malaysia dan boleh menasihati mana yang sesuai dengan saiz dan industri anda. Tanya kami tentang sistem semasa anda."),
        ("Bolehkah anda menguruskan gaji, KWSP dan PERKESO?", "Ya. Kami menjalankan gaji dan menyediakan serahan KWSP, PERKESO, SIP dan PCB supaya tanggungjawab majikan anda dipenuhi tepat pada masanya."),
        ("Bolehkah saya mengupah anda untuk akaun akhir tahun sahaja?", "Boleh, walaupun kami mengesyorkan simpan kira bulanan — ia biasanya lebih murah daripada membersihkan rekod setahun penuh pada akhir tahun."),
    ],
})

PAGES.append({
    "path": "perkhidmatan/audit/", "en_path": "services/audit/",
    "crumb": "Audit & jaminan", "eyebrow": "Audit · Malaysia",
    "title": "Audit Berkanun Sdn Bhd & PKS Malaysia | CCM",
    "desc": "Audit berkanun, persediaan audit dan semakan pengecualian untuk syarikat persendirian Malaysia. Bebas, mengikut jadual SSM. Yuran tetap. Shah Alam.",
    "h1": "Audit berkanun & jaminan untuk PKS Malaysia",
    "lead": "Audit bebas penyata kewangan anda yang memenuhi keperluan Akta Syarikat 2016 dan SSM — diselaraskan dengan akaun dan cukai anda supaya ia siap tepat pada masanya.",
    "box_title": "Apa yang termasuk", "box": ["Audit berkanun penyata kewangan", "Semakan kelayakan pengecualian audit",
                                         "Persediaan & penyelarasan audit", "Semakan bertujuan khas", "Cadangan kawalan dalaman"],
    "faq_h": "Soalan tentang audit",
    "body": """
<h2>Adakah Sdn Bhd anda perlu diaudit?</h2>
<p>Kebanyakan syarikat persendirian Malaysia mesti mempunyai penyata kewangan yang diaudit setiap tahun oleh juruaudit syarikat berlesen. Akta Syarikat 2016 membenarkan syarikat tertentu — contohnya syarikat dorman dan syarikat persendirian kecil yang layak ambang — menuntut pengecualian. Sama ada syarikat anda layak bergantung kepada hasil, aset dan syarat lain, jadi kami menyemak kelayakan anda sebelum mengesyorkan audit. Baca panduan kami: <a href="../../panduan/adakah-sdn-bhd-perlu-diaudit/">Adakah Sdn Bhd saya perlu diaudit?</a></p>
<h2>Apa yang terlibat dalam audit berkanun</h2>
<ul>
<li><strong>Perancangan</strong> — kami bersetuju tentang jadual dengan mengira ke belakang daripada tarikh akhir SSM dan LHDN anda.</li>
<li><strong>Persediaan</strong> — kami mengesahkan jadual, pengesahan bank dan dokumen sokongan anda sudah sedia.</li>
<li><strong>Kerja lapangan</strong> — audit baki dan transaksi, dengan pertanyaan yang jelas dan bukan kejutan.</li>
<li><strong>Pelaporan</strong> — penyata kewangan beraudit dan laporan juruaudit untuk ditandatangani pengarah dan difailkan dengan SSM.</li>
<li><strong>Maklum balas pengurusan</strong> — cadangan praktikal tentang kawalan dalaman dan simpan kira.</li>
</ul>
<h2>Tarikh akhir audit yang perlu dirancang</h2>
""" + tbl(["Langkah", "Tarikh akhir"], [
        ["Mengedarkan akaun beraudit kepada ahli", "Dalam 6 bulan selepas akhir tahun kewangan"],
        ["Memfailkan akaun beraudit dengan SSM", "Dalam 30 hari selepas pengedaran"],
        ["Menyerahkan Borang C kepada LHDN", "Dalam 7 bulan selepas akhir tahun kewangan"]]) + """
<p>Oleh kerana Borang C bergantung kepada akaun yang telah dimuktamadkan, audit yang lewat siap akan melewatkan penyerahan cukai anda juga. Menggunakan pasukan yang sama untuk <a href="../perakaunan-simpan-kira/">simpan kira</a>, penyelarasan audit dan <a href="../ejen-cukai/">cukai</a> memastikan semua tarikh akhir selari.</p>
<h2>Semakan bertujuan khas</h2>
<p>Kami juga membantu dengan semakan untuk pembiayaan bank, tender, pelabur dan usaha wajar, apabila pemberi pinjaman atau pihak lain meminta jaminan bebas melangkaui audit berkanun.</p>
""",
    "faqs": [
        ("Syarikat Malaysia yang manakah dikecualikan daripada audit?", "Syarikat dorman tertentu dan syarikat persendirian kecil yang layak ambang mungkin dikecualikan di bawah Akta Syarikat 2016. Kami menyemak angka dan syarat anda sebelum menasihati."),
        ("Berapa lama audit berkanun mengambil masa?", "Bergantung kepada saiz dan keadaan buku anda. Syarikat dengan simpan kira bulanan yang terkini diaudit lebih cepat, sebab itu kami merancang audit dari awal tahun."),
        ("Bolehkah firma yang melakukan simpan kira saya juga melakukan audit?", "Peraturan kebebasan terpakai. Kami menyelaraskan audit dan memastikan profesional berlesen yang betul mengendalikan setiap peranan, supaya buku dan audit anda kekal selari."),
        ("Apa berlaku jika kami memfailkan akaun beraudit lewat?", "SSM boleh mengenakan kompaun ke atas syarikat dan pegawainya. Kami boleh membantu anda mengejar ketinggalan dan menyelesaikan pemfailan yang tertunggak."),
    ],
})

PAGES.append({
    "path": "perkhidmatan/ejen-cukai/", "en_path": "services/tax-agent/",
    "crumb": "Ejen cukai & nasihat", "eyebrow": "Cukai · LHDN · Malaysia",
    "title": "Ejen Cukai Malaysia: Borang C, CP204 & SST | CCM",
    "desc": "Penyerahan cukai korporat, Borang C, anggaran CP204, SST dan pertanyaan LHDN untuk PKS Malaysia. Satu pasukan untuk akaun dan cukai. Shah Alam.",
    "h1": "Ejen cukai & nasihat untuk PKS Malaysia",
    "lead": "Penyerahan cukai korporat dan individu, anggaran CP204, SST dan pertanyaan LHDN — diuruskan oleh pasukan yang sama yang menyimpan buku anda, supaya angka dan pulangan anda sentiasa sepadan.",
    "box_title": "Apa yang termasuk", "box": ["Penyerahan cukai korporat Borang C", "Anggaran & semakan CP204", "Cukai pendapatan individu (Borang BE / B)",
                                         "Pendaftaran & penyata SST", "Perancangan & pengiraan cukai", "Sokongan pertanyaan & audit LHDN"],
    "faq_h": "Soalan tentang cukai",
    "body": """
<h2>Penyerahan cukai korporat untuk Sdn Bhd</h2>
<p>Setiap syarikat Malaysia mesti menyerahkan borang nyata cukai pendapatan (<strong>Borang C</strong>) kepada LHDN dalam tempoh tujuh bulan selepas akhir tahun kewangan — walaupun syarikat dorman atau mengalami kerugian. Kami menyediakan pengiraan cukai daripada akaun yang dimuktamadkan, menuntut elaun dan potongan yang anda layak, dan menyerahkannya melalui sistem e-Filing LHDN.</p>
<h2>CP204: menganggar cukai yang perlu dibayar</h2>
<p>Syarikat mesti mengemukakan anggaran cukai (<strong>CP204</strong>) sebelum bermula setiap tempoh asas dan membayar cukai melalui ansuran bulanan. Menganggar terlalu rendah boleh mengundang penalti, jadi kami menyemak anggaran anda berbanding keputusan tahun itu dan mengemukakan semakan dalam tempoh yang dibenarkan.</p>
<h2>SST dan cukai tidak langsung lain</h2>
<p>Jika perolehan anda mencapai ambang pendaftaran Cukai Jualan dan Perkhidmatan, kami menguruskan pendaftaran, penyata berkala dan penyimpanan rekod supaya anda kekal mematuhi Jabatan Kastam Diraja Malaysia.</p>
<h2>Perancangan cukai dan pertanyaan LHDN</h2>
<ul>
<li>Nasihat sepanjang tahun tentang potongan, elaun modal dan kesan cukai keputusan besar.</li>
<li>Jawapan kepada pertanyaan, surat semakan dan audit LHDN.</li>
<li>Penyerahan cukai pendapatan peribadi pengarah dan pemilik.</li>
</ul>
<h2>Mengapa perakaunan dan cukai paling baik bersama</h2>
<p>Pulangan cukai hanya sebaik akaun yang menjadi asasnya. Oleh kerana pasukan kami juga menguruskan <a href="../perakaunan-simpan-kira/">simpan kira</a> dan menyelaras <a href="../audit/">audit</a> anda, Borang C anda dibina daripada angka beraudit tanpa memasukkan semula data, dan CP204 anda mencerminkan prestasi sebenar perniagaan.</p>
<h2>Tarikh LHDN untuk Sdn Bhd lazim</h2>
""" + tbl(["Kewajipan", "Tarikh akhir lazim"], [
        ["Borang C (borang nyata cukai korporat)", "Dalam 7 bulan selepas akhir tahun kewangan"],
        ["Anggaran cukai CP204", "30 hari sebelum bermulanya tempoh asas"],
        ["Ansuran CP204", "Setiap bulan, pada atau sebelum 15 haribulan"]]) + """
<p class="meta">Tarikh adalah petunjuk — kami mengesahkan tarikh akhir sebenar untuk syarikat anda.</p>
""",
    "faqs": [
        ("Bilakah Borang C perlu diserahkan untuk syarikat saya?", "Dalam tempoh tujuh bulan selepas akhir tahun kewangan anda. Bagi akhir tahun 31 Disember, ia adalah 31 Julai tahun berikutnya."),
        ("Adakah syarikat dorman perlu menyerahkan borang nyata cukai?", "Ya. Syarikat masih perlu menyerahkan borang kepada LHDN walaupun tiada pendapatan atau dorman."),
        ("Apakah CP204 dan adakah saya memerlukannya?", "CP204 ialah anggaran cukai yang dikemukakan syarikat sebelum setiap tempoh asas, dibayar melalui ansuran bulanan. Syarikat baharu biasanya dikecualikan dalam dua tahun pertama, tetapi peraturannya khusus — kami akan mengesahkannya untuk anda."),
        ("Bolehkah anda berurusan dengan LHDN bagi pihak saya?", "Boleh. Sebagai ejen cukai anda, kami boleh menjawab pertanyaan, surat semakan dan audit LHDN serta mewakili syarikat dalam surat-menyurat."),
    ],
})

PAGES.append({
    "path": "perkhidmatan/daftar-sdn-bhd/", "en_path": "services/sdn-bhd-registration/",
    "crumb": "Daftar Sdn Bhd", "eyebrow": "Pendaftaran syarikat · SSM",
    "title": "Daftar Sdn Bhd di Malaysia (SSM) | CCM Secretarial",
    "desc": "Pendaftaran Sdn Bhd dengan SSM langkah demi langkah: syarat, dokumen, tempoh dan pematuhan tahun pertama. Juga LLP dan syarikat asing. Shah Alam.",
    "h1": "Daftar Sdn Bhd di Malaysia dengan SSM",
    "lead": "Kami uruskan carian nama, pemerbadanan SSM, perlembagaan, pelantikan setiausaha syarikat dan pendaftaran LHDN — supaya syarikat anda disediakan dengan betul, kali pertama.",
    "box_title": "Anda akan perlukan", "box": ["Sekurang-kurangnya 1 pengarah yang lazimnya bermastautin di Malaysia", "Sekurang-kurangnya 1 pemegang saham",
                                          "Alamat pejabat berdaftar di Malaysia", "Setiausaha syarikat berlesen (kami lantikkan)",
                                          "Salinan kad pengenalan pengarah & pemegang saham", "2–3 pilihan nama syarikat"],
    "faq_h": "Soalan tentang pendaftaran syarikat",
    "howto": {"name": "Cara mendaftar Sdn Bhd di Malaysia", "steps": [
        ("Pilih dan tempah nama syarikat", "Kemukakan dua atau tiga pilihan nama kepada SSM untuk carian dan kelulusan nama."),
        ("Sediakan butiran pemerbadanan", "Sahkan pengarah, pemegang saham, modal saham, alamat berdaftar dan aktiviti perniagaan."),
        ("Lantik setiausaha syarikat", "Lantik setiausaha syarikat berlesen dalam tempoh 30 hari selepas pemerbadanan."),
        ("Kemukakan permohonan kepada SSM", "Failkan permohonan pemerbadanan bersama perlembagaan dan perakuan yang diperlukan."),
        ("Terima Perakuan Pemerbadanan", "SSM mengeluarkan perakuan dan nombor pendaftaran syarikat."),
        ("Daftar dengan LHDN dan buka akaun bank", "Sediakan fail cukai dan gunakan dokumen pemerbadanan untuk perbankan perniagaan.")]},
    "body": """
<h2>Syarat pendaftaran Sdn Bhd di Malaysia</h2>
<p>Syarikat sendirian berhad (Sdn Bhd) ialah struktur paling biasa bagi PKS Malaysia kerana ia menghadkan liabiliti pemilik kepada modal yang telah dilaburkan. Di bawah Akta Syarikat 2016, anda memerlukan:</p>
<ul>
<li>Sekurang-kurangnya <strong>seorang pengarah</strong> yang lazimnya bermastautin di Malaysia;</li>
<li>Sekurang-kurangnya <strong>seorang pemegang saham</strong> (orang yang sama boleh menjadi pengarah dan pemegang saham);</li>
<li><strong>Alamat pejabat berdaftar</strong> di Malaysia;</li>
<li><strong>Setiausaha syarikat</strong> yang dilantik dalam tempoh 30 hari selepas pemerbadanan;</li>
<li>Nama syarikat yang tersedia dan diluluskan oleh SSM.</li>
</ul>
<h2>Cara pendaftaran Sdn Bhd berfungsi, langkah demi langkah</h2>
<ol>
<li><strong>Carian nama</strong> — kami menyemak dan menempah nama pilihan anda dengan SSM.</li>
<li><strong>Sediakan butiran</strong> — pengarah, pemegang saham, modal saham, alamat dan kod aktiviti perniagaan.</li>
<li><strong>Failkan dengan SSM</strong> — kami mengemukakan permohonan dan perlembagaan bagi pihak anda.</li>
<li><strong>Perakuan Pemerbadanan</strong> — SSM mengeluarkan perakuan dan nombor syarikat anda.</li>
<li><strong>Persediaan selepas pemerbadanan</strong> — daftar berkanun, resolusi lembaga pertama, pendaftaran fail cukai LHDN dan dokumen pembukaan akaun bank.</li>
</ol>
<div class="callout"><strong>Jangan berhenti pada perakuan.</strong> Kebanyakan penalti tahun pertama datang daripada langkah yang pengasas tidak tahu wujud — melantik setiausaha syarikat, memfailkan maklumat pemilikan benefisial, penyata tahunan pertama dan Borang C pertama anda. Pakej <em>Launch</em> kami meliputi pemerbadanan serta pematuhan tahun pertama anda.</div>
<h2>Sdn Bhd, LLP, milik tunggal atau cawangan asing?</h2>
""" + tbl(["Struktur", "Sesuai untuk", "Perkara utama"], [
        ["Milik tunggal / perkongsian", "Perniagaan sangat kecil, berisiko rendah", "Pemilik bertanggungan peribadi; pendaftaran mudah"],
        ["Sdn Bhd (syarikat sendirian berhad)", "PKS berkembang, kontrak, tender, pelabur", "Liabiliti terhad; setiausaha syarikat, penyata tahunan dan biasanya audit"],
        ["LLP (perkongsian liabiliti terhad)", "Amalan profesional", "Liabiliti rakan kongsi terhad; pemfailan lebih ringan daripada Sdn Bhd"],
        ["Cawangan / subsidiari syarikat asing", "Perniagaan luar negara memasuki Malaysia", "Pilihan bergantung kepada aktiviti dan pemilikan; ejen pemastautin atau pegawai pematuhan diperlukan"]]) + """
<p>Tidak pasti yang mana sesuai? Kami menasihati dalam panggilan pertama, tanpa bayaran. Pengasas luar negara? Kami juga menguruskan semakan dan pengesahan dokumen serta urusan ejen pemastautin.</p>
<h2>Selepas pendaftaran: apa yang perlu dilakukan Sdn Bhd baharu</h2>
<p>Sediakan <a href="../perakaunan-simpan-kira/">simpan kira</a> dari hari pertama, kemas kini <a href="../setiausaha-syarikat/">daftar berkanun</a> anda, dan catat penyata tahunan serta audit pertama anda. <a href="../../panduan/kalendar-pematuhan-sdn-bhd-malaysia/">Kalendar pematuhan</a> kami menunjukkan apa yang perlu dibuat dan bila.</p>
""",
    "faqs": [
        ("Berapa lama masa untuk mendaftar Sdn Bhd di Malaysia?", "Apabila nama diluluskan dan dokumen lengkap, pemerbadanan SSM biasanya pantas. Kami mengesahkan tempoh yang realistik dalam panggilan pertama."),
        ("Berapakah modal minimum untuk Sdn Bhd?", "Tiada modal minimum berkanun yang tinggi; jumlahnya ditetapkan pemegang saham berdasarkan keperluan perniagaan. Kami menasihati jumlah yang munasabah untuk perbankan dan kredibiliti."),
        ("Bolehkah warga asing memiliki 100% Sdn Bhd?", "Bergantung kepada aktiviti perniagaan dan sebarang garis panduan atau syarat pelesenan sektor. Kami menyemak rancangan anda dan menasihati struktur sebelum anda memfailkan."),
        ("Adakah saya perlukan setiausaha syarikat sebelum mendaftar?", "Setiausaha syarikat mesti dilantik dalam tempoh 30 hari selepas pemerbadanan. Kami melantik setiausaha anda sebagai sebahagian daripada pakej pendaftaran."),
        ("Bolehkah anda mendaftar LLP atau cawangan asing juga?", "Ya. Kami menguruskan pendaftaran Sdn Bhd, LLP dan syarikat asing serta pematuhan berterusan selepas itu."),
    ],
})

PAGES.append({
    "path": "perkhidmatan/tukar-setiausaha-syarikat/", "en_path": "services/switch-company-secretary/",
    "crumb": "Tukar setiausaha syarikat", "eyebrow": "Pertukaran setiausaha syarikat",
    "title": "Tukar Setiausaha Syarikat di Malaysia | Beralih ke CCM",
    "desc": "Tidak berpuas hati dengan setiausaha syarikat atau tertunggak penyerahan SSM? Kami uruskan serahan rekod, selesaikan penyata lewat dan pastikan anda patuh.",
    "h1": "Tukar setiausaha syarikat di Malaysia — tanpa tekanan",
    "lead": "Penyata tertunggak memang berlaku. Kami kumpulkan rekod anda daripada firma terdahulu, selesaikan yang tertunggak dan pastikan semuanya mengikut jadual selepas itu.",
    "box_title": "Cara kami permudahkan", "box": ["Kami meminta rekod daripada firma semasa anda", "Semakan pematuhan status SSM & LHDN",
                                                "Penyerahan tertunggak diselesaikan", "Borang pelantikan & peletakan jawatan diuruskan",
                                                "Pakej berterusan yang sesuai dengan anda"],
    "faq_h": "Soalan tentang pertukaran",
    "body": """
<h2>Bilakah anda patut menukar setiausaha syarikat?</h2>
<p>Perniagaan bertukar atas sebab praktikal: penyerahan lewat, tiada siapa menjawab mesej, yuran sentiasa berubah, atau firma hanya menguruskan satu bahagian pematuhan manakala perakaunan dan cukai dengan pihak lain. Jika mana-mana ini kedengaran biasa, menukar setiausaha syarikat lebih mudah daripada yang dijangka kebanyakan pemilik.</p>
<h2>Cara pertukaran berfungsi</h2>
<ol>
<li><strong>Semakan percuma</strong> — kami menyemak status syarikat anda dengan SSM dan LHDN dan menyenaraikan apa-apa yang tertunggak.</li>
<li><strong>Pelantikan</strong> — lembaga pengarah melantik kami sebagai setiausaha syarikat; kami menyediakan resolusi dan borang SSM.</li>
<li><strong>Serahan rekod</strong> — kami meminta daftar berkanun, buku minit dan penyerahan daripada setiausaha terdahulu supaya anda tidak perlu mengejarnya.</li>
<li><strong>Mengejar ketinggalan</strong> — kami menyelesaikan penyata tahunan dan pemfailan penyata kewangan yang lewat.</li>
<li><strong>Pematuhan berterusan</strong> — seorang wakil yang dikenali menjejak setiap tarikh akhir mulai saat ini.</li>
</ol>
<div class="callout"><strong>Sudah menerima notis kompaun?</strong> Hubungi kami sebelum yang seterusnya tiba. Kami akan menerangkan kedudukan anda dan apa yang diperlukan untuk kembali ke landasan.</div>
<h2>Semak kedudukan anda dahulu</h2>
<p>Cuba <a href="../../#health">semakan pematuhan 60 saat</a> kami untuk melihat penyerahan mana yang mungkin berisiko, atau baca panduan <a href="../../panduan/kalendar-pematuhan-sdn-bhd-malaysia/">kalendar pematuhan Sdn Bhd</a>.</p>
<h2>Satukan perakaunan, audit dan cukai di bawah satu bumbung</h2>
<p>Ramai pelanggan yang bertukar turut memindahkan <a href="../perakaunan-simpan-kira/">perakaunan</a>, <a href="../audit/">audit</a> dan <a href="../ejen-cukai/">cukai</a> mereka kepada kami, kerana satu pasukan yang memantau setiap tarikh akhir SSM dan LHDN bermakna tiada yang terlepas antara dua firma.</p>
""",
    "faqs": [
        ("Adakah setiausaha syarikat semasa saya akan bekerjasama dalam serahan?", "Biasanya ya. Kami menghantar permintaan dan menyusulinya untuk anda, dan kami tahu rekod apa yang SSM wajibkan diserahkan."),
        ("Adakah akan ada jurang dalam pematuhan semasa saya bertukar?", "Tidak. Kami mencatat tarikh akhir anda yang akan datang semasa semakan supaya tiada yang terlepas."),
        ("Bolehkah anda membaiki penyata tahunan dan akaun yang tertunggak?", "Ya. Kami menyelesaikan pemfailan lewat dan membantu anda memahami sebarang kompaun yang mungkin terpakai."),
        ("Adakah saya perlu memindahkan perakaunan saya juga?", "Tidak. Anda boleh menukar setiausaha syarikat sahaja dan menambah perakaunan, audit atau cukai kemudian."),
    ],
})

# ============================================================ GUIDES
GUIDES = []

GUIDES.append({
    "path": "panduan/syarat-setiausaha-syarikat-malaysia/", "en_path": "guides/company-secretary-requirements-malaysia/",
    "short": "Syarat setiausaha syarikat", "tag": "Setiausaha syarikat", "published": "2026-09-30", "updated_human": "30 September 2026",
    "title": "Syarat Setiausaha Syarikat di Malaysia (Panduan 2026)",
    "desc": "Siapa perlu ada setiausaha syarikat di Malaysia, siapa layak, bila melantik dan apa berlaku jika tidak. Panduan mudah untuk pemilik Sdn Bhd.",
    "h1": "Syarat setiausaha syarikat di Malaysia: panduan untuk pemilik Sdn Bhd",
    "lead": "Setiap syarikat Malaysia memerlukan setiausaha syarikat. Berikut siapa yang layak, bila anda mesti melantik dan apa peranannya.",
    "excerpt": "Siapa perlu ada setiausaha syarikat, siapa boleh bertindak sebagai setiausaha, bila melantik dan apa peranannya.",
    "faqs": [("Bolehkah pengarah menjadi setiausaha syarikat?", "Ya, pengarah juga boleh menjadi setiausaha syarikat jika memenuhi syarat kelayakan dalam Akta Syarikat 2016. Ramai pemilik memilih setiausaha luar sebaliknya."),
             ("Bolehkah warga asing menjadi setiausaha syarikat di Malaysia?", "Setiausaha mestilah individu yang lazimnya bermastautin di Malaysia dan layak di bawah Akta, jadi bukan pemastautin tidak boleh bertindak.")],
    "body": """
<h2>Adakah setiausaha syarikat wajib di Malaysia?</h2>
<p>Ya. Di bawah Akta Syarikat 2016, setiap syarikat yang diperbadankan di Malaysia — Sdn Bhd, syarikat awam atau syarikat berhad menurut jaminan — mesti mempunyai sekurang-kurangnya seorang setiausaha syarikat. Setiausaha pertama mesti dilantik dalam tempoh <strong>30 hari selepas pemerbadanan</strong>. Jika setiausaha berhenti, syarikat mesti mengisi kekosongan dalam tempoh yang ditetapkan oleh Akta.</p>
<h2>Siapa yang boleh menjadi setiausaha syarikat?</h2>
<p>Setiausaha mestilah individu yang lazimnya bermastautin di Malaysia dan salah seorang daripada yang berikut:</p>
<ul>
<li>Ahli badan profesional yang ditetapkan, seperti Institut Akauntan Malaysia atau Majlis Peguam Malaysia;</li>
<li>Seseorang yang dilesenkan oleh SSM sebagai setiausaha syarikat; atau</li>
<li>Orang lain yang diluluskan oleh SSM.</li>
</ul>
<p>Secara praktikal, kebanyakan PKS melantik setiausaha syarikat berlesen daripada firma luar, kerana kerja pemfailan memerlukan kepakaran dan berterusan.</p>
<h2>Apakah sebenarnya tugas setiausaha syarikat?</h2>
<ul>
<li>Memfailkan <strong>penyata tahunan</strong> dan penyata kewangan anda dengan SSM tepat pada masanya;</li>
<li>Menyediakan dan menyimpan minit mesyuarat lembaga dan mesyuarat agung;</li>
<li>Menyelenggara <strong>daftar berkanun</strong> (pengarah, ahli, caj);</li>
<li>Memfailkan notis perubahan — pengarah, pindahan saham, alamat berdaftar;</li>
<li>Menasihati pengarah tentang tugas berkanun dan pematuhan undang-undang syarikat.</li>
</ul>
<h2>Bagaimana jika tidak melantik?</h2>
<p>Gagal mempunyai setiausaha syarikat ialah kesalahan di bawah Akta dan boleh mengakibatkan kompaun atau penalti kepada syarikat dan pegawainya, malah menyukarkan setiap penyerahan lain. Jika syarikat anda sudah terlepas tempoh 30 hari, lantik setiausaha berlesen sekarang dan minta mereka menyemak penyerahan yang tertunggak.</p>
<p>Bersedia untuk melantik? Lihat <a href="../../perkhidmatan/setiausaha-syarikat/">perkhidmatan setiausaha syarikat</a> kami atau <a href="../../perkhidmatan/tukar-setiausaha-syarikat/">cara menukar setiausaha syarikat</a>.</p>
""",
})

GUIDES.append({
    "path": "panduan/kalendar-pematuhan-sdn-bhd-malaysia/", "en_path": "guides/sdn-bhd-compliance-calendar-malaysia/",
    "short": "Kalendar pematuhan Sdn Bhd", "tag": "Tarikh akhir SSM & LHDN", "published": "2026-09-30", "updated_human": "30 September 2026",
    "title": "Kalendar Pematuhan Sdn Bhd Malaysia: Tarikh Akhir SSM & LHDN",
    "desc": "Penyata tahunan, akaun beraudit, Borang C dan CP204 — tarikh akhir SSM dan LHDN yang perlu dipatuhi setiap Sdn Bhd Malaysia, dengan contoh.",
    "h1": "Kalendar pematuhan Sdn Bhd: tarikh akhir SSM dan LHDN di Malaysia",
    "lead": "Penyerahan yang mesti dibuat setiap syarikat persendirian Malaysia setiap tahun, kepada siapa dan bila ia perlu dibuat.",
    "excerpt": "Penyata tahunan, akaun beraudit, Borang C dan CP204 — tarikh akhir tahunan, dengan contoh.",
    "faqs": [("Apa berlaku jika saya terlepas tarikh akhir SSM atau LHDN?", "SSM dan LHDN boleh mengenakan kompaun dan penalti ke atas syarikat dan pegawainya. Semakin lama sesuatu penyerahan tertunggak, semakin tinggi kosnya untuk diselesaikan."),
             ("Adakah syarikat dorman masih mempunyai tarikh akhir?", "Ya. Syarikat dorman masih mesti memfailkan penyata tahunan dan menyerahkan borang nyata cukai, dan mungkin juga perlu menyediakan penyata kewangan.")],
    "body": """
<p>Terlepas tarikh akhir pematuhan ialah kos yang paling biasa — dan paling boleh dielakkan — bagi PKS Malaysia. Gunakan kalendar ini, atau <a href="../../#planner">perancang tarikh akhir</a> interaktif kami, untuk melihat apa yang terpakai kepada syarikat anda.</p>
<h2>Penyerahan tahunan sepintas lalu</h2>
""" + tbl(["Penyerahan", "Kepada siapa", "Tarikh akhir"], [
        ["Penyata tahunan", "SSM", "Dalam 30 hari selepas ulang tahun pemerbadanan (s.68 Akta Syarikat 2016)"],
        ["Mengedarkan penyata kewangan beraudit kepada ahli", "Pemegang saham", "Dalam 6 bulan selepas akhir tahun kewangan (s.258)"],
        ["Memfailkan penyata kewangan", "SSM", "Dalam 30 hari selepas pengedaran (s.259)"],
        ["Borang C (borang nyata cukai pendapatan korporat)", "LHDN", "Dalam 7 bulan selepas akhir tahun kewangan"],
        ["Anggaran cukai CP204", "LHDN", "30 hari sebelum bermulanya setiap tempoh asas"],
        ["Ansuran CP204", "LHDN", "Setiap bulan"],
        ["Caruman KWSP, PERKESO & SIP", "KWSP / PERKESO", "Setiap bulan (mengikut tarikh akhir berkanun)"],
        ["Penyata SST (jika berdaftar)", "Jabatan Kastam Diraja Malaysia", "Mengikut tempoh cukai"]]) + """
<h2>Contoh: diperbadankan 15 Mac, akhir tahun 31 Disember</h2>
""" + tbl(["Tarikh", "Apa yang perlu dibuat"], [
        ["15 Mac + 30 hari (14 April)", "Penyata tahunan kepada SSM"],
        ["30 Jun", "Edarkan akaun beraudit (6 bulan selepas 31 Disember)"],
        ["30 Julai", "Failkan akaun dengan SSM (30 hari selepas pengedaran)"],
        ["31 Julai", "Borang C kepada LHDN (7 bulan selepas 31 Disember)"],
        ["2 Disember", "Anggaran CP204 untuk tempoh asas seterusnya (30 hari sebelum 1 Januari)"]]) + """
<div class="callout"><strong>Petua:</strong> audit ialah penghalang utama. Jika buku anda lewat siap, setiap tarikh selepasnya akan terhimpit. <a href="../../perkhidmatan/perakaunan-simpan-kira/">Simpan kira</a> bulanan ialah cara paling mudah untuk memastikan seluruh kalendar kekal terkawal.</div>
<h2>Cara kekal di atas semuanya</h2>
<ul>
<li>Tetapkan akhir tahun kewangan anda dan rancang jadual audit ke belakang daripada tarikh akhir di atas.</li>
<li>Gunakan setiausaha syarikat yang menjejak tarikh SSM untuk anda — lihat <a href="../../perkhidmatan/setiausaha-syarikat/">perkhidmatan setiausaha syarikat</a> kami.</li>
<li>Minta <a href="../../perkhidmatan/ejen-cukai/">ejen cukai</a> anda menyemak anggaran CP204 berbanding keputusan sebenar tahun itu.</li>
</ul>
<p class="meta">Tarikh adalah petunjuk berdasarkan Akta Syarikat 2016 dan peraturan LHDN. Tarikh sebenar bergantung kepada keadaan syarikat anda dan sebarang lanjutan yang diumumkan pihak berkuasa.</p>
""",
})

GUIDES.append({
    "path": "panduan/adakah-sdn-bhd-perlu-diaudit/", "en_path": "guides/do-sdn-bhd-need-audit-malaysia/",
    "short": "Adakah Sdn Bhd perlu diaudit?", "tag": "Audit", "published": "2026-09-30", "updated_human": "30 September 2026",
    "title": "Adakah Sdn Bhd Perlu Diaudit? Pengecualian di Malaysia",
    "desc": "Kebanyakan syarikat persendirian Malaysia mesti diaudit. Ketahui siapa boleh dikecualikan (syarikat dorman dan yang layak ambang) dan apa yang perlu dibuat.",
    "h1": "Adakah Sdn Bhd saya perlu diaudit? Pengecualian di Malaysia diterangkan",
    "lead": "Kebanyakan syarikat persendirian mesti mengaudit akaun setiap tahun — tetapi sebahagian dikecualikan. Begini cara mengetahui anda termasuk yang mana.",
    "excerpt": "Kebanyakan syarikat persendirian perlu diaudit setiap tahun. Ketahui siapa dikecualikan dan apa yang perlu disemak dahulu.",
    "faqs": [("Adakah audit diperlukan jika syarikat saya tiada hasil?", "Syarikat tiada hasil atau dorman mungkin layak dikecualikan di bawah Akta Syarikat 2016, tertakluk kepada syarat. Semak sebelum anda memutuskan untuk tidak mengaudit."),
             ("Siapa yang menandatangani akaun beraudit?", "Juruaudit syarikat berlesen menandatangani laporan juruaudit, dan pengarah meluluskan serta menandatangani penyata kewangan.")],
    "body": """
<h2>Peraturan lalai: audit setiap tahun</h2>
<p>Di bawah Akta Syarikat 2016, penyata kewangan syarikat mesti diaudit oleh juruaudit syarikat berlesen sebelum diedarkan kepada ahli dan difailkan dengan SSM. Ini terpakai kepada kebanyakan Sdn Bhd, tanpa mengira saiz.</p>
<h2>Siapa yang boleh dikecualikan daripada audit?</h2>
<p>Akta membenarkan pengecualian bagi syarikat tertentu. Dua kumpulan yang paling relevan kepada PKS ialah:</p>
<ul>
<li><strong>Syarikat dorman</strong> — syarikat yang tidak menjalankan perniagaan dan tiada transaksi perakaunan yang ketara.</li>
<li><strong>Syarikat persendirian yang layak ambang</strong> — syarikat persendirian kecil yang memenuhi ambang berkanun bagi hasil dan kriteria lain yang ditetapkan dalam Akta dan peraturannya.</li>
</ul>
<p>Pengecualian tidak automatik, dan syarat boleh hilang apabila keadaan berubah. Syarikat yang layak satu tahun mungkin tidak layak pada tahun berikutnya.</p>
<h2>Walaupun dikecualikan, anda masih mempunyai tugas</h2>
<ul>
<li>Anda masih memerlukan <strong>rekod perakaunan</strong> yang betul dan penyata kewangan yang diluluskan pengarah.</li>
<li>Anda masih mesti memfailkan <strong>penyata tahunan</strong> dan, jika diperlukan, penyata kewangan dengan SSM.</li>
<li>Anda masih mesti menyerahkan <strong>Borang C</strong> kepada LHDN dalam tempoh tujuh bulan selepas akhir tahun.</li>
<li>Bank, pelabur dan tender mungkin masih meminta akaun beraudit.</li>
</ul>
<h2>Cara membuat keputusan</h2>
<ol>
<li>Sahkan sama ada syarikat dorman atau aktif berniaga.</li>
<li>Semak hasil dan syarat ambang lain bagi tahun kewangan itu.</li>
<li>Pertimbangkan sama ada pemberi pinjaman, pelabur atau pelanggan akan menginginkan angka beraudit juga.</li>
<li>Rekodkan keputusan dalam rekod pengarah anda.</li>
</ol>
<p>Kami menyemak kelayakan secara percuma sebelum mengesyorkan audit. Ketahui lebih lanjut tentang <a href="../../perkhidmatan/audit/">perkhidmatan audit dan jaminan</a> kami, atau semak <a href="../kalendar-pematuhan-sdn-bhd-malaysia/">kalendar pematuhan</a> penuh anda.</p>
""",
})

# ============================================================ PRIVACY
PRIVACY_UPDATED = "30 September 2026"
PRIVACY_PATH = "dasar-privasi/"
PRIVACY_HTML = """
<p>CCM Secretarial (Corporate Consultant &amp; Management) (“<strong>CCM</strong>”, “kami”) menghormati privasi anda. Dasar ini menerangkan bagaimana kami mengumpul, menggunakan dan melindungi data peribadi apabila anda melayari laman web ini atau menghubungi kami, selaras dengan Akta Perlindungan Data Peribadi 2010 Malaysia (“PDPA”).</p>
<h2>1. Siapa kami</h2>
<p>CCM Secretarial, 1, Jalan Elmina Ilham 18, Seksyen U16, Elmina, Shah Alam, Selangor, Malaysia. Telefon: 016-477 9365. E-mel: <a href="mailto:corpsec@ccmsecretarial.com">corpsec@ccmsecretarial.com</a>.</p>
<h2>2. Data peribadi yang kami kumpul</h2>
<ul>
<li><strong>Maklumat yang anda berikan</strong> — nama, nombor telefon, alamat e-mel, nama syarikat, perkhidmatan yang anda minati dan sebarang mesej yang anda hantar melalui borang pertanyaan, WhatsApp, e-mel atau telefon.</li>
<li><strong>Maklumat yang diperlukan untuk perkhidmatan kami</strong> — jika anda menjadi pelanggan, kami turut mengumpul maklumat pengenalan, syarikat dan kewangan yang diperlukan untuk menyediakan perkhidmatan setiausaha syarikat, perakaunan, audit dan cukai.</li>
<li><strong>Maklumat teknikal</strong> — data teknikal asas seperti jenis pelayar dan halaman yang dilawati, jika alat analitik diaktifkan pada laman web ini.</li>
</ul>
<h2>3. Cara kami menggunakan data anda</h2>
<ul>
<li>Untuk membalas pertanyaan anda dan memberi sebut harga;</li>
<li>Untuk menyediakan dan mentadbir perkhidmatan kami serta memenuhi obligasi profesional dan undang-undang kami, termasuk penyerahan kepada SSM dan LHDN;</li>
<li>Untuk menghantar peringatan dan makluman pematuhan yang relevan kepada syarikat anda;</li>
<li>Untuk menambah baik laman web dan perkhidmatan kami.</li>
</ul>
<h2>4. Pendedahan</h2>
<p>Kami tidak menjual data peribadi anda. Kami mungkin mendedahkannya kepada badan kerajaan dan kawal selia (seperti SSM dan LHDN) apabila diperlukan untuk menyediakan perkhidmatan kami, kepada pembekal perkhidmatan yang membantu menjalankan perniagaan kami (contohnya pembekal pemesejan, e-mel dan IT) di bawah obligasi kerahsiaan, dan apabila undang-undang mewajibkannya.</p>
<h2>5. WhatsApp dan e-mel</h2>
<p>Jika anda menghubungi kami melalui WhatsApp atau e-mel, mesej anda dikendalikan pada platform tersebut yang mempunyai dasar privasi sendiri. Sila elakkan menghantar maklumat sensitif, seperti nombor kad pengenalan penuh atau butiran bank, sehingga kita bersetuju tentang cara selamat untuk bertukar dokumen.</p>
<h2>6. Keselamatan dan penyimpanan</h2>
<p>Kami mengambil langkah munasabah untuk melindungi data peribadi daripada kehilangan, penyalahgunaan dan akses tanpa kebenaran. Kami menyimpan data hanya selama diperlukan bagi tujuan di atas dan untuk memenuhi keperluan penyimpanan rekod undang-undang, cukai dan profesional.</p>
<h2>7. Hak anda</h2>
<p>Di bawah PDPA anda boleh meminta akses kepada, atau pembetulan, data peribadi anda, dan anda boleh menarik balik persetujuan untuk penggunaan tertentu. Untuk berbuat demikian, e-mel <a href="mailto:corpsec@ccmsecretarial.com">corpsec@ccmsecretarial.com</a>. Kami mungkin perlu mengesahkan identiti anda terlebih dahulu.</p>
<h2>8. Kuki dan analitik</h2>
<p>Laman web ini pada masa ini tidak menggunakan kuki pengiklanan. Jika kami menambah analitik pada masa hadapan, kami akan mengemas kini dasar ini dan, jika dikehendaki, meminta persetujuan anda.</p>
<h2>9. Perubahan kepada dasar ini</h2>
<p>Kami mungkin mengemas kini dasar ini dari semasa ke semasa. Tarikh di bahagian atas menunjukkan bila ia terakhir disemak.</p>
<h2>10. Hubungi kami</h2>
<p>Ada soalan tentang dasar ini? E-mel <a href="mailto:corpsec@ccmsecretarial.com">corpsec@ccmsecretarial.com</a> atau telefon 016-477 9365.</p>
<p class="meta">Dasar ini ialah kenyataan umum dan perlu disemak oleh penasihat undang-undang CCM sebelum diterbitkan. Dalam sebarang percanggahan, versi Bahasa Inggeris terpakai.</p>
"""
