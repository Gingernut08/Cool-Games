class Room:
    def __init__(self, name, description, items = None):
        self.name = name
        self.description = description
        if items == None:
            self.items = [None]
        else:
            self.items = items

        self.connected_rooms = {}
    
    def connect_rooms(self, directions, rooms):
        for i in range(len(rooms)):
            self.connected_rooms[directions[i]] = rooms[i]
    
    def get_details(self):
        return f"\n{self.name}: {self.description}\n{self.get_items()}\n"
    
    def get_items(self):
        if self.items[0] == None:
            return "Items: \nNone"

        itemNames = []
        for i in range(len(self.items)):
            itemNames.append(self.items[i].name)
        return f"Items: \n{", ".join(itemNames)}"
    
    def add_item(self, item):
        if self.items == [None]:
            self.items = [item]
        else:
            self.items.append(item)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def add_to_room(self, room):
        room.add_item(self)

    def get_details(self):
        return f"\n{self.name}: \n{self.description}\n"



def create_rooms():
    global c1, c2, c3, c4, c5, c6, admin, cafeteria, communication, electrical, lowerEngine, medbay, navigation, o2, reactor, security, shields, storage, upperEngine, weapons

    c1Description = """
"""
    c1Items = [None]
    c1 = Room("Corridor 1", c1Description, c1Items)

    c2Description = """
"""
    c2Items = [None]
    c2 = Room("Corridor 2", c2Description, c2Items)
    
    c3Description = """
"""
    c3Items = [None]
    c3 = Room("Corridor 3", c3Description, c3Items)

    c4Description = """
"""
    c4Items = [None]
    c4 = Room("Corridor 4", c4Description, c4Items)

    c5Description = """
"""
    c5Items = [None]
    c5 = Room("Corridor 5", c5Description, c5Items)

    c6Description = """
"""
    c6Items = [None]
    c6 = Room("Corridor 6", c6Description, c6Items)


    adminDescription = """
The Admin room is a compact, high-tech area equipped with advanced consoles and monitors 
for managing crew activity and ship systems. A central feature is the map display, which 
provides real-time location data for players, aiding strategic planning. The card swipe 
task, a notorious challenge for many, is located here. Its clean and functional design 
emphasizes utility, making Admin essential for gathering information and completing 
critical tasks, while also being a potential target for sabotage.
"""
    adminItems = [None]
    admin = Room("Admin", adminDescription, adminItems)
    rooms.append(admin)

    cafeteriaDescription = """
The Cafeteria is a spacious, multifunctional area where crew members gather to eat, relax, 
and complete tasks. Its clean, symmetrical design includes central tables, bright overhead 
lighting, and functional decor like drink dispensers. A prominent feature is the emergency 
meeting button, used to call discussions or report findings. The open layout allows for 
easy movement and visibility, making it a relatively safe zone. The Cafeteria serves as 
both a social hub and a critical area for strategic decisions.
    """
    cafeteriaItems = [None]
    cafeteria = Room("Cafeteria", cafeteriaDescription, cafeteriaItems)
    rooms.append(cafeteria)

    communicationDescription = """
The Communications room is a compact, high-tech area critical for maintaining ship 
connectivity and relaying vital information. Its main feature is a large console used 
to restore communication systems and complete tasks. Flashing displays and illuminated 
panels add to its functional aesthetic. The room plays a crucial role in keeping systems 
operational, yet its isolated position makes it a risky location. Its sleek design 
balances practicality with accessibility, making it a vital area for technical operations.
"""
    communicationItems = [None]
    communication = Room("Communication", communicationDescription, communicationItems)
    rooms.append(communication)
        
    electricalDescription = """
The Electrical room is a dimly lit, densely packed area filled with wiring panels and 
system breakers. It is a hub for critical repair tasks, such as fixing lights or 
calibrating circuits. The confined, maze-like layout and numerous task stations make 
it both essential and perilous for crewmates, often a hotspot for sabotage. Bright 
flashes from live circuits illuminate its industrial design, emphasizing its raw 
functionality. Electrical is vital for system maintenance but carries significant 
risks for lone crewmates.
"""
    electricalItems = [None]
    electrical = Room("Electrical", electricalDescription, electricalItems)
    rooms.append(electrical)
    
    lowerEngineDescription = """
The Lower Engine is an industrial space dedicated to propulsion control and energy alignment. 
A prominent engine dominates the room, surrounded by glowing panels and mechanical systems. 
Task stations allow crew members to refuel or adjust energy flow to maintain operational 
efficiency. Its functional design features exposed pipes and metallic structures, underscoring 
its technical purpose. Bright but focused lighting illuminates the workspace, creating a 
high-tech, industrial atmosphere critical for maintaining the ship’s movement and power 
stability.
"""
    lowerEngineItems = [None]
    lowerEngine = Room("Lower Engine", lowerEngineDescription, lowerEngineItems)
    rooms.append(lowerEngine)
    
    medbayDescription = """
The MedBay is a sterile, clinical environment dedicated to health checks and biological 
analysis. Key features include a medical scanner for verifying crewmate tasks and 
stations for analyzing samples. Its bright lighting and clean design emphasize hygiene 
and precision. The MedBay is a space of trust and collaboration, as the visual task 
proves innocence. Despite its calming appearance, it’s a critical zone for impostors 
to target due to its relative isolation and importance in crew operations.
"""
    medbayItems = [None]
    medbay = Room("Medbay", medbayDescription, medbayItems)
    rooms.append(medbay)

    navigationDescription = """
The Navigation room is a sleek, futuristic space designed for plotting and maintaining 
the ship’s course. It features advanced control panels, star charts, and targeting systems 
used for steering and task completion. Bright screens and a compact layout emphasize its 
purpose as the ship's guidance hub. The interactive tasks, such as charting a course or 
aligning the ship, highlight its importance in mission success. Navigation's strategic 
role makes it a critical but vulnerable location.
"""
    navigationItems = [None]
    navigation = Room("Navigation", navigationDescription, navigationItems)
    rooms.append(navigation)

    o2Description = """
The O2 room is a vital space responsible for managing the ship’s oxygen supply. Compact 
and functional, it houses systems for refilling canisters and ventilating the ship. Bright 
panels and task stations dominate its design, ensuring functionality remains the priority. 
Tasks here involve precise interactions, such as cleaning filters or entering codes. Its 
role in life support makes O2 critical for survival, yet its isolated location makes it a 
high-risk zone for crew members.
"""
    o2Items = [None]
    o2 = Room("O2", o2Description, o2Items)
    rooms.append(o2)
    
    reactorDescription = """
The Reactor is a heavily secured area housing the ship’s primary energy source. Dominated 
by a massive reactor core, the room requires precision tasks like unlocking manifolds or 
stabilizing energy flow. Bright warning lights and industrial equipment highlight its 
critical nature. Its role in powering the ship makes it indispensable, but its distant 
location and reliance on team coordination for certain tasks make it a common target for 
sabotage, adding tension to its functional design.
"""
    reactorItems = [None]
    reactor = Room("Reactor", reactorDescription, reactorItems)
    rooms.append(reactor)
    
    securityDescription = """
The Security room is a surveillance hub equipped with monitors displaying real-time footage 
of various ship areas. Its central console allows crewmates to observe activity and identify 
threats, making it vital for detecting impostors. The room’s dim lighting and minimalist 
design ensure focus on the screens. Tasks such as rewiring or uploading data also occur here. 
Despite its strategic importance, its confined layout and limited exits make Security a 
high-risk area for unsuspecting players.
"""
    securityItems = [None]
    security = Room("Security", securityDescription, securityItems)
    rooms.append(security)

    shieldsDescription = """
The Shields room is a compact, specialized area responsible for maintaining the ship’s defensive 
systems. Its bright displays and illuminated panels reflect its high-tech function. A primary 
task involves recalibrating shields to reinforce the ship’s protection, providing visual 
confirmation of a crewmate’s innocence. The room’s small size and limited access points make 
it an ideal location for impostor ambushes. Despite its simplicity, Shields plays a vital role 
in ensuring the ship’s safety and operational integrity.
"""
    shieldsItems = [None]
    shields = Room("Shields", shieldsDescription, shieldsItems)
    rooms.append(shields)
    
    storageDescription = """
The Weapons room is a high-tech space designed for managing the ship’s offensive systems. It 
features a prominent weapons console for tasks like targeting asteroids, a visual proof of 
crewmate innocence. Bright displays and glowing panels create a futuristic atmosphere, while 
its compact layout ensures focus on critical tasks. The room’s strategic importance makes it 
a common site for both task completion and impostor ambushes. Weapons serves as a critical hub 
for ship defense and crew collaboration.
"""
    storageItems = [None]
    storage = Room("Storage", storageDescription, storageItems)
    rooms.append(storage)
    
    upperEngineDescription = """
The Upper Engine is a vital propulsion hub, featuring a massive glowing engine and control panels for 
managing thrust and alignment. Industrial pipes and machinery dominate the space, emphasizing its 
mechanical function. Tasks here include realigning the engine and refueling, ensuring the ship's 
propulsion remains operational. The room’s narrow layout and utilitarian design make it an essential 
yet challenging space for navigation. Bright lighting highlights the critical machinery, balancing 
functionality with a raw, industrial aesthetic.
"""
    upperEngineItems = [None]
    upperEngine = Room("Upper Engine", upperEngineDescription, upperEngineItems)
    rooms.append(upperEngine)

    weaponsDescription = """
The Weapons room is a high-tech space designed for managing the ship’s offensive systems. It features 
a prominent weapons console for tasks like targeting asteroids, a visual proof of crewmate innocence. 
Bright displays and glowing panels create a futuristic atmosphere, while its compact layout ensures 
focus on critical tasks. The room’s strategic importance makes it a common site for both task 
completion and impostor ambushes. Weapons serves as a critical hub for ship defense and crew 
collaboration.
    """
    weaponsItems = [None]
    weapons = Room("Weapons", weaponsDescription, weaponsItems)
    rooms.append(weapons)


    c1.connect_rooms([EAST, SOUTH, WEST], [cafeteria, medbay, upperEngine])
    c2.connect_rooms([NORTH, EAST, SOUTH, WEST], [upperEngine, security, lowerEngine, reactor])
    c3.connect_rooms([NORTH, EAST, WEST], [electrical, storage, lowerEngine])
    c4.connect_rooms([NORTH, EAST, SOUTH], [cafeteria, admin, storage])
    c5.connect_rooms([EAST, SOUTH, WEST], [shields, communication, storage])
    c6.connect_rooms([NORTH, SOUTH, EAST, WEST], [weapons, shields, navigation, o2])

    admin.connect_rooms([WEST], [c1])
    cafeteria.connect_rooms([EAST, SOUTH, WEST], [weapons, c4, c1])
    communication.connect_rooms([NORTH], [c5])
    electrical.connect_rooms([SOUTH], [c3])
    lowerEngine.connect_rooms([NORTH, EAST], [c2, c3])
    medbay.connect_rooms([NORTH], [c1])
    navigation.connect_rooms([WEST], [c6])
    o2.connect_rooms([EAST], [c6])
    reactor.connect_rooms([EAST], [c2])
    security.connect_rooms([WEST], [c2])
    storage.connect_rooms([NORTH, EAST, WEST], [c4, c5, c3])
    shields.connect_rooms([NORTH, WEST], [c6, c4])
    upperEngine.connect_rooms([EAST, SOUTH], [c1, c2])
    weapons.connect_rooms([SOUTH, WEST], [c6, cafeteria])

