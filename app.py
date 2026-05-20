import gradio as gr
import joblib
import numpy as np

# Load trained Random Forest model
model = joblib.load("random_forest_model.pkl")


def predict_fraud(
    step,
    amount,
    oldbalanceOrg,
    newbalanceOrig,
    oldbalanceDest,
    newbalanceDest,
    type_TRANSFER
):

    # Feature Engineering

    # Derive hour from step
    hour = step % 24

    is_night = 1 if hour < 6 else 0

    amount_ratio = amount / (oldbalanceOrg + 1)

    sender_balance_change = oldbalanceOrg - newbalanceOrig

    receiver_balance_change = newbalanceDest - oldbalanceDest

    sender_balance_zero = 1 if newbalanceOrig == 0 else 0

    receiver_balance_zero = 1 if newbalanceDest == 0 else 0

    # Arrange features in exact training order
    features = np.array([[
        step,
        amount,
        oldbalanceOrg,
        newbalanceOrig,
        oldbalanceDest,
        newbalanceDest,
        hour,
        is_night,
        amount_ratio,
        sender_balance_change,
        receiver_balance_change,
        sender_balance_zero,
        receiver_balance_zero,
        type_TRANSFER
    ]])

    # Prediction
    result = model.predict(features)[0]

    if result == 1:
        return "🚨 Fraud Transaction"

    return "✅ Normal Transaction"


# Gradio UI
interface = gr.Interface(

    fn=predict_fraud,

    inputs=[

        gr.Number(label="Step"),

        gr.Number(label="Amount"),

        gr.Number(label="Old Balance Sender"),

        gr.Number(label="New Balance Sender"),

        gr.Number(label="Old Balance Receiver"),

        gr.Number(label="New Balance Receiver"),

        gr.Radio(
            choices=[0, 1],
            label="Transaction Type (0 = Payment, 1 = Transfer)"
        )

    ],

    outputs=gr.Textbox(label="Prediction"),

    title="Online Fraud Detection System",

    description="Enter transaction details to detect fraud."

)

interface.launch()