#coding=UTF-8
import pymatgen.core as mg
import itertools
#import IPython
import random
import numpy as np
from matminer.data_retrieval.retrieve_MP import MPDataRetrieval
from pymatgen.ext.matproj import MPRester
mpdr = MPDataRetrieval(api_key=') 
######################################################################################################################################
#############   Obtain the CIF files and properties of crystals from the Material Project
def write_cif(data,name):
    with open('./cif/'+name+'.cif','w') as W:
        for i in data:
            W.write(i)

def write_data(data,name):
    #print (data)
    with open('all_data.txt','a') as A:
        A.write(str(name)+' ')
        all_targets_keys=['G_Reuss','G_VRH','G_Voigt','G_Voigt_Reuss_Hill','K_Reuss','K_VRH','K_Voigt','K_Voigt_Reuss_Hill','elastic_anisotropy','homogeneous_poisson','universal_anisotropy']
        for k in all_targets_keys:
            A.write(str(round(data[k],6))+' ')

        k='elastic_tensor'
        tensor=data[k]
        for i in range(len(tensor)):
            for j in range(len(tensor[i])):
                A.write(str(round(tensor[i][j],6))+' ')
        A.write('\n')

data = mpdr.get_dataframe({"elasticity": {"$exists": True},"cif": {"$exists": True}},
                        ['elasticity'])

for i in range(len(data['elasticity'])):
    print (i)
    print (data['material_id'])
    write_cif(data['cif'][i],str(i))
    write_data(data['elasticity'][i],str(i))

##############################################################################################3
################Generate graphs based on CIF files
formmp_graph import process
class class_II(object):
    def __init__(self,atomic_numbers,volume,cart_coords,lattice_matrix):
        self.atomic_numbers=atomic_numbers
        self.volume=volume
        self.cart_coords=cart_coords
        self.lattice_matrix=lattice_matrix


import pymatgen.core as mg
structures=[]
names=[]
all_atomic_number=[]
for nn in range(0,13172):
    print (nn)
    cif_string=str(nn)+'.cif'
    crystal = mg.Structure.from_file('./cif/'+cif_string, 'cif') 

    lattice_matrix=crystal.lattice.matrix
    atomic_numbers=crystal.atomic_numbers
    cart_coords=crystal.cart_coords
    volume=crystal.volume
    class_name='class_'+str(nn)
    #print (atomic_numbers,volume,cart_coords,lattice_matrix)
    class_name=class_II(atomic_numbers,volume,cart_coords,lattice_matrix)
    structures.append(class_name)
    names.append(str(nn))
    all_atomic_number=.extend(list(set(atomic_numbers)))
process('./',structures,names)


################################################
#####  13172 data were divided into training sets, test sets and validation sets
import numpy as np
import pandas as pd
import random
import json

new_dict={}
test=random.sample(range(13172),2000)
new_dict['test']=test
remanent2=set(range(13172))-set(test)
remanent3=random.sample(list(remanent2),8000)
new_dict['train']=remanent3
remanent4=list(remanent2-set(remanent3))
new_dict['val']=o4
with open("split_my_all.json","w") as f:
      json.dump(new_dict,f)




###########################################################################
################The data is divided into seven subsets according to different crystal systems, and the training set, test set and verification set in each subset remain the same as before

with open('split_my_all.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)
Test=json_data['test']
Train=json_data['train']
Val=json_data['val']


data = pd.read_csv('elestic_space_group.csv',sep=',',header=0)
all_crystal_sys=data['spacegroup.crystal_system']

new_dict={}
def find_target_name(List_name,crystal_sy,target_cs):
    #target_cs='tetragonal'
    find_tar_name=[]
    for i in List_name:
        if crystal_sy[i]==target_cs:
            find_tar_name.append(i)
    return find_tar_name

all_crystal_system=['triclinic','monoclinic','trigonal','orthorhombic','hexagonal','tetragonal','cubic']
for cs in all_crystal_system:
    out_test=find_target_name(Test,all_crystal_sys,cs)
    out_train=find_target_name(Train,all_crystal_sys,cs)
    out_val=find_target_name(Val,all_crystal_sys,cs)

    new_dict={}
    new_dict['test']=out_test
    new_dict['train']=out_train
    new_dict['val']=out_val
    with open('split_my_'+cs+'.json','w') as f:
          json.dump(new_dict,f)