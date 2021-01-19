import signal
import time
import run
from rdkit import Chem
import utils
import filtering
from rdkit.Chem.Crippen import MolLogP
from rdkit.Chem.Scaffolds.MurckoScaffold import MurckoScaffoldSmilesFromSmiles
import pickle
from rdkit.Chem.rdMolDescriptors import CalcNumRings
print(utils.sub_scaffold('O=C(Cn1nc(-c2ccccc2)ccc1=O)NCCc1c[nH]c2ccccc12'))
exit()
with open('candidates.txt','r') as f:
    lines=f.readlines()
    ms=[l.strip().split('\t')[0] for l in lines]
    print(ms[200])
    #ms=set(ms)
with open('results/debug/log','r') as f:
    lines=f.readlines()[37-1:28436]
    mi=[l.strip().split(' ')[1] for l in lines]
    print(mi[0])
    mi=set(mi)
print(len([l for l in ms if l not in mi]))
exit()
#with open('./results/dti_3/episodes','r') as f:
#    lines=f.readlines()
#    lines=[l.strip() for l in lines]
#    lines=[float(l.split('\t')[1]) for l in lines if len(l.split('\t'))>1 and '-' in l.split('\t')[1]]
#    print(min(lines))

class TimeOutException(Exception):
    pass

def alarm_handler(signum,frame):
    print('time')
    raise TimeOutException()

def calculatedocking(sm,sc,pr):
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(10)
    try:
        time.sleep(11)
        return run.docking(sm,sc,pr)[0]
    except TimeOutException as e:
        print('timetime')
    except:
        print('general')

smiles = 'O=C1Nc2ccccc2/C1=C/c1[nH]c2cc1CC2'
scaffold_sdf_fn = 'scaffold.sdf'
protein_pdbqt_fn = 'protein.pdbqt'
print(calculatedocking(smiles, scaffold_sdf_fn, protein_pdbqt_fn)) #[-8.59513664]
