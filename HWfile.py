#pylint:disable=W0301
#pylint:disable=W0312
def smth(*args):
	chl=[]
	p=0
	for i in args:
		chl.append(i);
		p+=1;
		print(p, chl[p-1])
	print(enumerate(chl));
	print(enumerate(args));
	othr=args;
	print(othr[0], enumerate(othr));
smth(7, 8)

