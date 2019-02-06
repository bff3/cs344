from math import sin, fabs

def LinearGrowthSin(x):
    return fabs(x*sin(x))

if __name__ == '__main__':
    for x in range(0,1000):
        x /= 100
        f = open("myfile.csv", "a")
        f.write(str(x)+","+str(LinearGrowthSin(x))+"\n")
