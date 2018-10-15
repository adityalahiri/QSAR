import sys,os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

path=os.getcwd()
all_mean_rms = []
for f in os.listdir(path):
	
	if os.path.isdir(f):
                error = 0
                for folder in os.listdir(f):
                	if os.path.isdir(f+"/"+folder):
                                
                                df_train = pd.read_csv(path+'/'+f+'/'+folder+'/independent_train.txt', header=None)
                                df_test = pd.read_csv(path+'/'+f+'/'+folder+'/independent_test.txt', header=None)

                                X_train = df_train.drop([df_train.columns[0], df_train.columns[-1]], axis=1)
                                y_train = df_train[df_train.columns[-1]]

                                X_test = df_test.drop([df_test.columns[0], df_test.columns[-1]], axis=1)
                                y_test = df_test[df_test.columns[-1]]

                                clf = RandomForestRegressor()

                                clf.fit(X_train, y_train)

                                y_out = clf.predict(X_test)

                                error = error + np.sqrt(mean_squared_error(y_test, y_out))
                                
                error/=10
                print(f+": "+str(error))
                
                all_mean_rms.append(error)

print(all_mean_rms)
		
				
