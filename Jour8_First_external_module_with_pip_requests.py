import requests 

url = "https://api.chucknorris.io/jokes/random"

def get_random_joke():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  
        joke = data['value']  
        print(data)  
        return joke 
        
    else:
        raise SystemExit("Erreur lors de l'appel a l'API")


def display_joke(joke):
    print("--Joke--")
    print(joke)

if __name__ == "__main__":
    joke = get_random_joke()
    display_joke(joke)
    