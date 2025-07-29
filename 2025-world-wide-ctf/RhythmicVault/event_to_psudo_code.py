code = ""
with open("code","r") as f:
    code = f.read()

tags = {}
for line in code.split("\n"):
    id = line.split(" ")[0]
    action = " ".join(line.split(" ")[1:])
    if id not in tags:
        tags[id] = []
    tags[id].append(action)

# print(tags)


visited = []

def traverse(tag,depth=0):
    global visited

    if tag in visited:
        return

    visited.append(tag)

    if tag not in tags:
        print(tag.ljust(16),"   " * (depth),f"ret ({tag})")
        return

    paths = tags[tag]
    for path in paths:
        if path.startswith("if"):
            print(tag.ljust(16),"   " * (depth),"if",path.split(" ")[1])
            if path.split(" ")[2] == "Run":
                traverse(path.split(" ")[3],depth+1)
            else:
                print(tag.ljust(16),"   " * (depth+1)," ".join(path.split(" ")[2:]))
        elif "Run" in path:
            print(tag.ljust(16),"   " * (depth),"Run",path.split(" ")[1])
            traverse(path.split(" ")[1],depth)
        else:
            print(tag.ljust(16),"   " * (depth),path)

traverse("main")


# print(code)