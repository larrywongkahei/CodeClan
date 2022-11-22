def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    if len(scores) <= 2:
        return sorted(scores)
    return sorted(scores)[-3::]

def personal_highest_to_lowest(scores):
    return sorted(scores)[::-1]
