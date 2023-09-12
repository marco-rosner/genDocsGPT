def write_documentation(filename, response):
    f = open(filename, "w")

    f.write(response)
    
    f.close