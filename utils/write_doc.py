def write_documentation(params, response):
    f = open(params["output_file"], "w")

    f.write(response)

    f.write("\n\n")
    f.write("*This documentation file was generated using [genDocsGPT](https://github.com/marco-rosner/genDocsGPT)*")
    
    f.close()

    print("API documentation generated")