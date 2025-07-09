import json
import datetime

# Choose either data-1.json or data-2.json
with open("./data-1.json", "r", encoding="utf-8") as f:
    inputData = json.load(f)


def convertFromFormat1(jsonObject):
    location_parts = jsonObject["location"].split("/")

    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],
        "location": {
            "country": location_parts[0],
            "city": location_parts[1],
            "area": location_parts[2],
            "factory": location_parts[3],
            "section": location_parts[4]
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"]
        }
    }


def convertFromFormat2(jsonObject):
    dt = datetime.datetime.fromisoformat(jsonObject["timestamp"].replace("Z", "+00:00"))
    timestamp_ms = int(dt.timestamp() * 1000)

    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": timestamp_ms,
        "location": {
            "country": jsonObject["country"],
            "city": jsonObject["city"],
            "area": jsonObject["area"],
            "factory": jsonObject["factory"],
            "section": jsonObject["section"]
        },
        "data": {
            "status": jsonObject["data"]["status"],
            "temperature": jsonObject["data"]["temperature"]
        }
    }


def unify(jsonObject):
    if jsonObject.get("device") is None:
        return convertFromFormat1(jsonObject)
    else:
        return convertFromFormat2(jsonObject)


def main():
    unified = unify(inputData)

    # Save to data-result.json
    with open("data-result.json", "w", encoding="utf-8") as f:
        json.dump(unified, f, ensure_ascii=False, indent=4)

    # Print to terminal
    print(json.dumps(unified, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    main()


# import json
# import datetime


# # Load both input files
# with open("./data-1.json", "r", encoding="utf-8") as f:
#     jsonData1 = json.load(f)

# with open("./data-2.json", "r", encoding="utf-8") as f:
#     jsonData2 = json.load(f)


# def convertFromFormat1(jsonObject):
#     location_parts = jsonObject["location"].split("/")

#     return {
#         "deviceID": jsonObject["deviceID"],
#         "deviceType": jsonObject["deviceType"],
#         "timestamp": jsonObject["timestamp"],
#         "location": {
#             "country": location_parts[0],
#             "city": location_parts[1],
#             "area": location_parts[2],
#             "factory": location_parts[3],
#             "section": location_parts[4]
#         },
#         "data": {
#             "status": jsonObject["operationStatus"],
#             "temperature": jsonObject["temp"]
#         }
#     }


# def convertFromFormat2(jsonObject):
#     dt = datetime.datetime.fromisoformat(jsonObject["timestamp"].replace("Z", "+00:00"))
#     timestamp_ms = int(dt.timestamp() * 1000)

#     return {
#         "deviceID": jsonObject["device"]["id"],
#         "deviceType": jsonObject["device"]["type"],
#         "timestamp": timestamp_ms,
#         "location": {
#             "country": jsonObject["country"],
#             "city": jsonObject["city"],
#             "area": jsonObject["area"],
#             "factory": jsonObject["factory"],
#             "section": jsonObject["section"]
#         },
#         "data": {
#             "status": jsonObject["data"]["status"],
#             "temperature": jsonObject["data"]["temperature"]
#         }
#     }


# def main():
#     unified_data = []

#     # Unify both entries
#     unified_data.append(convertFromFormat1(jsonData1))
#     unified_data.append(convertFromFormat2(jsonData2))

#     # Save to data-result.json
#     with open("data-result.json", "w", encoding="utf-8") as f:
#         json.dump(unified_data, f, ensure_ascii=False, indent=4)

#     # Print to terminal
#     print(json.dumps(unified_data, indent=4, ensure_ascii=False))


# if __name__ == '__main__':
#     main()
