import boto3

iam = boto3.client("iam")

users = iam.list_users()["Users"]

print("\nShadow Identity Report\n------------------------")

for user in users:
    name = user["UserName"]
    last_used = iam.get_user(UserName=name)
    print(f"User: {name} → Last Used: {last_used}")
