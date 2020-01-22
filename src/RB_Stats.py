from os import chdir
from glob import glob
import pandas as pd
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~For 2013 - 2014~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Move to place that holds all the CSV files
csv_file_path = 'C:/Users/12269/Documents/Rushing Stats'
chdir(csv_file_path)
# List all the CSV files in the folder
Y2013_2014 = sorted(glob('*RRushing_stats.csv'))
print(Y2013_2014)


def produceOneCSV(Y2013_2014, file_out):
    # Consolidate all CSV files into one object
    largeRB = pd.concat([pd.read_csv(file) for file in Y2013_2014], axis = 1)
    # Convert the above object into a csv file and export
    largeRB.to_csv(file_out, index=False, encoding="utf-8")

file_out = "LargeRB.csv"
produceOneCSV(Y2013_2014, file_out)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FOR 2014 - 2015 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

csv_file_path = 'C:/Users/12269/Documents/Rushing Stats'
chdir(csv_file_path)
# List all the CSV files in the folder
Y2014_2015 = sorted(glob('*ushing_stats.csv'))
print(Y2014_2015)


def produceOneCSV(Y2014_2015, file_out):
    # Consolidate all CSV files into one object
    largeRB2 = pd.concat([pd.read_csv(file) for file in Y2014_2015], axis = 1)
    # Convert the above object into a csv file and export
    largeRB2.to_csv(file_out, index=False, encoding="utf-8")

file_out = "LargeRB2.csv"
produceOneCSV(Y2014_2015, file_out)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FOR 2015 - 2016 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

csv_file_path = 'C:/Users/12269/Documents/Rushing Stats'
chdir(csv_file_path)
# List all the CSV files in the folder
Y2015_2016 = sorted(glob('*Rushing_stat.csv'))
print(Y2015_2016)


def produceOneCSV(Y2015_2016, file_out):
    # Consolidate all CSV files into one object
    largeRB3 = pd.concat([pd.read_csv(file) for file in Y2015_2016], axis = 1)
    # Convert the above object into a csv file and export
    largeRB3.to_csv(file_out, index=False, encoding="utf-8")

file_out = "LargeRB3.csv"
produceOneCSV(Y2015_2016, file_out)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FOR 2016 - 2017 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

csv_file_path = 'C:/Users/12269/Documents/Rushing Stats'
chdir(csv_file_path)
# List all the CSV files in the folder
Y2016_2017 = sorted(glob('*Rushing.csv'))
print(Y2016_2017)


def produceOneCSV(Y2016_2017, file_out):
    # Consolidate all CSV files into one object
    largeRB4 = pd.concat([pd.read_csv(file) for file in Y2016_2017], axis = 1)
    # Convert the above object into a csv file and export
    largeRB4.to_csv(file_out, index=False, encoding="utf-8")

file_out = "LargeRB4.csv"
produceOneCSV(Y2016_2017, file_out)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FOR 2017 - 2018 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

csv_file_path = 'C:/Users/12269/Documents/Rushing Stats'
chdir(csv_file_path)
# List all the CSV files in the folder
Y2017_2018 = sorted(glob('*Rushing_stats.csv'))
print(Y2017_2018)


def produceOneCSV(Y2017_2018, file_out):
    # Consolidate all CSV files into one object
    largeRB5 = pd.concat([pd.read_csv(file) for file in Y2017_2018], axis = 1)
    # Convert the above object into a csv file and export
    largeRB5.to_csv(file_out, index=False, encoding="utf-8")

file_out = "LargeRB5.csv"
produceOneCSV(Y2017_2018, file_out)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Put it all together ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

csv_file_path = 'C:/Users/12269/Documents/Rushing Stats'
chdir(csv_file_path)
# List all the CSV files in the folder
Final = sorted(glob('LargeRB*'))
print(Final)


def produceOneCSV(Final, file_out):
    # Consolidate all CSV files into one object
    totalLarge = pd.concat([pd.read_csv(file) for file in Final], axis = 0)
    # Convert the above object into a csv file and export
    totalLarge.to_csv(file_out, index=False, encoding="utf-8")

file_out = "totalLarge.csv"
produceOneCSV(Final, file_out)


RBdata2013 = pd.read_csv("../data/Rushing Stats/2013_Rushing_stats.csv")
RBdata2013.head()

RBdata2014 = pd.read_csv("../data/Rushing Stats/2014_Rushing_stats.csv")
RBdata2014.head()

RBdata2015 = pd.read_csv("../data/Rushing Stats/2015_Rushing_stats.csv")
RBdata2015.head()

RBdata2016 = pd.read_csv("../data/Rushing Stats/2016_Rushing_stats.csv")
RBdata2016.head()

RBdata2017 = pd.read_csv("../data/Rushing Stats/2017_Rushing_stats.csv")
RBdata2017.head()

RBdata2018 = pd.read_csv("../data/Rushing Stats/2018_Rushing_stats.csv")
RBdata2018.head()
