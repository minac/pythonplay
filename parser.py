f = open('input.txt', 'r')
f2 = open('output.txt', 'w')
for l in f:
    if "=" in l:
        l2 = l.split('=')
        l3 = l2[1]
    else:
        l3 = l
    l4 = l3.replace("\"","")
    l5 = l4.replace(";","")
    l6 = l5.replace("<br/>","\n")
    l7 = l6.replace("<hr class","")
    f2.write(l7)
    print l7

f.close()
f2.close()
