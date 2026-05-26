import streamlit as st
import os
import textwrap
import base64
from urllib.parse import quote
from streamlit_searchbox import st_searchbox
from insurance_data import data

# Languages Translation
translations = {
 "EN": {
    "insurance_info": "Insurance information",
    "status": "Status",
    "opd": "OPD",
    "ipd": "IPD",
    "company_type": "Company Type",
    "contact": "Contact",
    "client": "Client (click to expand)",
    "assistance": "Assistance company",
    "additional": "Additional information",
    "smart_search": "Smart Insurance Search",
    "smart_search_help": "Type to search insurance provider instanly",
    "default_option": "-- Selected Insurance --",
    "please_select": "Please select an insurance provider...",
    "loading": "Checking insurance information...",
    "info_msg": "This is the preliminary result only. Final verification by hospital's international insurance staff is required.",
    "warning_msg": "For admission cases, the patient must provide a deposit prior to admission and wait until the hospital receives the final Guarantee of Payment (GOP). If there are any excess charges, the patient will be responsible for them. The refund process depends on the bank's processing time.",
    "gop_sample": "GOP Sample",

    "Accepted": "Accepted",
    "Not Accepted": "Not accepted",
    "Accepted with conditions": "Accepted with conditions",

    "January": "January",
    "February": "February",
    "March": "March",
    "April": "April",
    "May": "May",
    "June": "June",
    "July": "July",
    "August": "August",
    "September": "September",
    "October": "October",
    "November": "November",
    "December": "December",

    "Germany": "Germany",
    "Netherland": "Netherlands",
    "United Kinngdom": "United Kingdom",
    "United States of America": "United States of America",
    "France": "France",
    "Thailand": "Thailand",
    "China": "China",
    "Denmark": "Denmark",
    "Finland": "Finland",
    "Belgium": "Belgium",
    "Luxembourg": "Luxembourg",
    "Switzerland": "Switzerland",
    "Slovenia": "Slovenia",
    "Poland": "Poland",
    "India": "India",
    "Norway": "Norway",
    "Ireland": "Ireland",
    "Japan": "Japan",
    "Australia": "Australia",
    "Last updated": "Last updated",

},
 "FR": {
     "insurance_info": "Informations d'assurance",
     "status": "Statut",
     "opd": "Consultation externe",
     "ipd": "Hospitalisation",
     "company_type": "Type d'entreprise",
     "contact": "Contact",
     "client": "Client (cliquez pour ourvir)",
     "assistance": "Société d'assistance",
     "additional": "Informations supplémentaires",
     "smart_search": "Recherche intelligente d'assurannce",
     "smart_search_help": "Tapez pour rechercher une assurance instantanément",
     "default_option": "-- Sélectionner une assurance --",
     "please_select": "Veuillez sélectionner une assurance...",
     "loading": "Vérification des informations d'assurance...",
     "info_msg": "Ce résultat est préliminaire. Une vérification finale par le service d'assurance internationale de l'hôpital est requise.",
     "warning_msg": "Pour les cas d'hospitalisation, le patient doit verser un dépôt avant l'admission et attendre que l'hôpital reçoive la garantie de paiement finale (GOP). En cas de frais supplémentaires, ils seront à la charge du patient. Le délai de remboursement dépend du traitement de la banque.",
     "gop_sample": "Exemple de la lettre de la prise en charge",

     "Accepted": "Accepté",
     "Not Accepted": "Non accepté",
     "Accepted with conditions": "Accepté sous conditions",

     "January": "janvier",
     "February": "février",
     "March": "mars",
     "April": "avril",
     "May": "mai",
     "June": "juin",
     "July": "juillet",
     "August": "août",
     "September": "septembre",
     "October": "octobre",
     "November": "nnovembre",
     "December": "décembre",

     "Germany": "Allemagne",
     "Netherlands": "Pays-Bas",
     "United Kingdom": "Royaume-Uni",
     "United States of America": "États-Unis d'Amérique",
     "France": "France",
     "Thailand": "Thaïlande",
     "China": "Chine",
     "Denmark": "Danemark",
     "Finland": "Finlande",
     "Belgium": "Belgique",
     "Luxembourg": "Luxembourg",
     "Switzerland": "Suisse",
     "Slovenia": "Slovénie",
     "Poland": "Pologne",
     "India": "Indie",
     "Norway": "Norvège",
     "Ireland": "Irlande",
     "Japan": "Japon",
     "Australia": "Australie",
     "Last updated": "Dernière mise à jour",
 },
 "DE": {
     "insurance_info": "Versicherungsinformationen",
     "status": "Status",
     "opd": "Ambulante Behandlung",
     "ipd": "Stationäre Behandlung",
     "company_type": "Unternehmenstyp",
     "contact": "Kontakt",
     "client": "Kunde (zum Öffnen klicken)",
     "assistance": "Assistanzunternehmen",
     "additional": "Zusätzliche Informationen",
     "smart_search": "Intelligente Versicherungssuche",
     "smart_search_help": "Tippe Sie, um sofort nach Versicherungen zu suchen",
     "default_option": "-- Versicherung auswählenn --",
     "please_select": "Bitte wählen Sie eine Versicherung aus...",
     "loading": "Überprüfung der Versicherungsinformationen...",
     "info_msg": "Dies ist nur ein vorläufiges Ergebnis. Eine endgültige Überprüfung durch die internationale Versicherungsabteilung des Krankenhauses ist erforderlich.",
     "warning_msg": "Bei stationären Aufnahmen muss der Patient vor der Aufnahme eine Anzahlung leisten und warten, bis das Krankenhaus die endgültige Kostenübernahmegarantie (GOP) erhält. Eventuelle Mehrkosten trägt der Patient selbst. Die Rückerstattung hängt von der Bearbeitungszeit der Bank ab.",
     "gop_sample": "Muster einer Kostenübernahmegarantie",

     "Accepted": "Akzeptiert",
     "Not Accepted": "Nicht akzeptiert",
     "Accepted with conditions": "Akzeptiert mit bedingungen",

     "January": "Januar",
     "February": "Februar",
     "March": "März",
     "April": "April",
     "May": "Mai",
     "June": "Juni",
     "July": "Juli",
     "August": "August",
     "September": "September",
     "October": "Oktober",
     "November": "November",
     "December": "Dezember",

     "Germany": "Deutschland",
     "Netherlands": "Niederlande",
     "United Kingdom": "Vereinigtes Königreich",
     "United States of America": "Vereinigte Staaten von Amerika",
     "France": "Frankreich",
     "Thailand": "Thailand",
     "China": "China",
     "Denmark": "Dänemark",
     "Belgium": "Belgien",
     "Luxembourg": "Luxemburg",
     "Finland": "Finnland",
     "Switzerland": "Schweiz",
     "Slovenia": "Slowenien",
     "Poland": "Polen",
     "India": "Indien",
     "Norwey": "Norwegen",
     "Ireland": "Irland",
     "Japan": "Japan",
     "Australia": "Australien",
     "Last updated": "Zuletzt aktualisiert",


 },
     
}

