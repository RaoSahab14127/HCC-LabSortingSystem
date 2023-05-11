import  os
import fnmatch
import shutil

folder = "../pdf/"

for f in os.listdir(folder):
    if os.path.isfile(folder + f):
        if fnmatch.fnmatch(f, 'CBC.pdf') or fnmatch.fnmatch(f, 'WBC.pdf') or fnmatch.fnmatch(f, 'BI.pdf') or fnmatch.fnmatch(f, 'HBHCT.pdf') or fnmatch.fnmatch(f, 'PLT.pdf') or fnmatch.fnmatch(f, 'DLC.pdf')or fnmatch.fnmatch(f, 'ESR.pdf') or fnmatch.fnmatch(f, 'MP.pdf') or fnmatch.fnmatch(f, 'LAP.pdf') or fnmatch.fnmatch(f, 'BM.pdf') or fnmatch.fnmatch(f, 'BONET.pdf') or fnmatch.fnmatch(f, 'PT.pdf') or fnmatch.fnmatch(f, 'APTT.pdf') or fnmatch.fnmatch(f, 'MIXIT.pdf') or fnmatch.fnmatch(f, 'FDP.pdf')or fnmatch.fnmatch(f, 'FACTA.pdf') or fnmatch.fnmatch(f, 'PLATA.pdf') or fnmatch.fnmatch(f, 'HBEL.pdf') or fnmatch.fnmatch(f, 'G6PD.pdf') or fnmatch.fnmatch(f, 'IRON.pdf') or fnmatch.fnmatch(f, 'FER.pdf') or fnmatch.fnmatch(f, 'TIBC.pdf'):
            shutil.copy2(folder + f,"./Haematology1")
            os.remove(folder + f)
            print("c1")
   
        elif fnmatch.fnmatch(f, 'HBP.pdf') or fnmatch.fnmatch(f, 'HAVABM.pdf') or fnmatch.fnmatch(f, 'HBSAG.pdf') or fnmatch.fnmatch(f, 'HEPSAB.pdf') or fnmatch.fnmatch(f, 'COREG.pdf') or fnmatch.fnmatch(f, 'COREM.pdf')or fnmatch.fnmatch(f, 'HCV.pdf') or fnmatch.fnmatch(f, 'HPE.pdf') or fnmatch.fnmatch(f, 'ANA.pdf') or fnmatch.fnmatch(f, 'ADNA.pdf') or fnmatch.fnmatch(f, 'RA.pdf') or fnmatch.fnmatch(f, 'HIV.pdf'):
            shutil.copy2(folder + f,"./Haematology2")
            os.remove(folder + f)
            print("c2")
        elif fnmatch.fnmatch(f, 'ABO.pdf') or fnmatch.fnmatch(f, 'SCREEN.pdf'):
            shutil.copy2(folder + f,"./Haematology3")
            os.remove(folder + f)
            print("c3")
        elif fnmatch.fnmatch(f, 'BLCS.pdf') or fnmatch.fnmatch(f, 'UCS.pdf') or fnmatch.fnmatch(f, 'SCS.pdf'):
            shutil.copy2(folder + f,"./Microbiology1")
            os.remove(folder + f)
            print("c4")
        elif fnmatch.fnmatch(f, 'SDR.pdf') or fnmatch.fnmatch(f, 'SOB.pdf') or fnmatch.fnmatch(f, 'STOORS.pdf') or fnmatch.fnmatch(f, 'STOFG.pdf'):
            shutil.copy2(folder + f,"./Microbiology2")
            os.remove(folder + f)
            print("c5")
        elif fnmatch.fnmatch(f, 'UDR.pdf') or fnmatch.fnmatch(f, 'URRS.pdf') or fnmatch.fnmatch(f, 'URBS.pdf') or fnmatch.fnmatch(f, 'URBP.pdf'):
            shutil.copy2(folder + f,"./Microbiology3")
            os.remove(folder + f)
            print("c6")
        elif fnmatch.fnmatch(f, 'FS.pdf') or fnmatch.fnmatch(f, 'FC.pdf'):
            shutil.copy2(folder + f,"./Microbiology4")
            os.remove(folder + f)
            print("c7")
        elif fnmatch.fnmatch(f, 'AFBS.pdf') or fnmatch.fnmatch(f, 'AFBC.pdf'):
            shutil.copy2(folder + f,"./Microbiology5")
            os.remove(folder + f)
            print("c8")
        elif fnmatch.fnmatch(f, 'ASO.pdf') or fnmatch.fnmatch(f, 'CRP.pdf') or fnmatch.fnmatch(f, 'RPR.pdf') or fnmatch.fnmatch(f, 'WIDAL.pdf') or fnmatch.fnmatch(f, 'TD.pdf') or fnmatch.fnmatch(f, 'MT.pdf'):
            shutil.copy2(folder + f,"./Microbiology6")
            os.remove(folder + f)
            print("c9")
            
