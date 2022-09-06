def run():

    acum = 0

    for i in range(1000, 10000):
        if str(i).count(str(0)) == 2:
            print(i)
            acum += 1
    
    print(f"Hay {acum} numeros de cuatro cifras con dos ceros")

if __name__ == "__main__":
    run()