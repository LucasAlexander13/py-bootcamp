data = []
with open("weather_data.csv", "r") as file:
    data = file.readlines()
    file.close()

print(data)
