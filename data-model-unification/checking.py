import streamlit as st
import json
import os
from datetime import datetime

# --- Streamlit Setup ---
st.set_page_config(page_title="Unified Device Data", layout="wide")
st.title("🛠️ Unified Device Telemetry")

# --- Sample Data (embedded) ---

# data-1.json format
data_1 = {
    "deviceID": "dh28dslkja",
    "deviceType": "LaserCutter",
    "timestamp": 1624445837783,
    "location": "japan/tokyo/keiyō-industrial-zone/daikibo-factory-meiyo/section-1",
    "operationStatus": "healthy",
    "temp": 22
}

# data-2.json format
data_2 = {
    "device": {
        "id": "dh28dslkja",
        "type": "LaserCutter"
    },
    "timestamp": "2021-06-23T10:57:17.783Z",
    "country": "japan",
    "city": "tokyo",
    "area": "keiyō-industrial-zone",
    "factory": "daikibo-factory-meiyo",
    "section": "section-1",
    "data": {
        "status": "healthy",
        "temperature": 22
    }
}

# --- Unification Functions ---

def unify_data_1(d):
    parts = d["location"].split("/")
    return {
        "deviceID": d["deviceID"],
        "deviceType": d["deviceType"],
        "timestamp": d["timestamp"],
        "location": {
            "country": parts[0],
            "city": parts[1],
            "area": parts[2],
            "factory": parts[3],
            "section": parts[4]
        },
        "data": {
            "status": d["operationStatus"],
            "temperature": d["temp"]
        }
    }

def unify_data_2(d):
    # Convert ISO timestamp to UNIX epoch (ms)
    ts = int(datetime.fromisoformat(d["timestamp"].replace("Z", "+00:00")).timestamp() * 1000)
    return {
        "deviceID": d["device"]["id"],
        "deviceType": d["device"]["type"],
        "timestamp": ts,
        "location": {
            "country": d["country"],
            "city": d["city"],
            "area": d["area"],
            "factory": d["factory"],
            "section": d["section"]
        },
        "data": {
            "status": d["data"]["status"],
            "temperature": d["data"]["temperature"]
        }
    }

# --- Combine & Unify ---
unified_result = unify_data_1(data_1)  # or unify_data_2(data_2)

# --- Save to file ---
os.makedirs("data", exist_ok=True)
with open("data/result.json", "w") as f:
    json.dump(unified_result, f, indent=2)

# --- Display in Streamlit ---
st.subheader("📦 Unified Device Data (JSON View)")
st.json(unified_result)

# --- Success Message ---
st.success("✅ Unified device data saved to 'data/result.json'")






# ===========================
# import json
# import streamlit as st
# import pandas as pd
# import os

# # --- Streamlit Config ---
# st.set_page_config(page_title="Unified Employee Data", layout="wide")
# st.title("📋 Unified Employee Data Viewer")

# # --- Sample Data (embedded instead of reading from files) ---
# # Simulated data-1.json (System A)
# data_1 = [
#     {
#         "emp_id": 101,
#         "full_name": "Aryan Raj",
#         "email": "aryan.raj@example.com",
#         "department": "Technology"
#     },
#     {
#         "emp_id": 102,
#         "full_name": "Anjali Mehra",
#         "email": "anjali.mehra@example.com",
#         "department": "Marketing"
#     }
# ]

# # Simulated data-2.json (System B)
# # Same records as data_1, but in a different schema
# data_2 = [
#     {
#         "id": "101",
#         "name": {
#             "first": "Aryan",
#             "last": "Raj"
#         },
#         "contact": {
#             "email_address": "aryan.raj@example.com"
#         },
#         "dept": "Tech"
#     },
#     {
#         "id": "102",
#         "name": {
#             "first": "Anjali",
#             "last": "Mehra"
#         },
#         "contact": {
#             "email_address": "anjali.mehra@example.com"
#         },
#         "dept": "Marketing"
#     }
# ]

# # --- Unification Functions ---
# def unify_data_1(data):
#     unified = []
#     for record in data:
#         unified.append({
#             "employee_id": int(record["emp_id"]),
#             "name": record["full_name"],
#             "email": record["email"],
#             "department": record["department"]
#         })
#     return unified

# def unify_data_2(data):
#     unified = []
#     for record in data:
#         name = f"{record['name']['first']} {record['name']['last']}"
#         department = "Technology" if record["dept"].lower().startswith("tech") else record["dept"]
#         unified.append({
#             "employee_id": int(record["id"]),
#             "name": name,
#             "email": record["contact"]["email_address"],
#             "department": department
#         })
#     return unified

# def unify_all(data_1, data_2):
#     return unify_data_1(data_1) + unify_data_2(data_2)

# # --- Process and Combine Data ---
# unified_result = unify_all(data_1, data_2)

# # --- Save unified result to file ---
# os.makedirs("data", exist_ok=True)
# with open("data/result.json", "w") as f:
#     json.dump(unified_result, f, indent=2)

# # --- Display as table ---
# df = pd.DataFrame(unified_result)
# st.subheader("🧾 Unified Employee Table")
# st.dataframe(df, use_container_width=True)

# # --- Success Message ---
# st.success("✅ Unified data saved to 'data/result.json'")