def create_items():
    global meetingButton, hammer
    meetingButton = Item("Meeting Button", "A Button covered with a glass casing")
    meetingButton.add_to_room(cafeteria)
    itemList.append(meetingButton)  
    hammer = Item("Hammer", "Sharp metal hammer with a long handle")
    hammer.add_to_room(cafeteria)
    itemList.append(hammer) 

    



def go_direction(direction):
    global currentRoom
    newRoom = currentRoom.connected_rooms.get(direction)
    if newRoom != None:
        currentRoom = newRoom
    else:
        print("Cannot go in this direction")
    
    print(f"{currentRoom.name}\n")

def pick_up_item(item):
    if len(currentRoom.items) != 0:
        i = 0
        for x in range(len(currentRoom.items)):
            if item == currentRoom.items[i].name.lower().split(" "):
                playerItems.append(currentRoom.items[i])
                currentRoom.items.pop(i)
                i -= 1
            else:
                print(currentRoom.items[i].name.lower())
            i += 1
    else:
        print("There are no items to be collected")
    tempPlayerItems = []
    for i in range(len(playerItems)):
        tempPlayerItems.append(playerItems[i].name)
    print(f"Items: \n{", ".join(tempPlayerItems)}")



def enter_command():
    command = str(input("Enter Go -   ").lower()).split(" ")
    command = [i for i in command if i != ""]
    match command[0]:
        case "go":
            command.pop(0)
            go_direction(command)
        case "look":
            command.pop(0)
            print(currentRoom.get_details())
        case "collect":
            command.pop(0)
            pick_up_item(command)
        case _:
            print("Verb not recognised")



NORTH = "north"
SOUTH = "south"
EAST = "east"
WEST = "west"
rooms = []
itemList = []
playerItems = []

create_rooms()
create_items()

currentRoom = cafeteria

while True:
    enter_command()










