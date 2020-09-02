
##################################################
# Delete DeploymentPackage that are not referenced
##################################################

deploymentPackages = []
deletedApp = 0
deploymentPackages = repository.search('udm.DeploymentPackage')

for item in deploymentPackages:
    try:
        repository.delete(item)
        deletedApp += 1
        print('DeploymentPackage ' + item + ' deleted')
    except:
        print('DeploymentPackage ' + item + ' not deleted')

print('-------------------------------')
print('Deleted ' + str(deletedApp)  + ' DeploymentPackage')
print(str(len(deploymentPackages) - deletedApp) + ' were not deleted')
print('-------------------------------')
