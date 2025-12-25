def outer():
    z = 5   # outer variable

    def inner():
        nonlocal z
        z = 10  # modifies outer variable
        print("Inside inner, z =", z)

    inner()
    print("Inside outer after inner, z =", z)

outer()
