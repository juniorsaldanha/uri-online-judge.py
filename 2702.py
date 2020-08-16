def function(x,y):
    total = int()
    for nx, ny in zip(x, y):
        if ny > nx: total += ny-nx
    print(total)
if __name__ == "__main__":
    var1, var2, var3 = input().split()
    var11, var22, var33 = input().split()
    function([int(var1),int(var2),int(var3)],[int(var11),int(var22),int(var33)])
    