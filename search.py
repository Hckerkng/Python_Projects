import requests 
import matplotlib.pyplot as plt
def get_img(url,filename="myimg"):
    page  = requests.get(url)
    if page.status_code == 200 : 
        tp = page.headers['Content-type']
        if tp.startswith('image'):
            ext = tp.split('/')[1].split(';')[0].strip()
            filename += "."+ext
            with open(filename,'wb') as fp: # context managers
                fp.write(page.content)
                fp.close()
            img = plt.imread(filename)
            plt.imshow(img)
            plt.xticks([])
            plt.yticks([])
            plt.show()
            
            return filename
        else: 
            print("NO image found in Data")
            return False
    elif page.status_code == 403 : 
        print("Limit Exceed")
    else : 
        print("Invalid URL or Data Not Avaiable")
        return False 


def search(query,api_key):
    """
    search will search for query place and return revelent information
    """
    url =  "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?\
input={}&inputtype=textquery&fields=photos,formatted_address,name,rating,\
opening_hours,geometry&key={}".format(query,api_key)
    page = requests.get(url)
    if page.status_code == 200 : 
        data = page.json()
        address = data.get('candidates')
        for addr in address : 
            if "formatted_address" in addr : 
                full_name = addr["formatted_address"]
                print("Full Name : ",full_name)
            if "name" in addr : 
                name = addr["name"]
                print("Comman Name : ",name)
            if "photos" in addr : 
                for photo in addr['photos'] :
                    if "photo_reference" in photo : 
                        ph_ref  = photo['photo_reference']
                        photo_url  = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={}&key={}".format(ph_ref,api_key)
                        get_img(photo_url)
                    else : 
                        print("No Photo Found")
            else : 
                print("No photo Available for this place")
             
    else : 
        print(f"Invalid Response From Server with Status Code {page.status_code}")
        
api_key = "AIzaSyBMaiKI0e1UYQFafXGyVEZZENlkkE1rbHw"
while input("Press any key to search a place : ") : 
    query = input("Enter palace name : ")
    search(query,api_key)
