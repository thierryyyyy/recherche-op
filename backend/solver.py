import numpy as np

def solve_balas_hammer(costs, supply, demand):
    costs = np.array(costs, dtype=float)
    s = np.array(supply, dtype=float)
    d = np.array(demand, dtype=float)
    m, n = costs.shape
    x = np.zeros((m, n))
    
    row_active = np.ones(m, dtype=bool)
    col_active = np.ones(n, dtype=bool)
    steps = []

    while row_active.any() and col_active.any():
        row_diffs = np.full(m, -1.0)
        col_diffs = np.full(n, -1.0)

        for i in range(m):
            if row_active[i]:
                active_costs = sorted(costs[i, col_active])
                row_diffs[i] = active_costs[1] - active_costs[0] if len(active_costs) > 1 else active_costs[0]

        for j in range(n):
            if col_active[j]:
                active_costs = sorted(costs[row_active, j])
                col_diffs[j] = active_costs[1] - active_costs[0] if len(active_costs) > 1 else active_costs[0]

        if np.max(row_diffs) >= np.max(col_diffs):
            i = np.where(row_diffs == np.max(row_diffs))[0][0]
            j_candidates = np.where(col_active)[0]
            j = j_candidates[np.argmin(costs[i, j_candidates])]
        else:
            j = np.where(col_diffs == np.max(col_diffs))[0][0]
            i_candidates = np.where(row_active)[0]
            i = i_candidates[np.argmin(costs[i_candidates, j])]

        val = min(s[i], d[j])
        x[i, j] = val
        s[i] -= val
        d[j] -= val

        if s[i] == 0: row_active[i] = False
        if d[j] == 0: col_active[j] = False
        
        steps.append({"origin": int(i), "dest": int(j), "qty": float(val)})

    return x.tolist(), float(np.sum(x * costs)), steps

def solve_minico(costs, supply, demand):
    costs = np.array(costs, dtype=float)
    s = np.array(supply, dtype=float)
    d = np.array(demand, dtype=float)
    m, n = costs.shape
    x = np.zeros((m, n))
    row_done = np.zeros(m, dtype=bool)
    steps = []

    for j in range(n):
        while d[j] > 0:
            available_rows = np.where(~row_done)[0]
            if len(available_rows) == 0: break
            
            i = available_rows[np.argmin(costs[available_rows, j])]
            val = min(s[i], d[j])
            x[i, j] = val
            s[i] -= val
            d[j] -= val
            
            if s[i] == 0: row_done[i] = True
            steps.append({"origin": int(i), "dest": int(j), "qty": float(val)})

    return x.tolist(), float(np.sum(x * costs)), steps
