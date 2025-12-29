import requests
url = "https://api.agify.io"


def get_age_prediction(name):
    reponse = requests.get(url, params= {"name" : name})
    if reponse.status_code == 200:
       data = reponse.json()  
       return data
    else:
        raise SystemExit("Erreur lors de l'appel a l'API = Erreur {reponse.status_code}")
    
def display_result(data):
    print("--- RESULT ---")
    print(f"Name : {data["name"]}")
    print(f"Prediction age : {data["age"]}")
    print(f"sample size : {data["count"]}")

if __name__ == "__main__":
   name = input("Enter a name :")
   result = get_age_prediction(name)
   display_result(result)
    
