import os

WORKING_FOLDER = '/..../exports/'

DAR_FOLDER = WORKING_FOLDER + 'dars/'
COMPOSITE_FOLDER = WORKING_FOLDER + 'composites/'
ENV_FOLDER = WORKING_FOLDER + 'environments/'
INFRA_FOLDER = WORKING_FOLDER + 'infrastructure/'
CONF_FOLDER = WORKING_FOLDER + 'configuration/'

ROOT_APP = 'Applications'
ROOT_ENV = 'Environments'
ROOT_INF = 'Infrastructure'
ROOT_CON = 'Configuration'

##################
# Init
##################
os.makedirs(DAR_FOLDER)
os.makedirs(COMPOSITE_FOLDER)
os.makedirs(ENV_FOLDER)
os.makedirs(INFRA_FOLDER)
os.makedirs(CONF_FOLDER)

####################################
# Directories
####################################

directories = []
def searchDirs(parentDir):
    childs = repository.search('core.Directory', parentDir)
    if parentDir not in [ROOT_APP, ROOT_ENV, ROOT_INF, ROOT_CON]:
        directories.append(parentDir)
    if len(childs) == 0:
        return
    for x in childs:
        searchDirs(x)

searchDirs(ROOT_APP)
searchDirs(ROOT_ENV)
searchDirs(ROOT_INF)
searchDirs(ROOT_CON)

with open(WORKING_FOLDER + 'Directories.txt', 'w') as f:
    for item in directories:
        f.write(item)
        f.write('\n')

print('-------------------------------')
print('Exported ' + str(len(directories))  + ' directories')
print('-------------------------------')


####################################
# Pipelines
# Export empty pipelines
####################################
pipelines = []
pipelines = repository.search('release.DeploymentPipeline')
with open(WORKING_FOLDER + 'Pipelines.txt', 'w') as f:
    for item in pipelines:
        f.write(item)
        f.write('\n')

print('-------------------------------')
print('Exported ' + str(len(pipelines))  + ' pipelines')
print('-------------------------------')

####################################
# Applications
####################################

applications = []
applications = repository.search('udm.Application')
with open(WORKING_FOLDER + 'Applications.txt', 'w') as f:
    for item in applications:
        app = repository.read(item)
        f.write(item)
        f.write(':')
        if hasattr(app,'lastVersion') == True:
            f.write(app.lastVersion)
        f.write(':')
        if hasattr(app,'pipeline') == True:
            if app.pipeline != None:
                f.write(app.pipeline)
        f.write('\n')

print('-------------------------------')
print('Exported ' + str(len(applications))  + ' applications')
print('-------------------------------')

####################################
# udm.DeploymentPackage
####################################

listOfDars = repository.search('udm.DeploymentPackage')

for item in listOfDars:
    print('Exporting ' + item)
    fileName = repository.exportDar(DAR_FOLDER, item)

print('-------------------------------')
print('Exported ' + str(len(listOfDars))  + ' deploymentPackage')
print('-------------------------------')

####################################
# udm.CompositePackage
####################################

listOfComposite = repository.search('udm.CompositePackage')

with open(COMPOSITE_FOLDER + 'Composites.txt', 'w') as f:
    for item in listOfComposite:
        # export the parent 
        items = item.split('/')
        items.pop()
        item = '/'.join(items)
        print('Exporting ' + item)
        fileName = repository.exportCisAndWait(item, COMPOSITE_FOLDER)
        f.write(fileName)
        f.write('\n')

print('-------------------------------')
print('Exported ' + str(len(listOfComposite))  + ' CompositePackage')
print('-------------------------------')

#######################################
# Infrastucture
#######################################

fileName = repository.exportCisAndWait(ROOT_INF,INFRA_FOLDER)
with open(INFRA_FOLDER + 'Infrastucture.txt', 'w') as f:
    f.write(fileName)

print ('---------------------------')
print ('Exported infrastucture in ' + fileName)
print ('---------------------------')


#######################################
# smtp, notifications and triggers
#######################################
listOfServer = repository.search('mail.SmtpServer')
with open(CONF_FOLDER + 'smtpservers.txt', 'w') as f:
    for item in listOfServer:
        # export the parent 
        items = item.split('/')
        items.pop()
        item = '/'.join(items)
        print('Exporting ' + item)
        fileName = repository.exportCisAndWait(item, CONF_FOLDER)
        f.write(fileName)
        f.write('\n')

listOfNotif = repository.search('trigger.EmailNotification')
with open(CONF_FOLDER + 'notifications.txt', 'w') as f:
    for item in listOfNotif:
        # export the parent 
        items = item.split('/')
        items.pop()
        item = '/'.join(items)
        print('Exporting ' + item)
        fileName = repository.exportCisAndWait(item, CONF_FOLDER)
        f.write(fileName)
        f.write('\n')

listOfTriggers = repository.search('trigger.TaskTrigger')
with open(CONF_FOLDER + 'triggers.txt', 'w') as f:
    for item in listOfTriggers:
        # export the parent 
        items = item.split('/')
        items.pop()
        item = '/'.join(items)
        print('Exporting ' + item)
        fileName = repository.exportCisAndWait(item, CONF_FOLDER)
        f.write(fileName)
        f.write('\n')

#######################################
# Configuration
#######################################
fileName = repository.exportCisAndWait(ROOT_CON,CONF_FOLDER)
with open(CONF_FOLDER + 'Configuration.txt', 'w') as f:
    f.write(fileName)

print ('---------------------------')
print ('Exported configuration in ' + fileName)
print ('---------------------------')

#######################################
# Environments
#######################################

fileName = repository.exportCisAndWait('Environments',ENV_FOLDER)
with open(ENV_FOLDER + 'Environments.txt', 'w') as f:
    f.write(fileName)

print ('---------------------------')
print ('Exported Environments in ' + fileName)
print ('---------------------------')