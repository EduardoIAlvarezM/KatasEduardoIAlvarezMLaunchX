#def main():
#    open("/path/to/mars.jpg")
#if __name__ == '__main__':
#    main()
#SALIDA
#Traceback (most recent call last):
#  File "C:\Users\Zer0\Documents\gitHubCourse\kata10\open.py", line 4, in <module>
#    main()
#  File "C:\Users\Zer0\Documents\gitHubCourse\kata10\open.py", line 2, in main
#    open("/path/to/mars.jpg")
#FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'

try:
    open('config.txt')
except FileNotFoundError:
    print("Couldn't find the config.txt file!")