'''
this file generate a C library with library name (interface) == 'interface.h'

and the path of folder, ex:
./document
will be generated './document/interface.h'
'''

def generate_library(library_name, path_to_generate_library):
    library_filename = library_name + '.h'
    with open(library_filename, 'r') as package_file:
        library_data = package_file.read()

    with open(path_to_generate_library + library_filename, 'w') as file:
        file.write(library_data)