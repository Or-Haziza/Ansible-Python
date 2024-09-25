import boto3
import json
import yaml

ec2 = boto3.resource('ec2')
OrEc2 = []
for instance in ec2.instances.all():
    #
    try:
        for tag in instance.tags:

            if tag["Key"] == "Name":
                if tag["Value"] == "or_mysql" or tag["Value"] == "or_ngnix" :
                    OrEc2.append(instance.id)

    except:
        print("you dont have date yet",instance.id)




print(OrEc2)
all_tags = []
ec3 = boto3.client('ec2')
for instance1 in OrEc2:
    response = ec3.describe_instances(InstanceIds=[instance1])
    tags = response['Reservations'][0]['Instances'][0].get('Tags', [])
    all_tags.append({'InstanceId': instance1, 'Tags': tags})
    print(tags)

    with open('tags.json', 'w') as file:
        json.dump(all_tags, file, indent=4)


with open('tags.json', 'r') as file:
    data = json.load(file)


with open('tags.yml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)

print("Converted tags.json to tags.yml")