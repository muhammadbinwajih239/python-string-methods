license_plate = input("Enter your License Plate: ")

license_plate = license_plate.strip().upper()

if (
    len(license_plate) == 8
    and license_plate[:3].isalpha()
    and license_plate[3] == "-"
    and license_plate[4:].isdigit()
):
    print(f"Valid License Plate: {license_plate}")
else:
    print("Invalid License Plate.")
