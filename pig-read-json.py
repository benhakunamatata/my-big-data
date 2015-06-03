from org.json.simple.parser import JSONParser

def get_file_content(filename):
    filestr = ""
    try:
        json_file = open(filename)
        filestr = json_file.read()
        json_file.close()
    except:
        print 'File reading Error for %s .' % (filename)
    return filestr

def get_json(json_str):
    json_data = {}
    try:
        parser = JSONParser()
        json_data = parser.parse(json_str)
        # json_file.close()
        print json_data
    except:
        print 'JSON parsing Error for %s .' % (json_str)
    return json_data

def get_params_as_json():
    filename = 'src/main/pig/dm2_bigtable_params.json'
    content = get_file_content(filename)
    json_data = get_json(content)
    json_data = dict(json_data)
    return json_data
    
