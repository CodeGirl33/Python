
import numpy as np
def using_searchsorted():
    start_idx = np.searchsorted(intervals['start_time'].values, data['time'].values)-1
    end_idx = np.searchsorted(intervals['end_time'].values, data['time'].values)
    mask = (start_idx == end_idx)
    result = data.copy()
    result['interval_id'] = result['start_time'] = result['end_time'] = np.nan
    result['interval_id'][mask] = start_idx
    result.loc[mask, 'start_time'] = intervals['start_time'][start_idx[mask]].values
    result.loc[mask, 'end_time'] = intervals['end_time'][end_idx[mask]].values
    return result

