def climbingLeaderboard(ranked, player):
    ranked = sorted(list(set(ranked)), reverse=True)
    player = sorted(player, reverse=True)
    
    l = len(ranked)
    j = 0

    res = []
    
    for n in range(len(player)):
        while j < l and player[n]<ranked[j]:
            j += 1
        res.append(j + 1)
    
    res = sorted(res, reverse=True)
    return res