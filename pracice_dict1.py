dict={
    "veed":"House",
    "ente":"Mine",
    "njan":"Iam",
    "sugham":"Fine"
}
key=input("Enter the key :")

if dict.get(key)==None:
    print("The Value is not present")
else:
    print(f"The meaning of the {key} is :",dict.get(key))