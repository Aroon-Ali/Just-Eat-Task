import requests

base_url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode"

#Get data function
def get_postcode_info(name):
    url = f"{base_url}/{name}"
    response = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"})

    if response.status_code == 200:
        restaurant_data = response.json() #convert to python dictionary
        return restaurant_data #return as dictionary
    else:
        print(f"Error: Failed to retrieve data {response.status_code}") #Allows for lookup
        return None
    
#Include strip, upper and replace in case of whitespace, lowercase and trailing spaces    
postcode = input("Enter postcode: ").strip().upper().replace(" ", "")

print("\n")#print extra line for readability

#Use function to get restaurant info
restaurant_info = get_postcode_info(postcode)


if restaurant_info['restaurants'] == []:
    postcode = input("INVALID - enter a valid postcode: ").strip().upper().replace(" ", "")
    restaurant_info = get_postcode_info(postcode)


store_list = restaurant_info['restaurants']

#Filter for restaurants 
list_restaurants = [
    restaurant for restaurant in store_list
    if "Groceries" not in [cuisine["name"] for cuisine in restaurant["cuisines"]]
]

cuisine_exclusions = ["Deals", "Collect stamps", "Freebies"] #These are NOT cuisines

#We only want the first 10 as per brief. Using print statements as a simple solution.
for i in range(0, 10):
    rest_pick = list_restaurants[i]

    print(f"Restaurant {i+1}")

    #Name
    restaurant_name = rest_pick["name"]
    print(f"Name: {restaurant_name}")

    #Cuisines
    cuisine_list = [cuisine["name"] for cuisine in rest_pick["cuisines"] 
                    if cuisine["name"] not in cuisine_exclusions]
    print("Cuisines: ", ", ".join(cuisine_list) )


    #Rating
    print("Rating: ", rest_pick["rating"]["starRating"])


    #Address
    address = rest_pick["address"]
    print("Address:", f"{address['firstLine']}, {address['city']}, {address['postalCode']}\n")
