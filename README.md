## FLASK PROJECT ##

#### Edits : #### 

> 1. main.py - correct 'flask shell' (add relation)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'Job': Job}


> 2. app/tables - add handlers for other tables

> 3. templates/tables - add templates for other tables