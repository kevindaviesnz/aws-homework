#from classes.Electric import Electric
#from classes.ICE import ICE
from classes import Electric, ICE

def main():
    ev = Electric('Tesla', 1000)
    ev.drive()
    ice = ICE('Holden', 1000)
    ice.drive()


if __name__ == "__main__":
    main()