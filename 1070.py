def function(x:int):
    for _ in range(1,7):
        if x%2 == 0: x+=1
        print(x)
        if x%2 != 0: x+=2

if __name__ == "__main__":
    function(int(input()))