a=input()
index_h=a.find('h')
index_e=a.find('e',index_h+1)
index_l=a.find('l',index_e+1)
index_ll=a.find('l',index_l+1)

index_o=a.find('o',index_ll+1)
if index_h==-1:
    print("NO")
elif index_e==-1:
    print("NO")
elif index_l==-1 or index_ll==-1:
    print("NO")
elif index_o==-1:
    print("NO")
else:
    print("YES")
