def consolidate_hours(parsed):
    import pandas as pd
    frame = pd.DataFrame(parsed,columns=['micro', 'user', 'start', 'end', 'hours', 'cost_hours'])
    sum_frame = frame.groupby(['micro', 'user']).agg({'hours': 'sum', 'cost_hours':'sum'})
    return sum_frame