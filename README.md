# SimpleScript
some little, but useful scripts in life

## bfnode.py
node check script with brief output:

check if the node is working normally,
including function can get you spare cores, which is usally dealed with job sub controller,
but I want a **breif** output especially when there are dozen nodes.

## deljob
if hundreds jobs submitted and one want to delete only part of them,
the script allows one delete jobs in python slice fever, like `deljob slice_str`, of slice string including "3", ":3", "2:", "1:3", "::2"

## add_info_to_lmp_dump
add missing info to mdanalysis trajectory object reading from lammps dump file.
Mdanalysis is useful, but it's not easy to find functions you want, so I put it here

## seq_reorder
reorder numpy array rows by another integers array, can be used at reordering positions of atoms
