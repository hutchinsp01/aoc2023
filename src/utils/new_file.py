import os

l = filter(lambda x: "__" not in x and ".py" in x, os.listdir("src"))
l = list(l)
n = int(sorted(l)[-1][:2]) + 1 if len(l) > 0 else 1

# new_file_template.txt
# replace <DAY_NUM>
template_path = "src/utils/new_file_template.txt"
with open(template_path, "r") as f:
    TEMPLATE = f.read()
    DEFAULT_FILE = TEMPLATE.replace("<DAY_NUM>", str(n))

path = f"src/{n:02d}.py"
with open(path, "w") as f:
    f.write(DEFAULT_FILE)

print(f"Enter your solution in {path}")
