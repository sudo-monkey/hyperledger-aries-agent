# Where all magics happen
## Script
- (recommendation) To ensure a smooth script make sure to copy an already built von-network into project directory. If haven't clone the repo inside project directory:
```git clone https://github.com/bcgov/von-network.git```
- cd into von-network and run
```./manage build```
- (requirement) install xdotools by running:
```sudo apt-get install -y xdotool```
- (requirement) install terminator by running:
```sudo apt-get install -y terminator```
- back to project directory, make the script executable:
```chmod +x start.sh```

- IMPORTANT: run the following steps inside terminator terminator. If you are using gnome-terminal, run ```terminator``` or skip this step if you are already using terminator as terminal

- run the spell:
```./start.sh```

## Manual initialization
- There are 3 components in this namely testnet (von-network), Capuchin.Cloudagent (Aries Cloud Agent) and the controller (Flask)

- To deploy cd into von-network and build
``` ./manage build . ```
- Run the Testnet with logs
``` ./manage start --logs ```

- For fresh ledger, register DID inside localhost:9000 with wallet seed 'bcgt' and alias 'bcgt'; leave DID blank

- Then cd back into previous directory using "cd .." and run the main controller
``` docker-compose -f docker-compose-main.yml up ```

- The controller will be running and and listening to responses. @ port 5000"

- Now the controller has been running, run the wallet agent by using:
``` docker-compose -f docker-compose-cloudagentv2.yml up ```

- with the right configs (ledger & controller ip address), you should be able to up the wallet agent 


# Git guides

## Git Flow

## Create and switch to branch locally

- Creates new branch developer
 ``` git branch developer ```
- Switch branch to develop
``` git checkout develop ```
- Create and switch to branch
``` git checkout -b feature/aries-init-connection ```

- Pull latest remote branch (codes)
 ``` git pull ```
 ``` git pull develop ```
 ``` git pull feature/abc/```

## Push your local codes to remote
- Add new change to your local git heaf
``` git add . ``` 
- Add commit message  
``` git commit -m "Areis innit connection 18.10.2021.11.30" ``` 
- Push code to remote
``` git push ```


