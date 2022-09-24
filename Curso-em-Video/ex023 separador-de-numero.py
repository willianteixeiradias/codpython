num = int(input('digite um numero'))
if  num < 999:
        u = num //1 % 10
        d = num //10 % 10
        c = num //100 % 10
        print('analisando numero:{}'.format(num))
        print (' a unidade deste numero é:{}'.format(u))
        print ('a dezena deste numero é:{}'.format(d))
        print('a centena deste numero é{}'.format(c))
else:
             print('digite um valor valido')