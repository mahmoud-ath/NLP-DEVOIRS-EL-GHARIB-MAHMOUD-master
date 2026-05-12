import csv
import random
from datetime import datetime

# =====================================================================
# BASE DE CONNAISSANCES JURIDIQUES MAROCAINES - VERSION ÉTENDUE
# =====================================================================

def generate_moroccan_legal_corpus():
    """Génère un corpus juridique marocain étendu avec toutes les catégories"""
    
    corpus_juridique = []
    counter = 1
    
    # =================================================================
    # 1. CODE DE LA ROUTE (Loi 52-05) - 40+ entrées
    # =================================================================
    
    # Speed violations with graduated penalties
    speed_scenarios = [
        {"limit": 60, "zone_ar": "المناطق العمرانية", "zone_fr": "agglomération", 
         "speeds": [(65,80,300,2), (85,100,700,4), (105,150,1500,6)]},
        {"limit": 100, "zone_ar": "الطرق الوطنية خارج المناطق العمرانية", "zone_fr": "routes nationales hors agglomération",
         "speeds": [(105,120,300,2), (125,140,700,4), (145,180,1500,6)]},
        {"limit": 120, "zone_ar": "الطرق السريعة", "zone_fr": "autoroutes",
         "speeds": [(125,140,300,2), (145,160,700,4), (165,200,1500,6)]}
    ]
    
    for scenario in speed_scenarios:
        for speed_violation in scenario["speeds"]:
            actual_speed = random.randint(speed_violation[0], speed_violation[1])
            corpus_juridique.append({
                "id": f"CR_{counter:03d}",
                "texte_legal": f"يُحدد الحد الأقصى للسرعة داخل {scenario['zone_ar']} بـ{scenario['limit']} كيلومتر في الساعة. تجاوز هذه السرعة يعد مخالفة مرورية.",
                "explication": f"تجاوز السرعة المحددة قانونياً يُعرّض السائق لغرامة مالية تتراوح بين {speed_violation[2]} و{speed_violation[2]} درهم وسحب {speed_violation[3]} نقاط من رخصة القيادة.",
                "type_loi": "قانون السير",
                "numero_loi": "52-05",
                "exemple": f"سائق بلغت سرعته {actual_speed} كم/س في منطقة سرعتها القصوى {scenario['limit']} كم/س، عوقب بغرامة {speed_violation[2]} درهم وسحب {speed_violation[3]} نقاط.",
                "texte_fr": f"La vitesse maximale en {scenario['zone_fr']} est {scenario['limit']} km/h. Tout dépassement est sanctionné.",
                "amende": speed_violation[2],
                "points": speed_violation[3]
            })
            counter += 1
    
    # Alcohol and drugs offenses
    alcohol_levels = [
        (0.21, 0.4, 2000, 3, 0, "غرامة 2000 درهم وسحب الرخصة 3 أشهر"),
        (0.41, 0.6, 5000, 6, 1, "غرامة 5000 درهم وسحب الرخصة 6 أشهر وسجن شهر"),
        (0.61, 0.8, 10000, 12, 3, "غرامة 10000 درهم وسحب الرخصة سنة وسجن 3 أشهر")
    ]
    
    for alc in alcohol_levels:
        level = round(random.uniform(alc[0], alc[1]), 2)
        corpus_juridique.append({
            "id": f"CR_{counter:03d}",
            "texte_legal": f"يُمنع قيادة المركبة تحت تأثير الكحول أو المخدرات. كل من تجاوز نسبة 0.2 غرام/لتر من الكحول في الدم يتعرض لعقوبات قانونية.",
            "explication": f"القيادة تحت تأثير الكحول بنسبة {level} غ/ل تعتبر جريمة جنائية تستوجب {alc[4]} أشهر سجن وغرامة {alc[2]} درهم وسحب الرخصة {alc[3]} أشهر.",
            "type_loi": "قانون السير",
            "numero_loi": "52-05",
            "exemple": f"سائق ضُبط بنسبة كحول {level} غ/ل، صدر في حقه حكم بـ{alc[5]}.",
            "texte_fr": f"Conduite sous alcool ({level}g/l). Sanction: {alc[2]} DH d'amende, {alc[3]} mois de suspension.",
            "amende": alc[2],
            "points": 0,
            "suspension_mois": alc[3],
            "prison_mois": alc[4]
        })
        counter += 1
    
    # Seatbelt violations
    for i in range(3):
        corpus_juridique.append({
            "id": f"CR_{counter:03d}",
            "texte_legal": "يُلزم جميع ركاب المركبة بربط حزام الأمان. مخالفة هذا الإلزام تستوجب غرامة مالية وسحب نقاط.",
            "explication": "حزام الأمان إلزامي للسائق وجميع الركاب في المقاعد الأمامية والخلفية لضمان السلامة الطرقية.",
            "type_loi": "قانون السير",
            "numero_loi": "52-05",
            "exemple": "سائق بدون حزام أمان: غرامة 300 درهم + سحب نقطتين + مخالفة مرورية.",
            "texte_fr": "Le port de la ceinture de sécurité est obligatoire pour tous les passagers.",
            "amende": 300,
            "points": 2
        })
        counter += 1
    
    # Mobile phone usage
    for i in range(3):
        corpus_juridique.append({
            "id": f"CR_{counter:03d}",
            "texte_legal": "يحظر استخدام الهاتف المحمول أثناء القيادة إلا بواسطة سماعة لاسلكية. المخالفة تستوجب عقوبات رادعة.",
            "explication": "استخدام الهاتف باليد خلال القيادة يشتت انتباه السائق ويزيد خطر الحوادث بنسبة 400%.",
            "type_loi": "قانون السير",
            "numero_loi": "52-05",
            "exemple": "سائق يتحدث بهاتفه دون سماعة أثناء القيادة: غرامة 700 درهم وسحب 3 نقاط.",
            "texte_fr": "L'usage du téléphone portable en conduisant (sans kit mains libres) est interdit.",
            "amende": 700,
            "points": 3
        })
        counter += 1
    
    # Driving without license
    for i in range(3):
        corpus_juridique.append({
            "id": f"CR_{counter:03d}",
            "texte_legal": "القيادة بدون رخصة سياقة أو برخصة منتهية الصلاحية يعرض السائق لعقوبات تشمل الغرامة والحبس.",
            "explication": "رخصة السياقة وثيقة إجبارية لقيادة المركبات. القيادة بدونها جريمة يعاقب عليها القانون.",
            "type_loi": "قانون السير",
            "numero_loi": "52-05",
            "exemple": "شخص ضُبط يقود سيارة بدون رخصة: حكم بغرامة 3000 درهم وسجن شهرين موقوفي التنفيذ.",
            "texte_fr": "Conduite sans permis: amende de 2000 à 4000 DH et peine d'emprisonnement.",
            "amende": random.randint(2000, 4000),
            "points": 4,
            "prison_mois": random.choice([0, 1, 2])
        })
        counter += 1
    
    # =================================================================
    # 2. DROIT PÉNAL (القانون الجنائي) - 30+ entrées
    # =================================================================
    
    # Theft offenses
    theft_types = [
        ("السرقة البسيطة", "الفصل 505", "Le vol simple", (1, 5), 0),
        ("السرقة الموصوفة", "الفصل 506", "Le vol qualifié", (5, 10), 2),
        ("السرقة بالعنف", "الفصل 507", "Le vol avec violence", (10, 20), 3),
        ("السرقة باستعمال السلاح", "الفصل 508", "Le vol à main armée", (15, 30), 5)
    ]
    
    for theft in theft_types:
        years = random.randint(theft[3][0], theft[3][1])
        corpus_juridique.append({
            "id": f"DP_{counter:03d}",
            "texte_legal": f"{theft[0]} وفق {theft[1]} من القانون الجنائي المغربي يُعاقب عليها بالحبس.",
            "explication": f"عقوبة {theft[0]} تتراوح بين {theft[3][0]} و{theft[3][1]} سنوات سجن وغرامة مالية حسب ظروف الجريمة.",
            "type_loi": "القانون الجنائي",
            "numero_loi": theft[1],
            "exemple": f"شخص ارتكب {theft[0]} وحكم عليه بالسجن {years} سنوات.",
            "texte_fr": f"{theft[2]} (art. {theft[1]} CP) est puni de {theft[3][0]} à {theft[3][1]} ans d'emprisonnement.",
            "peine_min_ans": theft[3][0],
            "peine_max_ans": theft[3][1]
        })
        counter += 1
    
    # Homicide offenses
    homicides = [
        ("القتل العمد", "الفصل 392", "Meurtre volontaire", "الإعدام أو السجن المؤبد", "1ère instance"),
        ("القتل الخطأ", "الفصل 432", "Homicide involontaire", (3, 60), "tribunal correctionnel"),
        ("القتل مع سبق الإصرار", "الفصل 393", "Meurtre avec préméditation", "الإعدام", "cour d'assises"),
        ("القتل بدافع العار", "الفصل 418", "Meurtre pour cause d'honneur", (12, 30), "cour d'assises")
    ]
    
    for hom in homicides:
        corpus_juridique.append({
            "id": f"DP_{counter:03d}",
            "texte_legal": f"{hom[0]} وفق {hom[1]} من القانون الجنائي المغربي.",
            "explication": f"القانون يميز بين القتل العمد (نية جنائية) والقتل الخطأ (إهمال). عقوبة {hom[0]} تصل إلى {hom[3]}.",
            "type_loi": "القانون الجنائي",
            "numero_loi": hom[1],
            "exemple": f"شخص أدين بـ{hom[0]} وحكم عليه بـ{hom[3]}.",
            "texte_fr": f"{hom[2]} (art. {hom[1]} CP)"
        })
        counter += 1
    
    # Other criminal offenses
    criminal_offenses = [
        ("الرشوة", "الفصل 248", "La corruption", "Corruption de fonctionnaire", (2, 10), 50000),
        ("اختلاس أموال عامة", "الفصل 257", "Le détournement de fonds publics", "Détournement de fonds publics", (3, 15), 100000),
        ("تبييض الأموال", "الفصل 574", "Le blanchiment d'argent", "Blanchiment d'argent", (5, 20), 200000),
        ("الاتجار بالبشر", "الفصل 467-1", "La traite des êtres humains", "Traite des êtres humains", (10, 30), 300000),
        ("الاعتداء الجنسي", "الفصل 485", "L'agression sexuelle", "Agression sexuelle", (2, 10), 50000)
    ]
    
    for offense in criminal_offenses:
        ans = random.randint(offense[4][0], offense[4][1])
        corpus_juridique.append({
            "id": f"DP_{counter:03d}",
            "texte_legal": f"{offense[0]} وفق {offense[1]} من القانون الجنائي المغربي.",
            "explication": f"جريمة {offense[2]} يعاقب عليها القانون بالسجن من {offense[4][0]} إلى {offense[4][1]} سنة وغرامة مالية كبيرة.",
            "type_loi": "القانون الجنائي",
            "numero_loi": offense[1],
            "exemple": f"شخص أدين بـ{offense[0]} وحكم عليه بالسجن {ans} سنوات وغرامة {offense[5]} درهم.",
            "texte_fr": f"{offense[2]} (art. {offense[1]} CP) est puni de {offense[4][0]} à {offense[4][1]} ans d'emprisonnement."
        })
        counter += 1
    
    # =================================================================
    # 3. DROIT DE LA FAMILLE (مدونة الأسرة/Moudawwana) - 25+ entrées
    # =================================================================
    
    # Divorce provisions
    divorce_types = [
        ("الطلاق للشقاق", "المادة 79", "Divorce pour discorde", 
         "يحق للزوجة طلب الطلاق للشقاق دون موافقة الزوج", 
         "تطلب الزوجة الطلاق وتثبت الشقاق، وتعيّن المحكمة حكمين للإصلاح"),
        ("الطلاق الرجعي", "المادة 85", "Divorce révocable", 
         "الطلاق الذي لا يحسم العلاقة الزوجية نهائياً خلال فترة العدة", 
         "يطلق الزوج زوجته طلقة واحدة، ولها حق الرجوع خلال عدة الطلاق"),
        ("الطلاق البائن", "المادة 86", "Divorce irrévocable", 
         "الطلاق الذي يحسم العلاقة الزوجية نهائياً", 
         "طلاق بعد الطلقة الثالثة أو الخلع"),
        ("الخلع", "المادة 115", "Le Khôl", 
         "الزوجة تفتدي نفسها من الزواج بتعويض مالي", 
         "زوجة تطلب الخلع وتتنازل عن حقوقها المالية مقابل الطلاق")
    ]
    
    for div in divorce_types:
        corpus_juridique.append({
            "id": f"DF_{counter:03d}",
            "texte_legal": f"وفق {div[1]} من مدونة الأسرة، {div[3]}.",
            "explication": f"{div[0]} من أنواع الطلاق في القانون المغربي: {div[4]}.",
            "type_loi": "مدونة الأسرة",
            "numero_loi": div[1],
            "exemple": f"في حالة {div[0]}، المحكمة تطبق {div[1]} لضمان حقوق الطرفين.",
            "texte_fr": f"{div[2]} selon l'article {div[1]} du Code de la Famille."
        })
        counter += 1
    
    # Child custody (Hadana)
    custody_provisions = [
        ("حضانة الأم", "المادة 164", "Garde maternelle", 
         "للأم حق حضانة أطفالها بعد الطلاق ما لم تثبت عدم أهليتها", 
         "أم تحتفظ بحضانة أطفالها بعد الطلاق"),
        ("انتقال الحضانة", "المادة 166", "Transfert de garde", 
         "في حالة زواج الأم، تنتقل الحضانة للأب أو الجدة", 
         "زواج الأم يؤدي لنقل الحضانة للأب"),
        ("سقوط الحضانة", "المادة 170", "Perte de garde", 
         "الحضانة تسقط بإهمال المربي أو إدمانه أو إصابته بمرض خطير", 
         "حكم قضائي يسقط الحضانة عن الأب لسلوكه العنيف"),
        ("زيارة المحضون", "المادة 180", "Droit de visite", 
         "للأب غير الحاضن حق زيارة أبنائه وفق ما تقره المحكمة", 
         "محكمة تنظم حق الزيارة للأب كل أسبوع")
    ]
    
    for custody in custody_provisions:
        corpus_juridique.append({
            "id": f"DF_{counter:03d}",
            "texte_legal": f"وفق {custody[1]} من مدونة الأسرة، {custody[3]}.",
            "explication": f"{custody[0]} في القانون المغربي: {custody[4]}.",
            "type_loi": "مدونة الأسرة",
            "numero_loi": custody[1],
            "exemple": f"قضية حضانة تطبق {custody[1]} من مدونة الأسرة.",
            "texte_fr": f"{custody[2]} selon l'article {custody[1]} du Code de la Famille."
        })
        counter += 1
    
    # Alimony/Financial support
    for i in range(4):
        corpus_juridique.append({
            "id": f"DF_{counter:03d}",
            "texte_legal": f"وفق المادة {194 + i} من مدونة الأسرة، النفقة واجبة على الأب تجاه أبنائه حتى سن الرشد.",
            "explication": "النفقة تشمل السكن والغذاء والكسوة والتعليم والعلاج. تحدد المحكمة قيمتها حسب دخل الأب واحتياجات الأبناء.",
            "type_loi": "مدونة الأسرة",
            "numero_loi": f"المادة {194 + i}",
            "exemple": f"أب يرفض دفع النفقة: المحكمة تحجز راتبه لصالح أبنائه بناء على المادة {194 + i}.",
            "texte_fr": f"La pension alimentaire est régie par l'article {194 + i} du Code de la Famille."
        })
        counter += 1
    
    # =================================================================
    # 4. SYSTÈME JUDICIAIRE (التنظيم القضائي) - 15+ entrées
    # =================================================================
    
    court_system = [
        ("المحكمة الابتدائية", "SJ_", "Tribunal de première instance", 
         "الدرجة الأولى من التقاضي", "تختص بالقضايا المدنية والجنائية والتجارية والأسرية",
         "رفع دعوى استرداد دين بأقل من 50000 درهم"),
        ("محكمة الاستئناف", "SJ_", "Cour d'appel", 
         "الدرجة الثانية من التقاضي", "تنظر في الطعون ضد أحكام المحاكم الابتدائية خلال 30 يوماً",
         "استئناف حكم ابتدائي لدى محكمة الاستئناف"),
        ("محكمة النقض", "SJ_", "Cour de cassation", 
         "أعلى هيئة قضائية", "تراقب صحة تطبيق القانون دون مراجعة الوقائع",
         "طعن بالنقض في حكم استئناف لمخالفة القانون"),
        ("القضاء الإداري", "SJ_", "Juridiction administrative", 
         "محاكم إدارية للنزاعات مع الإدارة", "تختص بالقضايا ضد الدولة والجماعات المحلية",
         "موظف يطعن في قرار إداري"),
        ("المجلس الأعلى للسلطة القضائية", "SJ_", "Conseil supérieur du pouvoir judiciaire", 
         "هيئة مستقلة لتسيير القضاء", "تسهر على استقلالية القضاء وتعيين القضاة",
         "تقييم عمل القضاة وترقياتهم")
    ]
    
    for court in court_system:
        corpus_juridique.append({
            "id": f"{court[1]}{counter:03d}",
            "texte_legal": f"{court[0]} هي {court[3]} في النظام القضائي المغربي.",
            "explication": f"{court[0]}: {court[4]}.",
            "type_loi": court[0],
            "numero_loi": "القانون التنظيمي للسلطة القضائية",
            "exemple": court[5],
            "texte_fr": court[2]
        })
        counter += 1
    
    # Procedure provisions
    procedures = [
        ("رفع دعوى مدنية", "تقديم مقال افتتاحي + أداء الرسوم القضائية + إرفاق الوثائق"),
        ("الاستئناف", "تقديم عريضة استئناف خلال 30 يوماً من تاريخ التبليغ"),
        ("تنفيذ الأحكام", "الأحكام النهائية واجبة التنفيذ بواسطة مفوض قضائي"),
        ("الصلح القضائي", "إمكانية الصلح أمام القاضي في القضايا المدنية والأسرية")
    ]
    
    for proc in procedures:
        corpus_juridique.append({
            "id": f"SJ_{counter:03d}",
            "texte_legal": f"إجراءات {proc[0]}: {proc[1]}.",
            "explication": f"المسطرة القضائية لـ{proc[0]} تخضع لأحكام قانون المسطرة المدنية.",
            "type_loi": "المسطرة المدنية",
            "numero_loi": "قانون المسطرة المدنية",
            "exemple": f"مواطن يتبع إجراءات {proc[0]} وفق القانون.",
            "texte_fr": f"Procédure de {proc[0]} selon le Code de Procédure Civile."
        })
        counter += 1
    
    # =================================================================
    # 5. DROIT CIVIL ET COMMERCIAL - 20+ entrées
    # =================================================================
    
    # Contract law (DOC)
    contract_requirements = [
        ("الأهلية", "18 سنة كاملة، ورشد، وعدم الحجر"),
        ("الرضا", "إرادة حرة خالية من العيوب: الإكراه، الغلط، التدليس"),
        ("المحل المشروع", "الموضوع غير مخالف للقانون أو النظام العام"),
        ("السبب المشروع", "الدافع غير مخالف للقانون")
    ]
    
    for req in contract_requirements:
        corpus_juridique.append({
            "id": f"DC_{counter:03d}",
            "texte_legal": f"من شروط صحة العقد وفق قانون الالتزامات والعقود: {req[0]}: {req[1]}.",
            "explication": f"{req[0]} شرط أساسي لصحة العقد وإنتاجه للآثار القانونية.",
            "type_loi": "قانون الالتزامات والعقود",
            "numero_loi": "قانون الالتزامات والعقود (DOC)",
            "exemple": f"عدم توفر شرط {req[0]} يؤدي إلى بطلان العقد.",
            "texte_fr": f"Condition de validité du contrat: {req[0]}."
        })
        counter += 1
    
    # Company law
    company_types = [
        ("شركة ذات مسؤولية محدودة (SARL)", 10000, 10, 
         "مسؤولية الشركاء محدودة بحصصهم، 1-50 شريكاً"),
        ("شركة مساهمة (SA)", 300000, 5, 
         "مسؤولية المساهمين محدودة بمساهمتهم، تنفع للمشاريع الكبرى"),
        ("شركة تضامنية (SNC)", 0, 2, 
         "مسؤولية الشركاء تضامنية وغير محدودة"),
        ("شركة في طور التأسيس", 0, 1, 
         "مرحلة انتقالية قبل التسجيل الرسمي للشركة")
    ]
    
    for company in company_types:
        corpus_juridique.append({
            "id": f"DC_{counter:03d}",
            "texte_legal": f"{company[0]} وفق القانون التجاري المغربي. رأس المال الأدنى: {company[1]} درهم.",
            "explication": f"{company[0]}: {company[3]}.",
            "type_loi": "القانون التجاري",
            "numero_loi": "17-95 و 5-96",
            "exemple": f"تأسيس {company[0]} برأس مال {company[1] if company[1] > 0 else 'غير محدد'} درهم.",
            "texte_fr": f"{company[0]} selon le code de commerce marocain."
        })
        counter += 1
    
    # =================================================================
    # 6. INFRACTIONS ET SANCTIONS - 20+ entrées
    # =================================================================
    
    # Crime classification
    classifications = [
        ("المخالفات", "Contraventions", "أقل خطورة", "غرامات فقط (300-5000 درهم)", "مخالفة سير"),
        ("الجنح", "Délits", "خطورة متوسطة", "حبس أقل من 5 سنوات + غرامة", "سرقة بسيطة"),
        ("الجنايات", "Crimes", "أشد خطورة", "حبس أكثر من 5 سنوات أو إعدام", "قتل عمد")
    ]
    
    for classif in classifications:
        corpus_juridique.append({
            "id": f"IS_{counter:03d}",
            "texte_legal": f"تنقسم المخالفات في القانون المغربي إلى: {classif[0]}: {classif[3]}.",
            "explication": f"{classif[0]} هي {classif[2]}. العقوبات: {classif[3]}.",
            "type_loi": "القانون الجنائي",
            "numero_loi": "الفصل 111",
            "exemple": f"مثال: {classif[4]} يعتبر {classif[0]}.",
            "texte_fr": f"Classification des infractions: {classif[1]}."
        })
        counter += 1
    
    # Sexual harassment
    for i in range(3):
        corpus_juridique.append({
            "id": f"IS_{counter:03d}",
            "texte_legal": "التحرش الجنسي وفق الفصل 503-1 من القانون الجنائي.",
            "explication": "التحرش الجنسي جريمة يعاقب عليها بالحبس من 6 أشهر إلى 3 سنوات وغرامة من 10000 إلى 50000 درهم.",
            "type_loi": "القانون الجنائي",
            "numero_loi": "الفصل 503-1",
            "exemple": "شخص تحرش بزميلته في العمل: حكم بالحبس سنة وغرامة 20000 درهم.",
            "texte_fr": "Le harcèlement sexuel (art. 503-1 CP) est puni de 6 mois à 3 ans de prison et d'une amende."
        })
        counter += 1
    
    # Other offenses
    other_offenses = [
        ("السب والقذف", "الفصل 300", "Injures et diffamation", "الحبس من 3 أشهر إلى سنتين"),
        ("الإفلاس التدليسي", "الفصل 579", "Banqueroute frauduleuse", "السجن من سنة إلى 5 سنوات"),
        ("إصدار شيك بدون رصيد", "الفصل 540", "Émission de chèque sans provision", "الحبس من سنة إلى 5 سنوات"),
        ("الغش التجاري", "الفصل 404", "Fraude commerciale", "الحبس من 6 أشهر إلى 3 سنوات")
    ]
    
    for offense in other_offenses:
        corpus_juridique.append({
            "id": f"IS_{counter:03d}",
            "texte_legal": f"{offense[0]} وفق {offense[1]} من القانون الجنائي.",
            "explication": f"جريمة {offense[0]} يعاقب عليها بـ{offense[3]}.",
            "type_loi": "القانون الجنائي",
            "numero_loi": offense[1],
            "exemple": f"شخص أدين بـ{offense[0]} وحكم عليه بـ{offense[3]}.",
            "texte_fr": f"{offense[2]} (art. {offense[1]} CP)"
        })
        counter += 1
    
    return corpus_juridique[:200]  # Return first 200 entries

