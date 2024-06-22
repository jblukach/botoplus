import uuid

def _dict(count,data,key):

    count += 1
    indent = _indent(count)

    for k,v in data[key].items():

        print(indent+k+' '+str(type(v)))

        if type(v) is dict:
            _dict(count,data[key],k)

        if type(v) is list:
            _list(count,data[key],k)

def _dictdeflate(count,data,key,deflated,dupe):

    count += 1

    for k,v in data[key].items():

        if type(v) is not dict and type(v) is not list:

            name = k+'_'+str(count)

            if name in dupe:
                name = name+'_'+str(uuid.uuid1())

            dupe.append(name)
            deflated[name] = v

        if type(v) is dict:
            _dictdeflate(count,data[key],k,deflated,dupe)

        if type(v) is list:
            _listdeflate(count,data[key],k,deflated,dupe)

def _indent(count):
    return '\t' * count

def _list(count,data,key):

    count += 1
    indent = _indent(count)
    index = 0

    for item in data[key]:

        print(indent+str(index)+' '+str(type(item)))

        if type(item) is dict:
            _dict(count,data[key],index)

        if type(item) is list:
            _list(count,data[key],index)

        index += 1

def _listdeflate(count,data,key,deflated,dupe):

    count += 1
    index = 0

    for item in data[key]:

        if type(item) is not dict and type(item) is not list:

            name = key+'_'+str(count)+'_'+str(index)

            if name in dupe:
                name = name+'_'+str(uuid.uuid1())

            dupe.append(name)
            deflated[name] = item

        if type(item) is dict:
            _dictdeflate(count,data[key],index,deflated,dupe)

        if type(item) is list:
            _listdeflate(count,data[key],index,deflated,dupe)

        index += 1

def deflation(data,dupe):

    deflated = {}

    count = 0

    if type(data) is dict:

        for k,v in data.items():

            if type(v) is not dict and type(v) is not list:

                name = k

                if name in dupe:
                    name = name+'_'+str(uuid.uuid1())

                deflated[name] = v

            if type(v) is dict:
                _dictdeflate(count,data,k,deflated,dupe)

            if type(v) is list:
                _listdeflate(count,data,k,deflated,dupe)

    return deflated

def strturuce(data):

    if type(data) is dict:

        for key, value in data.items():

            count = 0
            indent = _indent(count)

            print(indent+key+' '+str(type(value)))

            if type(value) is dict:
                _dict(count,data,key)

            if type(value) is list:
                _list(count,data,key)

    if type(data) is list:

        for item in data:

            count = 0
            indent = _indent(count)
            index = 0

            print(indent+str(index)+' '+str(type(item)))

            if type(item) is dict:
                _dict(count,data,index)

            if type(item) is list:
                _list(count,data,index)

            index += 1
