import json

# --- Unification Functions ---
def unify_model_a(model_a):
    unified = []
    for record in model_a:
        unified.append({
            "employee_id": int(record["emp_id"]),
            "name": record["full_name"],
            "email": record["email"],
            "department": record["department"]
        })
    return unified

def unify_model_b(model_b):
    unified = []
    for record in model_b:
        name = f"{record['name']['first']} {record['name']['last']}"
        department = "Technology" if record["dept"].lower().startswith("tech") else record["dept"]
        unified.append({
            "employee_id": int(record["id"]),
            "name": name,
            "email": record["contact"]["email_address"],
            "department": department
        })
    return unified

def unify_all(model_a, model_b):
    unified_a = unify_model_a(model_a)
    unified_b = unify_model_b(model_b)
    return unified_a + unified_b

# --- Load data from JSON files ---
with open("data/model_a.json", "r") as f:
    model_a = json.load(f)

with open("data/model_b.json", "r") as f:
    model_b = json.load(f)

# --- Unify and Save Result ---
unified_result = unify_all(model_a, model_b)

with open("unified_employees.json", "w") as f:
    json.dump(unified_result, f, indent=2)

print("✅ Unified data saved to 'unified_employees.json'")




# def unify_model_a(model_a):
#     unified = []
#     for record in model_a:
#         unified.append({
#             "employee_id": int(record["emp_id"]),
#             "name": record["full_name"],
#             "email": record["email"],
#             "department": record["department"]
#         })
#     return unified

# def unify_model_b(model_b):
#     unified = []
#     for record in model_b:
#         name = f"{record['name']['first']} {record['name']['last']}"
#         department = "Technology" if record["dept"].lower().startswith("tech") else record["dept"]
#         unified.append({
#             "employee_id": int(record["id"]),
#             "name": name,
#             "email": record["contact"]["email_address"],
#             "department": department
#         })
#     return unified

# def unify_all(model_a, model_b):
#     unified_a = unify_model_a(model_a)
#     unified_b = unify_model_b(model_b)
#     return unified_a + unified_b

# # Sample Data
# model_a = [
#     {
#         "emp_id": 101,
#         "full_name": "Aryan Raj",
#         "email": "aryan.raj@example.com",
#         "department": "Technology"
#     }
# ]

# model_b = [
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
#     }
# ]

# # Unify data
# unified_result = unify_all(model_a, model_b)

# # Display result
# import json
# print(json.dumps(unified_result, indent=2))
