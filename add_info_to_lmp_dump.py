import MDAnalysis as mda
from MDAnalysis.topology import guessers
import numpy as np
import pandas as pd
import re

def add_ele_info(traj, ele_dic):
    ele = list(map(ele_dic.get, traj.atoms.types))
    traj.add_TopologyAttr('elements', ele)

def add_topo_to_lmp_dump(traj):
# add element info
    ele_dic = {'1':'C', '2':'H', '3':'N', '4':'O'}
    add_ele_info(traj, ele_dic)
# guess mass
    masses = guessers.guess_masses(traj.atoms.elements)
    traj.add_TopologyAttr('masses', masses)

    return traj

traj = mda.Universe("./test.lammpstrj", format = "LAMMPSDUMP")
traj = add_topo_to_lmp_dump(traj)

xyz = mda.Universe("ref.xyz") 

# print(traj.select_atoms("bynum 1").positions)
# print(xyz.select_atoms("bynum 1").positions)

for ts in traj.trajectory:
    print(ts.frame)
    print(ts.positions[0, :])
    print(traj.atoms.elements)
    print(traj.atoms.masses)
    traj.atoms.write("ts0.xyz")

    break
