data = []
with open("weather_data.csv", "r") as file:
    for line in file:
        data.append(line.split(","))
    file.close()

print(data)