note_translations = {

    "Pay & Claim": {
        "EN": "Pay & Claim",
        "FR": "Paiement puis remboursement",
        "DE": "Selbst zahlen und Rückerstattung beantragen"
        
        
    },

    "Direct billing (Depend on your policy)": {
        "EN": "Direct billing (Depend on your policy)",
        "FR": "Facturation directe (selon votre police d'assurance)",
        "DE": "Direktabrechnung (abhängig von Ihrer Police)"
        
        
    },

    "Direct billing accepted": {
        "EN": "Direct billing accepted",
        "FR": "Facturation directe acceptée",
        "DE": "Direktabrechnung akzeptiert"

    },

    "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued": {
        "EN": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued",
        "FR": "Une garantie de paiement initiale (GOP) est requise, et une garantie de paiement finale doit être émise",
        "DE": "Eine anfängliche Kostenübernahmegarantie (GOP) ist erforderlich, und eine endgültige GOP muss ausgestellt werden"
        
    },

    "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement": {
        "EN": "Initial Guarantee of Payment (GOP) is required, and a final GOP must be issued before discharge. If you do not wish to wait, please make a deposit or pay and claim reimbursement",
        "FR": "Une garantie de paiement initiale (GOP) est requise, et une GOP finale doit être émise avant la sortie. Si vous ne souhaitez pas attendre, veuillez verser un dépôt ou payer puis demander le remboursement",
        "DE": "Eine anfängliche Kostenübernahmegarantie (GOP) ist erforderlich, und eine endgültige GOP muss vor der Entlassung ausgestellt werden. Wenn Sie nicht warten möchten, leisten Sie bitte eine Kaution oder zahlen Sie selbst und beantragen anschließend die Rückerstattung"
        
    },

    "Policy begin with APA, contact APRIL Assistance Thailand requests GOP for hospitalisation, there is limitation for room cost (Depend on your policy) and home medication will be under self-pay": {
        "EN": "Policy begin with APA, contact APRIL Assistance Thailand requests GOP for hospitalisation, there is limitation for room cost (Depend on your policy) and home medication will be under self-pay",
        "FR": "Si la police commence par APA, veuillez contacter APRIL Assistance Thailand pour demander une GOP pour l'hospitalisation. Il existe une limitation des frais de chambre (selon votre police) et les médicaments à domicile seront à la charge du patient",
        "DE": "Wenn die Police mit APA beginnt, kontaktieren Sie APRIL Assistance Thailand, um eine GOP für die stationäre Behandlung anzufordern. Für die Zimmerkosten gilt eine Begrenzung (abhängig von Ihrer Police), und Medikamente für zu Hause müssen selbst bezahlt werden"

    },

    "APRIL Assistance accepts cases from partners such as SOS First Denmark, SOS International Netherlands, Gjensidige, Gouda, and the IAG Group. Kindly contact your primary insurance provider before coming to the hospital": {
        "EN": "APRIL Assistance accepts cases from partners such as SOS First Denmark, SOS International Netherlands, Gjensidige, Gouda, and the IAG Group. Kindly contact your primary insurance provider before coming to the hospital",
        "FR": "APRIL Assistance accepte les dossiers provenant de partenaires tels que SOS First Denmark, SOS International Netherlands, Gjensidige, Gouda et le groupe IAG. Veuillez contacter votre assureur principal avant de vous rendre à l'hôpital",
        "DE": "APRIL Assistance akzeptiert Fälle von Partnern wie SOS First Denmark, SOS International Netherlands, Gjensidige, Gouda und der IAG-Gruppe. Bitte kontaktieren Sie Ihren Hauptversicherer, bevor Sie ins Krankenhaus kommen",
        
    },

    "Direct billing (Depend on your policy)": {
        "EN": "Direct billing (Depend on your policy)",
        "FR": "Facturation directe (selon votre police d'assurance)",
        "DE": "Direktabrechnung (abhängig von Ihrer Versicherungspolice)"
       
    },

    "APRIL Assistance Thailand - For evacuation & repatriation": {
        "EN": "APRIL Assistance Thailand - For evacuation & repatriation",
        "FR": "APRIL Assistance Thailande – pour l’évacuation et le rapatriement",
        "DE": "APRIL Assistance Thailand – für Evakuierung und Rückführung"
        
    },

    "Direct billing can be applied up to $250 $500 $600 $750 depend on policy, in case medical expenses more than direct billing limit, GOP is required": {
        "EN": "Direct billing can be applied up to $250 $500 $600 $750 depend on policy, in case medical expenses more than direct billing limit, GOP is required",
        "FR": "La facturation directe peut être appliquée jusqu’à 250$, 500$, 600$ ou 750$ selon votre police d’assurance. En cas de frais médicaux dépassant la limite de facturation directe, une garantie de paiement (GOP) est requise",
        "DE": "Die Direktabrechnung kann je nach Versicherungspolice bis zu 250$, 500$, 600$ oder 750$ angewendet werden. Falls die medizinischen Kosten das Limit der Direktabrechnung überschreiten, ist eine Kostenübernahmegarantie (GOP) erforderlich"
    },

    "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay": {
        "EN": "Please coordinate with your insurance provider to open a claim with the hospital, otherwise, the expenses will be under self-pay",
        "FR": "Veuillez coordonner avec votre compagnie d’assurance afin d’ouvrir un dossier de prise en charge auprès de l’hôpital ; sinon, les frais seront à votre charge",
        "DE": "Bitte stimmen Sie sich mit Ihrer Versicherung ab, um im Krankenhaus einen Leistungsfall zu eröffnen; andernfalls müssen Sie die Kosten selbst tragen."
    
    },

    "The hospital does not accept direct billing from BlueCrossBlueShield. Please contact your insurer to request an initial Guarantee of Payment (GOP) for both outpatient and inpatient services. Otherwise, the expenses will be under self-pay": {
        "EN": "The hospital does not accept direct billing from BlueCrossBlueShield. Please contact your insurer to request an initial Guarantee of Payment (GOP) for both outpatient and inpatient services. Otherwise, the expenses will be under self-pay",
        "FR": "L’hôpital n’accepte pas la facturation directe de la part de BlueCross BlueShield. Veuillez contacter votre assureur afin de demander une garantie de paiement initiale (GOP) pour les soins ambulatoires et hospitaliers. Dans le cas contraire, les frais seront à votre charge",
        "DE": "Das Krankenhaus akzeptiert keine Direktabrechnung mit BlueCross BlueShield. Bitte wenden Sie sich an Ihre Versicherung, um eine anfängliche Kostenübernahmegarantie (GOP) für ambulante und stationäre Leistungen zu beantragen. Andernfalls müssen Sie die Kosten selbst tragen"
       
    },

    "The hospital does not accept direct billing from Anthem. Please contact your insurer to request an initial Guarantee of Payment (GOP) for both outpatient and inpatient services. Otherwise, the expenses will be under self-pay": {
        "EN": "The hospital does not accept direct billing from Anthem. Please contact your insurer to request an initial Guarantee of Payment (GOP) for both outpatient and inpatient services. Otherwise, the expenses will be under self-pay",
        "FR": "L’hôpital n’accepte pas la facturation directe de la part d'Anthem. Veuillez contacter votre assureur afin de demander une garantie de paiement initiale (GOP) pour les soins ambulatoires et hospitaliers. Dans le cas contraire, les frais seront à votre charge.",
        "DE": "Das Krankenhaus akzeptiert keine Direktabrechnung mit Anthem. Bitte wenden Sie sich an Ihre Versicherung, um eine anfängliche Kostenübernahmegarantie (GOP) für ambulante und stationäre Leistungen zu beantragen. Andernfalls müssen Sie die Kosten selbst tragen.",
        
    },

    "Accepted via APRIL Assistance Thailand": {
        "EN": "Accepted via APRIL Assistance Thailand",
        "FR": "Accepté via APRIL Assistance Thailand",
        "DE": "Akzeptiert über APRIL Assistance Thailand"
       
    },

    "Accepted via Euro Center Thailand": {
        "EN": "Accepted via Euro Center Thailand",
        "FR": "Accepté via Euro Center Thailand",
        "DE": "Akzeptiert über Euro Center Thailand"

    },

    "SOS First Denmark is a partner of APRIL Assistance Thailand. They will issue the initial GOP for both outpatient and inpatient services through APRIL Assistance only": {
        "EN": "SOS First Denmark is a partner of APRIL Assistance Thailand. They will issue the initial GOP for both outpatient and inpatient services through APRIL Assistance only",
        "FR": "SOS First Denmark est un partenaire d’APRIL Assistance Thailand. Ils émettront la GOP initiale pour les soins ambulatoires et hospitaliers uniquement via APRIL Assistance",
        "DE": "SOS First Denmark ist ein Partner von APRIL Assistance Thailand. Sie stellen die erste GOP für ambulante und stationäre Leistungen ausschließlich über APRIL Assistance aus",
        

    },

    "Contact via local assistance - Assist International Services, But the final decision rests with Regency Company. This company is very strict when it comes to issuing a GOP, as they require extensive medical documentation, including previous medical history and other supporting documents that may not always be necessary. As a result, many cases end up being declined and are therefore handled on a self-pay basis": {
        "EN": "Contact via local assistance - Assist International Services, But the final decision rests with Regency Company. This company is very strict when it comes to issuing a GOP, as they require extensive medical documentation, including previous medical history and other supporting documents that may not always be necessary. As a result, many cases end up being declined and are therefore handled on a self-pay basis",
        "FR": "Contact via l’assistance locale – Assist International Services. Toutefois, la décision finale revient à la société Regency. Cette société est très stricte en ce qui concerne l’émission d’une GOP, car elle exige une documentation médicale complète, y compris les antécédents médicaux et d’autres documents justificatifs qui ne sont pas toujours nécessaires. Par conséquent, de nombreux dossiers sont refusés et sont donc traités en auto-paiement",
        "DE": "Kontakt über den lokalen Assistance-Dienst – Assist International Services. Die endgültige Entscheidung liegt jedoch bei der Firma Regency. Dieses Unternehmen ist bei der Ausstellung einer GOP sehr streng, da es umfangreiche medizinische Unterlagen verlangt, einschließlich der bisherigen Krankengeschichte und weiterer unterstützender Dokumente, die nicht immer erforderlich sind. Infolgedessen werden viele Fälle abgelehnt und daher als Selbstzahler behandelt",
       
    },

    "Europ Assistance has many branches worldwide, including Belgium, Portugal, Switzerland, Argentina, Australia, Australia/New Zealand, Austria, Brazil, Canada, Chile, China, the Czech Republic, France, Germany, Greece, Hong Kong, Hungary, India, Italy, Japan, Bahrain, Jordan, Poland, Singapore, Spain, Taiwan, Thailand, Uruguay, the United States of America, Malaysia, and the Netherlands. Please inform them before going to the hospital": {
        "EN": "Europ Assistance has many branches worldwide, including Belgium, Portugal, Switzerland, Argentina, Australia, Australia/New Zealand, Austria, Brazil, Canada, Chile, China, the Czech Republic, France, Germany, Greece, Hong Kong, Hungary, India, Italy, Japan, Bahrain, Jordan, Poland, Singapore, Spain, Taiwan, Thailand, Uruguay, the United States of America, Malaysia, and the Netherlands. Please inform them before going to the hospital",
        "FR": "Europ Assistance dispose de nombreuses filiales dans le monde, notamment en Belgique, au Portugal, en Suisse, en Argentine, en Australie, en Australie/Nouvelle-Zélande, en Autriche, au Brésil, au Canada, au Chili, en Chine, en Tchéquie, en France, en Allemagne, en Grèce, à Hong Kong, en Hongrie, en Inde, en Italie, au Japon, à Bahreïn, en Jordanie, en Pologne, à Singapour, en Espagne, à Taïwan, en Thaïlande, en Uruguay, aux États-Unis d'Amérique, en Malaisie et aux Pays-Bas. Veuillez les informer avant de vous rendre à l’hôpital",
        "DE": "Europ Assistance verfügt weltweit über zahlreiche Niederlassungen, unter anderem in Belgien, Portugal, der Schweiz, Argentinien, Australien, Australien/Neuseeland, Österreich, Brasilien, Kanada, Chile, China, Tschechien, Frankreich, Deutschland, Griechenland, Hongkong, Ungarn, Indien, Italien, Japan, Bahrain, Jordanien, Polen, Singapur, Spanien, Taiwan, Thailand, Uruguay, den Vereinigten Staaten von Amerika, Malaysia und den Niederlanden. Bitte informieren Sie diese vor Ihrem Krankenhausbesuch",
        
    },

    "Falck Global Assistance is the local assistance provider in Thailand. They receive most cases from Scandinavian countries. If you hold insurance that uses Falck Global Assistance as its local partner in Thailand, please contact your primary insurance provider to open a claim": {
        "EN": "Falck Global Assistance is the local assistance provider in Thailand. They receive most cases from Scandinavian countries. If you hold insurance that uses Falck Global Assistance as its local partner in Thailand, please contact your primary insurance provider to open a claim",
        "FR": "Falck Global Assistance est le prestataire d’assistance local en Thaïlande. Ils reçoivent la majorité des dossiers en provenance des pays scandinaves. Si votre assurance utilise Falck Global Assistance comme partenaire local en Thaïlande, veuillez contacter votre assureur principal pour ouvrir un dossier",
        "DE": "Falck Global Assistance ist der lokale Assistenzdienst in Thailand. Sie erhalten die meisten Fälle aus skandinavischen Ländern. Wenn Ihre Versicherung Falck Global Assistance als lokalen Partner in Thailand nutzt, wenden Sie sich bitte an Ihren Hauptversicherer, um einen Schadenfall zu eröffnen",
        
    },

    "The hospital can accept cases directly from IMA France. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand": {
        "EN": "The hospital can accept cases directly from IMA France. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand",
        "FR": "L'hôpital peut accepter des dossiers directement de IMA France. Dans certains cas, ils peuvent également être attribués par l’intermédiaire d’un prestataire d’assistance local en Thaïlande",
        "DE": "Das Krankenhaus kann Fälle direkt von IMA France annehmen. Alternativ werden Fälle manchmal über einen lokalen Assistenzdienst in Thailand zugewiesen",
        
    },

    "The hospital can accept cases directly from IMA Benelux assistance (Belgium). Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand": {
        "EN": "The hospital can accept cases directly from IMA Benelux (Belgium). Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand",
        "FR": "L’hôpital peut accepter des dossiers directement de IMA Benelux (Belgique). Dans certains cas, les dossiers peuvent également être attribués par l’intermédiaire d’un prestataire d’assistance local en Thaïlande",
        "DE": "Das Krankenhaus kann Fälle direkt von IMA Benelux (Belgien) annehmen. Alternativ werden Fälle manchmal über einen lokalen Assistenzdienst in Thailand zugewiesen",
    
    },
    
    "The hospital can accept cases from CFE only via the assistance company VYV International Assistance (Groupe VYV). This arrangement applies to hospitalization only and cannot be used for outpatient treatment": {
        "EN": "The hospital can accept cases from CFE only via the assistance company VYV International Assistance (Groupe VYV). This arrangement applies to hospitalization only and cannot be used for outpatient treatment",
        "FR": "L’hôpital peut accepter des dossiers de la CFE uniquement via la société d’assistance VYV International Assistance (Groupe VYV). Cet accord s’applique uniquement à l’hospitalisation et ne couvre pas les soins ambulatoires",
        "DE": "Das Krankenhaus kann Fälle von der CFE nur über das Assistenzunternehmen VYV International Assistance (Groupe VYV) annehmen. Diese Regelung gilt ausschließlich für stationäre Behandlungen und nicht für ambulante Behandlungen",
        
    },

    "Accepted only via VYV International Assistance (Groupe VYV)": {
        "EN": "Accepted only via VYV International Assistance (Groupe VYV)",
        "FR": "Accepté uniquement via VYV International Assistance (Groupe VYV)",
        "DE": "Nur über VYV International Assistance (Groupe VYV) akzeptiert"
        
    },

    "The hospital can directly accept cases from VYV International Assistance (Groupe VYV) for day-case procedures and hospitalization only. As this is a social security insurance scheme for expatriates, co-payment applies: 70% is covered by the insurance and 30% is the patient’s responsibility. Medications for home use are not covered, and outpatient treatment is on a pay-and-claim basis only": {
        "EN": "The hospital can directly accept cases from VYV International Assistance (Groupe VYV) for day-case procedures and hospitalization only. As this is a social security insurance scheme for expatriates, co-payment applies: 70% is covered by the insurance and 30% is the patient’s responsibility. Medications for home use are not covered, and outpatient treatment is on a pay-and-claim basis only",
        "FR": "L’hôpital peut accepter directement des dossiers de VYV International Assistance (Groupe VYV) uniquement pour les interventions en ambulatoire (day case) et l’hospitalisation. Comme il s’agit d’un régime de sécurité sociale pour expatriés, un co-paiement s’applique : 70 % sont pris en charge par l’assurance et 30 % restent à la charge du patient. Les médicaments à domicile ne sont pas couverts, et les soins externes sont uniquement en mode « paiement puis remboursement »",
        "DE": "Das Krankenhaus kann Fälle direkt von VYV International Assistance (Groupe VYV) nur für tagesstationäre Eingriffe und stationäre Behandlungen annehmen. Da es sich um eine Sozialversicherungsregelung für Expatriates handelt, gilt eine Kostenbeteiligung: 70 % werden von der Versicherung übernommen und 30 % sind vom Patienten zu tragen. Medikamente für den Heimgebrauch sind nicht abgedeckt, und ambulante Behandlungen erfolgen ausschließlich nach dem Prinzip „zahlen und erstatten lassen“",
        
    },

    "The hospital can accept cases directly from ADAC Versicherung AG. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand, please coordinate with them prior": {
        "EN": "The hospital can accept cases directly from ADAC Versicherung AG. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand, please coordinate with them prior",
        "FR": "L’hôpital peut accepter les dossiers directement de ADAC Versicherung AG. Alternativement, les dossiers peuvent parfois être attribués par un prestataire d’assistance local en Thaïlande ; veuillez coordonner avec celui-ci au préalable",
        "DE": "Das Krankenhaus kann Fälle direkt von ADAC Versicherung AG übernehmen. Alternativ können Fälle gelegentlich über einen lokalen Assistance-Dienstleister in Thailand zugewiesen werden; bitte stimmen Sie sich vorab mit diesem ab"
    },

    "The hospital cannot accept cases directly from Helsana. In cases requiring hospitalization, please coordinate with Helsana and request that the claim be opened with the hospital through a local assistance provider in Thailand": {
        "EN": "The hospital cannot accept cases directly from Helsana. In cases requiring hospitalization, please coordinate with Helsana and request that the claim be opened with the hospital through a local assistance provider in Thailand",
        "FR": "L’hôpital ne peut pas accepter les dossiers directement de Helsana. En cas d’hospitalisation, veuillez coordonner avec Helsana et leur demander d’ouvrir le dossier auprès de l’hôpital par l’intermédiaire d’un prestataire d’assistance local en Thaïlande",
        "DE": "Das Krankenhaus kann Fälle nicht direkt von Helsana annehmen. Im Falle eines Krankenhausaufenthalts wenden Sie sich bitte an Helsana und bitten Sie darum, den Fall über einen lokalen Assistance-Dienstleister in Thailand an das Krankenhaus weiterzuleiten"
    },

    "The hospital cannot accept cases directly from SOS International Netherlands. In cases requiring outpatient or hospitalization, please coordinate with SOS Internnational and request that the claim be opened with the hospital through APRIL Assistance Thailand": {
        "EN": "The hospital cannot accept cases directly from SOS International Netherlands. In cases requiring outpatient or hospitalization, please coordinate with SOS Internnational and request that the claim be opened with the hospital through APRIL Assistance Thailand",
        "FR": "L’hôpital ne peut pas accepter directement les dossiers provenant de SOS International Netherlands. En cas de consultation externe ou d’hospitalisation, veuillez coordonner avec SOS International et demander que la prise en charge soit ouverte auprès de l’hôpital par l’intermédiaire d’APRIL Assistance Thailand",
        "DE": "Das Krankenhaus kann Fälle nicht direkt von SOS International Netherlands annehmen. In Fällen, die eine ambulante Behandlung oder einen Krankenhausaufenthalt erfordern, koordinieren Sie bitte mit SOS International und veranlassen Sie, dass die Kostenübernahme über APRIL Assistance Thailand beim Krankenhaus eröffnet wird",
    },

    "The hospital does not accept Anthem insurance due to they did not provide the coverage even coordinate with GeoBlue": {
        "EN": "The hospital does not accept Anthem insurance due to they did not provide the coverage even coordinate with GeoBlue",
        "FR": "L’hôpital n’accepte pas l’assurance Anthem, car aucune garantie de prise en charge n’a été fournie, même après coordination avec GeoBlue",
        "DE": "Das Krankenhaus akzeptiert die Anthem-Versicherung nicht, da trotz Abstimmung mit GeoBlue keine Kostenübernahmegarantie bereitgestellt wurde"
    },

    "GeoBlue is the assistance company based in the United States of America and acts on behalf of BlueCrossBlueShield, Anthem, Horizon, Highmark, Excellus, Premera, Carefirst, Florida Blue, Regence, Capital Blue, Independence, Wellmark to arrange patient referrals to network hospitals. However, coordination with the hospital may be delayed due to the time zone difference": {
        "EN": "GeoBlue is the assistance company based in the United States of America and acts on behalf of BlueCrossBlueShield, Anthem, Horizon, Hightmark, Excellus, Premera, Carefirst, Florida Blue, Regence, Capital Blue, Independence, Wellmark to arrange patient referrals to network hospitals. However, coordination with the hospital may be delayed due to the time zone difference",
        "FR": "GeoBlue est la société d’assistance basée aux États-Unis d’Amérique et agit pour le compte de BlueCross BlueShield, Anthem, Horizon, Highmark, Excellus, Premera, CareFirst, Florida Blue, Regence, Capital Blue, Independence et Wellmark afin d’organiser les orientations des patients vers les hôpitaux du réseau. Toutefois, la coordination avec l’hôpital peut être retardée en raison du décalage horaire",
        "DE": "GeoBlue ist ein in den Vereinigten Staaten von Amerika ansässiges Assistance-Unternehmen und handelt im Namen von BlueCross BlueShield, Anthem, Horizon, Highmark, Excellus, Premera, CareFirst, Florida Blue, Regence, Capital Blue, Independence und Wellmark, um Patientenüberweisungen an Krankenhäuser im Netzwerk zu organisieren. Die Koordination mit dem Krankenhaus kann sich jedoch aufgrund der Zeitverschiebung verzögern"
    },

    "An initial Guarantee of Payment (GOP) is required. Otherwise, the patient will need to settle the expenses directly with the hospital and submit a reimbursement claim afterward": {
        "EN": "An initial Guarantee of Payment (GOP) is required. Otherwise, the patient will need to settle the expenses directly with the hospital and submit a reimbursement claim afterward",
        "FR": "Une garantie de paiement initiale (GOP) est requise. À défaut, le patient devra régler directement les frais auprès de l’hôpital, puis soumettre une demande de remboursement par la suite",
        "DE": "Eine anfängliche Kostenübernahmegarantie (Guarantee of Payment – GOP) ist erforderlich. Andernfalls muss der Patient die Kosten direkt beim Krankenhaus begleichen und anschließend einen Erstattungsantrag einreichen"
    },

    "The hospital can accept cases directly from ATMS Insurance. However, as part of the insurance process, they have requested that the patient wait until the final Guarantee of Payment (GOP) is issued to the hospital. Under no circumstances should the patient be discharged before this process is completed": {
        "EN": "The hospital can accept cases directly from ATMS Insurance. However, as part of the insurance process, they have requested that the patient wait until the final Guarantee of Payment (GOP) is issued to the hospital. Under no circumstances should the patient be discharged before this process is completed",
        "FR": "L’hôpital peut accepter directement les dossiers provenant d’ATMS Insurance. Toutefois, dans le cadre de la procédure d’assurance, il a demandé que le patient attende jusqu’à l’émission de la garantie finale de paiement (GOP) à l’hôpital. Le patient ne doit en aucun cas être autorisé à sortir avant la finalisation de cette procédure",
        "DE": "Das Krankenhaus kann Fälle direkt von ATMS Insurance annehmen. Im Rahmen des Versicherungsprozesses wurde jedoch darum gebeten, dass der Patient wartet, bis die endgültige Kostenübernahmegarantie (Guarantee of Payment – GOP) an das Krankenhaus übermittelt wurde. Der Patient darf unter keinen Umständen entlassen werden, bevor dieser Vorgang abgeschlossen ist"
    },

    "The hospital can accept cases directly from CMA. However, as part of the insurance process, they have requested that the patient wait until the final Guarantee of Payment (GOP) is issued to the hospital. Under no circumstances should the patient be discharged before this process is completed": {
        "EN": "The hospital can accept cases directly from CMA. However, as part of the insurance process, they have requested that the patient wait until the final Guarantee of Payment (GOP) is issued to the hospital. Under no circumstances should the patient be discharged before this process is completed",
        "FR": "L’hôpital peut accepter directement les dossiers provenant de CMA. Toutefois, dans le cadre de la procédure d’assurance, il a demandé que le patient attende jusqu’à l’émission de la garantie finale de paiement (GOP) à l’hôpital. Le patient ne doit en aucun cas être autorisé à sortir avant la finalisation de cette procédure",
        "DE": "Das Krankenhaus kann Fälle direkt von CMA annehmen. Im Rahmen des Versicherungsprozesses wurde jedoch darum gebeten, dass der Patient wartet, bis die endgültige Kostenübernahmegarantie (Guarantee of Payment – GOP) an das Krankenhaus übermittelt wurde. Der Patient darf unter keinen Umständen entlassen werden, bevor dieser Vorgang abgeschlossen ist"

    },

    "Policies beginning with “GG” or policy number XXXXXXX: In the event of an emergency, hospitalization, or medical expenses exceeding 2,500 GBP (108,000 THB), please contact CEGA Assistance to request the initial Guarantee of Payment (GOP), as APRIL International UK does not have an in-house team to issue GOP": {
        "EN": "Policies beginning with “GG” or policy number XXXXXXX: In the event of an emergency, hospitalization, or medical expenses exceeding 2,500 GBP (108,000 THB), please contact CEGA Assistance to request the initial Guarantee of Payment (GOP), as APRIL International UK does not have an in-house team to issue GOP",
        "FR": "Les polices commençant par « GG » ou le numéro de police XXXXXXX : en cas d’urgence, d’hospitalisation ou de frais dépassant 2 500 GBP (108 000 THB), veuillez contacter CEGA Assistance afin de demander la garantie initiale de paiement (GOP), car APRIL International UK ne dispose pas d’une équipe interne pour émettre le GOP",
        "DE": "Policen, die mit „GG“ beginnen, oder Policennummer XXXXXXX: Im Falle eines Notfalls, einer Krankenhausaufnahme oder bei Kosten von mehr als 2.500 GBP (108.000 THB) wenden Sie sich bitte an CEGA Assistance, um die anfängliche Kostenübernahmegarantie (Guarantee of Payment – GOP) anzufordern, da APRIL International UK nicht über ein internes Team zur Ausstellung von GOP verfügt",
    },

    "The hospital can accept cases directly from CEGA Assistance. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital can accept cases directly from CEGA Assistance. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital peut accepter directement les dossiers provenant de CEGA Assistance. Alternativement, les dossiers peuvent parfois être attribués par l’intermédiaire d’un prestataire d’assistance local en Thaïlande. Veuillez coordonner avec votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von CEGA Assistance annehmen. Alternativ können Fälle gelegentlich über einen lokalen Assistance-Dienstleister in Thailand zugewiesen werden. Bitte stimmen Sie sich vor Ihrem Krankenhausbesuch mit Ihrer Versicherung ab"

    },

    "Gouda & Gjensidige is a partner of APRIL Assistance Thailand. They will issue the initial GOP for both outpatient and inpatient services through APRIL Assistance": {
        "EN": "Gouda & Gjensidige is a partner of APRIL Assistance Thailand. They will issue the initial GOP for both outpatient and inpatient services through APRIL Assistance",
        "FR": "Gouda & Gjensidige est partenaire d’APRIL Assistance Thailand. Ils émettront la garantie initiale de paiement (GOP) pour les services ambulatoires et d’hospitalisation par l’intermédiaire d’APRIL Assistance",
        "DE": "Gouda & Gjensidige ist ein Partner von APRIL Assistance Thailand. Die anfängliche Kostenübernahmegarantie (Guarantee of Payment – GOP) für ambulante und Stationäre Behandlung wird über APRIL Assistance ausgestellt"

    },

     "The hospital can accept cases directly from IMG UK. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital can accept cases directly from IMG UK. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital peut accepter directement les dossiers provenant d’IMG UK. Alternativement, les dossiers peuvent parfois être attribués par l’intermédiaire d’un prestataire d’assistance local en Thaïlande. Veuillez coordonner avec votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von IMG UK annehmen. Alternativ können Fälle gelegentlich über einen lokalen Assistance-Dienstleister in Thailand zugewiesen werden. Bitte stimmen Sie sich vor Ihrem Krankenhausbesuch mit Ihrer Versicherung ab"

    },

    "The hospital can accept cases directly from IMG USA. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital can accept cases directly from IMG USA. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital peut accepter directement les dossiers provenant d’IMG USA. Alternativement, les dossiers peuvent parfois être attribués par l’intermédiaire d’un prestataire d’assistance local en Thaïlande. Veuillez coordonner avec votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von IMG USA annehmen. Alternativ können Fälle gelegentlich über einen lokalen Assistance-Dienstleister in Thailand zugewiesen werden. Bitte stimmen Sie sich vor Ihrem Krankenhausbesuch mit Ihrer Versicherung ab"

    },

    "The hospital can accept cases directly from Assist International Services (AIS), Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital can accept cases directly from Assist International Services (AIS), Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital peut accepter directement les dossiers provenant d’Assist International Services (AIS). Veuillez coordonner avec votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von Assist International Services (AIS) annehmen. Bitte stimmen Sie sich vor Ihrem Krankenhausbesuch mit Ihrer Versicherung ab"
    },

    "The hospital cannot accept cases directly from WrLife. We only accept Guarantees of Payment (GOP) issued through Assist International Services (AIS). Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital cannot accept cases directly from WrLife. We only accept Guarantees of Payment (GOP) issued through Assist International Services (AIS). Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital ne peut pas accepter directement les dossiers provenant de WrLife. Nous acceptons uniquement les garanties de paiement (GOP) émises par l’intermédiaire d’Assist International Services (AIS). Veuillez coordonner avec votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle nicht direkt von WrLife annehmen. Wir akzeptieren ausschließlich Kostenübernahmegarantien (Guarantees of Payment – GOP), die über Assist International Services (AIS) ausgestellt werden. Bitte stimmen Sie sich vor Ihrem Krankenhausbesuch mit Ihrer Versicherung ab"
    },

    "There is no contract with the hospital; therefore, the case will be handled under a pay-and-claim process": {
        "EN": "There is no contract with the hospital; therefore, the case will be handled under a pay-and-claim process",
        "FR": "Il n’existe aucun contrat avec l’hôpital ; le dossier sera donc traité selon une procédure de paiement et remboursement",
        "DE": "Es besteht kein Vertrag mit dem Krankenhaus; daher wird der Fall im Rahmen eines „Pay-and-Claim“-Verfahrens abgewickelt"
    },

    "The hospital can accept cases directly from HanseMekur. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital can accept cases directly from HanseMekur. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital peut accepter directement les dossiers provenant de HanseMerkur. Alternativement, les dossiers peuvent parfois être attribués par l’intermédiaire d’un prestataire d’assistance local en Thaïlande. Veuillez coordonner avec votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von HanseMerkur annehmen. Alternativ können Fälle gelegentlich über einen lokalen Assistance-Dienstleister in Thailand zugewiesen werden. Bitte stimmen Sie sich vor Ihrem Krankenhausbesuch mit Ihrer Versicherung ab"

    },

    "The hospital cannot accept cases directly from DKV Deutsche Krankenversicherung AG. We only accept Guarantees of Payment (GOP) issued through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital cannot accept cases directly from DKV Deutsche Krankenversicherung AG. We only accept Guarantees of Payment (GOP) issued through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital ne peut pas accepter directement les dossiers provenant de DKV Deutsche Krankenversicherung AG. Nous acceptons uniquement les garanties de paiement (GOP) émises par l’intermédiaire d’un prestataire d’assistance local en Thaïlande. Veuillez coordonner avec votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle nicht direkt von DKV Deutsche Krankenversicherung AG annehmen. Wir akzeptieren ausschließlich Kostenübernahmegarantien (Guarantees of Payment – GOP), die über einen lokalen Assistance-Dienstleister in Thailand ausgestellt werden. Bitte stimmen Sie sich vor Ihrem Krankenhausbesuch mit Ihrer Versicherung ab",
    },

    "The hospital cannot accept cases directly from Huk-Coburg. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital cannot accept cases directly from Huk-Coburg. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital ne peut pas accepter directement les dossiers de Huk-Coburg. Veuillez contacter votre compagnie d’assurance avant de vous rendre à l’hôpital.",
        "DE": "Das Krankenhaus kann keine Fälle direkt von Huk-Coburg akzeptieren. Bitte stimmen Sie sich vor Ihrem Besuch im Krankenhaus mit Ihrer Versicherung ab",

    },
    
    "The hospital cannot accept cases directly from CSS Gruppe. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital cannot accept cases directly from CSS Gruppe. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital ne peut pas accepter directement les dossiers de CSS Gruppe. Veuillez contacter votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann keine Fälle direkt von CSS Gruppe akzeptieren. Bitte stimmen Sie sich vor Ihrem Besuch im Krankenhaus mit Ihrer Versicherung ab"

    },

    "The hospital cannot accept cases directly from Assura. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital cannot accept cases directly from Assura. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital ne peut pas accepter directement les dossiers d’Assura. Veuillez contacter votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann keine Fälle direkt von Assura akzeptieren. Bitte stimmen Sie sich vor Ihrem Besuch im Krankenhaus mit Ihrer Versicherung ab"
    },

    "The hospital cannot accept cases directly from UNIQA Switzerland. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital cannot accept cases directly from UNIQA Switzerland. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital ne peut pas accepter directement les dossiers d’UNIQA Switzerland. Veuillez contacter votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann keine Fälle direkt von UNIQA Switzerland akzeptieren. Bitte stimmen Sie sich vor Ihrem Besuch im Krankenhaus mit Ihrer Versicherung ab"
    },

    "The hospital cannot accept cases directly from SWICA Krankenversicherung AG. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital cannot accept cases directly from SWICA Krankenversicherung AG. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital ne peut pas accepter directement les dossiers de SWICA Krankenversicherug AG. Veuillez contacter votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann keine Fälle direkt von SWICA Krankenversicherug AG akzeptieren. Bitte stimmen Sie sich vor Ihrem Besuch im Krankenhaus mit Ihrer Versicherung ab"
    },

    "The hospital can accept cases directly from Medicall AG. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital":{
        "EN": "The hospital can accept cases directly from Medicall AG. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital peut accepter directement les dossiers de Medicall AG. Dans certains cas, les dossiers peuvent également être pris en charge par un prestataire d’assistance local en Thaïlande. Veuillez contacter votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von Medicall AG akzeptieren. Alternativ können Fälle manchmal über einen lokalen Assistance-Dienstleister in Thailand vermittelt werden. Bitte stimmen Sie sich vor Ihrem Besuch im Krankenhaus mit Ihrer Versicherung ab"
    
    },

    "The hospital accept only policy begin with PXXXXXXXXX. Direct billing may be available depending on the policy (this can be checked in the AWC portal). In cases involving high medical expenses, special procedures, vaccinations, special medications, high-cost medications, chemotherapy, or radiotherapy, a GOP is required. PLEASE CONFIRM with the International Insurance staff first": {
        "EN": "The hospital accept only policy begin with PXXXXXXXXX. Direct billing may be available depending on the policy (this can be checked in the AWC portal). In cases involving high medical expenses, special procedures, vaccinations, special medications, high-cost medications, chemotherapy, or radiotherapy, a GOP is required. PLEASE CONFIRM with the International Insurance staff first",
        "FR": "L’hôpital accepte uniquement les polices d’assurance commençant par « PXXXXXXXXX » La facturation directe peut être applicable selon la police d’assurance (cela peut être vérifié sur le portail AWC). En cas de frais médicaux élevés, de procédures spéciales, de vaccinations, de médicaments spéciaux, de médicaments coûteux, de chimiothérapie ou de radiothérapie, une GOP est requise. VEUILLEZ D’ABORD CONFIRMER avec le personnel du service des assurances internationales.",
        "DE": "Das Krankenhaus akzeptiert nur Versicherungspolicen, die mit „PXXXXXXXXX“ beginnen. Direktabrechnung kann je nach Versicherungspolice möglich sein (dies kann im AWC-Portal überprüft werden). Bei hohen medizinischen Kosten, speziellen Behandlungen, Impfungen, Spezialmedikamenten, hochpreisigen Medikamenten, Chemotherapie oder Strahlentherapie ist eine GOP erforderlich. BITTE bestätigen Sie dies zuerst mit dem Personal der internationalen Versicherungsabteilung.",
    },

    "The hospital accepts only policies beginning with ‘PXXXXXXXXX’ (gold insurance card). A deductible of USD 27 applies to the doctor’s fee. Direct billing may be available depending on the policy (this can be checked in the AWC portal). In cases involving high medical expenses, special procedures, vaccinations, special medications, high-cost medications, chemotherapy, or radiotherapy, a GOP is required. PLEASE CONFIRM with the International Insurance staff first": {
        "EN": "The hospital accepts only policies beginning with ‘PXXXXXXXXX’ (gold insurance card). A deductible of USD 27 applies to the doctor’s fee. Direct billing may be available depending on the policy (this can be checked in the AWC portal). In cases involving high medical expenses, special procedures, vaccinations, special medications, high-cost medications, chemotherapy, or radiotherapy, a GOP is required. PLEASE CONFIRM with the International Insurance staff first",
        "FR": "L’hôpital accepte uniquement les polices d’assurance commençant par « PXXXXXXXXX » (carte d’assurance dorée). Une franchise de 27 USD s’applique aux honoraires du médecin. La facturation directe peut être applicable selon la police d’assurance (cela peut être vérifié sur le portail AWC). En cas de frais médicaux élevés, de procédures spéciales, de vaccinations, de médicaments spéciaux, de médicaments coûteux, de chimiothérapie ou de radiothérapie, une GOP est requise. VEUILLEZ D’ABORD CONFIRMER avec le personnel du service des assurances internationales",
        "DE": "Das Krankenhaus akzeptiert nur Versicherungspolicen, die mit „PXXXXXXXXX“ beginnen (goldene Versicherungskarte). Für das Arzthonorar fällt ein Selbstbehalt von 27 USD an. Direktabrechnung kann je nach Versicherungspolice möglich sein (dies kann im AWC-Portal überprüft werden). Bei hohen medizinischen Kosten, speziellen Behandlungen, Impfungen, Spezialmedikamenten, hochpreisigen Medikamenten, Chemotherapie oder Strahlentherapie ist eine GOP erforderlich. BITTE bestätigen Sie dies zuerst mit dem Personal der internationalen Versicherungsabteilung"
    },

    "The hospital can accept cases directly from Henner. Direct billing may be available for outpatient treatment. However, in cases requiring hospitalization or surgery, please coordinate with Henner and request that they open the claim directly with the hospital": {
        "EN": "The hospital can accept cases directly from Henner. Direct billing may be available for outpatient treatment. However, in cases requiring hospitalization or surgery, please coordinate with Henner and request that they open the claim directly with the hospital",
        "FR": "L’hôpital peut accepter directement les dossiers de Henner. La facturation directe peut être disponible pour les soins ambulatoires. Toutefois, en cas d’hospitalisation ou de chirurgie, veuillez contacter Henner et leur demander d’ouvrir le dossier directement auprès de l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von Henner akzeptieren. Direktabrechnung kann für ambulante Behandlungen möglich sein. Im Falle eines Krankenhausaufenthalts oder einer Operation wenden Sie sich bitte an Henner und bitten Sie darum, den Leistungsfall direkt beim Krankenhaus zu eröffnen"

    },

    "The hospital can accept cases directly from Henner VUMI. Direct billing may be available for outpatient treatment. However, in cases requiring hospitalization or surgery, please coordinate with Henner and request that they open the claim directly with the hospital": {
        "EN": "The hospital can accept cases directly from Henner VUMI. Direct billing may be available for outpatient treatment. However, in cases requiring hospitalization or surgery, please coordinate with Henner and request that they open the claim directly with the hospital",
        "FR": "L’hôpital peut accepter directement les dossiers de Henner VUMI. La facturation directe peut être disponible pour les soins ambulatoires. Toutefois, en cas d’hospitalisation ou de chirurgie, veuillez contacter Henner et leur demander d’ouvrir le dossier directement auprès de l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von Henner VUMI akzeptieren. Direktabrechnung kann für ambulante Behandlungen möglich sein. Im Falle eines Krankenhausaufenthalts oder einer Operation wenden Sie sich bitte an Henner und bitten Sie darum, den Leistungsfall direkt beim Krankenhaus zu eröffnen"

    },

    "The hospital can accept cases directly from MSH China. Direct billing may be available for outpatient treatment. However, for expenses exceeding 10,000 THB, or for dental treatment, optical services, health check-ups, special medications, special vaccines, high-cost medications, specialised ultrasound examinations, CT scans, MRI scans, STD treatment, chemotherapy, or radiotherapy, pre-authorisation and a GOP are required. Furthermore, for cases requiring hospitalisation or surgery, please coordinate with MSH China in advance": {
        "EN": "The hospital can accept cases directly from MSH China. Direct billing may be available for outpatient treatment. However, for expenses exceeding 10,000 THB, or for dental treatment, optical services, health check-ups, special medications, special vaccines, high-cost medications, specialised ultrasound examinations, CT scans, MRI scans, STD treatment, chemotherapy, or radiotherapy, pre-authorisation and a GOP are required. Furthermore, for cases requiring hospitalisation or surgery, please coordinate with MSH China in advance",
        "FR": "L’hôpital peut accepter directement les dossiers provenant de MSH China. La prise en charge directe peut être disponible pour les traitements ambulatoires. Toutefois, pour les frais dépassant 10 000 THB, ou pour les soins dentaires, les services d’optique, les bilans de santé, les médicaments spéciaux, les vaccins spéciaux, les médicaments coûteux, les examens échographiques spécialisés, les scanners CT, les IRM, le traitement des MST, la chimiothérapie ou la radiothérapie, une préautorisation ainsi qu’une garantie de prise en charge (GOP) sont requises. En outre, pour les cas nécessitant une hospitalisation ou une intervention chirurgicale, veuillez coordonner avec MSH China à l’avance",
        "DE": "Das Krankenhaus kann Fälle direkt von MSH China annehmen. Eine Direktabrechnung kann für ambulante Behandlungen verfügbar sein. Bei Kosten über 10.000 THB oder bei zahnärztlichen Behandlungen, optischen Leistungen, Gesundheits-Check-ups, speziellen Medikamenten, speziellen Impfstoffen, hochpreisigen Medikamenten, speziellen Ultraschalluntersuchungen, CT-Scans, MRT-Untersuchungen, Behandlungen von sexuell übertragbaren Krankheiten, Chemotherapie oder Strahlentherapie sind jedoch eine Vorabgenehmigung sowie eine Kostenübernahmegarantie (GOP) erforderlich. Darüber hinaus bitten wir Sie, in Fällen, die einen Krankenhausaufenthalt oder eine Operation erfordern, MSH China im Voraus zu kontaktieren"
    },

    "The hospital can accept cases directly from MSH International. Direct billing may be available for outpatient treatment. However, for expenses exceeding 10,000 THB, or for dental treatment, optical services, health check-ups, special medications, special vaccines, high-cost medications, specialised ultrasound examinations, CT scans, MRI scans, STD treatment, chemotherapy, or radiotherapy, pre-authorisation and a GOP are required. Furthermore, for cases requiring hospitalisation or surgery, please coordinate with MSH International in advance": {
        "EN": "The hospital can accept cases directly from MSH International. Direct billing may be available for outpatient treatment. However, for expenses exceeding 10,000 THB, or for dental treatment, optical services, health check-ups, special medications, special vaccines, high-cost medications, specialised ultrasound examinations, CT scans, MRI scans, STD treatment, chemotherapy, or radiotherapy, pre-authorisation and a GOP are required. Furthermore, for cases requiring hospitalisation or surgery, please coordinate with MSH International in advance",
        "FR": "L’hôpital peut accepter directement les dossiers provenant de MSH International. La prise en charge directe peut être disponible pour les traitements ambulatoires. Toutefois, pour les frais dépassant 10 000 THB, ou pour les soins dentaires, les services d’optique, les bilans de santé, les médicaments spéciaux, les vaccins spéciaux, les médicaments coûteux, les examens échographiques spécialisés, les scanners CT, les IRM, le traitement des MST, la chimiothérapie ou la radiothérapie, une préautorisation ainsi qu’une garantie de prise en charge (GOP) sont requises. En outre, pour les cas nécessitant une hospitalisation ou une intervention chirurgicale, veuillez coordonner avec MSH International à l’avance",
        "DE": "Das Krankenhaus kann Fälle direkt von MSH China annehmen. Eine Direktabrechnung kann für ambulante Behandlungen verfügbar sein. Bei Kosten über 10.000 THB oder bei zahnärztlichen Behandlungen, optischen Leistungen, Gesundheits-Check-ups, speziellen Medikamenten, speziellen Impfstoffen, hochpreisigen Medikamenten, speziellen Ultraschalluntersuchungen, CT-Scans, MRT-Untersuchungen, Behandlungen von sexuell übertragbaren Krankheiten, Chemotherapie oder Strahlentherapie sind jedoch eine Vorabgenehmigung sowie eine Kostenübernahmegarantie (GOP) erforderlich. Darüber hinaus bitten wir Sie, in Fällen, die einen Krankenhausaufenthalt oder eine Operation erfordern, MSH International im Voraus zu kontaktieren"
    },

    "The hospital can accept cases directly from Healthmetrics. In cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please coordinate with your insurance provider": {
        "EN": "The hospital can accept cases directly from Healthmetrics. In cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please coordinate with your insurance provider",
        "FR": "L’hôpital peut accepter directement les dossiers provenant de Healthmetrics. En cas d’hospitalisation ou d’intervention chirurgicale, une garantie de prise en charge (GOP) initiale est requise, et une GOP finale devra ensuite être émise. Veuillez coordonner avec votre assureur",
        "DE": "Das Krankenhaus kann Fälle direkt von Healthmetrics annehmen. In Fällen, die einen Krankenhausaufenthalt oder eine Operation erfordern, ist zunächst eine Kostenübernahmegarantie (Guarantee of Payment – GOP) erforderlich; anschließend muss eine endgültige GOP ausgestellt werden. Bitte stimmen Sie sich mit Ihrem Versicherungsanbieter ab"
    },

    "The hospital can accept cases directly from EMA Global Thailand. In cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please carefully review the GOP, as it may contain complex conditions such as deductibles, excess charges, room rate limitations, and miscellaneous fee restrictions. Please coordinate with your insurance provider": {
        "EN": "The hospital can accept cases directly from EMA Global Thailand. In cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please carefully review the GOP, as it may contain complex conditions such as deductibles, excess charges, room rate limitations, and miscellaneous fee restrictions. Please coordinate with your insurance provider",
        "FR": "L’hôpital peut accepter directement les dossiers provenant d’EMA Global Thailand. En cas d’hospitalisation ou d’intervention chirurgicale, une garantie de prise en charge (GOP) initiale est requise, et une GOP finale devra ensuite être émise. Veuillez examiner attentivement la GOP, car elle peut comporter des conditions complexes telles que des franchises, des participations excédentaires, des limitations des frais de chambre et des restrictions concernant les frais divers. Veuillez coordonner avec votre assureur",
        "DE": "Das Krankenhaus kann Fälle direkt von EMA Global Thailand annehmen. In Fällen, die einen Krankenhausaufenthalt oder eine Operation erfordern, ist zunächst eine Kostenübernahmegarantie (Guarantee of Payment – GOP) erforderlich; anschließend muss eine endgültige GOP ausgestellt werden. Bitte prüfen Sie die GOP sorgfältig, da sie komplexe Bedingungen wie Selbstbehalte, Zusatzkosten, Begrenzungen der Zimmerkosten sowie Einschränkungen bei sonstigen Gebühren enthalten kann. Bitte stimmen Sie sich mit Ihrem Versicherungsanbieter ab"
    },

    "The hospital cannot accept cases directly from Aetna International. We only accept Guarantees of Payment (GOP) issued through Allianz Worldwide Care. If no Guarantee of Payment has been sent to the hospital, treatment will proceed on a pay-and-claim basis. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital cannot accept cases directly from Aetna International. We only accept Guarantees of Payment (GOP) issued through Allianz Worldwide Care. If no Guarantee of Payment has been sent to the hospital, treatment will proceed on a pay-and-claim basis. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital ne peut pas accepter directement les dossiers provenant d’Aetna International. Nous acceptons uniquement les garanties de prise en charge (GOP) émises par l’intermédiaire d’Allianz Worldwide Care. Si aucune GOP n’a été envoyée à l’hôpital, les frais devront être réglés par le patient avant remboursement selon la procédure de remboursement (« pay and claim »). Veuillez coordonner avec votre assureur avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle von Aetna International nicht direkt annehmen. Wir akzeptieren ausschließlich Kostenübernahmegarantien (Guarantee of Payment – GOP), die über Allianz Worldwide Care ausgestellt werden. Wenn keine GOP an das Krankenhaus übermittelt wurde, erfolgt die Behandlung auf Basis eines „Pay-and-Claim“-Verfahrens. Bitte stimmen Sie sich vor Ihrem Krankenhausbesuch mit Ihrem Versicherungsanbieter ab",
    },

    "The hospital can accept cases directly from AWP Thailand Services. In cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital can accept cases directly from AWP Thailand Services. In cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital peut accepter directement les dossiers provenant d’AWP Thailand Services. En cas d’hospitalisation ou d’intervention chirurgicale, une garantie de prise en charge (GOP) initiale est requise, et une GOP finale devra ensuite être émise. Veuillez coordonner avec votre assureur avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von AWP Thailand Services annehmen. In Fällen, die einen Krankenhausaufenthalt oder eine Operation erfordern, ist zunächst eine Kostenübernahmegarantie (Guarantee of Payment – GOP) erforderlich; anschließend muss eine endgültige GOP ausgestellt werden. Bitte stimmen Sie sich vor Ihrem Krankenhausbesuch mit Ihrem Versicherungsanbieter ab"
    },

    "Assigned local assistance provider in Thailand to issue the initial Guarantee of Payment (GOP)": {
        "EN": "Assigned local assistance provider in Thailand to issue the initial Guarantee of Payment (GOP)",
        "FR": "Prestataire d’assistance local désigné en Thaïlande pour émettre la garantie de prise en charge (GOP) initiale",
        "DE": "Beauftragter lokaler Assistance-Dienstleister in Thailand zur Ausstellung der ersten Kostenübernahmegarantie (GOP)"
    },

    "A local assistance provider in Thailand has been assigned to issue the initial Guarantee of Payment (GOP), and a final GOP must be issued before discharge. If you do not wish to wait for the final GOP, please make a deposit or proceed on a pay-and-claim reimbursement basis": {
        "EN": "A local assistance provider in Thailand has been assigned to issue the initial Guarantee of Payment (GOP), and a final GOP must be issued before discharge. If you do not wish to wait for the final GOP, please make a deposit or proceed on a pay-and-claim reimbursement basis",
        "FR": "Un prestataire d’assistance local en Thaïlande a été désigné pour émettre la garantie de prise en charge (GOP) initiale, et une GOP finale devra être émise avant la sortie de l’hôpital. Si vous ne souhaitez pas attendre la GOP finale, veuillez effectuer un dépôt ou procéder selon la procédure de remboursement (« pay and claim »)",
        "DE": "Ein lokaler Assistance-Dienstleister in Thailand wurde beauftragt, die erste Kostenübernahmegarantie (GOP) auszustellen; zudem muss vor der Entlassung eine endgültige GOP ausgestellt werden. Falls Sie nicht auf die endgültige GOP warten möchten, leisten Sie bitte eine Vorauszahlung oder nutzen Sie das „Pay-and-Claim“-Erstattungsverfahren"
    },

    "The hospital cannot accept cases directly from AXA Krankenversicherung AG. In cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital cannot accept cases directly from AXA Krankenversicherung AG. In cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital ne peut pas accepter directement les dossiers provenant d’AXA Krankenversicherung AG. En cas d’hospitalisation ou d’intervention chirurgicale, une garantie de prise en charge (GOP) initiale est requise, et une GOP finale devra ensuite être émise. Veuillez coordonner avec votre assureur avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle von AXA Krankenversicherung AG nicht direkt annehmen. In Fällen, die einen Krankenhausaufenthalt oder eine Operation erfordern, ist zunächst eine Kostenübernahmegarantie (Guarantee of Payment – GOP) erforderlich; anschließend muss eine endgültige GOP ausgestellt werden. Bitte stimmen Sie sich vor Ihrem Krankenhausbesuch mit Ihrem Versicherungsanbieter ab"
    },

    "Cashless service / An initial Guarantee of Payment (GOP) is required for travel insurance policies": {
        "EN": "Cashless service / An initial Guarantee of Payment (GOP) is required for travel insurance policies",
        "FR": "Service de prise en charge directe (« cashless ») / Une garantie de prise en charge (GOP) initiale est requise pour les polices d’assurance voyage",
        "DE": "Direktabrechnungsservice („Cashless Service“) / Für Reiseversicherungspolicen ist eine erste Kostenübernahmegarantie (GOP) erforderlich"

    },

    "The hospital can accept cases directly from AIG Japan. Direct billing may be available for outpatient treatment; however, for AIG travel insurance policies, an initial Guarantee of Payment (GOP) is required for outpatient services. In cases requiring hospitalization or surgery, please coordinate with AIG Japan and request that the claim be opened directly with the hospital": {
        "EN": "The hospital can accept cases directly from AIG Japan. Direct billing may be available for outpatient treatment; however, for AIG travel insurance policies, an initial Guarantee of Payment (GOP) is required for outpatient services. In cases requiring hospitalization or surgery, please coordinate with AIG Japan and request that the claim be opened directly with the hospital",
        "FR": "L’hôpital peut accepter directement les dossiers provenant d’AIG Japan. La prise en charge directe peut être disponible pour les traitements ambulatoires ; toutefois, pour les polices d’assurance voyage AIG, une garantie de prise en charge (GOP) initiale est requise pour les soins ambulatoires. En cas d’hospitalisation ou d’intervention chirurgicale, veuillez coordonner avec AIG Japan et leur demander d’ouvrir directement le dossier de prise en charge auprès de l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von AIG Japan annehmen. Eine Direktabrechnung kann für ambulante Behandlungen möglich sein; für Reiseversicherungspolicen von AIG ist jedoch eine erste Kostenübernahmegarantie (GOP) für ambulante Leistungen erforderlich. In Fällen, die einen Krankenhausaufenthalt oder eine Operation erfordern, wenden Sie sich bitte an AIG Japan und bitten Sie darum, den Leistungsfall direkt mit dem Krankenhaus zu eröffnen"
    },

    "The hospital cannot accept cases directly from CORIS Slovenia; however, they have an agreement with APRIL Assistance Thailand. Please coordinate with your insurance provider before coming to the hospital, as APRIL Assistance Thailand will act on behalf of CORIS Slovenia": {
        "EN": "The hospital cannot accept cases directly from CORIS Slovenia; however, they have an agreement with APRIL Assistance Thailand. Please coordinate with your insurance provider before coming to the hospital, as APRIL Assistance Thailand will act on behalf of CORIS Slovenia",
        "FR": "L’hôpital ne peut pas accepter directement les dossiers provenant de CORIS Slovenia ; toutefois, un accord est en place avec APRIL Assistance Thailand. Veuillez coordonner avec votre assureur avant de vous rendre à l’hôpital, car APRIL Assistance Thailand agira au nom de CORIS Slovenia",
        "DE": "Das Krankenhaus kann Fälle von CORIS Slovenia nicht direkt annehmen; es besteht jedoch eine Vereinbarung mit APRIL Assistance Thailand. Bitte stimmen Sie sich vor Ihrem Krankenhausbesuch mit Ihrem Versicherungsanbieter ab, da APRIL Assistance Thailand im Namen von CORIS Slovenia tätig wird",
    },

    "The hospital cannot accept cases directly from ERGO Seguros de Viaje; however, they have an agreement with Euro Center Thailand. Please coordinate with your insurance provider before coming to the hospital, as Euro Center Thailand will act on behalf of ERGO Seguros de Viaje Sucursol": {
        "EN": "The hospital cannot accept cases directly from ERGO Seguros de Viaje; however, they have an agreement with Euro Center Thailand. Please coordinate with your insurance provider before coming to the hospital, as Euro Center Thailand will act on behalf of ERGO Seguros de Viaje Sucursol",
        "FR": "L’hôpital ne peut pas accepter directement les dossiers provenant d’ERGO Seguros de Viaje ; toutefois, un accord est en place avec Euro Center Thailand. Veuillez coordonner avec votre assureur avant de vous rendre à l’hôpital, car Euro Center Thailand agira au nom d’ERGO Seguros de Viaje Sucursal",
        "DE": "Das Krankenhaus kann Fälle von ERGO Seguros de Viaje nicht direkt annehmen; es besteht jedoch eine Vereinbarung mit Euro Center Thailand. Bitte stimmen Sie sich vor Ihrem Krankenhausbesuch mit Ihrem Versicherungsanbieter ab, da Euro Center Thailand im Namen von ERGO Seguros de Viaje Sucursal tätig wird"
    },

    "The hospital cannot accept cases directly from Pohjala Vakuutus; however, they have an agreement with Euro Center Thailand. Please coordinate with your insurance provider before coming to the hospital, as Euro Center Thailand will act on behalf of Pohjala Vakuutus": {
        "EN": "The hospital cannot accept cases directly from Pohjala Vakuutus; however, they have an agreement with Euro Center Thailand. Please coordinate with your insurance provider before coming to the hospital, as Euro Center Thailand will act on behalf of Pohjala Vakuutus",
        "FR": "L’hôpital ne peut pas accepter directement les dossiers provenant de Pohjola Vakuutus ; toutefois, un accord est en place avec Euro Center Thailand. Veuillez coordonner avec votre assureur avant de vous rendre à l’hôpital, car Euro Center Thailand agira au nom de Pohjola Vakuutus",
        "DE": "Das Krankenhaus kann Fälle von Pohjola Vakuutus nicht direkt annehmen; es besteht jedoch eine Vereinbarung mit Euro Center Thailand. Bitte stimmen Sie sich vor Ihrem Krankenhausbesuch mit Ihrem Versicherungsanbieter ab, da Euro Center Thailand im Namen von Pohjola Vakuutus tätig wird"
    },

    "The hospital cannot accept cases directly from Foyer Global Healthcare; however, they have an agreement with Euro Center Thailand. Please coordinate with your insurance provider before coming to the hospital, as Euro Center Thailand will act on behalf of Foyer Global Healthcare": {
        "EN": "The hospital cannot accept cases directly from Foyer Global Healthcare; however, they have an agreement with Euro Center Thailand. Please coordinate with your insurance provider before coming to the hospital, as Euro Center Thailand will act on behalf of Foyer Global Healthcare",
        "FR": "L’hôpital ne peut pas accepter directement les dossiers provenant de Foyer Global Healthcare ; toutefois, un accord est en place avec Euro Center Thailand. Veuillez coordonner avec votre assureur avant de vous rendre à l’hôpital, car Euro Center Thailand agira au nom de Foyer Global Healthcare",
        "DE": "Das Krankenhaus kann Fälle von Foyer Global Healthcare nicht direkt annehmen; es besteht jedoch eine Vereinbarung mit Euro Center Thailand. Bitte stimmen Sie sich vor Ihrem Krankenhausbesuch mit Ihrem Versicherungsanbieter ab, da Euro Center Thailand im Namen von Foyer Global Healthcare tätig wird"
    },

    "Cashless service / A Guarantee of Payment (GOP) is required for high-cost medical expenses exceeding THB 15,000. Please refer to the additional information below for further details": {
        "EN": "Cashless service / A Guarantee of Payment (GOP) is required for high-cost medical expenses exceeding THB 15,000. Please refer to the additional information below for further details",
        "FR": "Service de prise en charge directe (« cashless ») / Une garantie de prise en charge (GOP) est requise pour les frais médicaux élevés dépassant 15 000 THB. Veuillez consulter les informations complémentaires ci-dessous pour plus de détails",
        "DE": "Direktabrechnungsservice („Cashless Service“) / Eine Kostenübernahmegarantie (GOP) ist bei hohen medizinischen Kosten über 15.000 THB erforderlich. Weitere Details entnehmen Sie bitte den nachstehenden Zusatzinformationen"
    },

    "For AXA Global Health (AXA PPP), direct billing is available for outpatient visits with medical expenses not exceeding THB 15,000 (including specialist consultations), laboratory tests, blood tests, acne medications, procedures, eye/ear drops, medications & dressings, and physiotherapy (limited to a maximum of 5 sessions per facility). Pre-authorisation is required for outpatient visits exceeding THB 15,000, more than 5 physiotherapy sessions at the same facility, psychiatric consultations, gynecological conditions (e.g. PCOS, menopause), CT scans, MRI scans, PET scans, dental services, optical services (including optician services, prescription glasses, or contact lenses), health check-ups, infertility treatments, sexual health services, contraception, conditions related to learning or developmental delay, genetic testing, alcohol or drug abuse treatment, vaccinations, maternity care, vitamin or supplement injections/IV infusions, and hair loss shampoo": {
        "EN": "For AXA Global Health (AXA PPP), direct billing is available for outpatient visits with medical expenses not exceeding THB 15,000 (including specialist consultations), laboratory tests, blood tests, acne medications, procedures, eye/ear drops, medications & dressings, and physiotherapy (limited to a maximum of 5 sessions per facility). Pre-authorisation is required for outpatient visits exceeding THB 15,000, more than 5 physiotherapy sessions at the same facility, psychiatric consultations, gynecological conditions (e.g. PCOS, menopause), CT scans, MRI scans, PET scans, dental services, optical services (including optician services, prescription glasses, or contact lenses), health check-ups, infertility treatments, sexual health services, contraception, conditions related to learning or developmental delay, genetic testing, alcohol or drug abuse treatment, vaccinations, maternity care, vitamin or supplement injections/IV infusions, and hair loss shampoo",
        "FR": "Pour AXA Global Health (AXA PPP), la prise en charge directe est possible pour les consultations ambulatoires dont les frais médicaux ne dépassent pas 15 000 THB (y compris les consultations de spécialistes), les analyses de laboratoire, les analyses sanguines, les traitements contre l’acné, les procédures médicales, les gouttes oculaires et auriculaires, les médicaments et pansements, ainsi que la physiothérapie (limitée à 5 séances maximum par établissement). Une préautorisation est requise pour les consultations ambulatoires dépassant 15 000 THB, plus de 5 séances de physiothérapie dans le même établissement, les consultations psychiatriques, les affections gynécologiques (par ex. SOPK, ménopause), les examens CT, IRM et PET scan, les soins dentaires, les services d’optique (y compris chez un opticien ou pour la prescription de lunettes ou lentilles), les bilans de santé, les traitements de fertilité, les soins liés à la santé sexuelle, la contraception, les troubles liés aux difficultés d’apprentissage ou au retard du développement, les tests génétiques, les traitements liés à l’alcool ou aux drogues, les vaccinations, les soins de maternité, les injections ou perfusions de vitamines et compléments, ainsi que les shampoings contre la chute des cheveux",
        "DE": "Für AXA Global Health (AXA PPP) ist eine Direktabrechnung für ambulante Behandlungen möglich, sofern die medizinischen Kosten 15.000 THB nicht überschreiten (einschließlich Facharztkonsultationen), Laboruntersuchungen, Bluttests, Akne-Medikationen, Behandlungen, Augen- und Ohrentropfen, Medikamente und Verbandsmaterial sowie Physiotherapie (maximal 5 Sitzungen pro Einrichtung). Eine Vorabgenehmigung ist erforderlich für ambulante Behandlungen über 15.000 THB, mehr als 5 Physiotherapiesitzungen in derselben Einrichtung, psychiatrische Konsultationen, gynäkologische Erkrankungen (z. B. PCOS, Menopause), CT-, MRT- und PET-Untersuchungen, zahnärztliche Leistungen, optische Leistungen (einschließlich Optikerleistungen sowie Brillen- oder Kontaktlinsenverordnungen), Gesundheits-Check-ups, Kinderwunschbehandlungen, sexuelle Gesundheitsleistungen, Verhütung, Behandlungen im Zusammenhang mit Lern- oder Entwicklungsstörungen, genetische Tests, Alkohol- oder Drogenabhängigkeit, Impfungen, Schwangerschaftsleistungen, Vitamin- oder Nahrungsergänzungs-Injektionen bzw. Infusionen sowie Shampoos gegen Haarausfall"
    },

    "The hospital can accept cases directly from Emergency Assistance Japan (EAJ). Direct billing may be available for outpatient treatment; however, in cases requiring hospitalization or surgery, please coordinate with Emergency Assistance Japan (EAJ) and request that the claim be opened directly with the hospital": {
        "EN": "The hospital can accept cases directly from Emergency Assistance Japan (EAJ). Direct billing may be available for outpatient treatment; however, in cases requiring hospitalization or surgery, please coordinate with Emergency Assistance Japan (EAJ) and request that the claim be opened directly with the hospital",
        "FR": "L’hôpital peut accepter directement les dossiers provenant de Emergency Assistance Japan (EAJ). La prise en charge directe peut être disponible pour les traitements ambulatoires ; toutefois, en cas d’hospitalisation ou d’intervention chirurgicale, veuillez coordonner avec Emergency Assistance Japan (EAJ) et leur demander d’ouvrir directement le dossier de prise en charge auprès de l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von Emergency Assistance Japan (EAJ) annehmen. Eine Direktabrechnung kann für ambulante Behandlungen möglich sein; in Fällen, die einen Krankenhausaufenthalt oder eine Operation erfordern, wenden Sie sich bitte an Emergency Assistance Japan (EAJ) und bitten Sie darum, den Leistungsfall direkt mit dem Krankenhaus zu eröffnen."
    },

    "The hospital can accept cases directly from World Travel Protection (Australia). However, in cases requiring hospitalization or surgery, please coordinate with insurance provider and request that the claim be opened directly with the hospital": {
        "EN": "The hospital can accept cases directly from World Travel Protection (Australia). However, in cases requiring hospitalization or surgery, please coordinate with insurance provider and request that the claim be opened directly with the hospital",
        "FR": "L’hôpital peut accepter directement les dossiers provenant de World Travel Protection (Australia). Toutefois, en cas d’hospitalisation ou d’intervention chirurgicale, veuillez coordonner avec votre assureur et demander que le dossier de prise en charge soit ouvert directement auprès de l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von World Travel Protection (Australia) annehmen. In Fällen, die einen Krankenhausaufenthalt oder eine Operation erfordern, wenden Sie sich bitte an Ihren Versicherungsanbieter und bitten Sie darum, den Leistungsfall direkt mit dem Krankenhaus zu eröffnen",
    },

    "The hospital can accept cases directly from Eurocross. However, for cases requiring hospitalization or surgery, arrangements may sometimes be made through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital can accept cases directly from Eurocross. However, for cases requiring hospitalization or surgery, arrangements may sometimes be made through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital peut accepter les dossiers directement de la part d’Eurocross. Toutefois, pour les cas nécessitant une hospitalisation ou une intervention chirurgicale, les dossiers peuvent parfois être pris en charge par un prestataire d’assistance local en Thaïlande. Veuillez contacter votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von Eurocross übernehmen. In Fällen, die einen Krankenhausaufenthalt oder eine Operation erfordern, kann die Abwicklung jedoch manchmal über einen lokalen Assistance-Dienstleister in Thailand erfolgen. Bitte setzen Sie sich vor Ihrem Besuch im Krankenhaus mit Ihrem Versicherungsanbieter in Verbindung",

    },

    "The hospital cannot accept cases directly from Mgen. For cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital cannot accept cases directly from The hospital cannot accept cases directly from Mgen. For cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please coordinate with your insurance provider before coming to the hospital. For cases requiring hospitalization or surgery, an initial Guarantee of Payment (GOP) is required, and a final GOP must subsequently be issued. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital ne peut pas accepter les dossiers directement de la part de Mgen. Pour les cas nécessitant une hospitalisation ou une intervention chirurgicale, une garantie de paiement initiale (GOP) est requise, puis une garantie de paiement finale devra ensuite être émise. Veuillez contacter votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle nicht direkt von Mgen übernehmen. In Fällen, die einen Krankenhausaufenthalt oder eine Operation erfordern, ist zunächst eine Kostenübernahmegarantie (Guarantee of Payment – GOP) erforderlich; anschließend muss eine endgültige GOP ausgestellt werden. Bitte setzen Sie sich vor Ihrem Besuch im Krankenhaus mit Ihrem Versicherungsanbieter in Verbindung"
    },

    "The hospital can accept cases directly from William Russell. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital can accept cases directly from William Russell. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital peut accepter les dossiers directement de la part de William Russell. Toutefois, les dossiers peuvent parfois être pris en charge par un prestataire d’assistance local en Thaïlande. Veuillez contacter votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von William Russell übernehmen. Alternativ können Fälle manchmal über einen lokalen Assistance-Dienstleister in Thailand abgewickelt werden. Bitte setzen Sie sich vor Ihrem Besuch im Krankenhaus mit Ihrem Versicherungsanbieter in Verbindung"
    },

    "The hospital cannot accept cases directly from GAPI. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital cannot accept cases directly from GAPI. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital ne peut pas accepter les dossiers directement de la part de GAPI. Veuillez contacter votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle nicht direkt von GAPI übernehmen. Bitte setzen Sie sich vor Ihrem Besuch im Krankenhaus mit Ihrem Versicherungsanbieter in Verbindung",
    },

    "The hospital can accept cases directly from VHI Global Healthcare. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital can accept cases directly from VHI Global Healthcare. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital peut accepter les dossiers directement de la part de VHI Global Healthcare. Toutefois, les dossiers peuvent parfois être pris en charge par un prestataire d’assistance local en Thaïlande. Veuillez contacter votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von VHI Global Healthcare übernehmen. Alternativ können Fälle manchmal über einen lokalen Assistance-Dienstleister in Thailand abgewickelt werden. Bitte setzen Sie sich vor Ihrem Besuch im Krankenhaus mit Ihrem Versicherungsanbieter in Verbindun",
    },

    "The hospital cannot accept cases directly from ISON Care due to communication and email follow-up difficulties. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital cannot accept cases directly from ISON Care due to communication and email follow-up difficulties. Alternatively, cases may sometimes be assigned through a local assistance provider in Thailand. Please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital ne peut pas accepter les dossiers directement de la part d’ISON Care en raison de difficultés de communication et de suivi par e-mail. Toutefois, les dossiers peuvent parfois être pris en charge par un prestataire d’assistance local en Thaïlande. Veuillez contacter votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle aufgrund von Kommunikations- und E-Mail-Korrespondenzproblemen nicht direkt von ISON Care übernehmen. Alternativ können Fälle manchmal über einen lokalen Assistance-Dienstleister in Thailand abgewickelt werden. Bitte setzen Sie sich vor Ihrem Besuch im Krankenhaus mit Ihrem Versicherungsanbieter in Verbindung",
    },

    "The hospital can accept cases directly from Roy Medical Assistance. However, after completing outpatient treatment, the patient must wait at the cashier until the hospital receives the final Guarantee of Payment (GOP). If you do not wish to wait, please make a deposit or pay upfront and claim reimbursement later. For cases requiring hospitalization or surgery, please coordinate with your insurance provider before coming to the hospital": {
        "EN": "The hospital can accept cases directly from Roy Medical Assistance. However, after completing outpatient treatment, the patient must wait at the cashier until the hospital receives the final Guarantee of Payment (GOP). If you do not wish to wait, please make a deposit or pay upfront and claim reimbursement later. For cases requiring hospitalization or surgery, please coordinate with your insurance provider before coming to the hospital",
        "FR": "L’hôpital peut accepter les dossiers directement de la part de Roy Medical Assistance. Toutefois, après la fin du traitement en ambulatoire, le patient doit attendre à la caisse jusqu’à ce que l’hôpital reçoive la garantie de paiement finale (GOP). Si vous ne souhaitez pas attendre, veuillez effectuer un dépôt ou payer les frais et demander un remboursement par la suite. Pour les cas nécessitant une hospitalisation ou une intervention chirurgicale, veuillez contacter votre compagnie d’assurance avant de vous rendre à l’hôpital",
        "DE": "Das Krankenhaus kann Fälle direkt von Roy Medical Assistance übernehmen. Nach Abschluss der ambulanten Behandlung muss der Patient jedoch an der Kasse warten, bis das Krankenhaus die endgültige Kostenübernahmegarantie (Guarantee of Payment – GOP) erhalten hat. Wenn Sie nicht warten möchten, leisten Sie bitte eine Anzahlung oder zahlen Sie zunächst selbst und reichen Sie anschließend eine Erstattung ein. Für Fälle, die einen Krankenhausaufenthalt oder eine Operation erfordern, setzen Sie sich bitte vor Ihrem Besuch im Krankenhaus mit Ihrem Versicherungsanbieter in Verbind"

    },


}

