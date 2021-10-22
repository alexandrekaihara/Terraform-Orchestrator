# Terraform Azure Provider

Here contains all the descriptions to setup, use and execute the experiment described on the paper

## 1. Setup
This section is dedicated to describe all the steps to install and configure the machine to execute the terraform script

### Create the Azure account 
First step on setup is to create a account on the providers site:
1. Access https://azure.microsoft.com/pt-br/;
2. Click on create "free account";
3. Fill in the registration;
4. Then sign up

### Terraform installation
To install Terraform, follow these steps:
* Access https://www.terraform.io/downloads.html;
* Download the respective .zip file according to your Operating System;
* Unzip it;
* Add it to the environment variables;

### Install Azure Cli
To use the terraform Azure provider, it must be installed the Azure Cli, the following steps decribe the installation process:
1. Acess https://aka.ms/installazurecliwindows
2. Execute the .msi file and install
3. Open a cmd terminal and execute
> az login

Then a popup browser will open and login on your Azure account.
It will be necessary to allow terraform use your account to execute the .tf scripts.

## 2. Execution 
## 3. Interface Description
## 4. Difficulties
Above, will be listed all dificulties found on using Terraform to perform the experiment.
1. Despite all documentation available, there is a need to learn the syntax, which has not shown to be so intuitive.
