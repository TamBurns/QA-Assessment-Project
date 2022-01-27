# QA-Assessment-Project
Cocktail Library

PROJECT BRIEF

Design and build a cocktail recipe application, using MySQL to house the relevant data. It must be possible to add new cocktails, or amend, or delete, existing entries, to the library after deployment. Users must be able to search for a specific cocktail and return the relevant recipe, or search for a specific ingredient and return a list of relevant cocktails.


PLANNING

User Stories & User Journey









Risk Assessment



INFRASTRUCTURE


COMPONENTS





UNIT TESTING
Test each component part separately to the whole of the application.

Manual Testing A:
1. Checked that basic Flask application worked by running app.py outside of Docker.
    - Application was unable to connect.
    - Checked port was clear.
    - Application unable to connect.
    - Checked port reference specified in app.py file.
    - Tried changing port reference.
    - Application unable to connect.
    - Checked syntax of port reference.
    - Tried changing " to '
    - Application unable to connect.
    - Checked syntax.
    - Found and removed extra space.
    - Application connected and loaded page.
    
2. Checked that basic Flask application worked within Docker.
    - Built containers.
    - Application unable to connect.
    - Checked port for phpMyAdmin - connected.
    - Listed containers in terminal - 2 of 3 listed.
    - webapp container not built.
    - Checked .yml file for errors - structure and spelling appear correct.
    - Checked Dockerfile for errors - stucture and spelling appear correct.
    - Removed containers.
    - Cleared ports.
    - Rebuilt containers.
    - Application unable to connect.
    - Checked containers - still only 2.
    - Checked docker logs - COPY failed: file does not exist in build context error.
    - Checked Dockerfile - checked path of COPY command.
    - Removed and rebuilt containers.
    - Application unable to connect.
    - Scrolled through terminal output - file does not exist error. (cannot remember exact output at time of writing, but had to Google an explanation)
    - Error = Path error in Dockerfile. But path looks ok...
    - Visually check directory - ok - correct directory, correct folder.
    - Considered error may be due to lack of familiarity with Ubuntu file structure.
    - Tried specifying home directory in Dockerfile.
    - Removed and rebuilt containers.
    - Change to error: ~home/home/... 
    - Tried a few variations, to th same effect.
    - Compared file structure in VSCode to file structure of an application made by the class tutor.
    - Found that the app.py file was in the project folder, but not actually in the application folder.
    - Moved file.
    - Removed and rebuilt containers.
    - Application connected.
  
 3. Became unable to login to phpMyAdmin - Could not connect to MySQL.
    - Checked no accidental changes to .yml file.
    - Removed and rebuilt containers.
    - Unable to login.
    - Tried changing port reference.
    - Removed and rebuilt containers.
    - Unable to login.
    - Tried changing container and database names.
    - Removed and rebuilt containers.
    - Unable to create volume - not declared.
    - Updated volume declaration section.
    - Removed and rebuilt containers.
    - Unable to login.
    - Removed containers.
    - Cleared ports.
    - Rebuilt containers.
    - Unable to login.
    - Removed containers.
    - Returned .yml to original state.
    - Attempted to rebuild containers - process did not complete in terminal.
    - Restarted VM.
    - Attempted to rebuild containers - process did not complete in terminal.
    - Restarted VM.
    - Critical memory warning.
    - Deleted unnecessary folders.
    - Attempted to rebuild containers - process did not complete in terminal and VM froze.
    - Attempted to restart VM - process did not complete.
    - Attempted to restart VM - process did not complete.
    - Killed VM in favour of clone. 
 
4. Check that MySQL database connects to Flask application.
    - Updated app.py file with relevant code (on reflection, this should have been written in a separate file).
    - Check syntax near 'xxxx' error.
    - Altered and rerun.
    - Repeated a few times, then:
    - Module not found error - cannot find flask-mysqldb
    - Checked syntax (flask-mysqldb v. flask_mysqldb)
    - Checked Dockerfile and requirements.
    - Checked module installed on host (although this should not affect the container).
    - Issue not yet resolved.
  
Manual Testing B:
    - Code template drafted for testing of indivdual HTML pages
    - Code template drafted for testing for an image within a container
 

CI/CD PIPELINE


______________________________________________________

RETROSPECTIVE COMMENTS

Diversions from project brief:
The original assessment project brief required the application to be hosted in the cloud using Docker Swarm and to use Jenkins to create a CI/CD pipeline to automate the testing, integration and deployment of new code. However, although Jenkins was introduced, these aspects were not covered during the course.

What went well:
- starting to understand HTML.
- developing a mental checklist for connection errors.
- more able to interpret errors printed in terminal.

What didn't go well:
- Extensive time lost to looking for errors and trying to solve them.
- Extensive time lost due to increased frequency of migraines (most likely caused by over-excessive screentime).
- Failed an Agile principle by spending too much time playing around with cosmetics rather than functionality (partly because I enjoy the design aspect; partly because I was getting stressed and frustrated with the functionailty issues).
- Have realised that I do not have enough knowledge, or understanding of knowledge recently gained, to complete my own project goals. I thought I had some understanding, as things generally made sense when following the tutor. However, when it came to putting it all together myself, it became obvious that I have not yet retained enough knowledge, or yet gained enough understanding, to fully realise this project.

What would I change:
- Remember not to get hung-up on aesthetics and complete functionality first.
- Keep it simple and within the bounds of existing knowledge.
- Gain a higher level of understanding of all aspects before starting.
- Start working towards project with a modular approach from the beginning of the course, rather than trying to do it all at towards the end. 
- Make more effort to obtain a recommended reading list. I did ask for one before the course began and I regret not asking again after the course started. Some of the tutors did share pdfs and recommend alternative online resources to the class, but a few paper reference books would have helped to reduce screentime and migraines. I'm also someone who retains knowledge better and faster through reading than through lectures and I feel that this would have helped to cement my understanding. 




