# SP25_DS5111_ddb4tr
## 1. Manual Initial Setup
Before running the automated scripts, manually update the package lists on the new VM:

```bash
sudo apt update
```

## 2. Configure Git Credentials and SSH Key
Set up Git credentials and generate an SSH key using the scripts from the last lab. Ensure you have the proper Git authentication configured.

```bash
# Example command to generate SSH key (if not already set up)
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# Add SSH key to the SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

## 3. Clone the Repository
Once Git and SSH are configured, clone the repository to your VM:

```bash
git clone git@github.com:BardiaNikpour/SP25_DS5111_ddb4tr.git
cd SP25_DS5111_ddb4tr
```

## 4. Run the Initialization Script
Execute the `init.sh` script to install necessary dependencies:

```bash
./init.sh
```
## 5. Run the Initialization Script
Execute the `install_chrome_headless.sh` script to install chrome:

```bash
./install_chrome_headless.sh
```
## 6. test the makefile
Execute the `make` script to make sure makefile working"

```bash
make
```
## 7. Run the makefile
Execute the `makefile` to create env:

```bash
make update
```
## 8. Run the tree
run the tree to see the output:

```bash
tree <your project-repo> -I env
```

home/ubuntu/SP25_DS5111_ddb4tr
├── Assignment2
│   ├── Assignment2-Screenshot.png
│   └── SP25_bardia_ddb4tr.pem
├── Lab-02
│   ├── google-chrome-stable_current_amd64.deb
│   ├── init.sh
│   ├── install_chrome_headless.sh
│   ├── makefile
│   ├── makefile.txt
│   ├── requirements.txt
│   ├── ygainers.csv
│   └── ygainers.html
├── README.md
├── init.sh
├── install_chrome_headless.sh
└── makefile.txt
