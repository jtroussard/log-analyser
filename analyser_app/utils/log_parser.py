import re, hashlib

def hash_error(error):
    hash = hashlib.md5(extract_stack_trace(error).encode('utf-8'))
    return(hash.hexdigest())

def extract_stack_trace(error):
    s_error = error.split("\n")
    copy = False
    stack_line = []
    stack_trace = []
    for line in s_error:
        exception_line = re.search(r'.*(Consumer exception:.*)', line)
        if exception_line:
            copy = True
            stack_trace.append(exception_line.group(1))
            continue
        elif copy:
            stack_trace.append(line)
    return "\n".join(stack_trace)

def extract_error_description(error):
    description = re.search(r'.*(Consumer exception:.*)', error.split("\n")[0])
    if description:
        return description.group(1)
    return None

def join_error(error):
    seperator = ""
    return seperator.join(error)

# unit test needs:
# - two error lines right after eachother
# - INFO WARN DEBUG line right after error
# - empty lines
def get_errors(log):
    copy = False
    error = []
    errors = []
    
    for line in log:
        error_line = re.search( r'[0-9]{4}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}\sERROR.*', line)
        other_line = re.search( r'[0-9]{4}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}\s(?:INFO|WARN|DEBUG).*', line)

        if error_line:
            if len(error) > 0:
                errors.append(join_error(error))
                error = []
            copy = True
            error.append(line)
            continue
        elif line == ("" or "\n") or other_line:
            copy = False
            if len(error) > 0:
                errors.append(join_error(error))
                error = []
            continue
        elif copy:
            error.append(line)
    return errors

# logFile = "/home/troussard/EnterpriseRx/erx/dev/server/jboss-eap-7.1/standalone/log/erx.log"
# with open(logFile, 'r') as logFile:
#         errors = get_errors(logFile)

#         for error in errors:
#             # print(extract_error_description(error))
#             # print(error)
#             # print(extract_stack_trace(error))
#             # print(hash_error(error))
#             pass
#         print(hash_error(errors[13]))
#         print(hash_error(errors[13]) == hash_error(errors[20]))
#         test = "d41d8cd98f00b204e9800998ecf8427e"
#         print(hash_error(errors[13]) == test)
