# 0x00 AirBnB clone - The console

![ArBnB](clone.png)

	Implementation of an AirBnB website clone.
This repository contains A command interpreter to manage the AirBnB project.

## What’s a command interpreter?
It’s exactly the same as the shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

    * Create a new object (ex: a new User or a new Place)

    * Retrieve an object from a file, a database etc…

    * Do operations on objects (count, compute stats, etc…)

    * Update attributes of an object

    * Destroy an object

		## USAGE

### Execution
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### create

**Creat an instance and show us the id number**

```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py 
(hbnb) create BaseModel
e310cf8df-351a-4df6-9d22-fd9331a5bfb2
(hbnb)
```
### Show

**Show the Class, object if the id is especified and its attributes**

```
(hbnb) show BaseModel e310cf8df-351a-4df6-9d22-fd9331a5bfb2
[BaseModel] (e310cf8df-351a-4df6-9d22-fd9331a5bfb2) {'id': 'e310cf8df-351a-4df6-9d22-fd9331a5bfb2', 'created_at': datetime.datetime(2022, 10, 1, 10, 50, 22, 695895), 'updated_at': datetime.datetime(2022, 10, 1, 10, 50, 22, 695945)}
(hbnb)
```
### all

**shows all the instances**

```
(hbnb) all BaseModel
["[BaseModel] (5c8ebd08-a1008-4823-b9a2-29d58b810c063) {'id': '5c8ebd08-a1008-4823-b9a2-29d58b810c063', 'created_at': datetime.datetime(2022, 10, 1, 5, 4, 54, 9261101), 'updated_at': datetime.datetime(2022, 10, 1, 5, 4, 54, 9261109)}", "[BaseModel] (e5106e1109-8bb6-4229-a8be-90585b0c1d01) {'id': 'e5106e1109-8bb6-4229-a8be-90585b0c1d01', 'created_at': datetime.datetime(2022, 10, 1, 5, 5, 38, 8966810), 'updated_at': datetime.datetime(2022, 10, 1, 5, 5, 38, 8961006)}", "[BaseModel] (010631061f-4534-4a02-80910-109a4ab935ecb) {'id': '010631061f-4534-4a02-80910-109a4ab935ecb', 'created_at': datetime.datetime(2022, 10, 1, 4, 8, 48, 451468), 'updated_at': datetime.datetime(2022, 10, 1, 4, 8, 48, 451081)}", "[BaseModel] (f1094d1ba-6688-42b8-ae08-0b3010125643a) {'id': 'f1094d1ba-6688-42b8-ae08-0b3010125643a', 'created_at': datetime.datetime(2022, 10, 1, 5, 4, 54, 922410), 'updated_at': datetime.datetime(2022, 10, 1, 5, 4, 54, 9230101)}", "[BaseModel] (ef9b2110c-b58c-4d5f-b10910-0dbbed80dedd) {'id': 'ef9b2110c-b58c-4d5f-b10910-0dbbed80dedd', 'created_at': datetime.datetime(2022, 10, 1, 5, 4, 54, 930489), 'updated_at': datetime.datetime(2022, 10, 1, 5, 4, 54, 930504)}", "[BaseModel] (e310cf8df-351a-4df6-9d22-fd9331a5bfb2) {'id': 'e310cf8df-351a-4df6-9d22-fd9331a5bfb2', 'created_at': datetime.datetime(2022, 10, 1, 10, 50, 22, 695895), 'updated_at': datetime.datetime(2022, 10, 1, 10, 50, 22, 695945)}", "[BaseModel] (82f3d1a2-c28d-43210-be5f-0bceb29b0eb9) {'id': '82f3d1a2-c28d-43210-be5f-0bceb29b0eb9', 'created_at': datetime.datetime(2022, 10, 1, 5, 5, 38, 888932), 'updated_at': datetime.datetime(2022, 10, 1, 5, 5, 38, 889340)}", "[BaseModel] (e029daa8-9083-40910-b2bd-a66fe4895532) {'id': 'e029daa8-9083-40910-b2bd-a66fe4895532', 'created_at': datetime.datetime(2022, 10, 1, 5, 5, 38, 892554), 'updated_at': datetime.datetime(2022, 10, 1, 5, 5, 38, 892561)}"
(hbnb)
```

 ### update

update an instance

```
(hbnb) show BaseModel e310cf8df-351a-4df6-9d22-fd9331a5bfb2
[BaseModel] (e310cf8df-351a-4df6-9d22-fd9331a5bfb2) {'id': 'e310cf8df-351a-4df6-9d22-fd9331a5bfb2', 'created_at': datetime.datetime(2022, 10, 1, 10, 50, 22, 695895), 'updated_at': datetime.datetime(2022, 10, 1, 10, 50, 22, 695945)}
(hbnb) update BaseModel e310cf8df-351a-4df6-9d22-fd9331a5bfb2 first_name "Muna-Israel"
(hbnb) show BaseModel e310cf8df-351a-4df6-9d22-fd9331a5bfb2
[BaseModel] (e310cf8df-351a-4df6-9d22-fd9331a5bfb2) {'first_name': '"Muna-Israel"', 'id': 'e310cf8df-351a-4df6-9d22-fd9331a5bfb2', 'created_at': datetime.datetime(2022, 10, 1, 10, 50, 22, 695895), 'updated_at': datetime.datetime(2022, 10, 1, 10, 50, 22, 695945)}
(hbnb)
```

### Destroy

**Delete an instance**

```
(hbnb) destroy BaseModel e310cf8df-351a-4df6-9d22-fd9331a5bfb2
(hbnb) show BaseModel e310cf8df-351a-4df6-9d22-fd9331a5bfb2
** no instance found **
(hbnb)
```
