import streamlit as st
import pandas as pd
import plotly.express as px
import smtplib
from email.message import EmailMessage

data = pd.read_csv("/Users/anoutsala/Documents/datathon_2024/records.csv")

st.title("Conflict Zones and Safe Areas")

fig = px.scatter_mapbox(
    data,
    lat="latitude",
    lon="longitude",
    color="fatalities_binned", 
    hover_name="location",
    zoom=3,
    height=500,
    mapbox_style="carto-positron",
)
st.plotly_chart(fig)

# User Preferences
st.subheader("Set Your Preferences")
region = st.selectbox("Select Region of Interest", data["region"].unique())
email = st.text_input("Enter Your Email for Alerts")

if st.button("Subscribe"):
    st.success(f"Subscribed to alerts for {region}. Notifications will be sent to {email}.")

def send_email(to_email, region):
    msg = EmailMessage()
    msg["Subject"] = f"Conflict Alert: {region}"
    msg["From"] = "your-email@example.com"
    msg["To"] = to_email
    msg.set_content(f"Conflict detected in {region}. Stay safe!")

    with smtplib.SMTP("smtp.sendgrid.net", 587) as server:
        server.login("apikey", "your-sendgrid-api-key")
        server.send_message(msg)

if st.button("Subscribe"):
    send_email(email, region)
    st.success(f"Subscribed to alerts for {region}. Notifications will be sent to {email}.")
