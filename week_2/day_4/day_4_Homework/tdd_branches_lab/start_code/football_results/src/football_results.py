def get_result(final_score):
    home_score = final_score["home_score"]
    away_score = final_score["away_score"]
    if home_score > away_score:
        return "Home win"
    elif home_score < away_score:
        return "Away win"
    return "Draw"

def get_results(final_scores):
    return [get_result(final_score) for final_score in final_scores]
    # (You could try and use a list comprehension for this)