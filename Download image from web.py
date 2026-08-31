import requests

url = "https://image.shutterstock.com/shutterstock/photos/76166707/display_1500/stock-photo-one-tree-and-perfect-grass-field-76166707.jpg"  # Example Wikipedia image URL mentioned by the instructor

# Make a request and get a response object
response = requests.get(url)

# Open a new file in write-binary mode ('wb') and write the image content
with open("image.jpg", "wb") as file:
    file.write(response.content)