"""
identifies atoms capable of hydrogen bonding
"""
import mdtraj as md

def count(top_object):
"""
Returns list of indeces of specific atoms
"""
	c = [atom.index for atom in top_object.atoms if atom.element.symbol is 'C']
	n = [atom.index for atom in top_object.atoms if atom.element.symbol is 'N']
	s = [atom.index for atom in top_object.atoms if atom.element.symbol is 'S']
	o = [atom.index for atom in top_object.atoms if atom.element.symbol is 'O']
	p = [atom.index for atom in top_object.atoms if atom.element.symbol is 'P']
	h = [atom.index for atom in top_object.atoms if atom.element.symbol is 'H']
	return n, h, o, s, p



t = md.load('aa2ar_prot.pdb')
top = t.topology

n_atom_indices = count(top)[0]
for bond in top.bonds:
"""
returns all bonds containing nitrogen atoms and the indeces of the bonded atoms
"""
	if bond[0].index in n_atom_indices:
		print(bond, bond[0].index, bond[1].index)
		


n_donor = []
n_acceptor = []

n_atom_indices = count(top)[0]
for bond in top.bonds:
"""
assigns nitrogen atoms as acceptors or donors
"""
	for bond[0].index in n_atom_indeces :
		if bond[1].element.symbol == 'H' :
        		n_donor.append(bond[0].index)
   		 else:
   	    		n_acceptor.append(bond[0].index)
	  

print(n_donor)

print(n_acceptor)

o_both = []
o_acceptor = []

o_atom_indices = count(top)[2]
for bond in top.bonds:   
"""
assigns oxygen atoms as acceptors or both donors and acceptors
"""
    if bond[1].element.symbol == 'H' :
    	n_both.append(bond[0].index)
    else:
    	n_acceptor.append(bond[0].index)
	  

print(n_donor)


