def explain_prediction(prediction):

    if prediction > 350:
        return "High demand spike predicted due to trend growth."

    elif prediction > 250:
        return "Moderate demand increase expected."

    else:
        return "Demand forecast remains stable."