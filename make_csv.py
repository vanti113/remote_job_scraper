import csv


def save_to_csv(name, data):
    file = open(f"{name}.csv", mode="w")
    write = csv.writer(file)
    write.writerow(["Title", "Company", "Link"])
    for list in data:
        write.writerow([f"{list[0]}", f"{list[1]}", f"{list[2]}"])
