# https://www.reddit.com/r/dataisbeautiful/comments/msv3pn/oc_republican_states_trail_democratic_states_in/
# https://www.nytimes.com/interactive/2020/us/covid-19-vaccine-doses.html
import json
from matplotlib import pyplot as plt


with open('./states-data.json') as f:
  data = json.load(f)

def judgement(state):
    # return state['population']
    return state['dosesGiven'] / state['dosesDelivered']

states_data = sorted(data, key=lambda state: judgement(state), reverse=True)
fig,ax = plt.subplots()

plt.rcParams["figure.figsize"] = (15,6)

y_data = [judgement(state) for state in states_data]
x_data = [state['dosesGiven'] for state in states_data]
colors = ['#497ffc' if state['wasBiden'] else '#fc5549' for state in states_data]
plt.scatter(x_data, y_data, c=colors)

dot_labels = [state['initials'] for state in states_data]
# To give a label to each dot
for i, txt in enumerate(dot_labels):
    ax.annotate(txt, (x_data[i], y_data[i]), rotation=45)


from matplotlib.ticker import FuncFormatter

def millions_formatter(x, pos):
    return f'{x / 1000000}'

def percent_formatter(y, pos):
    return f'{int(y * 100)}%'

ax.xaxis.set_major_formatter(FuncFormatter(millions_formatter))
ax.yaxis.set_major_formatter(FuncFormatter(percent_formatter))
ax.set_xlabel('Doses Given to State (in millions)')

plt.show()
