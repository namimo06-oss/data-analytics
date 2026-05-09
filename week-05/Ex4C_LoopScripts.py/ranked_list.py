# LAB 3
# RANKED LIST USING ENUMERATE
colors= ["blue", "yellow","purple","orange","pink"]


# NORMAL ORDER (starting at 1)
for index, item in enumerate(colors, start=1):
    # If it's the first item in the list
    if index == 1:
        print(f"{index}. {item} <- top pick!")
    else:
        print(f"{index}. {item}")

# BONUS: REVERSED LIST
print("\nReversed order:")
for index, item in enumerate(reversed(colors), start=1):
    print(f"{index}. {item}")

