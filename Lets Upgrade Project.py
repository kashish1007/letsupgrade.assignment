def celcius_to_frainite(inp):
    fran = inp * 9/5 + 32
    return fran

if __name__ == "__main__":
    inp = float(input(f"°C -> "))
    result = celcius_to_frainite(inp)
    print(f"°F ->{result}")
