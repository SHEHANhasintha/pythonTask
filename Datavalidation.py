"""
    Data Validation

"""

def validateUsers(userJsonDict,cb):
    finalDataTup = [];
    if ("users" in userJsonDict):
        users = userJsonDict["users"];
        for data in users:
            try:
                # check index number
                if ("indexNumber" in data): 
                    finalDataTup.insert(0,data["indexNumber"]);
                else:
                    print("indexNumber required")
                    continue;

                # check firstName
                if ("firstName" in data["name"]): 
                    finalDataTup.insert(1,data["name"]["firstName"]);
                else:
                    print("firstName required")
                    continue;

                # check last name
                if ("lastName" in data["name"]): 
                    finalDataTup.insert(2,data["name"]["lastName"]);
                else:
                    print("lastName required")
                    continue;

                # check location
                if ("location" in data): 
                    finalDataTup.insert(3,data["location"]);

                # check age
                if ("age" in data): 
                    finalDataTup.insert(4,data["age"]);

                # convert into a tuple for passed as arguments to function
                finalDataTup = tuple(finalDataTup);

                # passing arguments
                cb(*finalDataTup)
                finalDataTup = [];
            except Exception as err:
                print(err)
                
                