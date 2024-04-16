import math

def get_top_bottom(current_node, mapp, bottom = False):
    x, y = current_node
    map_height = len(mapp)
    return (x, (y + (2*bottom - 1) ) % map_height), mapp  # ADJUST HEIGHT WHEN h IS 3**(0.5)/2

def get_right_left(current_node, mapp, wantTopOrBottom = False, left = False):
    x, y = current_node
    map_width = len(mapp[0])
    if mapp[y][(x + (-2*left + 1 )) % map_width] != " ":
        return ((x + (-2*left + 1 )) % map_width, y), mapp
    else:
    	return get_right_left(((x + (-2*left + 1 )) % map_width, y), mapp, left = left)
    # return ((x + int(1/(wantTopOrBottom + 1)))%map_width, y), mapp  

def get_top_right_left(current_node, mapp, left = False):
    current_node, mapp = get_top_bottom(current_node, mapp)
    return get_right_left(current_node, mapp, left=left)

def get_bottom_right_left(current_node, mapp, left=False):
    current_node, mapp = get_top_bottom(current_node, mapp, bottom=True)
    return get_right_left(current_node, mapp, left=left)

def get_neighbours(current_node, mapp):
    getLeft = True
    return {
            'right' : get_right_left(current_node, mapp)[0],
            'left' : get_right_left(current_node, mapp, left = True)[0],
            'top-right' : get_top_right_left(current_node, mapp)[0],
            'top-left' : get_top_right_left(current_node, mapp, left=True)[0],
            'bottom-right' : get_bottom_right_left(current_node, mapp)[0],
            'bottom-left' : get_bottom_right_left(current_node, mapp, left=True)[0]
            }

def print_mapp(mapp, point = None):
    """
    FUNCTION TO VISUALISE THE LATTICE
    FOR WIDTH = 6, HEIGHT = 6, THE LATTICE WILL LOOK LIKE -

       0 1 2 3 4 5  - X POSITION/INDEX OF LATTICE POINT FOR LAYER 1 
        0 1 2 3 4 5 - X POSITION/INDEX OF LATTICE POINT FOR LAYER 2 
    --------------
    0| o o o o o o 
    1|  o o o o o o
    2| o o o o o o 
    3|  o o o o o o
    4| o o o o o o 
    5|  o o o o o o
    ^--- Y AXIS OF THE LATTICE
    """

    _width = max(len(mapp[1]), len(mapp[0]))
    _height = len(mapp)

    toColor = False
    if point:
        toColor = True
        toColor_y = point[1]
        toColor_x = point[0]
        _mapp_y = list(mapp[toColor_y]) 
        _mapp_y[toColor_x] = f"{GREEN+unit+RESET}"
        mapp[toColor_y] = "".join(_mapp_y)
    
    _string_mapp = ""
    
    for y in range(_height + 1):
        _line = []
        if not y:
            _line = []
            _line.append(" "*3)
            [_line.append(str(x//2)+ " ") for x in range(0, _width, 2)]
            _line = "".join(_line)
            _string_mapp += _line + "\n"
            
            _line = []
            _line.append(" "*4)
            [_line.append(str(x//2)+ " ") for x in range(0, _width, 2)]
            _line = "".join(_line)
            _string_mapp += _line + "\n"
            
            
            _line = []
            _line.append(" "*2)
            [_line.append('--') for x in range( _width//2 + 1)]
            _line = "".join(_line)
            _string_mapp += _line + "\n"
            continue
            
        _line.append(str(y-1) + "| ")
        _line.append(mapp[y-1])
        
        _line = "".join(_line)
        
        _string_mapp += _line + "\n"
    print(_string_mapp)
    # print()

def mapp_to_corr(pos):
    """
    FUNCTION TO CONVERT LATTICE POINT FROM REPRESENTAION TO PYTHON INDEX/COORDINATES.  
    """
    x, y = pos
    # return ((x+(y%2))/2, y)
    return (math.ceil((x+(y%2)*(-1))/2), y)

def corr_to_mapp(corr):
    """
    FUNCTION TO CONVERT LATTICE POINT FROM PYTHON INDEX/COORDINATES TO REPRESENTAION.  
    """
    x, y = corr 
    return (2*x + (y%2) , y)


MAP_HEIGHT = 6
MAP_WIDTH = 6

GREEN = '\033[1;32;40m'
RESET = '\033[0m'

gap = 0

unit = "x"
space = " "

mapp = []
mapp_dict = {'nodes' : []}

for y in range(MAP_HEIGHT):
    _mapp = []
    _x = 0
    coor = []
    if gap:
        print(space, end="")
        _mapp.append(space)
        _x = 1
    for x in range(MAP_WIDTH):
        print(unit, end=" ") 
        _mapp.append(unit)

    mapp_dict['nodes'] += [(xs, y) for xs in range(_x, 2*MAP_WIDTH, 2)]
    mapp.append("".join(_mapp))
    gap = (gap+1)%2
    print()
    
# print(mapp_dict)
_mapp_parts = []
'''
for i in mapp:
    _inner = []
    for j in " ".join(i):
        _inner.append(j)
    _mapp_parts.append(_inner)
'''

to_print = ["".join([unit if (x,y) in mapp_dict['nodes'] else space for x in range(2*MAP_WIDTH)]) for y in range(MAP_HEIGHT) ]

# [print(i) for i in to_print]
# [print(i) for i in _mapp_parts]

print()
print_mapp(to_print)

_mapp_parts = to_print
    
x = int(input("Enter x : ").strip())
y = int(input("Enter y : ").strip())

curr = corr_to_mapp((x,y))

print(curr)
print_mapp(to_print, curr)

nb = get_neighbours(curr, _mapp_parts)
nb2 = {}
for _dir, _val in nb.items():
    nb2[_dir] = mapp_to_corr(_val)
print(nb2)
