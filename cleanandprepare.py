import sys,os

path=os.getcwd()
for f in os.listdir(path):
	
	if os.path.isdir(f):
		for folder in os.listdir(f):
			
			if os.path.isdir(f+"/"+folder):
				
				fp_test=open(path+'/'+f+'/'+folder+'/test.arff')
				fp_train=open(path+'/'+f+'/'+folder+'/train.arff')
				fpw_test=open(path+'/'+f+'/'+folder+'/independent_test.txt','w')
				fpw_train=open(path+'/'+f+'/'+folder+'/independent_train.txt','w')
		
				for line in fp_train:
					if line[0]!='@':
						fpw_train.write(line)
				for line in fp_test:
					if line[0]!='@':
						fpw_test.write(line)

