"""
Single source of truth for Ekdanta's real mandal dataset (from Advi's
'Ganpati 2026' research sheet). Used by:
  - generate_mandal_docs.py  -> builds RAG-ingestible text documents
  - app/api/mandals.py       -> serves structured JSON for map/list UI

Fields left "TO UPDATE" / "TO CONFIRM" mirror the source sheet honestly;
the app should surface them as unconfirmed rather than invent a value.
"""

MANDALS = [
    dict(
        doc_id="kasba_ganpati", name_en="Kasba Ganpati", name_mr="कसबा गणपती",
        manacha="1 (Pehila Manacha)", area="Kasba Peth, Pune", year="1639",
        category="manache_ganpati",
        history=(
            "Kasba Ganpati is the Gramdevata (presiding deity) of Pune and holds the most revered "
            "position among all Ganesh mandals in the city. The idol was found near the home of "
            "Vinayak Thakar, close to where Jijabai (mother of Chhatrapati Shivaji Maharaj) resided; "
            "on her orders the temple was built in 1639. Shivaji Maharaj is said to have sought this "
            "Ganpati's blessings before every campaign. The idol is swayambhu (self-originated), "
            "originally rice-grain sized, grown over centuries from devotees' red sandalwood paste. "
            "Lokmanya Tilak declared it Pune's Gramdevata and gave it the first Manacha position when "
            "public Ganeshotsav began in 1893. Visarjan of all other mandals begins only after Kasba "
            "Ganpati's immersion."
        ),
        idol="Swayambhu idol, originally rice-grain sized, grown over centuries via sandalwood paste offerings; simple Peshwa-style temple.",
        address="Kasba Peth, Pune 411011 (near Shaniwar Wada & Lal Mahal)",
        pandal_address="TO UPDATE — announced by mandal closer to festival (Aug 2026)",
        maps_link="TO UPDATE — check Kasba Ganpati Mandal Facebook/Instagram in August 2026",
        lat=18.51889, lng=73.85694,
        morning_aarti="Mangala Aarti: 5:45 AM", evening_aarti="Sayan Aarti: 9:00 PM",
        events="Grand Visarjan procession led by Mayor & Commissioner; Mhapurush Darshan on Day 1",
        notes="Confirm exact pandal location and aarti times for 2026 festival season",
    ),
    dict(
        doc_id="tambdi_jogeshwari", name_en="Tambdi Jogeshwari", name_mr="तांबडी जोगेश्वरी",
        manacha="2 (Dusra Manacha)", area="Budhwar Peth, Pune",
        year="1893 (Ganeshotsav); Temple 15th century", category="manache_ganpati",
        history=(
            "Tambdi Jogeshwari is primarily a temple of Goddess Jogeshwari, Pune's Gramdevi, distinct "
            "from Kasba Ganpati (Gramdevata); the Durga temple dates to the 15th century, one of Pune's "
            "oldest religious sites. Ganesh Chaturthi celebrations began here in 1893 when Bhau Bhendre "
            "introduced the idol, and Tilak gave it the second Manacha honour. Uniquely among the "
            "Manache 5, the idol is immersed and a new one installed every year. Since 2000 it has stood "
            "in a striking silver-dome pandal outside the temple, now an iconic Pune Ganeshotsav sight."
        ),
        idol="New idol installed every year — no permanent murti. Silver dome pandal (since 2000) is the visual centrepiece.",
        address="33A, Budhwar Peth Road, Budhwar Peth, Pune 411002 (near Appa Balwant Chowk)",
        pandal_address="TO UPDATE — silver dome outside the temple; confirm location for 2026",
        maps_link="TO UPDATE — check mandal's official pages in August 2026",
        lat=18.5175, lng=73.8562,
        morning_aarti="Mangala Aarti: 6:00 AM", evening_aarti="Sayan Aarti: 7:00 PM",
        events="Eco-friendly themes in recent years; traditional fervour rituals; rich cultural programs",
        notes="Confirm 2026 pandal location and silver dome setup date",
    ),
    dict(
        doc_id="guruji_talim", name_en="Guruji Talim Ganpati", name_mr="गुरुजी तालीम गणपती",
        manacha="3 (Tisra Manacha)", area="Laxmi Road, Budhwar Peth, Pune", year="1887",
        category="manache_ganpati",
        history=(
            "Guruji Talim Ganpati was established in 1887 — six years before Tilak's 1893 Sarvajanik "
            "Ganeshotsav — making it one of Pune's very first public Ganesh mandals. It was founded "
            "jointly by Ustad Nalban (Muslim) and Bhiku Shinde (Hindu); this Hindu-Muslim partnership "
            "made the mandal a powerful symbol of communal harmony. It is also credited with originating "
            "the dhol-tasha procession tradition, now inseparable from Ganeshotsav across Maharashtra. "
            "Located near Alka Talkies on Laxmi Road, it holds the third Manacha position."
        ),
        idol="No single permanent idol feature — celebrated for community spirit and secular roots; dhol-tasha performances are its most iconic aspect.",
        address="184, Laxmi Road, near Alka Talkies, Tulshibaug, Budhwar Peth, Pune 411002",
        pandal_address="TO UPDATE — confirm 2026 pandal location via mandal's social media",
        maps_link="TO UPDATE — check Guruji Talim Mandal pages in August 2026",
        lat=18.5163, lng=73.8558,
        morning_aarti="Mangala Aarti: 7:30 AM", evening_aarti="Sayan Aarti: 7:30 PM",
        events="Cultural events from 6 PM daily; space-themed decorations (2025); dhol-tasha competitions",
        notes="Verify founding family names; confirm 2026 pandal address",
    ),
    dict(
        doc_id="tulshibaug_ganpati", name_en="Tulshibaug Ganpati", name_mr="तुळशीबाग गणपती",
        manacha="4 (Chautha Manacha)", area="Tulshibaug, Budhwar Peth, Pune", year="1901",
        category="manache_ganpati",
        history=(
            "Tulshibaug Ganpati, established in 1901, is the fourth Manacha and sits in the heart of the "
            "historic Tulshibaug market. In 1975 it became the first mandal in Pune to use a fibreglass "
            "idol; the current idol is 13 feet tall, adorned with over 80 kg of silver ornaments. Evening "
            "aartis draw enormous crowds, and the narrow Tulshibaug lanes packed with devotees are one of "
            "the most memorable sights of Pune's Ganeshotsav."
        ),
        idol="13-feet tall fibreglass idol (first of its kind in Pune, 1975), adorned with 80+ kg of silver ornaments.",
        address="103, Tulshibaug Internal Road, near Jilbya Maruti Mandal, Tulshibaug, Budhwar Peth, Pune 411002",
        pandal_address="TO UPDATE — confirm 2026 pandal location",
        maps_link="TO UPDATE — check mandal pages in August 2026",
        lat=18.5158, lng=73.8553,
        morning_aarti="6:00 AM", evening_aarti="Aarti: 6:00 PM – 9:00 PM",
        events="Intricate flower arrangement decorations; traditional aarti every evening; cultural programs",
        notes="Confirm exact pandal location and 2026 aarti timings with mandal",
    ),
    dict(
        doc_id="kesariwada_ganpati", name_en="Kesariwada Ganpati", name_mr="केसरीवाडा गणपती",
        manacha="5 (Panchva Manacha)", area="Narayan Peth, Pune",
        year="1893 (1894 per some sources)", category="manache_ganpati",
        history=(
            "Kesariwada Ganpati is the Ganpati Lokmanya Tilak himself installed in 1893 inside "
            "Kesariwada, his personal residence — the very place from which he launched Sarvajanik "
            "Ganeshotsav, turning a household ritual into a mass movement against British rule. The "
            "Kesari newspaper, Tilak's Marathi journal for the freedom movement, was also published from "
            "here. A Tilak museum inside the Wada displays the historic palanquin used in the mandal's "
            "procession, and a statue of Tilak stands behind the Ganpati idol."
        ),
        idol="Idol housed within the historic Kesariwada; a Tilak statue stands behind it; simple murti, profound historical weight.",
        address="Kesariwada, 619, RB Kumthekar Road, Narayan Peth, Pune 411030",
        pandal_address="TO UPDATE — confirm 2026 pandal address via mandal",
        maps_link="TO UPDATE — check Kesari Trust social media in August 2026",
        lat=18.5135, lng=73.853,
        morning_aarti="6:00 AM", evening_aarti="7:00 PM",
        events="Tilak Museum open to visitors; freedom movement heritage walk; traditional procession with historic palanquin",
        notes="Confirm 2026 pandal address; museum visiting hours during festival",
    ),
    dict(
        doc_id="dagdusheth_halwai", name_en="Dagdusheth Halwai Ganpati", name_mr="दगडूशेठ हलवाई गणपती",
        manacha="Not Manacha — Most Famous", area="Budhwar Peth, Pune", year="1893",
        category="famous_temple",
        history=(
            "Dagdusheth Halwai Ganpati is arguably Maharashtra's most famous Ganesh temple. It was "
            "founded in 1893 by sweet merchant Shreemant Dagdusheth Halwai and his wife Lakshmibai after "
            "losing their son to plague. The temple trust is among India's richest religious trusts, "
            "funding an old-age home, orphanage, ambulance services, tribal health clinics, and "
            "cooperative banks. The 7.5-feet idol, commissioned in 1968 for the temple's 75th "
            "anniversary and crafted by Shree Shankar Appa Shilpi, is adorned with roughly 8 kg of gold "
            "and gems under a gold-plated dome. Over 1.5 million devotees visit during Ganeshotsav; "
            "witnessing this devotion is said to have inspired Tilak to launch Sarvajanik Ganeshotsav."
        ),
        idol="7.5-feet idol (1968) with ~8 kg gold and precious gems; gold-plated dome; silver doors depicting Ganesh's life; known as Navasacha Ganpati (wish-fulfilling).",
        address="Ganpati Bhavan, 250, Budhwar Peth, Pune 411002",
        pandal_address="Same as mandir — permanent pandal setup at the temple premises",
        maps_link="https://goo.gl/maps/dagdusheth",
        lat=18.5167, lng=73.8553,
        morning_aarti="Suprabhatam Aarti: 7:30 AM | Madhyan Aarti: 3:00 PM",
        evening_aarti="Mahamangal Aarti: 8:00 PM | Shejarti: 10:30 PM",
        events="Atharvashirsha recital (Day 4) with thousands of women chanting together; daily Abhishek 8 AM–3 PM; open 24/7 during festival",
        notes="Must-visit; confirm Atharvashirsha event date for 2026",
    ),
    dict(
        doc_id="sarasbaug_siddhivinayak", name_en="Sarasbaug Siddhivinayak (Talyatla Ganpati)",
        name_mr="सारसबाग सिद्धिविनायक (तळ्यातला गणपती)", manacha="Not Manacha",
        area="Sarasbaug, Pune", year="18th century (Peshwa era)", category="famous_temple",
        history=(
            "Sarasbaug Ganpati, also called Talyatla Ganpati ('Ganpati of the lake'), was built during "
            "the Peshwa era and houses Shree Siddhivinayak, the wish-fulfilling form of Ganesha. Set "
            "within the 25-acre Sarasbaug complex — originally an artificial lake — the temple sees over "
            "10,000 devotees on an average day, rising to 80,000 on Ganesh Chaturthi. It is a peaceful, "
            "scenic alternative to Dagdusheth for a quieter morning darshan, administered by the Peshwa "
            "Trust."
        ),
        idol="Traditional Siddhivinayak idol within a garden setting — peaceful, less crowded than the peth mandals.",
        address="Sarasbaug, Near Swargate, Pune 411037",
        pandal_address="Permanent temple — darshan at the temple itself",
        maps_link="https://goo.gl/maps/sarasbaug",
        lat=18.5009, lng=73.853,
        morning_aarti="6:00 AM", evening_aarti="8:00 PM",
        events="Special aarti during Ganesh Chaturthi; garden illuminated during festival; relatively peaceful compared to peth mandals",
        notes="Confirm 2026 timings; good to mention as quieter darshan option in app",
    ),
    dict(
        doc_id="tambat_ali_bhausaheb_rangari", name_en="Tambat Ali Ganpati (Bhausaheb Rangari Ganpati)",
        name_mr="तांबट आळी गणपती (भाऊसाहेब रंगारी गणपती)", manacha="Not Manacha",
        area="Budhwar Peth, Pune", year="1892", category="heritage",
        history=(
            "Tambat Ali Ganpati, officially Shrimant Bhausaheb Rangari Ganpati, was founded in 1892 by "
            "Bhausaheb Rangari, a close friend of Tilak — predating even the formal 1893 launch of "
            "Sarvajanik Ganeshotsav. Rangari's example inspired Tilak to take the festival to the "
            "masses, making this mandal the historical seed of the entire public Ganeshotsav tradition. "
            "Located in the historic Tambat Ali (coppersmiths' lane), it is known for simple, traditional "
            "devotion without grandeur."
        ),
        idol="Traditional simple murti — celebrated for purity of devotion rather than grandeur; located in the atmospheric Tambat Ali lane.",
        address="662-657, Bhau Rangari Road, Budhwar Peth, Pune 411002",
        pandal_address="TO UPDATE — confirm 2026 pandal",
        maps_link="TO UPDATE — August 2026",
        lat=18.5172, lng=73.856,
        morning_aarti="TO CONFIRM", evening_aarti="TO CONFIRM",
        events="Heritage walk through Tambat Ali; traditional copper craft demonstrations nearby",
        notes="Important historical mandal — add a 'Did you know?' fact card in the app",
    ),
    dict(
        doc_id="parvati_hill_ganpati", name_en="Parvati Devachi Ganpati (Parvati Hill Ganpati)",
        name_mr="पार्वती देवाची गणपती", manacha="Heritage Temple (Peshwa era)",
        area="Parvati Hill, Pune", year="18th century (Peshwa era)", category="heritage",
        history=(
            "The Parvati Hill temple complex, built by Peshwa Balaji Baji Rao (Nana Saheb) in the 18th "
            "century, sits atop a hillock 2,100 feet above sea level and includes temples of Parvati, "
            "Devdeveshwar, Vishnu, Kartikeya, and a Ganesh shrine. Devotees climb 103 steps for a "
            "360-degree panoramic view of Pune, including Shaniwar Wada, Sinhagad Fort and Pune "
            "University. A small pre-Peshwa Buddhist cave lies halfway up the hill."
        ),
        idol="Traditional Ganesh idol within the Parvati temple complex; the hilltop setting with sweeping views is the draw.",
        address="Parvati Hill, Parvati Gaon, Pune 411009 (103 steps from base)",
        pandal_address="TO UPDATE — darshan at the permanent temple; confirm any special pandal for 2026",
        maps_link="TO UPDATE — August 2026",
        lat=18.4972, lng=73.8467,
        morning_aarti="6:00 AM", evening_aarti="8:00 PM",
        events="Sunrise darshan on Chaturthi morning draws huge crowds; photography spots for city views",
        notes="Confirm if separate pandal set up outside temple during festival or just temple darshan",
    ),
    dict(
        doc_id="dashabhuja_ganapati", name_en="Dashabhuja Ganapati", name_mr="दशभुज गणपती",
        manacha="Heritage Temple (Peshwa era)", area="Erandwane, Karve Road, Pune",
        year="Peshwa era (pre-1818)", category="heritage",
        history=(
            "Dashabhuja Ganapati on Karve Road is a Peshwa-era temple notable for a rare feature: the "
            "idol's trunk rests on the right side (Dakshinabhimukhi), considered far more sacred than the "
            "common left-trunk form. 'Dashabhuja' means ten-armed. The temple once belonged to Sardar "
            "Haripant Phadke, a senior Peshwa sardar, and was later given as dowry to the Peshwas — it is "
            "one of Pune's few right-trunk Ganesh temples."
        ),
        idol="Ten-armed idol with the rare right-trunk (Dakshinabhimukhi) position, found in very few Maharashtra temples.",
        address="Erandwane, Karve Road, Pune 411004 (near Paud Phata flyover)",
        pandal_address="TO UPDATE — confirm 2026 pandal address",
        maps_link="TO UPDATE — August 2026",
        lat=18.5058, lng=73.8258,
        morning_aarti="TO CONFIRM", evening_aarti="TO CONFIRM",
        events="Special significance on Chaturthi; right-trunk darshan considered very auspicious",
        notes="Right-trunk fact is a great 'Did you know?' card for the app",
    ),
    dict(
        doc_id="parvati_nandan_khinditla", name_en="Parvati Nandan Ganpati (Khinditla Ganpati)",
        name_mr="पार्वती नंदन गणपती (खिंडीतला गणपती)", manacha="Heritage Temple (17th century)",
        area="Ganeshkhind, near Pune University, Pune", year="17th century", category="heritage",
        history=(
            "Parvati Nandan Ganpati, also called Khinditla Ganpati ('Ganpati of the mountain pass'), is "
            "a 17th-century temple in Ganeshkhind near Savitribai Phule Pune University, historically at "
            "old Pune's northwestern boundary. It is believed Rajmata Jijabai restored the temple, with a "
            "further Peshwa-era restoration during which legend says a treasure was found in the "
            "temple's well. 'Parvati Nandan' means Son of Parvati, another name for Ganesha."
        ),
        idol="Ancient stone idol in a compact, traditional temple — one of Pune's oldest Ganesh shrines.",
        address="Ganeshkhind, Near Savitribai Phule Pune University, Senapati Bapat Road, Pune 411007",
        pandal_address="TO UPDATE — primarily temple darshan",
        maps_link="TO UPDATE — August 2026",
        lat=18.558, lng=73.814,
        morning_aarti="TO CONFIRM", evening_aarti="TO CONFIRM",
        events="Quiet, heritage darshan experience — ideal for history enthusiasts",
        notes="Great 'hidden gem' angle for the app — not known to most tourists",
    ),
    dict(
        doc_id="chhatrapati_rajaram_mandal", name_en="Chhatrapati Rajaram Mandal Ganpati",
        name_mr="छत्रपती राजाराम मंडळ गणपती", manacha="Iconic Sarvajanik Mandal",
        area="Sadashiv Peth, Pune", year="1890s (one of Pune's oldest mandals)", category="sarvajanik_mandal",
        history=(
            "Chhatrapati Rajaram Mandal, one of Pune's oldest Sarvajanik mandals, is famous for "
            "extraordinary pandal decorations — artisans recreate famous Indian temples or monuments as "
            "the pandal theme each year. Named for Chhatrapati Rajaram Maharaj, son of Chhatrapati "
            "Shivaji Maharaj, it has built a century-plus reputation for creative excellence, drawing "
            "photographers, artists and families."
        ),
        idol="Traditional idol set within a spectacular recreated temple/monument pandal — a different architectural marvel every year.",
        address="871, Sadashiv Peth Road, Perugate, Sadashiv Peth, Pune 411030",
        pandal_address="TO UPDATE — pandal location confirmed closer to festival",
        maps_link="TO UPDATE — August 2026",
        lat=18.513, lng=73.849,
        morning_aarti="TO CONFIRM", evening_aarti="TO CONFIRM",
        events="Pandal inauguration event; photography-friendly; cultural performances; social programs",
        notes="Add a 'Best for photographers' tag in the app",
    ),
    dict(
        doc_id="hutatma_babu_genu", name_en="Hutatma Babu Genu Ganpati (Navsacha Ganpati)",
        name_mr="हुतात्मा बाबू गेनू गणपती (नवसाचा गणपती)", manacha="Iconic Sarvajanik Mandal",
        area="Mandai, Budhwar Peth, Pune", year="1970", category="sarvajanik_mandal",
        history=(
            "Hutatma Babu Genu Ganesh Mandal was founded in 1970 by seven young men from Mandai, named "
            "for freedom fighter Babu Genu Said, a mill worker martyred in 1930 lying before a British "
            "truck carrying foreign cloth. Known as Pune's beloved Navsacha Ganpati (wish-fulfilling), it "
            "has a 'wish pond' where devotees toss coins and make wishes, and pandals recreating iconic "
            "monuments (including Cambodia's Baphuon Shiva Temple) alongside a gold/diamond/silver-adorned "
            "idol."
        ),
        idol="Gold, diamond and silver-adorned idol with a Puneri pagadi (traditional turban) — considered the most beautiful idol in Mandai.",
        address="Near Mandai, Martyr Babu Genu Chowk, Budhwar Peth, Pune 411002",
        pandal_address="TO UPDATE — confirm 2026 pandal",
        maps_link="TO UPDATE — August 2026",
        lat=18.5168, lng=73.8558,
        morning_aarti="TO CONFIRM", evening_aarti="TO CONFIRM",
        events="Wish pond (navsachi vihir) open throughout; replica monument pandal; Babu Genu anniversary observed",
        notes="Add 'Navsacha Ganpati' as a badge/tag in the app",
    ),
    dict(
        doc_id="akhil_mandai_sharda", name_en="Akhil Mandai Mandal Ganpati (Sharda Ganpati)",
        name_mr="अखिल मंडई मंडळ गणपती (शारदा गणपती)", manacha="Iconic Sarvajanik Mandal",
        area="Mandai, Budhwar Peth, Pune", year="Early 20th century", category="sarvajanik_mandal",
        history=(
            "Akhil Mandai Mandal is known for two things: the stunning Sharda Ganpati idol, widely "
            "considered one of the most visually beautiful in Pune, and consistently high-quality pandal "
            "decorations. The mandal also runs social reform events and community initiatives during the "
            "10-day festival, combining devotion with civic engagement, and benefits from heavy footfall "
            "near Mandai market."
        ),
        idol="Sharda Ganpati idol, celebrated for its artistic beauty and craftsmanship.",
        address="Near Mandai Market, Budhwar Peth, Pune 411002",
        pandal_address="TO UPDATE — confirm 2026 pandal",
        maps_link="TO UPDATE — August 2026",
        lat=18.517, lng=73.8562,
        morning_aarti="TO CONFIRM", evening_aarti="TO CONFIRM",
        events="Social reform events; cultural programs; community social work during 10 days",
        notes="Add 'Known for beautiful idol' tag",
    ),
    dict(
        doc_id="natu_baug_ganpati", name_en="Natu Baug Ganpati", name_mr="नातू बाग गणपती",
        manacha="Iconic Sarvajanik Mandal", area="Sadashiv Peth, Pune",
        year="Early 20th century", category="sarvajanik_mandal",
        history=(
            "Natu Baug Ganpati is famous for spectacular light displays and immersive pandal experiences "
            "— elaborate themed pandals and state-of-the-art lighting draw visitors as much for the "
            "spectacle as the darshan. Named after the Natu family's garden nearby, it is especially "
            "popular with younger generations and families and regularly features on 'must-visit' lists."
        ),
        idol="Traditional idol in an extraordinary visual setting — the pandal and lighting are the attraction alongside the Ganpati.",
        address="Sadashiv Peth, Pune 411030",
        pandal_address="TO UPDATE — confirm 2026 pandal location",
        maps_link="TO UPDATE — August 2026",
        lat=18.5115, lng=73.8478,
        morning_aarti="TO CONFIRM", evening_aarti="TO CONFIRM",
        events="Light shows every evening; themed pandal experience; cultural programs",
        notes="Add 'Best for light displays' and 'Best for families' tags",
    ),
    dict(
        doc_id="shanipar_shaniwarwada", name_en="Shanipar Ganpati (Shaniwarwada Ganpati)",
        name_mr="शनिपार गणपती (शनिवारवाडा गणपती)", manacha="Iconic Sarvajanik Mandal",
        area="Near Shaniwarwada, Kasba Peth, Pune", year="Early 20th century", category="sarvajanik_mandal",
        history=(
            "Shanipar Ganpati sits near the iconic Shaniwarwada fort, former seat of the Peshwa empire, "
            "giving it unique historical gravitas. It is popular with tourists visiting Shaniwarwada who "
            "combine their heritage visit with Ganpati darshan; during Ganeshotsav the surrounding area "
            "comes alive with processions reflecting old Pune's petha-area festival spirit."
        ),
        idol="Traditional Ganpati idol in a historically rich setting near the Peshwa-era Shaniwarwada fort.",
        address="Near Shaniwarwada, Kasba Peth, Pune 411011",
        pandal_address="TO UPDATE — confirm 2026 pandal",
        maps_link="TO UPDATE — August 2026",
        lat=18.5196, lng=73.8553,
        morning_aarti="TO CONFIRM", evening_aarti="TO CONFIRM",
        events="Close to Shaniwarwada light and sound show; traditional processions in the petha lanes",
        notes="Add 'Near Shaniwarwada' tag for tourists combining heritage + darshan",
    ),
    dict(
        doc_id="jilbya_maruti_ganpati", name_en="Jilbya Maruti Ganpati", name_mr="जिलब्या मारुती गणपती",
        manacha="Iconic Sarvajanik Mandal", area="Tulshibaug, Budhwar Peth, Pune",
        year="Early 20th century", category="sarvajanik_mandal",
        history=(
            "Jilbya Maruti Ganpati sits in the Tulshibaug area near the Jilbya Maruti temple (named for "
            "the jalebis/jilbyas traditionally offered to Hanuman there). It benefits from being in the "
            "Tulshibaug-Dagdusheth corridor, one of Pune's highest-footfall festival zones, and is "
            "naturally visited alongside Tulshibaug Ganpati, Guruji Talim, and Tambdi Jogeshwari on the "
            "Manache Ganpati circuit."
        ),
        idol="Traditional Ganesh idol; its location in the busiest festival corridor is its defining feature.",
        address="Near Jilbya Maruti Temple, Tulshibaug Internal Road, Budhwar Peth, Pune 411002",
        pandal_address="TO UPDATE — confirm 2026 pandal",
        maps_link="TO UPDATE — August 2026",
        lat=18.5155, lng=73.855,
        morning_aarti="TO CONFIRM", evening_aarti="TO CONFIRM",
        events="Part of the dense Tulshibaug darshan corridor; traditional aarti; high energy atmosphere",
        notes="Include in the suggested 'Tulshibaug circuit' route in the app",
    ),
    dict(
        doc_id="tambe_ganpati", name_en="Tambe Ganpati (Shrimant Tambe Mandal)",
        name_mr="ताम्बे गणपती (श्रीमंत ताम्बे मंडळ)", manacha="Iconic Sarvajanik Mandal",
        area="Sadashiv Peth, Pune", year="Early 20th century", category="sarvajanik_mandal",
        history=(
            "Shrimant Tambe Mandal is a well-known traditional mandal of Sadashiv Peth, historically "
            "associated with Brahmin scholars, classical arts and Pune's intellectual life. For decades "
            "it has emphasised classical music, religious recitations and culturally rooted programs over "
            "spectacular decoration, popular with those who prefer an authentic, refined festival "
            "experience."
        ),
        idol="Traditional Ganesh idol emphasising religious and cultural authenticity over visual grandeur.",
        address="Sadashiv Peth, Pune 411030",
        pandal_address="TO UPDATE — confirm 2026 pandal",
        maps_link="TO UPDATE — August 2026",
        lat=18.5122, lng=73.8495,
        morning_aarti="TO CONFIRM", evening_aarti="TO CONFIRM",
        events="Classical music performances; religious recitations; Sadashiv Peth cultural programs",
        notes="Add 'Traditional / Cultural' tag for users who prefer authentic over spectacular",
    ),
    dict(
        doc_id="phadke_haud_ganpati", name_en="Phadke Haud Ganpati", name_mr="फडके हौद गणपती",
        manacha="Heritage Neighbourhood Mandal", area="Kasba Peth, Pune",
        year="Pre-independence era", category="heritage",
        history=(
            "Phadke Haud Ganpati is named after the historic Phadke Haud (water tank) in Kasba Peth, "
            "Pune's oldest neighbourhood, which historically served the area's daily water needs and "
            "became a community gathering point. Being in the same neighbourhood as the first-Manacha "
            "Kasba Ganpati, it forms part of the natural darshan circuit and reflects the community-rooted "
            "celebration style of old Pune's peth areas."
        ),
        idol="Traditional idol in a heritage Kasba Peth setting; the surrounding old wadas and narrow lanes are part of the atmosphere.",
        address="Near Phadke Haud, Kasba Peth Road, Kasba Peth, Pune 411011",
        pandal_address="TO UPDATE — confirm 2026 pandal",
        maps_link="TO UPDATE — August 2026",
        lat=18.5189, lng=73.8569,
        morning_aarti="TO CONFIRM", evening_aarti="TO CONFIRM",
        events="Part of Kasba Peth neighbourhood celebration; traditional community festival style",
        notes="Include in Kasba Peth area circuit suggestion in the app",
    ),
]

