data = []
with open("weather_data.csv", "r") as file:
    data = file.readlines().split(",")
    file.close()

print(data)