# Note translation function
def t(key):
    return translations[lang].get(key, key)

def translate_status(status):
    if not status:
        return "-"
    return translations[lang].get(status, status)

def translate_note(text):
    if not text:
        return "-"
    clean_text = str(text).strip()
    return note_translations.get(clean_text, {}).get(lang, clean_text)

month_translations = {
    "EN": {
        "January": "January",
        "February": "February",
        "March": "March",
        "April": "April",
        "May": "May",
        "June": "June",
        "July": "July",
        "August": "August",
        "September": "September",
        "October": "October",
        "November": "November",
        "December": "December",
    },
    "FR": {
        "January": "janvier",
        "February": "février",
        "March": "mars",
        "April": "avril",
        "May": "mai",
        "June": "juin",
        "July": "juillet",
        "August": "août",
        "September": "septembre",
        "October": "octobre",
        "November": "novembre",
        "December": "décembre",
    },
    "DE": {
        "January": "Januar",
        "February": "Februar",
        "March": "März",
        "April": "April",
        "May": "Mai",
        "June": "Juni",
        "July": "Juli",
        "August": "August",
        "September": "September",
        "October": "Oktober",
        "November": "November",
        "December": "Dezember",
    }
}

def translate_date(date_text):
    parts = date_text.split()

    if len(parts) == 3:
        day, month, year = parts
        translated_month = month_translations[lang].get(month, month)
        return f"{day} {translated_month} {year}"

    return date_text


