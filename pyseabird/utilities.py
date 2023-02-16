# Utilities

import re

def ReplacePlaceholderVariables(input_filename, output_filename, dictionary, dryrun=True):
    print("Placehodler variables")

    with open(input_filename, 'r') as file:
        data = file.read()

        for key, value in dictionary.items():
            print("kv", key, value)
            data = data.replace(key, value, 1) # The variable should only occour once!
        
        regexp_any_variable = "<hi-.+-var>" # will match any placeholder variable, ex <hi-anything-var>
        r1 = re.findall(regexp_any_variable, data)
        if r1:
            raise Exception("Error, there are un-replaced <hi-anything-var> variables!", r1) 

    if dryrun:
        print("Dry run output only")
    else:
        print("Writing to output-file", output_filename)
        with open(output_filename, 'w') as file:
            file.write(data)