x ,y, z = input("Expreesion: ").split(" ")
x = float(x)
z = float(z)
match y:
    case '+':
        x = x + z
    case '-':
        x = x - z
    case '*':
        x = x * z
    case '/':
        x = x / z
print(f"{x:.1f}")