import matplotlib.pyplot as plt
rmse = [1.10878, 1.10835, 1.10785, 1.10736, 1.10724, 1.10728, 1.10709, 1.10697,
1.10693, 1.10678, 1.10671, 1.10672, 1.10669, 1.10661]

rmse = [1.14592 ,1.14089 ,1.13981 ,1.13970 ,1.13879 ,1.13817 ,1.13817 ,1.13769 ,1.15879 ,1.15856 ,1.15833 ,1.18205 ,1.19544]

k = [5 ,25 ,50 ,75 ,100 ,125 ,150 ,175 ,200 ,225 ,250 ,275 ,300]

time = [115 ,116 ,117 ,119 ,118 ,120 ,120 ,120 ,121 ,122 ,122 ,124 ,124 ,127]

fig = plt.figure()
plt.plot(k,rmse)
plt.ylabel("RMSE",fontsize='18', fontweight='bold')
plt.xlabel("K",fontsize='18', fontweight='bold')
plt.xticks(k)
plt.grid()
plt.show()


