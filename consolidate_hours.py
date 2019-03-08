def consolidate_hours(parsed):
    import pandas as pd
    frame = pd.DataFrame(parsed,columns=['micro', 'user', 'start', 'end', 'hours', 'cost_hours', 'dayofweek', 'costcode'])
    
    sum_frame = frame.groupby(['micro', 'user']).agg({'hours': 'sum', 'cost_hours':'sum', 'costcode':'first'})
    return sum_frame



def add_costcodes(events):
    import csv
    import pandas as pd
    with open("legacy/emails_gmails_costcodes.csv", 'r') as f:
        reader = csv.reader(f)
        costcodes = list(reader)
        headers = costcodes.pop(0)
        frame = pd.DataFrame(costcodes,columns=headers)
        
    for i in range(len(events)):
        event = events[i]
        person = event[1].split()[1]
        
        costcode = (frame[frame['Gmail'] == person]['cost code'].any() or [None])
        #print("person is "+ person+ ", costcode is "+costcode)
        events[i].append(costcode)

    
    return events


if __name__ == "__main__":
    test = add_costcodes([])
    #print(test)