import numpy as np

def Matrixx(lenn):
    if lenn%2 == 1: # FOR HANDELING ERROR
        print("Length not multiple of 2")
        return 0
    
    M = []
    M_up = []
    M_ins = []

    # lenn = 8
    M_up = [[1/2 if i%(lenn//2)==j else 0 for i in range(lenn)] for j in range(lenn//2)]
    M_ins = [[(-1)**((i >= lenn//2))*1/2 if i%(lenn//2) == j else 0 for i in range(lenn)] for j in range(lenn//2)]
    
    for i in range(lenn):
        if i%2==0:
            M.append(M_up[i//2])
        else:
            M.append(M_ins[i//2])
    return M

if __name__ == "__main__":
    # print(Matrixx(2))
    print(np.array(Matrixx(int(input("Enter size of matrix : ")))))