base_path = os.path.dirname(__file__)

st.set_page_config(page_title="SIIEN", layout="centered")

# Language selector

lang_display = st.segmented_control(
    "Language",
    ["🇬🇧 English", "🇫🇷 Français", "🇩🇪 Deutsch"],
    default="🇬🇧 English"
)

if lang_display == "🇬🇧 English":
    lang = "EN"
elif lang_display == "🇫🇷 Français":
    lang = "FR"
else:
    lang = "DE"
             
# Theme style
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #f4faf6;
    }
    .stSelectbox label {
        font-weight : bold;
        color: #006b3f;
    }        
    .result-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 2px 8px rga (0,0,0,0.08);
        margin-top: 20px;
    }
            
    
    <style>
""", unsafe_allow_html=True)    

# SIIEN logo
coll, col2, col3 = st.columns([4,3,4])
with col2:
 logo_path = os.path.join(base_path, "siien_logo.png")
 st.image(logo_path, width=100)

# Insurance list
insurance_list = sorted([
    "APRIL Assistance Thailand", 
    "APRIL International France",
    "APRIL International UK",
    "APRIL Sompo",
    "Allianz Worldwide Care",
    "Allianz Worldwide Care - IOM Group",
    "Allianz Worldwide Care - MOFA Group (Embassy of Saudi Arabia)",
    "Asian Assistance", 
    "Asian Assistance - AXA Global Health (AXA PPP)",
    "Euro Center Thailand", 
    "BlueCrossBlueShield",
    "Anthem",
    "Horizon BlueCrossBlueShield",
    "Highmark BlueCrossBlueShield",
    "Excellus BlueCrossBlueShield",
    "Premera BlueCrossBlueShield",
    "Carefirst BlueCrossBlueShield",
    "Florida Blue",
    "Regence BlueCrossBlueShield",
    "Capital Blue",
    "Independence BlueCross",
    "Wellmark BlueCrossBlueShield",
    "Gouda & Gjensidige",
    "SOS First Denmark",
    "Regency Assurance",
    "Europ Assistance",
    "Falck Global Assistance",
    "IMA France",
    "IMA Benelux Assistance (Belgium)",
    "IMG UK",
    "IMG USA",
    "CFE (Caisse des Français de l'Étranger)",
    "VYV International Assistance (Groupe VYV)",
    "ADAC Versicherung AG",
    "Helsana Krankenversicherung AG",
    "CSS Gruppe",
    "Assura",
    "UNIQA Switzerland"
    "SWICA Krankenversicherung AG"
    "Medicall AG"
    "SOS International Netherlands",
    "GeoBlue",
    "ATMS (Asian Travel & Medical Services)",
    "CMA (Credible Medical Assistance)",
    "CEGA Assistance",
    "Assist International Services (AIS)",
    "Humana",
    "HanseMekur Reiseversicherung",
    "MD Medicus",
    "DKV Deutsche Krankenversicherung AG",
    "Malteser International",
    "Huk-Coburg",
    "Henner",
    "Henner VUMI",
    "MSH China",
    "MSH International",
    "Healthmetrics",
    "EMA Global Thailand"
    "Aetna International",
    "AWP Thailannd Services",
    "Axa Krankenversicherung AG",
    "AIG Japan",
    "CORIS Slovenia",
    "ERGO Forsikring",
    "ERGO Seguros de Viaje",
    "Pohjala Vakuutus",
    "Emergency Assistance Japan (EAJ)",
    "World Travel Protection (Australia)"
    "Eurocross",
    "Mgen",
    "William Russell",
    "GAPI",
    "VHI Global Healthcare",
    "ISON care",
    "Roy Medical Assistance",
    "BlueCrossBlueShield - Bupa",


], key=str.lower)

base_path = os.path.dirname(__file__)
forms_path = os.path.join(base_path, "Forms")

# Insurance logos

insurance_logos = {
    "APRIL Assistance Thailand": os.path.join(base_path, "aprilassistance_logo.png"),
    "APRIL International France": os.path.join(base_path, "april_internationalfrance_logo.png"),
    "APRIL International UK": os.path.join(base_path, "april_internationaluk_logo.png"),
    "APRIL Sompo": os.path.join(base_path, "aprilsompo_logo.png"),
    "Allianz Worldwide Care": [
        os.path.join(base_path, "awc_logo.png"),
        os.path.join(base_path, "awc1_logo.png")
    ],
    "Allianz Worldwide Care - IOM Group": os.path.join(base_path, "allianziom_logo.png"),
    "Allianz Worldwide Care - MOFA Group (Embassy of Saudi Arabia)": os.path.join(base_path, "allianzmofa_logo.png"),
    "Asian Assistance": os.path.join(base_path, "asianassistance_logo.png"),
    "Asian Assistance - AXA Global Health (AXA PPP)": [
        os.path.join(base_path, "asianassistance_logo.png"),
        os.path.join(base_path, "axappp_logo.png")
    ],
    "Euro Center Thailand": os.path.join(base_path, "eurocenter_logo.png"),
    "BlueCrossBlueShield": os.path.join(base_path, "bluecrossblueshield_logo.png"),
    "Anthem": os.path.join(base_path, "anthem_logo.png"),
    "Horizon BlueCrossBlueShield": os.path.join(base_path, "horizonbcbs_logo.png"),
    "Highmark BlueCrossBlueShield": os.path.join(base_path, "highmarkbcbs_logo.png"),
    "Excellus BlueCrossBlueShield": os.path.join(base_path, "excellusbcbs_logo.png"),
    "Premera BlueCrossBlueShield": os.path.join(base_path, "premerabcbs_logo.png"),
    "Carefirst BlueCrossBlueShield": os.path.join(base_path, "carefirstbcbs_logo.png"),
    "Regence BlueCrossBlushield": os.path.join(base_path, "regencebcbs_logo"),
    "Florida Blue": os.path.join(base_path, "floridablue_logo.png"),
    "Capital Blue": os.path.join(base_path, "capitalblue_logo.png"),
    "Independence BlueCross": os.path.join(base_path, "independencebcbs_logo.png"),
    "Wellmark BlueCrossBlueShield": os.path.join(base_path, "wellmarkbcbs_logo.png"),
    "Gouda & Gjensidige": [
        os.path.join(base_path, "gouda_logo.png"),
        os.path.join(base_path, "gjensidige_logo.png")
    ],
    "SOS First Denmark": os.path.join(base_path, "sosfirstdenmark_logo.png"),
    "Regency Assurance": os.path.join(base_path, "regencyassurance_logo.png"),
    "Europ Assistance": os.path.join(base_path, "europassistance_logo.png"),
    "Falck Global Assistance": os.path.join(base_path, "falckglobalassistance_logo.png"),
    "IMA France": os.path.join(base_path, "imafrance_logo.png"),
    "IMA Benelux Assistance (Belgium)": os.path.join(base_path, "imabeneluxassistance_logo.png"),
    "IMG UK": os.path.join(base_path, "imguk_logo.png"),
    "IMG USA": os.path.join(base_path, "imgusa_logo.png"),
    "CFE (Caisse des Français de l'Étranger)": os.path.join(base_path, "cfe_logo.png"),
    "VYV International Assistance (Groupe VYV)": os.path.join(base_path, "vyv_logo.png"),
    "ADAC Versicherung AG": os.path.join(base_path, "adac_logo.png"),
    "Helsana Krankenversicherung AG": os.path.join(base_path, "helsana_logo.png"),
    "CSS Gruppe": [
        os.path.join(base_path, "css_logo.png"),
        os.path.join(base_path, "css2_logo.png")
    ],
    "Assura": os.path.join(base_path, "assura_logo.png"),
    "UNIQA Switzerland": os.path.join(base_path, "uniqa_logo.png"),
    "SWICA Krankenversicherung AG": os.path.join(base_path, "swica_logo.png"),
    "Sanitas Krankenversicherung AG": os.path.join(base_path, "sanitas_logo.png"),
    "Medicall AG": os.path.join(base_path, "medicall_logo.png"),
    "SOS International Netherlands": os.path.join(base_path, "sosinternational_logo.png" ),
    "GeoBlue": os.path.join(base_path, "geoblue_logo.png" ),
    "ATMS (Asian Travel & Medical Services)": os.path.join(base_path, "atms_logo.png"),
    "CMA (Credible Medical Assistance)": os.path.join(base_path, "cma_logo.png"),
    "CEGA Assistance": os.path.join(base_path, "cega_logo.png"),
    "Assist International Services (AIS)": os.path.join(base_path, "assistinternational_logo.png"),
    "WrLife": os.path.join(base_path, "wrlife_logo.png"),
    "Humana": os.path.join(base_path, "humana_logo.png"),
    "HanseMekur Reiseversicherung": os.path.join(base_path, "hansemekur_logo.png"),
    "MD Medicus": os.path.join(base_path, "mdmedicus_logo.png"),
    "DKV Deutsche Krankenversicherung AG": os.path.join(base_path, "dkv_logo.png"),
    "Malteser International": os.path.join(base_path, "malteser_logo.png" ),
    "Huk-Coburg": os.path.join(base_path, "hukcoburg_logo.png"),
    "Henner": os.path.join(base_path, "henner_logo.png"),
    "Henner VUMI": [
        os.path.join(base_path, "hennervumi_logo.png"),
        os.path.join(base_path, "hnvumi_logo.png")
    ],
    "MSH China": os.path.join(base_path, "mshchina_logo.png"),
    "MSH International": os.path.join(base_path, "mshinter_logo.png"),
    "Healthmetrics": os.path.join(base_path, "healthmetrics_logo.png"),
    "EMA Global Thailand": os.path.join(base_path, "emath_logo.png"),
    "Aetna International": os.path.join(base_path, "aetnainter_logo.png"),
    "AWP Thailand Services": os.path.join(base_path, "awpth_logo.png"),
    "Axa Krankenversicherung AG": os.path.join(base_path, "axakranken_logo.png"),
    "AIG Japan": [
        os.path.join(base_path, "aigjapan_logo.png"),
        os.path.join(base_path, "aigjapan1_logo.png"),
    ],
    "CORIS Slovenia": os.path.join(base_path, "coris_logo.png"),
    "ERGO Forsikring": os.path.join(base_path, "ergo_logo.png"),
    "ERGO Seguros de Viaje": os.path.join(base_path, "ergoseguros_logo.png"),
    "Pohjala Vakuutus": os.path.join(base_path, "pohjala_logo.png"),
    "Foyer Global Healthcare":  os.path.join(base_path, "foyergroup_logo.png"),
    "Emergency Assistance Japan (EAJ)": os.path.join(base_path, "eaj_logo.png"),
    "World Travel Protection (Australia)": os.path.join(base_path, "worldtravel_logo.png"),
    "Eurocross": os.path.join(base_path, "eurocross_logo.png"),
    "Mgen": [
        os.path.join(base_path, "healthcase_logo.png"),
        os.path.join(base_path, "mgen_logo.png")
    ],
    "William Russell": os.path.join(base_path, "williamrussell_logo.png"),
    "GAPI": os.path.join(base_path, "gapi_logo.png"),
    "VHI Global Healthcare": os.path.join(base_path, "vhi_logo.png"),
    "ISON care": os.path.join(base_path, "ison_logo.png"),
    "Roy Medical Assistance": os.path.join(base_path, "roymedical_logo.png"),
    "BlueCrossBlueShield - Bupa": [
         os.path.join(base_path, ""),
         os.path.join(base_path, "")
    ],
       
}

gop_forms = {
    "APRIL Assistance Thailand": os.path.join(base_path, "GOP sample - APRIL Assistance.pdf"),
    "APRIL International France": os.path.join(base_path, "GOP sample - APRIL Assistance.pdf"),
    "APRIL International UK": os.path.join(base_path, "-"),
    "APRIL Sompo": os.path.join(base_path, "GOP sample - APRIL Assistance.pdf"),
    "Allianz Worldwide Care": os.path.join(base_path, "GOP sample - AWC (All groups).pdf"),
    "Allianz Worldwide Care - IOM Group": os.path.join(base_path, "GOP sample - AWC (All groups).pdf"),
    "Allianz Worldwide Care - MOFA Group (Embassy of Saudi Arabia)": os.path.join(base_path, "GOP sample - AWC (All groups).pdf"),
    "Asian Assistance": os.path.join(base_path, "GOP sample - Asian Assistance.pdf" ),
    "Euro Center Thailand": os.path.join(base_path, "GOP sample - Euro Center Thailand.pdf"),
    "Europ Assistance": os.path.join(base_path, "GOP sample - Europ Assistance.pdf"),
    "Falck Global Assistance": os.path.join(base_path, "GOP sample - Falck Global Assistance.pdf"),
    "IMA France": os.path.join(base_path, "GOP sample - IMA France.pdf"),
    "VYV International Assistance (Groupe VYV)": os.path.join(base_path, "GOP sample - VYV International Assistance.pdf"),
    "ADAC Versicherung AG": os.path.join(base_path, "GOP sample - ADAC.pdf"),
}

#Select insurance

default_option = t("default_option")
if "selected_insurance" not in st.session_state:
    st.session_state.selected_insurance = default_option

came_from_jump = False

jump_to = st.query_params.get("jump")

if jump_to in data:
    st.session_state.selected_insurance = jump_to
    came_from_jump = True
    st.query_params.clear()

initial_insurance = st.session_state.get("selected_insurance", None)

country_options = ["All Countries"] + sorted(set(
    info.get("Country")
    for info in data.values()
    if info.get("Country") not in [None, "-", ""]
))

selected_country = st.selectbox(
    "Insurance Country",
    country_options
)

current_insurance =st.session_state.get("selected_insurance", None)

if selected_country == "All Countries":
    filtered_data = data
else:
    filtered_data = {
        name: info
        for name, info in data.items()
        if info.get("Country") == selected_country
    }

insurance_list = sorted(filtered_data.keys())

if current_insurance not in filtered_data:
    st.session_state.selected_insurance = None

def search_insurance(searchterm):
    if not searchterm or searchterm.strip() == "":
        return insurance_list
    
    q = searchterm.lower().strip()

    return [
        insurance for insurance in insurance_list
        if q in insurance.lower()
    ]

country_key = selected_country

insurance = st_searchbox(
    search_function=search_insurance,
    placeholder=t("smart_search"),
    label="",
    key=f"insurance_searchbox_{country_key}",
    default_options=insurance_list,
)

if not insurance and came_from_jump and initial_insurance in filtered_data:
    insurance = initial_insurance

elif not insurance:
    st.session_state.selected_insurance = None
    st.info(t("please_select"))
    st.stop()

st.session_state.selected_insurance = insurance
result = filtered_data[insurance]
gop_form = gop_forms.get(insurance)


if insurance in insurance_logos:
    logo_data = insurance_logos[insurance]

    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

    if isinstance(logo_data, list):
        col1, col2, spacer = st.columns([1, 1, 4])

        with col1:
            if logo_data[0]:
                st.image(logo_data[0], width=140)

        with col2:
            if insurance == "Henner VUMI":
                st.markdown(
                    "<div style='height:35px;'></div>",
                    unsafe_allow_html=True
                )

            if len(logo_data) > 1 and logo_data[1]:
                st.image(logo_data[1], width=140)

    else:
        if logo_data:
            st.image(str(logo_data), width=200)


# Color Function Box

def get_status_style(status):
    status = str(status).strip().lower()

    if status == "accepted":
        return "#2e7d32", "#e8f5e9"
    elif status == "accepted with conditions":
        return "#ef6c00", "#fff3e0"
    elif status == "not accepted":
        return "#c62828", "#fdecea"
    else:
        return "#616161", "#f5f5f5"
    
def get_country_flag(country):
    flags = {
        "Australia": "🇦🇺",
        "Thailand": "🇹🇭",
        "China": "🇨🇳",
        "France": "🇫🇷",
        "Germany": "🇩🇪",
        "Belgium": "🇧🇪",
        "Luxembourg": "🇱🇺",
        "Netherlands": "🇳🇱",
        "Poland": "🇵🇱",
        "Slovenia": "🇸🇮",
        "Portuggl": "🇵🇹",
        "Spain": "🇪🇸",
        "Sweden": "🇸🇪",
        "Norway": "🇳🇴",
        "Denmark": "🇩🇰",
        "Finland": "🇫🇮",
        "Switzerland": "🇨🇭",
        "Ireland": "🇮🇪",
        "United Kingdom": "🇬🇧",
        "United States of America": "🇺🇸",
        "Vietnam": "🇻🇳",
        "Indonesia": "🇮🇩",
        "India": "🇮🇳",
        "Japan": "🇯🇵",
    }
    return flags.get(country, "🌍")

# Result

import time

result = {}
status = "-"
opd_status = "-"
opd_note = "-"
ipd_status = "-"
ipd_note = "-"
country = "-"
last_updated = "-"
country_flag = "🌐"

status_color, status_bg = get_status_style(status)
opd_color, opd_bg = get_status_style(opd_status)
ipd_color, ipd_bg = get_status_style(ipd_status)

if insurance in data:
    with st.spinner(t("loading")):
        time.sleep(1.5)
        result = data[insurance]
    
    status = result.get("Status", "--")
    opd_status = result.get("OPD_status", "--")
    opd_note = result.get("OPD_note", "--")
    ipd_status = result.get("IPD_status", "--")
    ipd_note = result.get("IPD_note", "--")
    country = result.get("Country", "--")
    last_updated = result.get("Last_updated", "--")
    assistance_company = result.get("Assistance company", "--")
    company_type = result.get("Company Type", "--")
    additional_info = result.get("Additional information", "--")

    if isinstance(additional_info, dict):
        additional_info = additional_info.get(lang, additional_info.get("EN", "-"))
    else:
        additional_info = translate_note(additional_info)

    if assistance_company in data:
        assistance_display = f"""
        <a href="?jump={quote(assistance_company)}"
           target="_self"
           style="color:#0f766e; font-weight:700; text-decoration:underline;">
           {translate_note(assistance_company)}
        </a>
        """
    else:
        assistance_display = translate_note(assistance_company)
    
    country_flag = get_country_flag(country)

else:
    st.info(t("please_select"))
    st.stop()

# Status color logic

status_color, status_bg = get_status_style(status)
opd_color, opd_bg = get_status_style(opd_status)
ipd_color, ipd_bg = get_status_style(ipd_status)

# CSS spacing for info / warning

st.markdown("""
    <style>
    .block-container {
        padding-top: 4rem !important;
    }

    div[data-testid="stSelectbox"] {
    margin-bottom: 8px;
    }

    .status-main {
    font-size: 18px
    font-weiht: 700;
    }

    .result-box {
    background-color: white;
    padding: 25px;
    border-radius: 16px;
    margin-top: 10px;
    margin-bottom: 10px;
    }

    .status-badge {
    padding: 5px 12px;
    border-radius: 999px;
    font-size: 15px;
    font-weight: 800 !importat;
    transition: all 0.2s ease;
    }

    div[data-testid="stInfo"] {
    margin-top: 20px;
    margin-bottom: 10px;
    }

    div[data-testid="stWarning"] {
    margin-top: 10px;
    margin-bottom: 20px;
    }

    </style>
    """, unsafe_allow_html=True)


gop_html = ""

if gop_form:
    gop_html = """
    <p style='margin-top:15px;'>
        <b>GOP sample Form available</b>
    </p>
    """
gop_status = os.path.basename(gop_form) if gop_form else "—"

# Result card

st.markdown(textwrap.dedent(f"""
<div class="result-box">

