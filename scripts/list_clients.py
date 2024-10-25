import os
import requests


def run():
   # Load the token from an environment variable
   TOKEN = os.getenv("SWISSQUOTE_API_TOKEN")

   # Define the API endpoint for retrieving managed clients
   url = "https://bankingapi.swissquote.ch/am-interface-v2/api/v1/clients"

   # Set up headers with authorization
   headers = {
       "Authorization": f"Bearer {TOKEN}"
   }

   # Make the request to get the clients list
   response = requests.get(url, headers=headers)

   # Check if the request was successful
   if response.status_code == 200:
      clients_list = response.json()
      print("Clients List:", clients_list)
   else:
      print(f"Failed to retrieve clients list: {response.status_code}")
      print("Error message:", response.json())


if __name__ == "__main__":
   run()

