import socket
from math import sqrt
from ast import literal_eval


def distance(a,b,x,y):
    return sqrt((x-a)**2+(y-b)**2)

def euclideanDistance(coordinate1, coordinate2):
    return pow(pow(coordinate1[0] - coordinate2[0], 2) + pow(coordinate1[1] - coordinate2[1], 2), .5)

if __name__ == '__main__':
    host = ''        # Symbolic name meaning all available interfaces
    port = 10256     # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    print host , port
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:

        try:
            data = conn.recv(6000)
            if data != "Error: Error is happening":

                #List of 100 randomly generated points
                coordList = list(literal_eval(data))

                distances = []
                coordDistList = {}
                for i in range(len(coordList)-1):
                    for j in range(i+1, len(coordList)):
                        calcDist = euclideanDistance(coordList[i],coordList[j])
                        distances += [calcDist]
                        coordDistList[calcDist] = (coordList[i],coordList[j])

                print "***************************"
                print "The minimum distance is " + str(min(distances))
                print "The coordinates are " + str(coordDistList[min(distances)])
                conn.sendall("Distance was calculated")

            else:
                print "***************************"
                print "Error: Error is happening"
                conn.sendall("Error")

            if not data: break

        except socket.error:
            print "Error Occured."
            break

    conn.close()
