import numpy as np
# regular positions shape: (N_atom, 3)

def reorder_test():
    N_atom = 4
    ori_pos = np.random.rand(N_atom,3)
    seq_test = np.arange(N_atom)
    np.random.shuffle(seq_test)
    print("\noriginal positions:")
    print(ori_pos)
    print("\nshuffled index number for test:")
    print(seq_test)
    new_pos = reorder_pos(seq_test, ori_pos)
    print("\nnew_pos after ordered with shuffled number:")
    print(new_pos)
    print("\nreturn to oringal positions by new_pos:")
    print(new_pos[seq_test, :])

def reorder_pos(new_order, pos):
    new_index = np.argsort(new_order)
    # res = pos[new_index[::-1], :]
    res = pos[new_index, :]
    return res


reorder_test()
