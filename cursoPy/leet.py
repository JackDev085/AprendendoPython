def likes(names):
    if names:
        if len(names)>0 and len(names)<2:
            return(f"{names[0]}likes this")

        elif len(names) > 1 and len(names) < 3:
            return(f"{names[0]} and {names[1]} like this")

        elif len(names) > 2 and len(names) < 4:
            return(f"{names[0]}, {names[1]} and {names[2]} like this")

        elif len(names) > 3:
            return(f"{names[0]}, {names[1]} and {len(names)-2} others like this")
    else:
        return("No one like this")
names = ['luiz', 'carla', 'julio', 'ricardo', 'samira']
likes(names)  


'Max, Mark and John like this' 


'Max, John and Mark like this'