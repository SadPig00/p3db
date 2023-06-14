import random
import pandas as pd
import math
from database import Database

df = pd.read_csv("structure_tiltmeter.dat")
modifyDf={ i:df[i]+random.uniform(-(abs(max(df[i]))-abs(min(df[i]))/2),
          (abs(max(df[i]))-abs(min(df[i]))/2)) if idx>0 else df[i] for idx,  i in enumerate(df) }
pd.DataFrame(modifyDf).to_csv("modifyDf.csv")
modifyDf = pd.read_csv("modifyDf.csv")
obj={}
for idx,key in enumerate(modifyDf):
    if(key == 'opdatetime') :
        obj.setdefault(key,modifyDf[key])
    else:
        if(idx%2==0):
            obj.update({key[:-2] : [math.atan2(x,y)*180/math.pi for x,y in zip(obj[key[:-2]],  modifyDf[key])]})
        else:
            obj.setdefault(key[:-2],  modifyDf[key])

pd.DataFrame(obj).to_csv('modifyDf_tiltCalc.csv')
db_class = Database()
modifyDf_tiltCalc = pd.read_csv("modifyDf_tiltCalc.csv")
for i in modifyDf_tiltCalc.values:
    db_class.execute("insert into tiltData values (null,'"+str(i[0])+"','"+str(i[1])+"','"+
                     str(i[2])+"','"+str(i[3])+"','"+str(i[4])+"','"+str(i[5])+
                     "','"+str(i[6])+"','"+str(i[7])+"')")
    db_class.commit()


temp_Batt = pd.read_csv("structuredata.dat")
for data in temp_Batt.values:
    db_class.execute("update tiltData set temp='"+str(data[3])+"', batt='"+str(data[2])
                     +"' where updatetime='"+str(data[1])+"'")
    db_class.commit()
result = db_class.executeAll("select * from tiltData where batt is not null and temp is not null")
pd.DataFrame(result).to_csv("AllCalcData.csv")


db_class = Database()
result = pd.read_csv("AllCalcData.csv")
for data in result.values:
    db_class.execute("insert into tiltData values (null,'" + str(i[2]) + "','" + str(i[3]) + "','" +
                     str(i[4]) + "','" + str(i[5]) + "','" + str(i[6]) + "','" + str(i[7]) +
                     "','" + str(i[8]) + "','" + str(i[9])+"','" +str(i[10]) + "','" +str(i[11]) + "')")

