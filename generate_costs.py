def generate_costs(frame):

    """
    Creates a Dataframe with unique users and costs/costcodes per microscope. 

    From a Dataframe with all users, microscopes and so on,
    generate a new one with unique users, microscope, actual costs
    (calculated from cost-hours and microscope-specific costs) and
    costcodes

    Parameters
    ----------
    frame : pd.Dataframe
        General dataframe with all information regarding users, microscopes and cost-hours
    
    Returns
    -------
    newframe: pd.Dataframe
        New Dataframe with unique users, costs and costcodes

    
    """
    import pandas as pd
    frame = frame.add_suffix('_summary').reset_index()
    
    users = frame['user'].unique().tolist()
    newframe = pd.DataFrame(users, columns=['user'])
    for micro in ['DV1', 'DV2', 'UltraVIEW']:
        micro_frame = frame[frame['micro'].str.contains(micro,case=False)]
        for index, row in newframe.iterrows():
            
            if (micro_frame['user']==row.user).any():
                newframe.loc[index,micro+'_hours'] = float(micro_frame[micro_frame['user']==row['user']]['cost_hours_summary'].sum())
            if (micro_frame[micro_frame['user']==row.user]['costcode_summary']).any():
                
                newframe.loc[index,'costcode'] = micro_frame[micro_frame['user']==row['user']]['costcode_summary'].iloc[0]
    newframe.fillna(0,inplace=True)
    newframe = add_access(newframe) 
    
    costs = load_costs()
    
    newframe = calculate_costs(newframe,costs)
    newframe = cleanup(newframe)

    return newframe



def add_access(frame):
    """
    Adds access level for a given user at a given microscope to Dataframe.

    Parameters
    ----------
    frame : pd.Dataframe
        General dataframe with all information regarding users, microscopes and cost-hours
    
    Returns
    -------
    frame : pd.Dataframe
        General dataframe with all information regarding users, microscopes and cost-hours - plus access levels

    
    """
    import pandas as pd
    access = pd.read_csv("legacy/emails_gmails_costcodes.csv")

    for micro in ['DV1', 'DV2', 'UltraVIEW']:
        
        for index, row in frame.iterrows():
            if (access['Gmail']==row.user.split(" ")[1]).any():
                frame.loc[index,micro+'_access'] = int(access[access['Gmail']==row.user.split(" ")[1]][micro])


    return frame


def load_costs():
    """
    Creates a Dataframe with CSV data for per-microscope costs.

    
    """
    import pandas as pd
    costs = pd.read_csv("legacy/costs.csv")
    return costs


def calculate_costs(frame,costs):
    """
    Calculates effective costs based on per-microscope hourly costs and number
    of cost-hours.

    Parameters
    ----------
    frame : pd.Dataframe
        General dataframe with all information regarding users, microscopes and cost-hours
    costs : pd.Dataframe
        Dataframe with per-microscope hourly costs
    
    Returns
    -------
    frame : pd.Dataframe
        General dataframe with all information regarding users, microscopes, cost-hours and actual costs

    
    """
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
    """
    Does a bit of tidying up on our main Dataframe - splitting user and email,
    removing empty lines and so on

    Parameters
    ----------
    frame : pd.Dataframe
        General dataframe with all information regarding users, microscopes, cost-hours and actual costs
    
    Returns
    -------
   frame : pd.Dataframe
        General dataframe with all information regarding users, microscopes, cost-hours and actual costs

    
    """
    for index, row in frame.iterrows():
        frame.loc[index,'username'] = row['user'].split(" ")[0]
        frame.loc[index,'email'] = row['user'].split(" ")[1]
        micros = ['DV1', 'DV2', 'UltraVIEW']
        empty = 1
        for micro in micros:
            if (row[micro+"_hours"]>0):
                empty = 0
        if empty:
            frame.drop(index,inplace=True)
    frame.drop("user", axis=1, inplace=True)
    cols = list(frame.columns.values)
    newcols = [cols[-2],cols[-1]]
    newcols.extend(cols[:1])
    newcols.extend(cols[2:-2])
    newcols.extend(cols[1:2])
    frame = frame[newcols]
    return frame