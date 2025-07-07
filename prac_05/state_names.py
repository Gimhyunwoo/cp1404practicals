"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
key_to_value = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}
print(key_to_value)

for code, name in key_to_value.items():
    print(f"{code:3} is {name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f'{state_code} is {key_to_value[state_code]}')
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()