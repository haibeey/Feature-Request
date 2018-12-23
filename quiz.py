from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb61otgAYrIpR_X0P1BQfDnFCCgCpi_GA8BQ1pEC0MoGjBEy-KqEX_\
fUUIVaYR2i_H4CUgtX5MRpGgKhTESkyYh73kwhUuAho74M93pcTVlt0Tnm_A53eC6abo2aSgRyiY1ZzRj\
cTrRZgWQwvwaxCjetuJwAZYgA6a-04B602zQYRbQoaWjdLzaWWXV-9kMUpqsaCQ'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
