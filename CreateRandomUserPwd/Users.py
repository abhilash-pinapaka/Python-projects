import requests
import json

url = "https://randomuser.me/api/"

def get_user():
    """
    :return: dictionary of user full name and email
    """
    #header={'Accept-content':'application/json','content-type':'application/json'}
    response = requests.get(url)
    resp_dict = response.json()
    user = {'fullname':resp_dict['results'][0]['name']['first']+' '+resp_dict['results'][0]['name']['last'],
                   'email':resp_dict['results'][0]['email'] }
    return user

if __name__ == '__main__':
    print(get_user())


