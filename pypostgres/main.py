import projectcars

def main():
    # create a class object
    pypg = projectcars.Projectcars()
    # close database connection
    pypg.close_connection()

if __name__ == "__main__":
    main()