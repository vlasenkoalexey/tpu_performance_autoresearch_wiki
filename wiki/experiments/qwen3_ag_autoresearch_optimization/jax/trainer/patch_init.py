with open("model/__init__.py", "r") as f:
    text = f.read()

new_text = text.replace("    set_splash_mesh,\n", "")
new_text = new_text.replace('"set_splash_mesh", ', "")

with open("model/__init__.py", "w") as f:
    f.write(new_text)

with open("trainer/model/__init__.py", "w") as f:
    f.write(new_text)
