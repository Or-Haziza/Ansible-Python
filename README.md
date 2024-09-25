# Project Map

This document provides an overview of the project structure, key components, and their relationships. It is designed to help users understand the organization and workflow of the project.

## Project Overview

This project involves automation for managing services on Amazon EC2 instances using Ansible and Python. The setup includes one Ansible controller machine and two managed instances, each with specific tags that dictate which services need to be installed.

## Project Structure

The project consists of the following key components:

### Playbook (playbook.yml)

- **Description**: Contains the main Ansible playbook used for installing and managing services based on tags.
- **Location**: Root directory
- **Key Tasks**:
  - Read tags file
  - Find tags for the current instance
  - Extract service and version from tags
  - Install and manage services (e.g., MySQL, Nginx)

### Tags File (tags.yml)

- **Description**: YAML file that specifies tags for EC2 instances, including service names and versions.
- **Location**: Root directory
- **Format**:
  ```yaml
  - InstanceId: "i-0bbeb22ee83963b1e"
    Tags:
      - Key: "Name"
        Value: "or_mysql"
      - Key: "Service"
        Value: "mysql"
      - Key: "Version"
        Value: "8.0"

  - InstanceId: "i-0399014ff3040b785"
    Tags:
      - Key: "Name"
        Value: "or_nginx"
      - Key: "Service"
        Value: "nginx"
      - Key: "Version"
        Value: "1.24"
  ```

### Inventory File (inventory.ini)

- **Description**: Lists the EC2 instances to be managed by Ansible.
- **Location**: Root directory
- **Format**:
  ```ini
  [ec2_instances]
  i-0bbeb22ee83963b1e ansible_host=your-ec2-instance-public-ip
  i-0399014ff3040b785 ansible_host=your-ec2-instance-public-ip
  ```

### Configuration File (ansible.cfg)

- **Description**: Ansible configuration file that specifies settings for running Ansible commands.
- **Location**: Root directory
- **Key Sections**:
  - **Defaults**: Configuration settings for Ansible behavior
  - **Inventory**: Path to the inventory file

### Python Script (tags-to-vars.py)

- **Description**: Script that converts tags from the `tags.yml` file into a variables file used by Ansible.
- **Location**: Root directory

## Workflow

### Preparation

1. **Connect to EC2 Instances**: Ensure that all instances are connected via SSH.
2. **Run the Tags Conversion Script**: Execute the Python script to convert tags to variables:
   ```bash
   python tags-to-vars.py
   ```
3. **Prepare the Inventory**: Ensure the `inventory.ini` file is correctly configured with instance details.

### Execution

4. **Run the Ansible Playbook**: Execute the playbook using the generated variables:
   ```bash
   ansible-playbook -i inventory.ini playbook.yml
   ```

### Verification

5. **Check Services**: Verify that services are installed and running on the EC2 instances as expected.

### Troubleshooting

If issues arise:
- Refer to this README for troubleshooting steps.
- Inspect logs for detailed error messages.

## Contribution

To contribute to the project:

1. Fork the repository.
2. Make improvements or fixes.
3. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
