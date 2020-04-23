# Iteration 6

Used technologies such as Flask, nginx, MongoDB, Mongo-Express, Docker-compose.

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
4. Check web site on url http://127.0.0.1/?url=https%3A%2F%2Fnews.tut.by%2Frss&limit=10&date=20191201 
5. If you want to see the database, then open a browser and paste the URL ( http://localhost:8081/db/News_feed )

6. If you want view the PDF file, execute the following commands:
    ```
        docker exec flask -it bash
        ls
    ```
    We see News_feed.pdf
