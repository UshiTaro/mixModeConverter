import sys
import skrf as rf
import numpy as np

if len(sys.argv) == 1:
    print("Mixmode S-parameter converter.")
    print("please input filename(.s4p)", file=sys.stderr)
    print()
    print("1-|      |-2      1 -|dd.s2p|dc.s2p|-2")
    print("  |[.s4p]|    ->     |------+------|")
    print("3-|      |-4      1'-|cd.s2p|cc.s2p|-2'")
    sys.exit(0)
try:
    fn = sys.argv[1]
    net = rf.Network(fn)
except:
    print("Error: File Couldn't Read.", file=sys.stderr)
    sys.exit(1)

freq = net.f
s4 = net.s

M = np.array([[1, 0, -1, 0],
              [0, 1, 0, -1],
              [1, 0, 1, 0],
              [0, 1, 0, 1]], dtype=complex)/np.sqrt(2)
Mi = np.linalg.inv(M)

sMM = np.matmul(np.matmul(M, s4), Mi)

sDD = sMM[:,:2,:2]
sDC = sMM[:, :2,2:]
sCC = sMM[:,2:,2:]
sCD = sMM[:, 2:,:2]

netDD = rf.Network(frequency=freq, s=sDD)
netDC = rf.Network(frequency=freq, s=sDC)
netCC = rf.Network(frequency=freq, s=sCC)
netCD = rf.Network(frequency=freq, s=sCD)
netDD.write_touchstone(filename=fn+"_dd.s2p")
netDC.write_touchstone(filename=fn+"_dc.s2p")
netCC.write_touchstone(filename=fn+"_cc.s2p")
netCD.write_touchstone(filename=fn+"_cd.s2p")
