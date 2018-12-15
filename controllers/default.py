# Notepadlayout
def Notepadlayout():
    return dict()

#Index page to Login
def index():
    return dict()

def authenticate():
    submitted_email = request.vars.email
    submitted_password = request.vars.password

    if db(db.noteWriter.db_email == submitted_email
            and db.noteWriter.db_password == submitted_password).count()>0:
        return redirect (URL('default','Read_Notes'))
    else:
        return 'User Not Found! <a href="register.html">Click here to register</a>'

#Register
def register():
    return dict()

#Storing the inputs in the database
def store():
    submitted_firstname = request.vars.firstname
    Submitted_middlename = request.vars.middlename
    submitted_lastname = request.vars.lastname
    submitted_email = request.vars.email 
    submitted_password = request.vars.password
    submitted_repassword = request.vars.repassword  
                        
    if  submitted_password == submitted_repassword:

        results = db.noteWriter.insert(
        db_firstname = submitted_firstname,
        db_middlename = Submitted_middlename,
        db_lastname = submitted_lastname,
        db_email = submitted_email,
        db_password = submitted_password,
        db_repassword = submitted_repassword
    )
                    
        return redirect('index.html')
    else:
        return redirect('register.html')

#Add Notes function
def Add_Notes():
    return dict()

#Recieve input to add notes to database
def AddNotes():
    submitted_title = request.vars.title 
    submitted_notes = request.vars.notes 

    results = db.Add_NOTES.insert(
        db_title = submitted_title,
        db_notes = submitted_notes)

    if results:
        return redirect('Read_Notes.html')
    else:
        return 'Something went wrong. Please try again <a href="Add_Notes.html">Click here to Add notes</a>'

#Read notes
def Read_Notes():
    read_Notes = db().select(db.Add_NOTES.ALL)
    return dict(readnotes = read_Notes)


#Update notes
def edit_notes():
    parameters = request.args
    submitted_id = parameters[0]

    notes = db(db.Add_NOTES.id == submitted_id).select()
    note = notes[0]
    return dict(note = note)


#Receive the imputs from the user
def update():
    submitted_title = request.vars.title 
    submitted_notes = request.vars.notes
    submitted_id = request.vars.id 

# Checking user input with the user database
    if db(db.Add_NOTES.id == submitted_id).select():
        
        db(db.Add_NOTES.id == submitted_id).update(
            db_title = submitted_title,
            db_notes = submitted_notes,
            id = submitted_id
        )
        return redirect('Read_Notes.html')
    else:
        return 'No Notes with this ID! <a href="edit_notes.html">Go back to edit notes'

# Delete Function
def delete():
    parameters = request.args
    submitted_id = parameters[0]

    if db(db.Add_NOTES.id == submitted_id).select():

        db(db.Add_NOTES.id == submitted_id).delete()
        
        return redirect(URL('Read_Notes.html'))
    else:
        return 'Unable to Delete. Please try again <a href="Read_Notes.html">Click here to read notes</a>'


