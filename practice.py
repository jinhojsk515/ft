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
