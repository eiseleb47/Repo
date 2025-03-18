import requests
from PIL import Image
import io
from matplotlib import pyplot as plt

print("I love Vienna")
print("I mean just look at it:")

url = "https://upload.wikimedia.org/wikipedia/commons/9/9f/Vienna_Austria_Skyline_Aerial%2C_October_2024.jpg"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

img = Image.open(io.BytesIO(response.content))
plt.figure(figsize=(20, 10))
plt.imshow(img)
plt.axis('off')
plt.show()

