from DerwentParser.Patent import  Patent
import  re
# FN Clarivate Analytics Web of Science
# VR 1.0
# PT P
# PN JP2020007234-A
# TI Mosaic serine protease large-form inhibitor useful for suppressing infection or growth of virus e.g. highly pathogenic influenza viruses, coronavirus and Ebola virus, comprises peptide compound(s).
# AU FUTAKAWA K
#    MAITA A
#    OKUMURA Y
# AE UNIV TOKUSHIMA NAT CORP (UTKU-C)
#    UNIV SAGAMI WOMENS (UYSA-Non-standard)
# GA 202006770N
# AB    NOVELTY - Mosaic serine protease large-form (MSPL) inhibitor comprises at least one peptide compound (I) as an active ingredient.
#    USE - The inhibitor is useful in composition for suppressing viral infection or growth, where the virus is chosen from highly pathogenic influenza viruses including natural and mutant forms, coronavirus, porcine epidemic diarrhea virus, HIV-1, Ebola virus and yellow fever virus (all claimed). The highly pathogenic influenza viruses are H5N1 viruses.
#    DETAILED DESCRIPTION - Mosaic serine protease large-form (MSPL) inhibitor comprises at least one peptide compound of formula: (R1)x-(Lys)l-(Gln)m-(Arg)n-R2 (I) as an active ingredient.
#    R1 = modifying group for an amino group on the N-terminal;
#    R2 = carboxy modifying group of a C-terminal arginine residue;
#    x, m = 0 or 1;
#    l, n = 1-3;and
#    l+m+n = 4, where when l is 2, m is 0.
# DC B05 (Other organics - aromatics, aliphatic, organo-metallics, compounds whose substituents vary such that they would be classified in several of B01 - B05.); B04 (Natural products and polymers. Including testing of body fluids (other than blood typing or cell counting), pharmaceuticals or veterinary compounds of unknown structure, testing of microorganisms for pathogenicity, testing of chemicals for mutagenicity or human toxicity and fermentative production of DNA or RNA. General compositions.); C03 (Other organic compounds, inorganic compounds and multicomponent mixtures. Polymers and proteins.); D16 (Fermentation industry - including fermentation equipment, brewing, yeast production, production of pharmaceuticals and other chemicals by fermentation, microbiology, production of vaccines and antibodies, cell and tissue culture and genetic engineering.)
# MC B04-C01; B10-A17; B14-A02; B14-D07C; C04-C01; C10-A17; C14-A02; C14-D07C; D05-H
# IP A61K-038/07; A61P-031/12; A61P-031/14; A61P-031/16; A61P-031/18; C07K-005/11
# PD JP2020007234-A   16 Jan 2020   A61K-038/07   202010   Pages: 14   Japanese
# AD JP2020007234-A    JP126822    03 Jul 2018
# PI JP126822    03 Jul 2018
# MN 218077101 K U; 218077102 K U
# UT DIIDW:202006770N
# ER
text=['FN Clarivate Analytics Web of Science\n', 'VR 1.0\n', 'PT P\n', 'PN CN209618737-U\n', 'TI Frame bridge culvert construction template trolley for mobile tower crane, has upright post whose bottom part is provided with balance weight base that is fixed on bridge plate of longitudinal rail through pulley, where pulley is driven by motor.\n', 'AU ZHANG G\n', '   LIU Y\n', '   LIU J\n', '   ZHANG P\n', '   TANG E\n', '   WANG Z\n', '   TANG B\n', '   HU W\n', '   ZENG X\n', '   ZHANG W\n', '   WANG B\n', '   YANG Y\n', '   DI Y\n', '   LI J\n', 'AE CHINA RAILWAY SEVENTH GROUP CO LTD (CREN-C)\n', '   CHINA RAILWAY SEVENTH GROUP ZHENGZHOU EN (CREN-C)\n', 'GA 2019964824\n', 'AB    NOVELTY - The utility model claims a mobile type tower crane for matching the frame bridge culvert construction, boom template trolley comprises upright post and connected with the upright post through a bearing, said lifting arm is provided with an electric hoist, the upright post is provided with the balance base, the balance weight pedestal through the pulley is set on the bridge plate of the longitudinal rail; the pulley is driven by a motor. The utility model has simple structure, easy manufacture and installation, high-efficiency and safe use, the tower crane can move, in the process of construction whether rebar conveying binding or template mounting and dismounting can reduces the manual investment, reduces the unnecessary financial investment, and in the process of construction can be reduced using higher danger coefficient of fixed tower crane and the use frequency of the truck crane, the efficient, light, practical and very suitable rebar template lifting and mounting the frame bridge culvert template trolley construction.\n', 'DC Q38 (Hoisting; Lifting; Hauling; Trucks (B66)); X25 (Industrial Electric Equipment)\n', 'MC Q38-B; X25-F05\n', 'IP B66C-023/62; B66C-023/78\n', 'PD CN209618737-U   12 Nov 2019   B66C-023/62   201989   Pages: 5   Chinese\n', 'AD CN209618737-U    CN20415956    29 Mar 2019\n', 'PI CN20415956    29 Mar 2019\n', 'UT DIIDW:2019964824\n', 'ER\n']
def parserPatent(textlines:list) -> Patent:
    text = ""
    for lines in textlines:
        text = text + lines

    TI=re.search(r"TI(.+)\n", text).group(1)#查找标题
    PNs=list(map(lambda x: x.strip(), filter(lambda x: True if x != "" else False,
                                         re.split(";|,",re.search(r"\nPN(.+)?\nTI",text).group(1)))))
    PN=PNs[0]
    if  re.search("\nAU(.+?)AE", text, flags=re.S):
        AU = list(map(lambda x: x.strip(), filter(lambda x: True if x != "" else False,
                                                   re.search("\nAU(.+?)AE", text, flags=re.S).group(1).split("\n"))))
    else:
        AU=None

    if re.search(r"\nIP(.+)\n",text):
        IPC=list(map(lambda x:x.strip(),re.search(r"\nIP(.+)?\n",text).group(1).split(";")))
        if len(IPC)<3:
            pass
        else:
            IPC=IPC[0:2]
    else:
        IPC=None

    if  re.search(r"PD(.+)\n", text):
        patentDetails=list(map(lambda x: x.strip(), re.search(r"\nPD(.+)?\n", text).group(1).split("   ")))

        if len(patentDetails)>=6:

            if patentDetails[4]!="":
                pages = re.search("Pages:\s(\d)+",patentDetails[4]).group(1)
            else:
                pages=None
            if patentDetails[5]!="":
                language = patentDetails[5]
            else:
                language=None
            if patentDetails[1] != "":
                time=re.search(r".+(\d{4})",patentDetails[1]).group(1)
            else:
                time=None


        else:

                time=None
                language=None
                pages=None

    else :
        pages=None
        language=None
        time=None
    #patentDetails example ['CN209618737-U', '12 Nov 2019', 'B66C-023/62', '201989', 'Pages: 5', 'Chinese']


    try:
        nationality=[re.match(r"\w{2}",x).group(0) for x in PNs ]
    except Exception as e:
        nationality=None
        print(PN,e)


    if  re.search(r"\nAE(.+?)\nGA", text,flags=re.S):
        AE=list(map(lambda x: x.strip(), re.split('\n',re.search(r"\nAE(.+)?\nGA", text,flags=re.S).group(1))))

    else:
        AE=None

    return Patent(TI,
        PNs[0],
        nationality,
        IPC,
        AU,
        AE,
        time,
        language,pages)


parserPatent(text)