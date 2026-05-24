# Database simulation

data = {
    "APRIL Assistance Thailand": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Thailand",
        "Last_updated": "11 May 2026",
        "Contact": "<a href='mailto:ops.th@april.co.th'>ops.th@april.co.th</a>",
        "Client":"ADAC Versicherung AG, APRIL International France, APRIL Sompo, Coris Slovenia, Gouda & Gjensidige, SOS First Denmark, SOS International Netherlands, IMG UK & USA, Anvil group, CEGA Assistance, ISON Poland, Healthmetric, GlobalExcel Indonesia, WorldTravelProtection, Flying Doctor (Byzinsight), Trails of Incochina and etc.",
        "Assistance company": "-",
        "Company Type": "Assistance Company",
        "Additional information": "APRIL Assistance accepts cases from partners such as SOS First Denmark, SOS International Netherlands, Gjensidige, Gouda, and the IAG Group. Kindly contact your primary insurance provider before coming to the hospital",
    },

    "APRIL International France": {
        "Status": "Accepted",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "France",
        "Last_updated": "11 May 2026",
        "Contact": "<a href='mailto:ops.th@april.co.th'>ops.th@april.co.th</a>",
        "Client":"APRIL Assistance Thailand",
        "Assistance company": "APRIL Assistance Thailand",
        "Company Type": "IPMI Provider",
        "Additional information": "Policy begin with APA, contact APRIL Assistance Thailand requests GOP for hospitalisation, there is limitation for room cost (Depend on your policy) and home medication will be under self-pay",
    },

    "APRIL International UK": {
        "Status": "Accepted with conditions",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "United Kingdom",
        "Last_updated": "11 May 2026",
        "Contact": "<a href='mailto:contact.th@april.com.th'>contact.th@april.com</a>",
        "Assistance company": "CEGA Assistance",
        "Company Type": "IPMI Provider",
        "Additional information": "Policies beginning with “GG” or policy number XXXXXXX: In the event of an emergency, hospitalization, or medical expenses exceeding 2,500 GBP (108,000 THB), please contact CEGA Assistance to request the initial Guarantee of Payment (GOP), as APRIL International UK does not have an in-house team to issue GOP",
    },

    "APRIL Sompo": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Direct billing (Depend on your policy)",
        "IPD_status": "Accepted", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Thailand",
        "Last_updated": "11 May 2026",
        "Contact": "<a href='mailto:provider.asia@april.com'>provider.asia@april.co.th</a>",
        "Client":"_",
        "Assistance company": "APRIL Assistance Thailand - For evacuation & repatriation",
        "Company Type": "IPMI Provider | Partner Plan",
        "Additional information": "Direct billing can be applied up to $250 $500 $600 $750 depend on policy, in case medical expenses more than direct billing limit, GOP is required",
    },

    "Allianz Worldwide Care": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Direct billing accepted",
        "IPD_status": "Accepted", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Ireland",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Assistance company": "-",
        "Company Type": "IPMI Provider | Partner Plan | TPA",
        "Additional information": "The hospital accept only policy begin with PXXXXXXXXX. Direct billing may be available depending on the policy (this can be checked in the AWC portal). In cases involving high medical expenses, special procedures, vaccinations, special medications, high-cost medications, chemotherapy, or radiotherapy, a GOP is required. PLEASE CONFIRM with the International Insurance staff first",

    },

    "Allianz Worldwide Care - IOM Group": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Direct billing accepted",
        "IPD_status": "Accepted", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Ireland",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Assistance company": "-",
        "Company Type": "IPMI Provider | Partner Plan | TPA",
        "Additional information": "The hospital accept only policy begin with PXXXXXXXXX. Direct billing may be available depending on the policy (this can be checked in the AWC portal). In cases involving high medical expenses, special procedures, vaccinations, special medications, high-cost medications, chemotherapy, or radiotherapy, a GOP is required. PLEASE CONFIRM with the International Insurance staff first",

    },

    "Allianz Worldwide Care - MOFA Group (Embassy of Saudi Arabia)": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Direct billing accepted",
        "IPD_status": "Accepted", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Ireland",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Assistance company": "-",
        "Company Type": "IPMI Provider | Partner Plan | TPA",
        "Additional information": "The hospital accepts only policies beginning with ‘PXXXXXXXXX’ (gold insurance card). A deductible of USD 27 applies to the doctor’s fee. Direct billing may be available depending on the policy (this can be checked in the AWC portal). In cases involving high medical expenses, special procedures, vaccinations, special medications, high-cost medications, chemotherapy, or radiotherapy, a GOP is required. PLEASE CONFIRM with the International Insurance staff first",

    },

    "Asian Assistance": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Thailand",
        "Last_updated": "11 May 2026",
        "Contact": "<a href='mailto:contact@asian-assistance.com'>contact@asian-assistance.com</a>",
        "Client":"AXA Global Health",
        "Assistance company": "-",
        "Company Type": "Assistance company",
        "Additional information": "-"
    },

    "Asian Assistance - AXA Global Health (AXA PPP)": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Cashless service / A Guarantee of Payment (GOP) is required for high-cost medical expenses exceeding THB 15,000. Please refer to the additional information below for further details",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Thailand",
        "Last_updated": "11 May 2026",
        "Contact": "<a href='mailto:contact@asian-assistance.com'>contact@asian-assistance.com</a>",
        "Client":"-",
        "Assistance company": "-",
        "Company Type": "Assistance company",
        "Additional information": {
            "EN": "For AXA Global Health (AXA PPP), direct billing is available for outpatient visits with medical expenses not exceeding THB 15,000 (including specialist consultations), laboratory tests, blood tests, acne medications, procedures, eye/ear drops, medications & dressings, and physiotherapy (limited to a maximum of 5 sessions per facility). <br><br>Pre-authorisation is required for outpatient visits exceeding THB 15,000, more than 5 physiotherapy sessions at the same facility, psychiatric consultations, gynecological conditions (e.g. PCOS, menopause), CT scans, MRI scans, PET scans, dental services, optical services (including optician services, prescription glasses, or contact lenses), health check-ups, infertility treatments, sexual health services, contraception, conditions related to learning or developmental delay, genetic testing, alcohol or drug abuse treatment, vaccinations, maternity care, vitamin or supplement injections/IV infusions, and hair loss shampoo",
            "FR": "Pour AXA Global Health (AXA PPP), la prise en charge directe est possible pour les consultations ambulatoires dont les frais médicaux ne dépassent pas 15 000 THB (y compris les consultations de spécialistes), les analyses de laboratoire, les analyses sanguines, les traitements contre l’acné, les procédures médicales, les gouttes oculaires et auriculaires, les médicaments et pansements, ainsi que la physiothérapie (limitée à 5 séances maximum par établissement). <br><br>Une préautorisation est requise pour les consultations ambulatoires dépassant 15 000 THB, plus de 5 séances de physiothérapie dans le même établissement, les consultations psychiatriques, les affections gynécologiques (par ex. SOPK, ménopause), les examens CT, IRM et PET scan, les soins dentaires, les services d’optique (y compris chez un opticien ou pour la prescription de lunettes ou lentilles), les bilans de santé, les traitements de fertilité, les soins liés à la santé sexuelle, la contraception, les troubles liés aux difficultés d’apprentissage ou au retard du développement, les tests génétiques, les traitements liés à l’alcool ou aux drogues, les vaccinations, les soins de maternité, les injections ou perfusions de vitamines et compléments, ainsi que les shampoings contre la chute des cheveux",
            "DE": "Für AXA Global Health (AXA PPP) ist eine Direktabrechnung für ambulante Behandlungen möglich, sofern die medizinischen Kosten 15.000 THB nicht überschreiten (einschließlich Facharztkonsultationen), Laboruntersuchungen, Bluttests, Akne-Medikationen, Behandlungen, Augen- und Ohrentropfen, Medikamente und Verbandsmaterial sowie Physiotherapie (maximal 5 Sitzungen pro Einrichtung). <br><br>Eine Vorabgenehmigung ist erforderlich für ambulante Behandlungen über 15.000 THB, mehr als 5 Physiotherapiesitzungen in derselben Einrichtung, psychiatrische Konsultationen, gynäkologische Erkrankungen (z. B. PCOS, Menopause), CT-, MRT- und PET-Untersuchungen, zahnärztliche Leistungen, optische Leistungen (einschließlich Optikerleistungen sowie Brillen- oder Kontaktlinsenverordnungen), Gesundheits-Check-ups, Kinderwunschbehandlungen, sexuelle Gesundheitsleistungen, Verhütung, Behandlungen im Zusammenhang mit Lern- oder Entwicklungsstörungen, genetische Tests, Alkohol- oder Drogenabhängigkeit, Impfungen, Schwangerschaftsleistungen, Vitamin- oder Nahrungsergänzungs-Injektionen bzw. Infusionen sowie Shampoos gegen Haarausfall",
    },
    },

    "Euro Center Thailand": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "Last_updated": "11 May 2026",
        "IPD_status": "Accepted",
        "Country": "Thailand",
        "Last_updated": "11 May 2026",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Contact": "bangkok@eurocenter",
        "Client":"ACS, Thaivivat, Sompo, Globality",
        "Assistance company" "-"
        "Company Type": "Medical Assistace | TPA",
        "Additional information":"-",
    },

    "BlueCrossBlueShield": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with conditions",
        "OPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
        "Country": "United States of America",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client":"Anthem BCSBS, Horizon BCBS, Highmark BCBS, Excellus BCBS, Premera BCBS, Carefirst BCBS, Florida Blue, Regence BCBS, Capital Blue, Independence Blue Cross, Wellmark BCBS ",
        "Assistance company": "GeoBlue",
        "Company Type": "Health Insurer | BCBS License",
        "Additional information": "The hospital does not accept direct billing from BlueCrossBlueShield. Please contact your insurer to request an initial Guarantee of Payment (GOP) for both outpatient and inpatient services. Otherwise, the expenses will be under self-pay",
    },

    "Anthem": {
       "Status": "Accepted with conditions",
       "OPD_status": "Accepted with conditions",
       "OPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "IPD_status": "Accepted with conditions",
       "IPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "Country": "United States of America",
       "Last_updated": "11 May 2026",
       "Contact": "-",
       "Client":"-",
       "Assistance company": "GeoBlue",
       "Company Type": "Health Insurer | BCBS License",
       "Additional information": "The hospital does not accept Anthem insurance due to they did not provide the coverage even coordinate with GeoBlue"
    },

    "Horizon BlueCrossBlueShield": {
       "Status": "Accepted with conditions",
       "OPD_status": "Accepted with conditions",
       "OPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "IPD_status": "Accepted with conditions",
       "IPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "Country": "United States of America",
       "Last_updated": "11 May 2026",
       "Contact": "-",
       "Client":"-",
       "Assistance company": "GeoBlue",
       "Company Type": "Health Insurer | BCBS License",
       "Additional information": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",

    },
           

    "Highmark BlueCrossBlueShield": {
       "Status": "Accepted with conditions",
       "OPD_status": "Accepted with conditions",
       "OPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "IPD_status": "Accepted with conditions",
       "IPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "Country": "United States of America",
       "Last_updated": "11 May 2026",
       "Contact": "-",
       "Client":"-",
       "Assistance company": "GeoBlue",
       "Company Type": "Health Insurer | BCBS License",
       "Additional information":"Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay"
    },

    "Excellus BlueCrossBlueShield": {
       "Status": "Accepted with conditions",
       "OPD_status": "Accepted with conditions",
       "OPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "IPD_status": "Accepted with conditions",
       "IPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "Country": "United States of America",
       "Last_updated": "11 May 2026",
       "Contact": "-",
       "Client":"-",
       "Assistance company": "GeoBlue",
       "Company Type": "Health Insurer | BCBS License",
       "Additional information":"Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay"
    },

    "Premera BlueCrossBlueShield": {
       "Status": "Accepted with conditions",
       "OPD_status": "Accepted with conditions",
       "OPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "IPD_status": "Accepted with conditions",
       "IPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "Country": "United States of America",
       "Last_updated": "11 May 2026",
       "Contact": "-",
       "Client":"-",
       "Assistance company": "GeoBlue",
       "Company Type": "Health Insurer | BCBS License",
       "Additional information":"Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay"
    },

    "Carefirst BlueCrossBlueShield": {
       "Status": "Accepted with conditions",
       "OPD_status": "Accepted with conditions",
       "OPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "IPD_status": "Accepted with conditions",
       "IPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "Country": "United States of America",
       "Last_updated": "11 May 2026",
       "Contact": "-",
       "Client":"-",
       "Assistance company": "GeoBlue",
       "Company Type": "Health Insurer | BCBS License",
       "Additional information":"Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay"
    },

    "Florida Blue": {
       "Status": "Accepted with conditions",
       "OPD_status": "Accepted with conditions",
       "OPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "IPD_status": "Accepted with conditions",
       "IPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "Country": "United States of America",
       "Last_updated": "11 May 2026",
       "Contact": "-",
       "Client":"-",
       "Assistance company": "GeoBlue",
       "Company Type": "Health Insurer | BCBS License",
       "Additional information":"Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay"
    },

    "Regence BlueCrossBlueShield": {
       "Status": "Accepted with conditions",
       "OPD_status": "Accepted with conditions",
       "OPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "IPD_status": "Accepted with conditions",
       "IPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "Country": "United States of America",
       "Last_updated": "11 May 2026",
       "Contact": "-",
       "Client":"-",
       "Assistance company": "GeoBlue",
       "Company Type": "Health Insurer | BCBS License",
       "Additional information":"Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay"
    },

    "Capital Blue": {
       "Status": "Accepted with conditions",
       "OPD_status": "Accepted with conditions",
       "OPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "IPD_status": "Accepted with conditions",
       "IPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "Country": "United States of America",
       "Last_updated": "11 May 2026",
       "Contact": "-",
       "Client":"-",
       "Assistance company": "GeoBlue",
       "Company Type": "Health Insurer | BCBS License",
       "Additional information":"Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay"
    },

    "Independence BlueCross": {
       "Status": "Accepted with conditions",
       "OPD_status": "Accepted with conditions",
       "OPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "IPD_status": "Accepted with conditions",
       "IPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "Country": "United States of America",
       "Last_updated": "11 May 2026",
       "Contact": "-",
       "Client":"-",
       "Assistance company": "GeoBlue",
       "Company Type": "Health Insurer | BCBS License",
       "Additional information":"Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay"
    },

     "Wellmark BlueCrossBlueShield": {
       "Status": "Accepted with conditions",
       "OPD_status": "Accepted with conditions",
       "OPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "IPD_status": "Accepted with conditions",
       "IPD_note": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
       "Country": "United States of America",
       "Last_updated": "11 May 2026",
       "Contact": "-",
       "Client":"-",
       "Assistance company": "GeoBlue",
       "Company Type": "Health Insurer | BCBS License",
       "Additional information":"Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay"
    },

    "Gouda & Gjensidige": {
       "Status": "Accepted with conditions",
       "OPD_status": "Accepted with conditions",
       "OPD_note": "Accepted via APRIL Assistance Thailand",
       "IPD_status": "Accepted with conditions",
       "IPD_note": "Accepted via APRIL Assistance Thailand",
       "Country": "Norway",
       "Last_updated": "11 May 2026",
       "Contact": "-",
       "Client": "-",
       "Assistance company": "APRIL Assistance Thailand",
       "Company Type": "Travel Insurance | Non-life insurer",
       "Additional information": "Gouda & Gjensidige is a partner of APRIL Assistance Thailand. They will issue the initial GOP for both outpatient and inpatient services through APRIL Assistance"
    },

    "SOS First Denmark": {
       "Status": "Accepted with conditions",
       "OPD_status": "Accepted with conditions",
       "OPD_note": "Accepted via APRIL Assistance Thailand",
       "IPD_status": "Accepted with conditions",
       "IPD_note": "Accepted via APRIL Assistance Thailand",
       "Country": "Denmark",
       "Last_updated": "11 May 2026",
       "Contact": "<a href='mailto:sos@sos.eu'>sos@sos.eu</a>",
       "Client": "ABC forsikring, AIG Denmark, AIG Finland, AIG Norge, AIG Sverige, AIG UK DK, AIG UK FL, AIG UK Norge, AIG UK SE, Aktsam, Alm.Brand, Aros Forsikring, Balder Forsikring, Betri Trygging, Bomholms Brandforsikring, Chubb - Denmark, Finland, Norway, Sweden, Codan, Cocordia Forsikring, Croisette Insurance Advisory, Dansk Rejseforsikring, Dansk Rejseforsikring AIG, Dina Försäkringar, Fennia, Folksam, Forsikringsselskabet Vendsyssel, Fremtind Norway, Himmerlad Forsikring, ICA Försäkring, Lähitapiola, Länsförsäkringar (LF), Pohjantähti, Trygg-Hansa, Watercircles Norge, Watercircles Sverige, Winterbergh Forsikrig and etc.",
       "Assistance company": "APRIL Assistance Thailand",
       "Company Type": "Assistance company",
       "Additional information": "SOS First Denmark is a partner of APRIL Assistance Thailand. They will issue the initial GOP for both outpatient and inpatient services through APRIL Assistance only"
    },

    "Regency Assurance": {
        "Status": "Not Accepted",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Not Accepted",
        "IPD_note": "Pay & Claim",
        "Country": "United Kingdom",
        "Last_updated": "11 May 2026",
        "Contact":"<a href='mailto:claims@regency-ga.com'>claims@regency-ga.com</a>",
        "Client":"-",
        "Assistance company": "Assist International Services (AIS)",
        "Company Type": "Unknown",
        "Additional information": "Contact via local assistance - Assist International Services, But the final decision rests with Regency Company. This company is very strict when it comes to issuing a GOP, as they require extensive medical documentation, including previous medical history and other supporting documents that may not always be necessary. As a result, many cases end up being declined and are therefore handled on a self-pay basis",
        
    },

    "Europ Assistance": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "-",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "-",
        "Company Type": "Assistance company | Travel Insurance",
        "Additional information": "Europ Assistance has many branches worldwide, including Belgium, Portugal, Switzerland, Argentina, Australia, Australia/New Zealand, Austria, Brazil, Canada, Chile, China, the Czech Republic, France, Germany, Greece, Hong Kong, Hungary, India, Italy, Japan, Bahrain, Jordan, Poland, Singapore, Spain, Taiwan, Thailand, Uruguay, the United States of America, Malaysia, and the Netherlands. Please inform them before going to the hospital",
    },

    "Falck Global Assistance": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Thailand",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "-",
        "Company Type": "Assistance company",
        "Additional information": "Falck Global Assistance is the local assistance provider in Thailand. They receive most cases from Scandinavian countries. If you hold insurance that uses Falck Global Assistance as its local partner in Thailand, please contact your primary insurance provider to open a claim",
    },

    "IMA France": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "France",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Clent": "-",
        "Assistance company": "-",
        "Company Type": "Assistance company",
        "Additional information": "The hospital can accept cases directly from IMA France. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand"
    },

    "IMA Benelux Assistance (Belgium)": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Belgium",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "-",
        "Company Type": "Assistance company",
        "Additional information": "The hospital can accept cases directly from IMA Benelux assistance (Belgium). Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand"
    },

    "IMG UK":{
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "United Kingdom",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "APRIL Assistance Thailand",
        "Company Type": "International Medical | Travel Medical Insurance",
        "Additional information": "The hospital can accept cases directly from IMG UK. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital"
    },

    "IMG USA": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "United States of America",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "APRIL Assistance Thailand",
        "Company Type": "International Medical | Travel Medical Insurance",
        "Additional information": "The hospital can accept cases directly from IMG USA. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital"
    },

    "CFE (Caisse des Français de l'Étranger)": {
        "Status": "Accepted with conditions",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Accepted",
        "IPD_note": "Accepted only via VYV International Assistance (Groupe VYV)",
        "Country": "France",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "VYV International Assistance (Groupe VYV)",
        "Company Type": "France Social Security Fund",
        "Additional information": "The hospital can accept cases from CFE only via the assistance company VYV International Assistance (Groupe VYV). This arrangement applies to hospitalization only and cannot be used for outpatient treatment"
    },

    "VYV International Assistance (Groupe VYV)": {
        "Status": "Accepted",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "France",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "CFE (Caisse des Français de l'Étranger), GAPI",
        "Assistance company": "-",
        "Company Type": "International Assistance",
        "Additional information": "The hospital can directly accept cases from VYV International Assistance (Groupe VYV) for day-case procedures and hospitalization only. As this is a social security insurance scheme for expatriates, co-payment applies: 70% is covered by the insurance and 30% is the patient’s responsibility. Medications for home use are not covered, and outpatient treatment is on a pay-and-claim basis only",

    },

    "ADAC Versicherung AG": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Germany",
        "Last_updated": "11 May 2026",
        "Contact": "ambulance@adac.de",
        "Assistance company": "APRIL Assistance Thailand",
        "Company Type": "Travel & Mobility Insurance",
        "Additional information": "The hospital can accept cases directly from ADAC Versicherung AG. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand, please coordinate with them prior"
    },

    "Helsana Krankenversicherung AG": {
        "Status": "Accepted with conditions",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Switzerland",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Assistance company": "Medicall, Asian Assistance",
        "Company Type": "Swiss Health Insurer",
        "Additional information": "The hospital cannot accept cases directly from Helsana. In cases requiring hospitalization, please coordinate with Helsana and request that the claim be opened with the hospital through a local assistance provider in Thailand",
    },

    "SOS International Netherlands": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with conditions",
        "OPD_note": "Accepted via APRIL Assistance Thailand",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Accepted via APRIL Assistance Thailand",
        "Country": "Netherlands",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Assistance company": "APRIL Assistance Thailand",
        "Company Type": "Assistance company",
        "Additional information": "The hospital cannot accept cases directly from SOS International Netherlands. In cases requiring outpatient or hospitalization, please coordinate with SOS Internnational and request that the claim be opened with the hospital through APRIL Assistance Thailand",
    },

    "GeoBlue": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required. Otherwise, the patient will need to settle the expenses directly with the hospital and submit a reimbursement claim afterward",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "United States of America",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "BlueCrossBlueShield, Anthem, Excellus BCBS, Premera BCBS, Carefirst BCBS, Florida Blue, Regence BCBS, Capital Blue, Independence Blue Cross, Wellmark BCBS",
        "Assistance company": "-",
        "Company Type": "International Health | Travel Medical Insurance",
        "Additional information": "GeoBlue is the assistance company based in the United States of America and acts on behalf of BlueCrossBlueShield, Anthem, Horizon, Highmark, Excellus, Premera, Carefirst, Florida Blue, Regence, Capital Blue, Independence, Wellmark to arrange patient referrals to network hospitals. However, coordination with the hospital may be delayed due to the time zone difference"
    },

    "ATMS (Asian Travel & Medical Services)": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "India",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "-",
        "Additional information": "The hospital can accept cases directly from ATMS Insurance. However, as part of the insurance process, they have requested that the patient wait until the final Guarantee of Payment (GOP) is issued to the hospital. Under no circumstances should the patient be discharged before this process is completed"

    },

    "CMA (Credible Medical Assistance)": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "India",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "-",
        "Company Type": "Assistance company | Medical Assistance",
        "Additional information": "The hospital can accept cases directly from CMA. However, as part of the insurance process, they have requested that the patient wait until the final Guarantee of Payment (GOP) is issued to the hospital. Under no circumstances should the patient be discharged before this process is completed"

    },

    "CEGA Assistance": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "United Kingdom",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "APRIL International UK",
        "Assistance company": "APRIL Assistance Thailand",
        "Company Type": "Assistance company | Medical Assistance",
        "Additional information": "The hospital can accept cases directly from CEGA Assistance. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital",
    },

    "Assist International Services (AIS)": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Thailand",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "WrLife, Regency",
        "Assistance company": "-",
        "Company Type": "Assistance company | Medical Assistance",
        "Additional information": "The hospital can accept cases directly from Assist International Services (AIS), Please coordinate with your insurance provider before coming to the hospital",
    },

    "WrLife": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with conditions",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "United Kingdom",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Assist International Services (AIS)",
        "Company Type": "International Insurance Broker | Medical Insurance for Expat",
        "Additional information": "The hospital cannot accept cases directly from WrLife. We only accept Guarantees of Payment (GOP) issued through Assist International Services (AIS). Please coordinate with your insurance provider before coming to the hospital",
    },

    "Humana": {
        "Status": "Not Accepted",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Not Accepted",
        "IPD_note": "Pay & Claim",
        "Country": "United States of America",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "-",
        "Company Type": "Domestic Health Insurannce",
        "Additional information": "There is no contract with the hospital; therefore, the case will be handled under a pay-and-claim process"

    },

    "HanseMekur Reiseversicherung": {
        "Status": "Accepted with conditions",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Germany",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "MD Medicus, Asian Assistance",
        "Company Type": "Assistance company | Health Insurance | International Travel Insurance",
        "Additional information": "The hospital can accept cases directly from HanseMekur. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital",

    },

    "MD Medicus": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Germany",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "HanseMekur, ",
        "Assistance company": "Asian Assistance",
        "Company Type": "Assistance company | Health Insurance | International Travel Insurance",
        "Additional information": "The hospital can accept cases directly from HanseMekur. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital"
    },

    "DKV Deutsche Krankenversicherung AG": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with conditions",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Germany",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Euro Center Prague",
        "Company Type": "Health Insurance | International Travel Insurance",
        "Additional information": "The hospital cannot accept cases directly from DKV Deutsche Krankenversicherung AG. We only accept Guarantees of Payment (GOP) issued through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital"

    },

    "Malteser International": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Germany",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "HanseMekur Reiseversicherung, Huk-Coburg, Debeka, Concordia Krankenversicherung AG ",
        "Assistance company": "-",
        "Company Type": "Assistance company | Health Insurance | International Travel Insurance",
        "Additional information": "The hospital can accept cases directly from Malteser International. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital"
    },

    "Huk-Coburg": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with conditions",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Germany",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Malteser International",
        "Company Type": "International Travel Insurance",
        "Additional information": "The hospital cannot accept cases directly from Huk-Coburg. Please coordinate with your insurance provider before coming to the hospital"
    },

    "Assura": {
        "Status": "Accepted with conditions",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Switzerland",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Medicall, Asian Assistance",
        "Company Type": "Health Insurance",
        "Additional information": "The hospital cannot accept cases directly from Assura. Please coordinate with your insurance provider before coming to the hospital"
    },

    
    "CSS Gruppe": {
        "Status": "Accepted with conditions",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Switzerland",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Medicall, Asian Assistance",
        "Company Type": "Health Insurance",
        "Additional information": "The hospital cannot accept cases directly from CSS Gruppe. Please coordinate with your insurance provider before coming to the hospital"
    },

    "UNIQA Switzerland": {
        "Status": "Accepted with conditions",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Switzerland",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Medicall, Asian Assistance",
        "Company Type": "Health Insurance",
        "Additional information": "The hospital cannot accept cases directly from UNIQA Switzerland. Please coordinate with your insurance provider before coming to the hospital"
    },

    "SWICA Krankenversicherung AG": {
        "Status": "Accepted with conditions",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Switzerland",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Medicall, Asian Assistance",
        "Company Type": "Health Insurance",
        "Additional information": "The hospital cannot accept cases directly from SWICA Krankenversicherung AG. Please coordinate with your insurance provider before coming to the hospital"
    },

    "Sanitas Krankenversicherung AG": {
        "Status": "Accepted with conditions",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Switzerland",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Medicall, Asian Assistance",
        "Company Type": "Health Insurance",
        "Additional information": "The hospital cannot accept cases directly from SWICA Krankenversicherung AG. Please coordinate with your insurance provider before coming to the hospital"

    },

    "Medicall AG": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Switzerland",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "Helsana, CSS Gruppe, Assura, UNIQA, SAWICA",
        "Assistance company": "Asian Assistance",
        "Company Type": "Health Insurance",
        "Additional information": "The hospital can accept cases directly from Medicall AG. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital"
    },

    "Henner": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Direct billing accepted",
        "IPD_status": "Accepted", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "France",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Assistance company": "-",
        "Company Type": "IPMI Provider",
        "Additional information": "The hospital can accept cases directly from Henner. Direct billing may be available for outpatient treatment. However, in cases requiring hospitalization or surgery, please coordinate with Henner and request that they open the claim directly with the hospital"

    },

    "Henner VUMI": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Direct billing accepted",
        "IPD_status": "Accepted", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "France",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Assistance company": "-",
        "Company Type": "IPMI Provider",
        "Additional information": "The hospital can accept cases directly from Henner VUMI. Direct billing may be available for outpatient treatment. However, in cases requiring hospitalization or surgery, please coordinate with Henner and request that they open the claim directly with the hospital"

    },

    "MSH China": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Direct billing accepted",
        "IPD_status": "Accepted", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "China",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Assistance company": "-",
        "Company Type": "IPMI Provider",
        "Additional information": {
            "EN": """The hospital can accept cases directly from MSH China. Direct billing may be available for outpatient treatment. However, for expenses <span style='color:#b00020; font-weight:800;'>exceeding 10,000 THB</span>, or for dental treatment, optical services, health check-ups, special medications, special vaccines, high-cost medications, specialised ultrasound examinations, CT scans, MRI scans, STD treatment, chemotherapy, or radiotherapy, pre-authorisation and a GOP are required. Furthermore, for cases requiring hospitalisation or surgery, please coordinate with MSH China in advance""",
            "FR": """L’hôpital peut accepter directement les dossiers provenant de MSH China. La prise en charge directe peut être disponible pour les traitements ambulatoires. Toutefois, pour les frais <span style='color:#b00020; font-weight:800;'>dépassant 10 000 THB</span>, ou pour les soins dentaires, les services d’optique, les bilans de santé, les médicaments spéciaux, les vaccins spéciaux, les médicaments coûteux, les examens échographiques spécialisés, les scanners CT, les IRM, le traitement des MST, la chimiothérapie ou la radiothérapie, une préautorisation ainsi qu’une garantie de prise en charge (GOP) sont requises. En outre, pour les cas nécessitant une hospitalisation ou une intervention chirurgicale, veuillez coordonner avec MSH China à l’avance""",
            "DE": """Das Krankenhaus kann Fälle direkt von MSH China annehmen. Eine Direktabrechnung kann für ambulante Behandlungen verfügbar sein. Bei Kosten <span style='color:#b00020; font-weight:800;'>über 10.000 THB</span> oder bei zahnärztlichen Behandlungen, optischen Leistungen, Gesundheits-Check-ups, speziellen Medikamenten, speziellen Impfstoffen, hochpreisigen Medikamenten, speziellen Ultraschalluntersuchungen, CT-Scans, MRT-Untersuchungen, Behandlungen von sexuell übertragbaren Krankheiten, Chemotherapie oder Strahlentherapie sind jedoch eine Vorabgenehmigung sowie eine Kostenübernahmegarantie (GOP) erforderlich. Darüber hinaus bitten wir Sie, in Fällen, die einen Krankenhausaufenthalt oder eine Operation erfordern, MSH China im Voraus zu kontaktieren"""
    },

    },

    "MSH International": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Direct billing accepted",
        "IPD_status": "Accepted", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "France",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Assistance company": "-",
        "Company Type": "IPMI Provider",
        "Additional information": {
            "EN": """The hospital can accept cases directly from MSH International. Direct billing may be available for outpatient treatment. However, for expenses <span style='color:#b00020; font-weight:800;'>exceeding 10,000 THB</span>, or for dental treatment, optical services, health check-ups, special medications, special vaccines, high-cost medications, specialised ultrasound examinations, CT scans, MRI scans, STD treatment, chemotherapy, or radiotherapy, pre-authorisation and a GOP are required. Furthermore, for cases requiring hospitalisation or surgery, please coordinate with MSH International in advance""",
            "FR": """L’hôpital peut accepter directement les dossiers provenant de MSH International. La prise en charge directe peut être disponible pour les traitements ambulatoires. Toutefois, pour les frais <span style='color:#b00020; font-weight:800;'>dépassant 10 000 THB</span>, ou pour les soins dentaires, les services d’optique, les bilans de santé, les médicaments spéciaux, les vaccins spéciaux, les médicaments coûteux, les examens échographiques spécialisés, les scanners CT, les IRM, le traitement des MST, la chimiothérapie ou la radiothérapie, une préautorisation ainsi qu’une garantie de prise en charge (GOP) sont requises. En outre, pour les cas nécessitant une hospitalisation ou une intervention chirurgicale, veuillez coordonner avec MSH International à l’avance""",
            "DE": """Das Krankenhaus kann Fälle direkt von MSH International annehmen. Eine Direktabrechnung kann für ambulante Behandlungen verfügbar sein. Bei Kosten <span style='color:#b00020; font-weight:800;'>über 10.000 THB</span> oder bei zahnärztlichen Behandlungen, optischen Leistungen, Gesundheits-Check-ups, speziellen Medikamenten, speziellen Impfstoffen, hochpreisigen Medikamenten, speziellen Ultraschalluntersuchungen, CT-Scans, MRT-Untersuchungen, Behandlungen von sexuell übertragbaren Krankheiten, Chemotherapie oder Strahlentherapie sind jedoch eine Vorabgenehmigung sowie eine Kostenübernahmegarantie (GOP) erforderlich. Darüber hinaus bitten wir Sie, in Fällen, die einen Krankenhausaufenthalt oder eine Operation erfordern, MSH Internnationnal im Voraus zu kontaktieren"""
    },
    },

    "Healthmetrics": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Indonesia",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Assistance company": "APRIL Assistance Thailand",
        "Company Type": "Assistance company",
        "Additional information": "The hospital can accept cases directly from Healthmetrics. In cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please coordinate with your insurance provider"
    },

    "EMA Global Thailand": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Thailand",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client":"Mgen",
        "Assistance company": "-",
        "Company Type": "Assistance Company",
        "Additional information": "The hospital can accept cases directly from EMA Global Thailand. In cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please carefully review the GOP, as it may contain complex conditions such as deductibles, excess charges, room rate limitations, and miscellaneous fee restrictions. Please coordinate with your insurance provider"
    },

    "Aetna International": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with conditions",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "United States of America",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Allianz Worldwide Care",
        "Company Type": "Health Insurance | International Insurance",
        "Additional information": "The hospital cannot accept cases directly from Aetna International. We only accept Guarantees of Payment (GOP) issued through Allianz Worldwide Care. If no Guarantee of Payment has been sent to the hospital, treatment will proceed on a pay-and-claim basis. Please coordinate with your insurance provider before coming to the hospital"
    }, 

    "AWP Thailand Services": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted",
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Thailand",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "-",
        "Company Type": "Health Insurance | Insurance partner",
        "Additional information": "The hospital can accept cases directly from AWP Thailand Services. In cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please coordinate with your insurance provider before coming to the hospital"
    },

    "Axa Krankenversicherung AG": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with conditions",
        "OPD_note": "Assigned local assistance provider in Thailand to issue the initial Guarantee of Payment (GOP)",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "A local assistance provider in Thailand has been assigned to issue the initial Guarantee of Payment (GOP), and a final GOP must be issued before discharge. If you do not wish to wait for the final GOP, please make a deposit or proceed on a pay-and-claim reimbursement basis",
        "Country": "Germany",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "MD Medicus, Asian Assistance",
        "Company Type": "Health Insurance",""
        "Additional information": "The hospital cannot accept cases directly from AXA Krankenversicherung AG. In cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please coordinate with your insurance provider before coming to the hospital",
        
    },

    "AIG Japan": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Cashless service / An initial Guarantee of Payment (GOP) is required for travel insurance policies",
        "IPD_status": "Accepted", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Japan",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Assistance company": "Emergency Assistance Japan (EAJ)",
        "Company Type": "Travel insurance",
        "Additional information": "The hospital can accept cases directly from AIG Japan. Direct billing may be available for outpatient treatment; however, for AIG travel insurance policies, an initial Guarantee of Payment (GOP) is required for outpatient services. In cases requiring hospitalization or surgery, please coordinate with AIG Japan and request that the claim be opened directly with the hospital",

    },

    "CORIS Slovenia": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with conditions",
        "OPD_note": "Accepted via APRIL Assistance Thailand",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Accepted via APRIL Assistance Thailand",
        "Country": "Slovenia",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "APRIL Assistance Thailand",
        "Company Type": "Assistance company",
        "Additional information": "The hospital cannot accept cases directly from CORIS Slovenia; however, they have an agreement with APRIL Assistance Thailand. Please coordinate with your insurance provider before coming to the hospital, as APRIL Assistance Thailand will act on behalf of CORIS Slovenia"

    },

    "ERGO Forsikring": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with conditions",
        "OPD_note": "Accepted via Euro Center Thailand",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Accepted via Euro Center Thailand",
        "Country": "Denmark",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Euro Center Thailand",
        "Company Type": "International Travel Insurance",
        "Additional information": "The hospital cannot accept cases directly from ERGO Forsikling; however, they have an agreement with Euro Center Thailand. Please coordinate with your insurance provider before coming to the hospital, as Euro Center Thailand will act on behalf of ERGO Forsikling"

    },

    "ERGO Seguros de Viaje": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with conditions",
        "OPD_note": "Accepted via Euro Center Thailand",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Accepted via Euro Center Thailand",
        "Country": "Spain",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Euro Center Thailand",
        "Company Type": "International Travel Insurance",
        "Additional information": "The hospital cannot accept cases directly from ERGO Seguros de Viaje; however, they have an agreement with Euro Center Thailand. Please coordinate with your insurance provider before coming to the hospital, as Euro Center Thailand will act on behalf of ERGO Seguros de Viaje Sucursol"

    },

    "Pohjala Vakuutus": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with conditions",
        "OPD_note": "Accepted via Euro Center Thailand",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Accepted via Euro Center Thailand",
        "Country": "Finland",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Euro Center Thailand",
        "Company Type": "International Travel Insurance",
        "Additional information": "The hospital cannot accept cases directly from Pohjala Vakuutus; however, they have an agreement with Euro Center Thailand. Please coordinate with your insurance provider before coming to the hospital, as Euro Center Thailand will act on behalf of Pohjala Vakuutus"

    },

    "Foyer Global Healthcare": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with conditions",
        "OPD_note": "Accepted via Euro Center Thailand",
        "IPD_status": "Accepted with conditions",
        "IPD_note": "Accepted via Euro Center Thailand",
        "Country": "Luxembourg",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Euro Center Thailand",
        "Company Type": "International Travel Insurance",
        "Additional information": "The hospital cannot accept cases directly from Foyer Global Healthcare; however, they have an agreement with Euro Center Thailand. Please coordinate with your insurance provider before coming to the hospital, as Euro Center Thailand will act on behalf of Foyer Global Healthcare"

    },

    "Emergency Assistance Japan (EAJ)": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Cashless service / An initial Guarantee of Payment (GOP) is required for travel insurance policies",
        "IPD_status": "Accepted", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Japan",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "AIG Japan",
        "Assistance company": "-",
        "Company Type": "Assistance company",
        "Additional information": "The hospital can accept cases directly from Emergency Assistance Japan (EAJ). Direct billing may be available for outpatient treatment; however, in cases requiring hospitalization or surgery, please coordinate with Emergency Assistance Japan (EAJ) and request that the claim be opened directly with the hospital"
    },

    "World Travel Protection (Australia)": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Australia",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "Medibank Travel Insurance",
        "Assistance company": "-",
        "Company Type": "Assistance company",
        "Additional information": "The hospital can accept cases directly from World Travel Protection (Australia). However, in cases requiring hospitalization or surgery, please coordinate with insurance provider and request that the claim be opened directly with the hospital"
    },

    "Eurocross": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Netherlands",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Asian Assistance",
        "Company Type": "Assistance company",
        "Additional information": "The hospital can accept cases directly from Eurocross. However, for cases requiring hospitalization or surgery, arrangements may sometimes be made through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital"
    },

    "Mgen": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with conditions",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted with conditions", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "France",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "EMA Global Thailand",
        "Company Type": "Assistance company",
        "Additional information": "The hospital cannot accept cases directly from Mgen. For cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please coordinate with your insurance provider before coming to the hospital"
    },

    "William Russell": {
        "Status": "Accepted with conditions",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Accepted with conditions", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "United Kingdom",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "-",
        "Company Type": "Life insurance | Health insurance | International Travel Insurance",
        "Additional information": "The hospital can accept cases directly from William Russell. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital"

    },

    "GAPI": {
        "Status": "Accepted with conditions",
        "OPD_status": "Not Accepted",
        "OPD_note": "Pay & Claim",
        "IPD_status": "Accepted with conditions", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "France",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "VYV International Assistance (Groupe VYV)",
        "Company Type": "Health insurance | International Travel Insurance",
        "Additional information": "The hospital cannot accept cases directly from GAPI. Please coordinate with your insurance provider before coming to the hospital"

    },

    "VHI Global Healthcare": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with condition",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted with conditions", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Ireland",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "Asian Assistance",
        "Company Type": "Health insurance | International Travel Insurance",
        "Additional information": "The hospital can accept cases directly from VHI Global Healthcare. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital"

    },

    "ISON care": {
        "Status": "Accepted with conditions",
        "OPD_status": "Accepted with condition",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted with conditions", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "Poland",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "APRIL Assistance Thailand",
        "Company Type": "International Travel Insurance",
        "Additional information": "The hospital cannot accept cases directly from ISON care due to communication and email follow-up difficulties. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital"
    },

    "Roy Medical Assistance": {
        "Status": "Accepted",
        "OPD_status": "Accepted",
        "OPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "IPD_status": "Accepted", 
        "IPD_note": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "Country": "India",
        "Last_updated": "11 May 2026",
        "Contact": "-",
        "Client": "-",
        "Assistance company": "-",
        "Company Type": "Assistance company",
        "Additional information": "The hospital can accept cases directly from Roy Medical Assistance. However, after completing outpatient treatment, the patient must wait at the cashier until the hospital receives the final Guarantee of Payment (GOP). If you do not wish to wait, please make a deposit or pay upfront and claim reimbursement later. For cases requiring hospitalization or surgery, please coordinate with your insurance provider before coming to the hospital",
    },

    
    



 }






