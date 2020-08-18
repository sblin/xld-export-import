import os

WORKING_FOLDER = '/..../exports/'

DAR_FOLDER = WORKING_FOLDER + 'dars/'
COMPOSITE_FOLDER = WORKING_FOLDER + 'composites/'
ENV_FOLDER = WORKING_FOLDER + 'environments/'
INFRA_FOLDER = WORKING_FOLDER + 'infrastructure/'
CONF_FOLDER = WORKING_FOLDER + 'configuration/'

print ('--------------------------')
print ('Importing folders')
print ('--------------------------')

directories = open(WORKING_FOLDER + 'Directories.txt','r').read().split('\n')

for d in directories:
    if len(d) > 0 :
        if repository.exists(d) == False :
           repository.create(factory.configurationItem(d,'core.Directory'))
           print('Creating folder ' + d)
        else:
            print('Skipping folder ' + d)

print ('--------------------------')
print ('Importing pipelines')
print ('--------------------------')

pipelines = open(WORKING_FOLDER + 'Pipelines.txt','r').read().split('\n')

for p in pipelines:
    if len(p) > 0 :
        if repository.exists(p) == False :
           repository.create(factory.configurationItem(p,'release.DeploymentPipeline'))
           print('Creating pipeline ' + p)
        else:
            print('Skipping pipeline ' + p)


print ('--------------------------')
print ('Importing applications')
print ('--------------------------')

applications = open(WORKING_FOLDER + 'Applications.txt','r').read().split('\n')

for a in applications:
    if len(a) > 0:
        items = a.split(':')
        name = items[0]
        lastVersion = items[1]
        pipeline = items[2]
        if repository.exists(name) == False:
            repository.create(factory.configurationItem(name, 'udm.Application', {'lastVersion': lastVersion, 'pipeline': pipeline}))
            print('Creating application ' + name)
        else:
            print('Skipping application ' + name)

print ('----------------------------')
print ('Importing deploymentPackages')
print ('----------------------------')

files = os.listdir(DAR_FOLDER)
for item in files:
    if item.endswith('.dar'):
        print('Importing ' + item)
        try:
            deployit.importPackage(DAR_FOLDER + item)
        except:
            print(item + ' already imported')

print ('----------------------------')
print ('Importing compositePackages')
print ('----------------------------')

files = open(COMPOSITE_FOLDER + 'Composites.txt','r').read().split('\n')

for item in files:
        print('Importing ' + item)
        try:
            repository.importCisAndWait(item)
        except:
            print(item + ' already imported')

print ('----------------------------')
print ('Importing Infrastructure')
print ('----------------------------')
infraArchive = open(INFRA_FOLDER + 'Infrastucture.txt','r').read()
repository.importCisAndWait(infraArchive)

print ('----------------------------')
print ('Importing Smtp Servers')
print ('----------------------------')
files = open(CONF_FOLDER + 'smtpservers.txt','r').read().split('\n')
for item in files:
        print('Importing ' + item)
        try:
            repository.importCisAndWait(item)
        except:
            print(item + ' already imported')

print ('----------------------------')
print ('Importing Notifications')
print ('----------------------------')
files = open(CONF_FOLDER + 'notifications.txt','r').read().split('\n')
for item in files:
        print('Importing ' + item)
        try:
            repository.importCisAndWait(item)
        except:
            print(item + ' already imported')

print ('----------------------------')
print ('Importing Triggers')
print ('----------------------------')
files = open(CONF_FOLDER + 'triggers.txt','r').read().split('\n')
for item in files:
        print('Importing ' + item)
        try:
            repository.importCisAndWait(item)
        except:
            print(item + ' already imported')

print ('----------------------------')
print ('Importing Configuration')
print ('----------------------------')
confArchive = open(CONF_FOLDER + 'Configuration.txt','r').read()
repository.importCisAndWait(confArchive)


print ('----------------------------')
print ('Importing Environments')
print ('----------------------------')
envArchive = open(ENV_FOLDER + 'Environments.txt','r').read()
repository.importCisAndWait(envArchive)