<h3>{t("insurance_info")}</h3>

<p style='color:#666; margin-top:-8px;'>
{country_flag} {t(country)} · {t("Last updated")}: {translate_date(last_updated)}
</p>

<p><b>{t("status")}:</b>
<span style='color:{status_color}; background-color:{status_bg}; padding:4px 10px; border-radius:999px; font-weight:800;'>
{translate_status(status)}
</span>
</p>

<hr>

<p><b>{t("opd")}:</b>
<span style='color:{opd_color}; background-color:{opd_bg}; padding:4px 10px; border-radius:999px; font-weight:800;'>
{translate_status(opd_status)}
</span>
</p>

<p style='margin-top:8px; color:#666;'>
{translate_note(opd_note)}
</p>

<p><b>{t("ipd")}:</b>
<span style='color:{ipd_color}; background-color:{ipd_bg}; padding:4px 10px; border-radius:999px; font-weight:800;'>
{translate_status(ipd_status)}
</span>
</p>

<p style='margin-top:8px; color:#666;'>
{translate_note(ipd_note)}
</p>

<hr>

<p><b>{t("company_type")}:</b> {company_type}</p>

<p><b>{t("contact")}:</b> {result.get("Contact", "—")}</p>

<details>
<summary><b>{t("client")}</b></summary>
<p>{result.get("Client", "—")}</p>
</details>

<p><b>{t("assistance")}:</b> {assistance_display}</p>

<p><b>{t("additional")}:</b><br>
{additional_info}
</p>

</div>
"""), unsafe_allow_html=True)

# GOP Download Section

if gop_form and os.path.exists(gop_form):

    st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)

    with open(gop_form, "rb") as file:
        gop_base64 = base64.b64encode(file.read()).decode()

    gop_filename = os.path.basename(gop_form)

    st.markdown(f"""<div class="result-box" style="margin-top:-15px;">
<h3>{t("gop_sample")}</h3>

<a href="data:application/pdf;base64,{gop_base64}"
download="{gop_filename}"
style="
display:inline-block;
margin-top:10px;
padding:10px 16px;
border:1px solid #ddd;
border-radius:8px;
background-color:#f8f8f8;
color:#333;
font-weight:700;
text-decoration:none;
">
📄 {gop_filename}
</a>

</div>""", unsafe_allow_html=True)

# Instruction box

st.info(t("info_msg"))
st.warning(t("warning_msg"))