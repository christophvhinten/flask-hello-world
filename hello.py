from flask import Flask, request
from markupsafe import escape

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

import sys
def getSysInfo():

    sysInfo = ''
    
    # Python sys information
    sysInfo = sysInfo + '\n<br><br>\n' + 'Executable: ' + sys.executable
    sysInfo = sysInfo + '\n<br><br>\n' + 'Path: ' + '; '.join(sys.path)
    sysInfo = sysInfo + '\n<br><br>\n' + 'Version: ' + sys.version.replace('\n', '')
    #sysInfo = sysInfo + '\n<br><br>\n' + 'API_Version: ' + ''.join(str(sys.api_version))
    sysInfo = sysInfo + '\n<br><br>\n' + 'Platform: ' + sys.platform
    sysInfo = sysInfo + '\n<br><br>\n' + 'Thread_Info: ' + str(sys.thread_info)

    # Python sys implementation
    sysInfo = sysInfo + '\n<br><br>\n' + 'Implementation: ' + str(sys.implementation)

    # Python sys modules
    sysInfo = sysInfo + '\n<br><br>\n' + 'Built_In Modules: ' + ''.join(sys.builtin_module_names)
    #sysInfo = sysInfo + '\n<br><br>\n' + 'Loaded Modules: ' + ''.join(list(sys.modules.keys()))
    
    print(sysInfo)

    return sysInfo

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----


app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    message = f'Hello, {escape(name)}!'

    sysInfo = getSysInfo()
    #message = message + '<br><br>' + f'{escape(sysInfo)}'
    message = message + '<br><br>' + sysInfo
    
    return message


if __name__ == '__main__':
    app.run()
