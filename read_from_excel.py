# formats the first row to get labels
def format(str):
    '''(String) -> String'''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_" #legal characters for title names CANNOT INCLUDE SPACES
    new = ""
    for i in range(len(str)):
        if(str[i] in alphabet):#current character isn't a tab
            new+= str[i]
        else:
            new+= " "
    return new
            
from pandas import read_csv as read
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

df = read("pitching.csv")

row1 = "last_name	first_name	player_id	year	p_k_percent	n_fastball_formatted	fastball_avg_speed	fastball_avg_spin	fastball_avg_break_x	fastball_avg_break_z	fastball_avg_break	fastball_range_speed	n_breaking_formatted	breaking_avg_speed	breaking_avg_spin	breaking_avg_break_x	breaking_avg_break_z	breaking_avg_break	breaking_range_speed	n_offspeed_formatted	offspeed_avg_speed	offspeed_avg_spin	offspeed_avg_break_x	offspeed_avg_break_z	offspeed_avg_break	offspeed_range_speed"
predictors = format(row1).split(" ")
kp = df.iloc[:,4] # strikeout percentage for every pitcher

# dictionary of predictors and their relationshop to k%
r = {}

# display the correlation between each
for i in range(5, len(predictors)):
    if (i != 5 and i != 12 and i != 19): #skip the "formatted" labels
        predictor = df.iloc[:,i]
        r[predictors[i]] = pearsonr(kp, predictor).correlation
        plt.bar(i*2, r[predictors[i]], label=predictors[i])

print(r)

plt.plot(0,0)
plt.plot(0,1)

# plot the datas
plt.xlabel('Pearson Correlation')
plt.title('Correlation between Pitch Metrics and Strikeout Percentage')
plt.legend(title='Pitch Metric/Predictor',loc='upper left')
plt.grid(True)
plt.xticks([])
plt.show()