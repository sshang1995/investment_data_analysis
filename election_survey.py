import numpy as np
import matplotlib.pyplot as plt


survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']


total_ceballos = sum([1 for i in survey_responses if i == 'Ceballos'])
print(total_ceballos)

survey_len = float(len(survey_responses))
percentage_ceballos = total_ceballos/survey_len*100
print(percentage_ceballos)

possible_surveys = np.random.binomial(survey_len,0.54,size=10000) / survey_len

ceballos_loss_surveys=np.mean(possible_surveys <0.5)
print(ceballos_loss_surveys)

large_survey = np.random.binomial(float(7000),0.54,size=10000)/float(7000)

plt.close()
plt.hist(possible_surveys, range = (0,1),bins = 20)
plt.hist(large_survey, alpha=0.5, range = (0,1),bins = 20)
plt.show()

ceballos_loss_new = np.mean(large_survey<0.5)
print(ceballos_loss_new)

