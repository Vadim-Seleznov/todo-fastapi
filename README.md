## TODO-LIST BACKEND

This is my first api written in FastAPI for simple todo-list CRUD

requirements you can see in file requirements.txt

## VVCOMMIT

Project powered by my own github CLI tool - vvcommit: https://github.com/Vadim-Seleznov/vvcommit

## HOW TO RUN
first off all you need python on your PC!

then do venv
```bash
python -m venv venv
```

then activate venv (for example if you use CachyOS with fish console)
```bash
source venv/bin/activate.fish
```

then just do

```bash
uvicorn app.main:app --reload
```

and you are good to go! (Backend will be at localhos:8000 most likely)
