def format(s):
    '''(String) -> String'''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_" #legal characters for title names CANNOT INCLUDE SPACES
    new = ""
    for i in range(len(s)):
        if(s[i] in alphabet):#current character isn't a tab
            new+= s[i]
        else:
            new+= " "
    return new
            
from pandas import read_csv as read
import numpy as np

df = read("pitching.csv")
pitching = np.asarray(df)

s = "last_name	first_name	player_id	year	p_k_percent	n_fastball_formatted	fastball_avg_speed	fastball_avg_spin	fastball_avg_break_x	fastball_avg_break_z	fastball_avg_break	fastball_range_speed	n_breaking_formatted	breaking_avg_speed	breaking_avg_spin	breaking_avg_break_x	breaking_avg_break_z	breaking_avg_break	breaking_range_speed	n_offspeed_formatted	offspeed_avg_speed	offspeed_avg_spin	offspeed_avg_break_x	offspeed_avg_break_z	offspeed_avg_break	offspeed_range_speed"
categories = format(s).split(" ")
kp = pitching[:,4].astype(float) #K%

for i in range(5, len(categories)):
    stat = pitching[:,i].astype(float)
    r = np.corrcoef(kp, stat)
    print(categories[i])
    print(abs(round(r[0,1], 5)))
