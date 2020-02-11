#Alex Harris
#CS160 9am

def main():

    #list of versions
    versions = ["Mavericks", "Yosemite", "El Capitan", "Sierra", "High Sierra", "Mojave"]

    #Get the version the user wants
    userVersion = input("Please input the version: ")

    #split the version the user entered
    partOne, partTwo, partThree = userVersion.split(".")

    #reassign the version to the version in the list
    userVersion = versions[int(partTwo) - 9]

    #Tell the user the version name
    print("The name of that version is", userVersion+".")

main()