"""
Hex Colour Lookup
Estimate: 20 minutes
Actual: 22 minutes
"""

HEX_COLOURS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite1": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "blue": "#0000ff"
}


def main():
    """Get color names from the user and display their hex codes."""
    colour_name = input("Enter colour name (blank to quit): ").lower()

    while colour_name != "":
        colour_code = HEX_COLOURS.get(colour_name)
        if colour_code:
            print(f"The hex code for {colour_name} is {colour_code}")
        else:
            print("Invalid colour name")

        colour_name = input("Enter colour name (blank to quit): ").lower()


main()