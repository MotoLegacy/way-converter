# Simple Python 2 script to convert the NZ:P Demo waypoints to the NZ:P Reboot format
# Script created by Ian Bowling aka MotoLegacy

originalFile = raw_input("Name of waypoint file: ")
#Remove the extension from the file if it exists (to create fixed name)
if ".way" in originalFile:
	originalFile = originalFile.split('.', 1)[0]

def convert(way, lnum):
	origin = wayid = ""

	target1 = target2 = target3 = target4 = target5 = target6 = target7 = target8 = ""

	with open(originalFile+".way", "r") as org, open(originalFile+"_fixed.way", "a+") as new:
		for i, line in enumerate(org):
			if i == 3-1+lnum:
				origin = line
				origin = origin.split('=', 1)[1]
			if i == 4-1+lnum:
				wayid = line
				wayid = wayid.split('=', 1)[1]
			if i == 6-1+lnum:
				target1 = line
				target1 = target1.split('=', 1)[1]
				if target1 == " \n": #blank target
					target1 = " ]"
				if target1 != " ]":
					target1 = " " + target1
			if i == 7-1+lnum:
				target2 = line
				target2 = target2.split('=', 1)[1]
				if target2 == " \n":
					target2 = " ]"
				if target2 != " ]":
					target2 = " " + target2
				if target1 == " ]" or target1 == "":
					target2 = ""
			if i == 8-1+lnum:
				target3 = line
				target3 = target3.split('=', 1)[1]
				if target3 == " \n":
					target3 = " ]"
				if target3 != " ]":
					target3 = " " + target3
				if target2 == " ]" or target2 == "":
					target3 = ""
			if i == 9-1+lnum:
				target4 = line
				target4 = target4.split('=', 1)[1]
				if target4 == " \n":
					target4 = " ]"
				if target4 != " ]":
					target4 = " " + target4
				if target3 == " ]" or target3 == "":
					target4 = ""
			if i == 10-1+lnum:
				target5 = line
				target5 = target5.split('=', 1)[1]
				if target5 == " \n":
					target5 = " ]"
				if target5 != " ]":
					target5 = " " + target5
				if target4 == " ]" or target4 == "":
					target5 = ""
			if i == 11-1+lnum:
				target6 = line
				target6 = target6.split('=', 1)[1]
				if target6 == " \n":
					target6 = " ]"
				if target6 != " ]":
					target6 = " " + target6
				if target5 == " ]" or target5 == "":
					target6 = ""
			if i == 12-1+lnum:
				target7 = line
				target7 = target7.split('=', 1)[1]
				if target7 == " \n":
					target7 = " ]"
				if target7 != " ]":
					target7 = " " + target7
				if target6 == " ]" or target6 == "":
					target7 = ""
			if i == 13-1+lnum:
				target8 = line
				target8 = target8.split('=', 1)[1]
				if target8 == " \n":
					target8 = " ]"
				if target8 != " ]":
					target8 = " " + target8
				if target7 == " ]" or target7 == "":
					target8 = ""
		new.write("waypoint\n{\n id:"+wayid+" origin:"+origin+" targets:\n [\n"+target1+target2+target3+target4+target5+target6+target7+target8+"\n}\n\n")

		way = int(way)
		way -= 1
		if way != 0:
			convert(way, lnum+15)

#Search for how many waypoints are in the file
f = open(originalFile+".way")
contents = f.read()
f.close()
number = contents.count("Waypoint")
print ("Found " + str(number) + " waypoints")

convert(number, 0)

print("Finished!")