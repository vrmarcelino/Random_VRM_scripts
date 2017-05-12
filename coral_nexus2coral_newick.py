#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:26:02 2017
Rename species name in a tree
First convert it to newick with HV's script nexus2newick.pl
Run it in Nightowl - ete2 has compatibility problems in my mac
@author: VanessaRM
"""

import re
from ete2 import Tree

t = Tree("01_Huang_MolecularTree.nwk")


for leaf in t.iter_leaves():
    sp_name = str(leaf.name)
    new_name = sp_name.split('_', 1) [-1]
    leaf.name = new_name

# save in newick, format = 5 (internal and leaf branches + leaf names)
t.write(format=5, outfile="formated_tree.nwk")

