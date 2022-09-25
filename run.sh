read -p "Install [I] or Run [R]" i

if [[ $i == "R" ]]; then
    node index.js
else
    npm install
fi

read -p "Press [Enter] key to exit..."