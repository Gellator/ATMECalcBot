import sqlite3
import datetime
import time

database_file = 'Troops.db'
table_name = 'Units'

def TESTGetCostPerUnit(unit):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    Select_sql = f"SELECT * FROM Units WHERE Apothecary_Duration = {unit}"
    for row in conn.execute(Select_sql):
        print(row)
    conn.close()

def Get_Cost_Per_Unit_Lost(unit,amount_injured, amount_lost):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    string = "'" + unit + "'"                                                   # Done for formating of input data to match -SG
    Select_sql = f"SELECT * FROM Units WHERE Title={string}"
    for row in conn.execute(Select_sql):
        perCommand =row[1]
        '''
        try:
            conscript = time.strptime(row[6], "%H:%M:%S")
            #per_unit_time = conscript - datetime.timedelta(seconds=conscript.second)
            time.time()
            per_unit_time = (conscript.time()/perCommand)* amount_lost
            print(per_unit_time)
        except ValueError:
            print("Invalid format of time Please check UnitDatabase.csv to address issue")
        try:
            apothecary = datetime.datetime.strptime(row[8], "%H:%M:%S")
            per_unit_time = apothecary - datetime.timedelta(seconds=apothecary.second)
            per_unit_time = apothecary/perCommand
            time_per_apothecary = per_unit_time.strftime("%H:%M:%S")
        except ValueError:
            print("Invalid format of time Please check UnitDatabase.csv to address issue")    
        '''
        wood =(row[2]/perCommand)*amount_lost
        ore = (row[3]/perCommand)*amount_lost
        grain =(row[4]/perCommand)*amount_lost
        gold =(row[5]/perCommand)*amount_lost
        apothGrain = (row[7]/perCommand)*amount_injured
        #print(time_per_apothecary)
        
        
    conn.close()
    Resources_lost = Unit_Losses(wood, ore, grain, gold, apothGrain)
    return Resources_lost
    
def SQLCheck():
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    for row in conn.execute('''SELECT * FROM Units '''):
        print(row)
    conn.close()

class Unit_Losses:
    def __init__(self, wood_lost, ore_lost, grain_lost, gold_lost, grain_for_apoth_lost):
        self.wood_lost = wood_lost
        self.ore_lost = ore_lost
        self.grain_lost = grain_lost
        self.gold_lost = gold_lost
        self.grain_for_apoth_lost = grain_for_apoth_lost
    
    def GetTotal(self):
        total = self.wood_lost + self.ore_lost +self.grain_lost+self.gold_lost+self.grain_for_apoth_lost
        return total
        
           
def Calculate_Cost_Per_Amy(unit1,injured1, lost1, unit2,injured2, lost2, unit3,injured3, lost3):
    losses=[]
    Set1=Get_Cost_Per_Unit_Lost(unit1,injured1, lost1)
    Set2=Get_Cost_Per_Unit_Lost(unit2,injured2, lost2)
    Set3=Get_Cost_Per_Unit_Lost(unit3,injured3, lost3)
    wood_lost = Set1.wood_lost + Set2.wood_lost + Set3.wood_lost
    ore_lost = Set1.ore_lost + Set2.ore_lost + Set3.ore_lost
    grain_lost = Set1.grain_lost + Set2.grain_lost + Set3.grain_lost
    gold_lost = Set1.gold_lost + Set2.gold_lost + Set3.gold_lost
    grain_for_apoth_lost = Set1.grain_for_apoth_lost + Set2.grain_for_apoth_lost + Set3.grain_for_apoth_lost
    
    print("This is the wood lost: " , wood_lost)
    print("This is the ore lost: " ,ore_lost)
    print("This is the grain lost: " ,grain_lost)
    print("This is the gold lost: " ,gold_lost)
    print("This is the grain for apothecary lost: " ,grain_for_apoth_lost)
    Battle_Losses = Unit_Losses(wood_lost, ore_lost, grain_lost, gold_lost, grain_for_apoth_lost)
    return Battle_Losses
    
def Compare_Battle_Cost(Army1Cost, Army2Cost):
    print("ok")
    Cost1 = Army1Cost.GetTotal()
    Cost2 = Army2Cost.GetTotal()
    total = Cost1 + Cost2
    Percent1 = (Cost1/total)*100
    Percent2 = (Cost2/total)*100
    return Percent1, Percent2
        

if __name__ == "__main__":
    #SQLCheck()
    #Get_Cost_Per_Unit_Lost('Ents', 43)    
    Your_Army_Cost = Calculate_Cost_Per_Amy('Sharpshooter',10,507, 'Guard of the Tower',20, 127,'Dragoon',5,74 )
    Enemy_Army_Cost = Calculate_Cost_Per_Amy('Sharpshooter',10,800, 'Guard of the Tower',20, 1023,'Dragoon',5,80 )
    Rating1, Rating2 = Compare_Battle_Cost(Your_Army_Cost,Enemy_Army_Cost)
    print(Rating1)
    print(Rating2)


#TODO
'''
Create Discord Bot GUI to provide info to bot

'''