# Iteration 6

Гsed technologies such as Flask, nginx, MongoDB, Mongo-Express, Docker-compose.

## Install RSS reader (work)
1. Create docker container:
    ```
    docker run -it -v /var/run/docker.sock:/var/run/docker.sock python /bin/bash
    ```
2. Paste this commands into the console:

    ```
    git clone https://github.com/ZayJob/PythonHomework
    cd PythonHomework
    
    git branch --track iteration_6 remotes/origin/iteration_6
    git checkout iteration_6
    ```

2. Paste this command into the console:

    ```
    chmod +x install_script.sh && . install_script.sh
    ```

3. Use for run app:
    ```
    docker-compose build
    docker-compose up -d
    ```
4. If you want to see the database, then open a browser and paste the URL ( http://localhost:8081/db/News_feed )

5. If you want view the PDF file, execute the following commands:
    ```
        docker exec flask -it bash
        ls
    ```
    We see News_feed.pdf