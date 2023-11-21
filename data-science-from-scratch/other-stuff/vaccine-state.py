# https://www.reddit.com/r/dataisbeautiful/comments/msv3pn/oc_republican_states_trail_democratic_states_in/
# https://www.nytimes.com/interactive/2020/us/covid-19-vaccine-doses.html

import json
from matplotlib import pyplot as plt


with open('./states-data.json') as f:
  data = json.load(f)

def judgement(state):
  # return state['population']
  return state['dosesGiven'] / state['population']

states_data = sorted(data, key=lambda state: judgement(state), reverse=True)[:25]

# Lets default our image to a larger size
plt.rcParams["figure.figsize"] = (15,6)

x_data = range(len(states_data))
y_data = [judgement(state) for state in states_data]

# We need these for fancy labels later
fig,ax = plt.subplots()

# by saving the bars to a value, we can color individually
barlist = plt.bar(x_data, y_data)
for i, bar in enumerate(barlist):
    bar.set_color('#497ffc' if states_data[i]['wasBiden'] else '#fc5549')

# This is how to rotate the labels (plt.subplots needs to go before the data)
plt.xticks(range(len(states_data)), [state['name'] for state in states_data])
ax.set_xticklabels([state['name'] for state in states_data])
fig.autofmt_xdate(rotation=45)

plt.show()
