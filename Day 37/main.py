import requests
from datetime import datetime

USERNAME = "zelkova"
TOKEN = "qwerty123"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# bikin akun pixela make request.post
# response = requests.post(url = pixela_endpoint, json = user_params)
# print(response.text)




graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# https://pixe.la/v1/users/zelkova/graphs/graph1

graph_config = {
    "id" : "graph1", # id graph yang akan dibuat
    "name" : "Jogging graph",# nama graph yang akan dibuat
    "unit" : "Km",
    "type" : "float",
    "color" : "momiji"

}

headers = {
    # ini adalah cara lebih aman dari pada api key
    "X-USER-TOKEN" : TOKEN
}
# # Bagian pada saat akan membuat graph
# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
# print(response.text)



# melakukan post pixel ke graph
pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()

pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    #"date" : "20250708",
    "quantity" : "9.99",
    
}

# response_pixel = requests.post(url = pixel_post_endpoint, json = pixel_config, headers=headers)
# print(response_pixel.text)




### Mengupdate (PUT) data kemarin yang sudah ada
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/20250709" 

updated_pixel = {
    "quantity" : "12.34"
}

# response_pixel_update = requests.put(url = update_pixel_endpoint, json = updated_pixel, headers=headers)
# print(response_pixel_update.text)


### menghapus (delettet) data pixel salah satu tanggal
delete_pixel_endpoint =  f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/20250708"


response_del_pixel = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response_del_pixel.text)