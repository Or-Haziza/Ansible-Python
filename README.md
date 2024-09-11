# Project Map

This document provides an overview of the project structure, key components, and their relationships. It is designed to help users understand the organization and workflow of the project.

## Project Structure

The project consists of the following key components:

1. **Playbook (`playbook1.yml`)**
   - **Description**: Contains the main Ansible playbook used for installing and managing services based on tags.
   - **Location**: Root directory
   - **Key Tasks**:
     - Read tags file
     - Find tags for current instance
     - Extract service and version from tags
     - Install and manage services (MySQL, Nginx)

2. **Tags File (`tags.yml`)**
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

3. **Inventory File (`inventory.ini`)**
   - **Description**: Lists the EC2 instances to be managed by Ansible.
   - **Location**: Root directory
   - **Format**:
     ```ini
     [ec2_instances]
     i-0bbeb22ee83963b1e ansible_host=your-ec2-instance-public-ip
     i-0399014ff3040b785 ansible_host=your-ec2-instance-public-ip
     ```

4. **Configuration File (`ansible.cfg`)**
   - **Description**: Ansible configuration file that specifies settings for running Ansible commands.
   - **Location**: Root directory
   - **Key Sections**:
     - **Defaults**: Configuration settings for Ansible behavior
     - **Inventory**: Path to the inventory file

5. **README File (`README.md`)**
   - **Description**: Provides an overview of the project, setup instructions, and usage guidelines.
   - **Location**: Root directory
   - **Key Sections**:
     - Project overview
     - Setup instructions
     - Usage example
     - Troubleshooting
     - Contribution guidelines

## Workflow

1. **Preparation**:
   - Ensure that `tags.yml` and `inventory.ini` are correctly configured with instance details and tags.
   - Review and update `playbook1.yml` as needed.

2. **Execution**:
   - Run the Ansible playbook to install and manage services:
     ```bash
     ansible-playbook -i inventory.ini playbook1.yml
     ```

3. **Verification**:
   - Check that services are installed and running on the EC2 instances as expected.

4. **Troubleshooting**:
   - If issues arise, refer to the `README.md` for troubleshooting steps or inspect logs for detailed error messages.

## Contribution

To contribute to the project:
- Fork the repository
- Make improvements or fixes
- Submit a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



## הודעה בשביל עצמי
להוסיך את השימוש בסקריפט פייתון שמכין את קובץ הTags.yaml לפי המצב בחשבון aws של ה-user
