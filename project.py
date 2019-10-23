import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from keras.callbacks import EarlyStopping
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

prescribers = pd.read_csv('/Users/brooklynokelley-bangsberg/Downloads/prescriber-info.csv')
overdoses = pd.read_csv('/Users/brooklynokelley-bangsberg/Downloads/overdoses.csv')
opioids = pd.read_csv('/Users/brooklynokelley-bangsberg/Downloads/opioids.csv')
prescribers.head()

prescribers.describe()

specialty = pd.DataFrame(prescribers.groupby(['Specialty']).count()['NPI']).sort_values('NPI')
