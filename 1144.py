def function(x:int):
    for i in range(1,x+1):
        print(f"{i} {i*i} {i*(i*i)}\n{i} {i*i+1} {i*(i*i)+1}")

if __name__ == "__main__":
    function(int(input()))
    # function(5)