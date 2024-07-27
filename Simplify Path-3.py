path = "/a/./b/../../c/"
stack = []
components = path.split('/')
for component in components:
    if component == "" or component == ".":
        continue
    elif component == "..":
        if stack:
            stack.pop()
    else:
        stack.append(component)
canonical_path = "/" + "/".join(stack)
print(canonical_path)  
