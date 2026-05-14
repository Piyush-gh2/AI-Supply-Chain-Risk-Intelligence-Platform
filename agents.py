from src.loader import load_data
from src.forecasting import predict_demand
from src.risk_engine import detect_risk
from src.explainable_ai import explain_prediction

def run_supply_chain_ai():

    df = load_data()

    prediction = predict_demand(df)

    latest_inventory = df["inventory"].iloc[-1]
    latest_delay = df["supplier_delay"].iloc[-1]

    risk = detect_risk(latest_inventory, latest_delay)

    explanation = explain_prediction(prediction)

    return df, prediction, risk, explanation