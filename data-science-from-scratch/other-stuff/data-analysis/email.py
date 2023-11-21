# https://www.reddit.com/r/dataisbeautiful/comments/msv3pn/oc_republican_states_trail_democratic_states_in/
# https://www.nytimes.com/interactive/2020/us/covid-19-vaccine-doses.html
import json
from matplotlib import pyplot as plt
import datetime

def Average(lst):
    if len(lst) == 0: return 0
    return sum(lst) / len(lst)

def convert_date(date):
    x = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    return x.strftime("%m-%d")

with open('./email.json') as f:
  email_data = json.load(f)

email_data = [email for email in email_data if sum(email['sales']) < 3000]


def get_sum_sales():
    emails_by_sum = sorted(email_data, key=lambda x: sum(x['sales']), reverse=True)

    fig,ax = plt.subplots()

    x_data = [email['name'] for email in emails_by_sum]
    y_data = [sum(email['sales']) for email in emails_by_sum]
    colors = ['#497ffc' if email['type'] == 'ind' else '#fc5549' for email in emails_by_sum]
    barlist = plt.bar(x_data, y_data, label="hi")
    for i, bar in enumerate(barlist):
        bar.set_color('#497ffc' if emails_by_sum[i]['type'] == 'blast' else '#fc5549')

    for i, value in enumerate(y_data):
        plt.text(x = i-0.2 , y = value + 30, s = value, size = 6, rotation=45)

    plt.xticks(range(len(emails_by_sum)), [state['name'] for state in emails_by_sum])
    ax.set_xticklabels([f"{state['name'][0:15]}..." for state in emails_by_sum])
    fig.autofmt_xdate(rotation=30)

    plt.title("Total Sales Per Email")
    plt.ylabel("Total Sales")
    plt.show()

def find_data():
    def find_below(amnt):
        below_amnt = [email for email in email_data if sum(email['sales']) < amnt]
        num_below_amnt = len(below_amnt)
        pcent_below_amnt = round(100 * num_below_amnt / len(email_data))
        print(f"Num of emails below ${amnt}: {len(below_amnt)}, or {pcent_below_amnt}% of all emails")
    find_below(500)
    find_below(1)

    def blast_emails():
        blasts = [sum(email['sales']) for email in email_data if email['type'] == 'blast']

        avg_clicks = Average([ email['clicks'] for email in email_data if email['type'] == 'blast'])
        print(f"{avg_clicks}")

        print(f"Number of blast emails: {len(blasts)}")
        print(f"Average money earned by blasts: {Average(blasts)}")

    def ind_emails():
        ind = [sum(email['sales']) for email in email_data if email['type'] == 'ind']
        avg_clicks = Average([ email['clicks'] for email in email_data if email['type'] == 'ind'])
        print(f"{avg_clicks}")
        print(f"Number of independent emails emails: {len(ind)}")
        print(f"Average money earned by ind: {Average(ind)}\n")

    blast_emails()
    ind_emails()


find_data()
get_sum_sales()
