def write_documentation(params, response):
    f = open(params["output_file"], "w")

    f.write("[![genDocsGPT](https://img.shields.io/badge/Doc%20generated%20by-genDocsGPT-blue)](https://github.com/marco-rosner/genDocsGPT)")
    f.write("\n\n")

    f.write(response)

    f.write("\n\n")
    f.write("*This documentation file was generated using [genDocsGPT](https://github.com/marco-rosner/genDocsGPT)*")
    
    f.close()

    print("API documentation generated")