import json, unittest, datetime

# Load all three input files
with open("./data-1.json", "r", encoding="utf-8") as f:
    jsonData1 = json.load(f)

with open("./data-2.json", "r", encoding="utf-8") as f:
    jsonData2 = json.load(f)

with open("./data-result.json", "r", encoding="utf-8") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1(jsonObject):
    # Split the location string
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
    # Convert ISO timestamp to UNIX timestamp in milliseconds
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


def main(jsonObject):
    result = {}

    if jsonObject.get("device") is None:
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):
        # This test just verifies jsonExpectedResult is well-formed
        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):
        result = main(jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):
        result = main(jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )


if __name__ == '__main__':
    unittest.main()








# import json, unittest, datetime

# # Load all three input files
# with open("./data-1.json", "r", encoding="utf-8") as f:
#     jsonData1 = json.load(f)

# with open("./data-2.json", "r", encoding="utf-8") as f:
#     jsonData2 = json.load(f)

# with open("./data-result.json", "r", encoding="utf-8") as f:
#     jsonExpectedResult = json.load(f)


# def convertFromFormat1(jsonObject):
#     # Split the location string
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
#     # Convert ISO timestamp to UNIX timestamp in milliseconds
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


# def main(jsonObject):
#     if jsonObject.get("device") is None:
#         return convertFromFormat1(jsonObject)
#     else:
#         return convertFromFormat2(jsonObject)


# class TestSolution(unittest.TestCase):

#     def test_sanity(self):
#         # This test just verifies jsonExpectedResult is well-formed
#         result = json.loads(json.dumps(jsonExpectedResult))
#         self.assertEqual(result, jsonExpectedResult)

#     def test_dataType1(self):
#         result = main(jsonData1)
#         self.assertEqual(
#             result,
#             jsonExpectedResult,
#             'Converting from Type 1 failed'
#         )

#     def test_dataType2(self):
#         result = main(jsonData2)
#         self.assertEqual(
#             result,
#             jsonExpectedResult,
#             'Converting from Type 2 failed'
#         )


# if __name__ == '__main__':
#     unittest.main()
