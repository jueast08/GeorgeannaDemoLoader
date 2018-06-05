# GeorgeannaDemoLoader
Note : I'll be redoing the readme so that it's all fancy and what not as I move along

Georgeanna is a client that lauches preconfigured commands one after the other. By setting up an entire command suite, we can limit the "demo-effect" and leave a trace that is easy to follow and launch

This is a work in process that I've used on occasion to automate demonstrations that I've has to carry out for work. Rather than memorizing the commands and trying to make them work during a demo, I pre-program them and their explications so that anyone can replay the presentation even without my help.

## Installation :
Georgeanna is still being developed. To use the project, clone this Git repository. For the moment, georgeanna can be installed in any non hidden folder. To use the command, you would need to also point your $PATH variable on the georgeanna directory 

This is how one would go about installing on linux
`git clone git@github.com:jueast08/GeorgeannaDemoLoader.git && mv georgeannaDemoLoader /usr/local/bin/georgeanna`
`export PATH=/usr/local/bin/georgeanna/:${PATH}`

## Launch:
When launching the command `georgeanna <command>`, if a file is needed, it will look in the current working directory for a playbook.json unless a file name is passed after the command

ex `~$> georgeanna validate` will search for a playbook.json in the ~ folder and then test to see if the playbook.json is not only a valid JSON file but also a valid Georgeanna Playbook
Georgeanna has 2 commands for the moment : (1) valide, which allows a user to see if his JSON is compatible with Georgeanna and (2) run which will run the commands in the playbook.


## Tests:
Tests can be launched by using the following command in the georgeanna root folder `$> python -m unittest discover`. You may have to install some dependecies

You can test how Georgeanna functions by launching `georgeanna [run/validate] tests/valid.json` from the georgeanan root folder


## Example of a valid JSON :
```json
{
    "name": "Demo 1",
    "description": "This is a demo file. qsfqdfqfdqsfqsfqs",
    "metadata" : {
	"name": "name",
	"email": "email",
	"date":"date"
    },
    "commands" : [
	{
	    "description": "ls without shell",
	    "command": "ls",
	    "options": ["-ali"]
	},
	{
	    "description": "ls with shell",
	    "command": "ls -ali",
	    "shell": true
	},
	{
	    "description": "sleep",
	    "command": "sleep 10",
	    "shell": true
	}
    ]
}
```
