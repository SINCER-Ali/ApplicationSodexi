from .models import Cyd


def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            cyd = Cyd(
                code_app=line[0:5].strip(),
                code_carte=line[5:7].strip(),
                num_cpt_urn_collectif=line[7:16].strip(),
                iata_orig=line[16:21].strip(),
                iata_dest=line[21:26].strip(),
                code_cca=line[26:27].strip(),
                cie_lta=line[27:30].strip(),
                num_lta=line[30:38].strip(),
                code_double=line[38:39].strip(),
                date_emission=line[39:47].strip(),
                unite_poids=line[47:48].strip(),
                pd_brut=line[48:55].strip(),
                pd_taxable=line[55:62].strip(),
                typ=line[62:63].strip(),
                mnt_htfac=line[63:78].strip(),
                cf1=line[78:81].strip(),
                mf1=line[81:96].strip(),
                cf2=line[96:99].strip(),
                mf2=line[99:114].strip(),
                cf3=line[114:117].strip(),
                mf3=line[117:132].strip(),
                cf4=line[132:135].strip(),
                mf4=line[135:150].strip(),
                cf5=line[150:153].strip(),
                mf5=line[153:168].strip(),
                filler=line[168:169].strip(),
                cmf=line[169:184].strip(),
                monnaie_fac=line[184:187].strip(),
                nb_dec_fac=line[187:188].strip(),
                code_service=line[188:190].strip(),
                code_tva=line[190:191].strip(),
                mode_paiement=line[191:193].strip(),
                mnt_compt=line[193:208].strip(),
                monnaie_compt=line[208:211].strip(),
                nb_dec_compt=line[211:212].strip(),
                num_cpt_urn_individuel=line[212:219].strip(),
                n_facture_af=line[219:229].strip()
            )
            cyd.save()

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import datetime

def generate_pdf(cyd_objects, file_path):
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica", 12)
    c.drawString(100, height - 50, "RAPPORT DE VENTE LTA AIR FRANCE / SODEXI")
    c.drawString(100, height - 70, "CLIENTS AIR FRANCE")
    c.drawString(100, height - 90, f"Date d'impression {datetime.datetime.now().strftime('%d %B %Y')}")

    headers = ["U.F. Cie", "Num Lta", "Date", "Origine", "Destination", "Poids", "Tarif AF", "Tarif Sodexi", "Ecart"]
    c.drawString(50, height - 130, " ".join(headers))

    y = height - 150
    for cyd in cyd_objects:
        values = [
            cyd.code_app,
            cyd.num_lta,
            cyd.date_emission,
            cyd.iata_orig,
            cyd.iata_dest,
            cyd.pd_brut,
            cyd.mnt_htfac,
            cyd.mf1,
            "0.00"
        ]
        c.drawString(50, y, " ".join(values))
        y -= 20
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
