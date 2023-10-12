
def parse_headers(header_line):
    return header_line.strip().split(',')
def parse_values(data_line):
    values=[]
    items = data_line.strip().split(',')
    for item in items:
        item=item.strip()
        if item == '':
            values.append(0.0)
        try:
            values.append(float(item))
        except ValueError:
            values.append(item.strip('"'))   
    return values              
def create_item_dict(values,headers):
    result={}
    for values,headers in zip(values,headers):
        result[headers]=values
    return result        
def read_csv(path):
    result=[]
    with open(path,'r')as f:
        lines=f.readlines()
        headers=parse_headers(lines[0])
        for data_line in lines[1:]:
            values=parse_values(data_line)
            item_dict=create_item_dict(values,headers)
            result.append(item_dict)
        return result    
data_dict=read_csv('reading files\deniro.csv')
print(data_dict)
