units=int(input(' units:'))
if ( units>=1 and units<=100):
    cost=(units*1.5);
elif(units<=200)   :
    cost=((units*100)+(units-100)*2.5 );
elif(units<=300):
    cost=((100*1.5)+(100*2.5)+(units-200)*4);
elif(units<=350):
    cost=((100*1.5)+(100*2.5)+(100*4)+(units-300)*5);
elif(units>350):
    cost=((100*1.5)+(100*2.5)+(100*4)+(100*5)+(units-350)*15);
print("bill=",cost)               