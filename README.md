# Snakex

A competitive version of the classical snake game.

**Requires pygame**

Possible bug fixes and updates are to be done

**Uses LAN**

## Usage

### Server

Run the script to start the server.

```bash
python3 server.py
```

Wait for up to 4 players.

Type **start** to start the game.

Type **quit** to shutdown the server.

Game settings might be changed from **util.py**

### Client

Run the script to connect to the server and wait for the game to start.

```bash
python3 client.py <server_ip>(optional) <client_ip>(optional)
```

Server ip and port are asked if not provided as arguments.

Use arrow keys to move.

## License
[MIT](https://choosealicense.com/licenses/mit/)