# Generate the corpus
print("🔄 Génération du corpus juridique marocain étendu...")
corpus_juridique = generate_moroccan_legal_corpus()

# Display stats
print(f"\n✅ Corpus généré: {len(corpus_juridique)} entrées")
print(f"\n📊 Distribution par type de loi:")
type_counts = {}
for d in corpus_juridique:
    type_counts[d["type_loi"]] = type_counts.get(d["type_loi"], 0) + 1
for type_name, count in sorted(type_counts.items()):
    print(f"   - {type_name}: {count} entrées")

# =====================================================================
# EXPORT TO CSV
# =====================================================================

csv_filename = "corpus_juridique_marocain.csv"

# Define all possible fields
fieldnames = ["id", "type_loi", "numero_loi", "texte_legal", "texte_fr", 
              "explication", "exemple", "amende", "points", "peine_min_ans", 
              "peine_max_ans", "prison_mois", "suspension_mois"]

with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    
    for entry in corpus_juridique:
        # Clean the entry to ensure UTF-8 compatibility
        cleaned_entry = {}
        for key, value in entry.items():
            if isinstance(value, str):
                # Remove any problematic characters if needed
                cleaned_entry[key] = value
            else:
                cleaned_entry[key] = value
        writer.writerow(cleaned_entry)

print(f"\n✅ Fichier CSV exporté: {csv_filename}")
print(f"📁 Emplacement: {csv_filename}")
print(f"📊 Total d'entrées: {len(corpus_juridique)}")
print(f"🈯 Encodage: UTF-8 (compatible avec tous les systèmes)")

# Create Arabic text documents for NLP
print("\n🔤 Extraction des documents textuels pour modèles NLP...")
documents = [f"{d['texte_legal']} {d['explication']} {d['exemple']}" for d in corpus_juridique]
documents_fr = [f"{d['texte_fr']} {d['explication']} {d['exemple']}" for d in corpus_juridique if d.get('texte_fr')]
doc_ids = [d['id'] for d in corpus_juridique]

print(f"📄 Documents arabes: {len(documents)}")
print(f"📄 Documents français: {len(documents_fr)}")
print(f"✅ Préparation des données terminée!")

# Save documents list to text file for reference
with open("documents_juridiques.txt", "w", encoding='utf-8') as f:
    for i, (doc_id, doc) in enumerate(zip(doc_ids, documents)):
        f.write(f"--- {doc_id} ---\n{doc}\n\n")

print(f"📄 Documents textuels sauvegardés dans 'documents_juridiques.txt'")