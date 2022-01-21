#/bin/bash

echo REGISTERING DID ON TESTNET........

# Uncomment and edit these to bypass the prompts for the values.
#    If commented out, the reads will be used to ask the user for the config values
# ORG_TITLE=my-org-full-name
# MY_ORG=my-organization
# MY_PERMIT=my-permit

if [ -z ${ORG_TITLE+x} ]; then
    read -p 'Please provide a descriptive title for your permit-issuing organization (e.g. City of Victoria): ' ORG_TITLE
fi

if [ -z ${MY_ORG+x} ]; then
    read -p 'Please provide a domain for your permit-issuing organization - no spaces (e.g. city-of-victoria): ' MY_ORG
fi
# Strip white spaces, just to be sure
MY_ORG=`echo ${MY_ORG// /} | xargs`

if [ -z ${MY_PERMIT+x} ]; then
    read -p 'Please provide the name of the permit your organization will issue - no spaces (e.g. museum-permit): ' MY_PERMIT
fi
# Strip white spaces, just to be sure
MY_PERMIT=`echo ${MY_PERMIT// /} | xargs`

echo ""

# Generate the seed from MY_ORG, making sure it is 32 characters long
export MY_SEED=`echo ${MY_ORG}0000000000000000000000000000 | cut -c 1-32`

echo How will you be the VON Issuer/Verifier Agent:
echo
echo 1 - Using Play with Docker in your browser
echo 2 - Using docker on your own machine - with local von-network and TheOrgBook instances
echo 3 - Some other way

# Determine the example to expand and expand it
select example in "1" "2" "3"; do
    case $example in
        1 ) 
            myhost=`ifconfig eth1 | grep inet | cut -d':' -f2 | cut -d' ' -f1 | sed 's/\./\-/g'`
            export ENDPOINT_HOST="ip${myhost}-${SESSION_ID}-5001.direct.labs.play-with-docker.com"
            export LEDGER=http://138.197.138.255
            export GENESIS_URL=${LEDGER}/genesis
            __TOBAPIURL=https://demo-api.orgbook.gov.bc.ca/api/v2/
            __TOBAPPURL=https://demo.orgbook.gov.bc.ca/en/home

            break;;
        2 ) 
            unset ENDPOINT_HOST
            export LEDGER=http://localhost:9000
            export GENESIS_URL=${LEDGER}/genesis
            __TOBAPIURL=http://tob-api:8080/api/v2
            __TOBAPPURL=http://localhost:8080

            # Adjustments to files for local execution
            sed -i.bak "s/#local//g" docker/docker-compose.yml
            sed -i.bak "s/ INDY_GENESIS_URL/ #INDY_GENESIS_URL/" von-x-agent/config/settings.yml
            sed -i.bak "s/ AUTO_REGISTER_DID/ #AUTO_REGISTER_DID/" von-x-agent/config/settings.yml
            find docker von-x-agent -name "*.bak" -type f|xargs rm -f

            break;;
        3 ) 
            read -p "Enter the agent host you are using (e.g. localhost:5001): " __AGENTHOST
            export ENDPOINT_HOST=${__AGENTHOST}
            read -p "Enter the URL of the ledger you are using: " __LEDGER
            export LEDGER=${__LEDGER}
            export GENESIS_URL=${LEDGER}/genesis
            __TOBAPIURL=Update-With-OrgBook-API-URL
            __TOBAPPURL=Update-With-OrgBook-Application-URL
            echo NOTE: TheOrgBook API and Application URLs must be updated in von-x-agent/config/settings.yml

            break;;
    esac
done
echo ""

# OK - time to make all the substitutions...
sed -i.bak "s/my-organization0000000000000000/${MY_SEED}/g" von-x-agent/config/settings.yml
sed -i.bak "s#TOBAPIURL#${__TOBAPIURL}#g" von-x-agent/config/settings.yml
sed -i.bak "s#TOBAPPURL#${__TOBAPPURL}#g" von-x-agent/config/settings.yml
sed -i.bak "s#GENESISURL#${GENESIS_URL}#g" von-x-agent/config/settings.yml
find von-x-agent/config -name "*.yml" -exec sed -i.bak "s/my-org-full-name/${ORG_TITLE}/g" {} +
find von-x-agent/config -name "*.yml" -exec sed -i.bak s/my-organization/${MY_ORG}/g {} +
find von-x-agent/config -name "*.yml" -exec sed -i.bak s/my-permit/${MY_PERMIT}/g {} +
find von-x-agent -name "*.bak" -type f|xargs rm -f

# Register DID
# https://gist.github.com/subfuzion/08c5d85437d5d4f00e58
echo ""
echo Registering DID on Ledger ${LEDGER} - the Ledger MUST be running for this to work
echo ""
echo \{\"role\":\"TRUST_ANCHOR\",\"alias\":\"${MY_ORG}\",\"did\":null,\"seed\":\"${MY_SEED}\"\} >tmp.json
MY_DID=`curl -s -d "@tmp.json" -X POST ${LEDGER}/register | awk -F'"' '/did/ { print $4 }'`
echo My DID was registered as: $MY_DID
rm tmp.json
echo ""

# Update the MY-DID entries in the yml files
find von-x-agent/config -name "*.yml" -exec sed -i.bak s/X3tCbZSE9uUb223KYDWd6o/$MY_DID/g {} +
find von-x-agent -name "*.bak" -type f|xargs rm -f

echo -------------------------
echo The following updates were made to the configuration files:
echo ""

grep "${ORG_TITLE}" von-x-agent/config/*.yml
grep ${MY_ORG} von-x-agent/config/*.yml
grep ${MY_PERMIT} von-x-agent/config/*.yml
grep ${MY_DID} von-x-agent/config/*.yml
grep ${MY_SEED} von-x-agent/config/*.yml
grep ${__TOBAPIURL} von-x-agent/config/*.yml
grep ${__TOBAPPURL} von-x-agent/config/*.yml
grep ${GENESIS_URL} von-x-agent/config/*.yml

# Clean up
unset ORG_TITLE MY_ORG MY_PERMIT MY_DID MY_SEED __TOBAPIURL __TOBAPPURL