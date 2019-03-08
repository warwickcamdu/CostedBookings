def generate_costs(frame):
    import pandas as pd
    frame = frame.add_suffix('_summary').reset_index()
    users = frame['user'].unique().tolist()
    newframe = pd.DataFrame(users, columns=['user'])
    for micro in ['DV1', 'DV2', 'UltraVIEW']:
        micro_frame = frame[frame['micro'].str.contains(micro,case=False)]
        for index, row in newframe.iterrows():
            if (micro_frame['user']==row.user).any():
                newframe.loc[index,micro+'_hours'] = float(micro_frame[micro_frame['user']==row['user']]['cost_hours_summary'])
        
    newframe.fillna(0,inplace=True)
    newframe = add_access(newframe) 
    
    costs = load_costs()
    
    newframe = calculate_costs(newframe,costs)
    newframe = cleanup(newframe)

    return newframe



def add_access(frame):
    import pandas as pd
    access = pd.read_csv("legacy/emails_gmails_costcodes.csv")

    for micro in ['DV1', 'DV2', 'UltraVIEW']:
        
        for index, row in frame.iterrows():
            if (access['Gmail']==row.user.split(" ")[1]).any():
                frame.loc[index,micro+'_access'] = int(access[access['Gmail']==row.user.split(" ")[1]][micro])


    return frame


def load_costs():
    import pandas as pd
    costs = pd.read_csv("legacy/costs.csv")
    return costs


def calculate_costs(frame,costs):
    micros = ['DV1', 'DV2', 'UltraVIEW']
    titles = ['Deltavision Elite (DV1)', 'Deltavision Personal (DV2)', 'UltraVIEW spinning disk']
    for i in range(len(micros)):
        micro = micros[i]
        title = titles[i]
        for index, row in frame.iterrows():
            
            if costs[costs['access level'] == row[micro+'_access']][title].any():
                
                cost = costs[costs['access level'] == row[micro+'_access']][title]

            else:
                cost = 0
            frame.loc[index,micro+'_cost'] = float(cost)*row[micro+'_hours']
    
    frame['total_cost'] = frame.iloc[:,-3:].sum(axis=1)
    for micro in micros:
        frame.drop(micro+"_cost", axis=1, inplace=True)
        frame.drop(micro+"_access", axis=1, inplace=True)
    
    return frame

def cleanup(frame):
    for index, row in frame.iterrows():
        frame.loc[index,'username'] = row['user'].split(" ")[0]
        frame.loc[index,'email'] = row['user'].split(" ")[1]
        micros = ['DV1', 'DV2', 'UltraVIEW']
        empty = 1
        for micro in micros:
            if (row[micro+"_hours"]>0):
                empty = 0
        print(empty)
        if empty:
            frame.drop(index,inplace=True)
    frame.drop("user", axis=1, inplace=True)
    cols = list(frame.columns.values)
    newcols = [cols[-2],cols[-1]]
    newcols.extend(cols[:-2])
    frame = frame[newcols]
    return frame