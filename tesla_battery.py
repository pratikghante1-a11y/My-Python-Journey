def check_tesla_battery(percentage):
    if percentage <= 20:
        return " Battery Low! I M Finding The Charging Station to charge The vehicle..."
    elif percentage == 100:
        return " Battery Full! Your Journey will be Continue."
    else:
        return " The Car is moving . Battery level: " + str(percentage) + "%"
status = check_tesla_battery(15) 
print(status)
