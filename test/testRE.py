import re

text=['asy manufacture and installation, high-efficiency and safe use, the tower crane can move, in the process of construction whether rebar conveying binding or template mounting and dismounting can reduces the manual investment, reduces the unnecessary financial investment, and in the process of construction can be reduced using higher danger coefficient of fixed tower crane and the use frequency of the truck crane, the efficient, light, practical and very suitable rebar template lifting and mounting the frame bridge culvert template trolley construction.\n', 'DC Q38 (Hoisting; Lifting; Hauling; Trucks (B66)); X25 (Industrial Electric Equipment)\n', 'MC Q38-B; X25-F05\n', 'IP B66C-023/62; B66C-023/78\n', 'PD CN209618737-U   12 Nov 2019   B66C-023/62   201989   Pages: 5   Chinese\n', 'AD CN209618737-U    CN20415956    29 Mar 2019\n', 'PI CN20415956    29 Mar 2019\n', 'UT DIIDW:2019964824\n', 'ER\n']
text='''PT P
PN WO2020077281-A1
TI System for monitoring, testing and controlling carotenoid extraction process, comprises input system feeding into carotenoid extraction process system, and data acquisition circuit structured to interpret multiple detection values.
AU ALLEN S D
   CELLA C H
AE WATER SOLUTIONS INC (WATE-Non-standard)
GA 202029700W
AB    NOVELTY - System comprises an input system feeding into a carotenoid extraction process system, a data acquisition circuit structured to interpret multiple detection values, where each of the multiple detection values corresponding to input received from multiple sensors. Each of the multiple sensors operatively is coupled to multiple components of the carotenoid extraction process system. A data analysis circuit is structured to analyze the multiple detection values to determine a state of the carotenoid extraction process. An analysis response circuit is structured to control an aspect of the carotenoid extraction process system in response to the state.
   USE - System for monitoring, testing and controlling carotenoid extraction process.
   ADVANTAGE - The system improves prediction of the outcome, and facilitates high speed processing, low power dissipation, and reduced manufacturing cost compared with board-level integration.
   DETAILED DESCRIPTION - INDEPENDENT CLAIMS are included for the following:
   (1) a method for extracting carotenoids from a carotenoid-containing source, which involves admixing the carotenoid-containing source with an organic solvent and a surfactant to form a slurry, treating the slurry with another organic solvent to form a carotenoid-surfactant combination, separating the treated slurry into a liquid fraction and a solid fraction, separating portion solution of the combination and the organic solvent, and then processing the solid fraction in an anaerobic digester to produce methane;
   (2) a system for extracting carotenoids from a carotenoid-containing source, which comprises a data acquisition circuit structured to collect multiple detection values, and a machine learning data analysis circuit structured to receive the detection values;
   (3) a system for treating hydraulic fracturing water having a machine learning system or artificial intelligence system for predicting an outcome or a state of a treatment process, which comprises a data acquisition circuit and a machine learning data analysis circuit;
   (4) a system for monitoring, testing, and controlling hydraulic fracturing water treatment process, which comprises a data acquisition circuit structured and a data analysis circuit;
   (5) a system for monitoring, testing, and controlling impound water treatment process, which comprises an input system and a data analysis circuit;
   (6) a system for treating impound water, which comprises a data acquisition circuit and a machine learning data analysis circuit; and
   (7) a system for treating a waste source, which comprises a waste source, a management system structured to monitor and control aspects of the system, and a treatment and separation system structured to receive a process condition from the management system.
   DESCRIPTION OF DRAWING(S) - The drawing shows a diagrammatic view of the waste treatment system.
   Waste source (102)
   Management system (104)
   Waste treatment and separation system (108)
   Collection system (110)
DC H01 (Obtaining crude oil and natural gas - including exploration, drilling, well completion, production and treatment. General off-shore platform and drilling technology is included together with the treatment of tar sands and oil shales (C10G, E21B).); J01 (Separation - including evaporation, crystallisation, solvent extraction, chromatography, dialysis, osmosis including drying gases and/or vapours, and separation of solids from gases, liquids and other solids. Isotope separation, filter materials (including molecular sieves for separation), and centrifuges (except where used for analysis) (B01D, B03, B04, B07B).); A97 (Miscellaneous goods not specified elsewhere - including papermaking, gramophone records, detergents, food and oil well applications.); D15 (Chemical or biological treatment of water, industrial waste and sewage - including purification, sterilising or testing water, scale prevention, treatment of sewage sludge, regeneration of active carbon which has been used for water treatment and impregnating water with gas e.g. CO2, but excluding plant and anti-pollution devices (C02).); T01 (Digital Computers)
MC H01-C03; H01-C11; H01-D; H01-E04; J01-C01A; A12-L04B; D04-A01H; T01-J07A3; T01-J16C2
IP B01D-011/02; C07C-403/08; C07C-403/24
PD WO2020077281-A1   16 Apr 2020   C07C-403/24   202034   Pages: 139   English
AD WO2020077281-A1    WOUS055961    11 Oct 2019
PI US744963P    12 Oct 2018
DS WO2020077281-A1:
		      (National): AE; AG; AL; AM; AO; AT; AU; AZ; BA; BB; BG; BH; BN; BR; BW; BY; BZ; CA; CH; CL; CN; CO; CR; CU; CZ; DE; DJ; DK; DM; DO; DZ; EC; EE; EG; ES; FI; GB; GD; GE; GH; GM; GT; HN; HR; HU; ID; IL; IN; IR; IS; JO; JP; KE; KG; KH; KN; KP; KR; KW; KZ; LA; LC; LK; LR; LS; LU; LY; MA; MD; ME; MG; MK; MN; MW; MX; MY; MZ; NA; NG; NI; NO; NZ; OM; PA; PE; PG; PH; PL; PT; QA; RO; RS; RU; RW; SA; SC; SD; SE; SG; SK; SL; SM; ST; SV; SY; TH; TJ; TM; TN; TR; TT; TZ; UA; UG; US; UZ; VC; VN; ZA; ZM; ZW
      (Regional): BW; GH; GM; KE; LR; LS; MW; MZ; NA; RW; SD; SL; ST; SZ; TZ; UG; ZM; ZW; EA; AL; AT; BE; BG; CH; CY; CZ; DE; DK; EE; ES; FI; FR; GB; GR; HR; HU; IE; IS; IT; LT; LU; LV; MC; MK; MT; NL; NO; PL; PT; RO; RS; SE; SI; SK; SM; TR; OA
UT DIIDW:202029700W
ER'''

print(re.search("\nAU(.+?)AE", text, flags=re.S).group(0))


